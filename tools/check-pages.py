#!/usr/bin/env python3
"""Check the GoHighLevel paste pages before anyone pastes them.

For every funnel/0*.html (or the files of another folder) this fails on:
  - any byte above 0x7F (prints line and column);
  - unbalanced start/end tags for div, section, form, ul, ol, li, p, span, a, button, label, select, script, style;
  - an inline <script> that node --check rejects (skipped, with a note, when node is not installed);
  - target="_blank", window.open, loading="lazy" on an iframe, forms/submit, "/book", /claim? and /claim" (old paths).
It prints one line per file and exits 1 when any file fails.

Usage:  python3 tools/check-pages.py [--src DIR | --dir DIR | --out DIR] [DIR ...]
  With no folder it checks funnel/ at the repo root. --dir, --src and --out all name the folder to check
  (so the same flags work as on make-live.py). --config is accepted and ignored.
Python 3 standard library only.
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BALANCED = ('div', 'section', 'form', 'ul', 'ol', 'li', 'p', 'span', 'a', 'button', 'label', 'select', 'script', 'style')
FORBIDDEN = [
    ('target="_blank"', re.compile(r'''target\s*=\s*["']?_blank''', re.I)),
    ('window.open', re.compile(r'window\s*\.\s*open\b')),
    ('loading="lazy" on an iframe', re.compile(r'''<iframe\b[^>]*\bloading\s*=\s*["']?lazy''', re.I | re.S)),
    ('forms/submit', re.compile(r'forms/submit')),
    ('"/book" (old path, now /interview)', re.compile(r'''["']/book["']''')),
    ('/claim? (old path, now /claim-second)', re.compile(r'/claim\?')),
    ('/claim" (old path, now /claim-second)', re.compile(r'''/claim["']''')),
]


class Tags(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.starts = {t: 0 for t in BALANCED}
        self.ends = {t: 0 for t in BALANCED}
        self.scripts = []          # (line, body) of inline scripts
        self._script = None

    def handle_starttag(self, tag, attrs):
        if tag in self.starts:
            self.starts[tag] += 1
        if tag == 'script':
            a = dict(attrs)
            kind = (a.get('type') or '').strip().lower()
            runs = not a.get('src') and kind in ('', 'text/javascript', 'application/javascript', 'module')
            self._script = [self.getpos()[0], []] if runs else None

    def handle_startendtag(self, tag, attrs):
        pass  # a self-closed tag counts as neither a start nor an end

    def handle_endtag(self, tag):
        if tag in self.ends:
            self.ends[tag] += 1
        if tag == 'script' and self._script is not None:
            self.scripts.append((self._script[0], ''.join(self._script[1])))
            self._script = None

    def handle_data(self, data):
        if self._script is not None:
            self._script[1].append(data)


def check_file(path, node):
    """Return (problems, notes) for one page."""
    problems, notes = [], []
    raw = open(path, 'rb').read()
    # 1. ASCII only (reported per character: line, column, the character)
    bad = []
    for n, line in enumerate(raw.decode('utf-8', 'replace').split('\n'), 1):
        for col, ch in enumerate(line, 1):
            if ord(ch) > 127:
                bad.append((n, col, ch))
    for n, col, ch in bad[:5]:
        problems.append(f'non-ASCII character U+{ord(ch):04X} at line {n}, column {col}')
    if len(bad) > 5:
        problems.append(f'... {len(bad) - 5} more non-ASCII characters ({len(bad)} in all)')
    if not bad and any(b > 127 for b in raw):
        problems.append('file is not valid UTF-8 and has bytes above 0x7F')
    text = raw.decode('utf-8', 'replace')
    # 2. tag balance and inline scripts
    p = Tags()
    try:
        p.feed(text)
        p.close()
    except Exception as e:  # html.parser is lenient, but never trust it blindly
        problems.append(f'html parser error: {e}')
    for t in BALANCED:
        if p.starts[t] != p.ends[t]:
            problems.append(f'<{t}> opened {p.starts[t]} times, closed {p.ends[t]}')
    # 3. node --check on each inline script
    if node:
        tmp = tempfile.mkdtemp(prefix='check-pages-')
        try:
            for i, (line, body) in enumerate(p.scripts, 1):
                f = os.path.join(tmp, f's{i}.js')
                with open(f, 'w', encoding='utf-8') as fh:
                    fh.write(body)
                r = subprocess.run([node, '--check', f], capture_output=True, text=True)
                if r.returncode:
                    msg = [x for x in r.stderr.splitlines() if x.strip()]
                    first = next((x for x in msg if 'Error' in x), msg[0] if msg else 'syntax error')
                    shown = re.search(r':(\d+)$', msg[0]) if msg else None
                    where = f' (script line {shown.group(1)})' if shown else ''
                    problems.append(f'inline script {i} (starts at file line {line}){where}: {first}')
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    else:
        notes.append('node not installed, scripts not syntax-checked')
    # 4. forbidden strings
    for label, rx in FORBIDDEN:
        for m in rx.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            problems.append(f'forbidden {label} at line {line}')
    return problems, notes, len(p.scripts)


def check_dir(folder, quiet=False):
    """Check every 0*.html in folder. Returns the number of failing files (also 1 if none found)."""
    files = sorted(glob.glob(os.path.join(folder, '0*.html')))
    if not files:
        print(f'check-pages: no 0*.html files in {folder}')
        return 1
    node = shutil.which('node')
    failed = 0
    for f in files:
        problems, notes, nscripts = check_file(f, node)
        name = os.path.basename(f)
        if problems:
            failed += 1
            print(f'FAIL {name}')
            for x in problems:
                print(f'     - {x}')
        elif not quiet or notes:
            extra = f' ({"; ".join(notes)})' if notes else ''
            print(f'ok   {name}: ASCII, tags balanced, {nscripts} script(s){extra}')
    return failed


def main(argv):
    folders = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ('--src', '--dir', '--out', '--config'):
            if i + 1 >= len(argv):
                sys.exit(f'{a} needs a value')
            if a != '--config':
                folders.append(argv[i + 1])
            i += 2
        elif a in ('-h', '--help'):
            print(__doc__)
            return 0
        elif a.startswith('-'):
            sys.exit(f'unknown option {a}\n{__doc__}')
        else:
            folders.append(a)
            i += 1
    if not folders:
        folders = [os.path.join(ROOT, 'funnel')]
    failed = sum(check_dir(os.path.abspath(f)) for f in folders)
    print('RESULT: FAIL' if failed else 'RESULT: all pages pass')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
