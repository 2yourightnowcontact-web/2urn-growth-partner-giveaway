#!/usr/bin/env python3
"""Build the pasteable pages with the real GoHighLevel values written in.

The repo pages carry no webhook and no booking link (the repo is public). The real values live in a
git-ignored live-config.json at the repo root (copy tools/live-config.example.json and fill it in):

  webhook              Inbound Webhook URL of workflow A "Giveaway Entry"         -> pages 01 and 04 (GHL_CONFIG.webhook)
  nominate_webhook     Inbound Webhook URL of workflow F "Nomination"             -> page 02 (GW_TY.nominateWebhook)
  interview_calendar   widget booking link of the Introduction Interview calendar -> page 06 (GW_BOOK.bookingUrl)
  claim_calendar       booking link for second-place claim calls                  -> page 03 (GW_CLAIM.bookingUrl)
  third_place_calendar booking link for third-place claim calls                   -> page 05 (GW_CLAIM3.bookingUrl)
  preview_pages        "path=previewPageId" pairs, comma separated, one per funnel step  -> every page (GW_PREVIEW.map)
                       e.g. "/lead-engine=ID,/interview=ID,/entered=ID,/refer=ID,/claim-second=ID,/claim-third=ID".
                       It makes the hand-offs between pages work on GoHighLevel preview links, before the funnel has a domain.

claim_calendar may be left "": the kit uses ONE calendar for interviews and second-place claims, so an empty claim_calendar
uses interview_calendar. third_place_calendar is the separate Free Audit + Website Call calendar and has no fallback.

It copies the six pages to live/ (git-ignored) with those values written into the config objects, asserts that each
replacement matched exactly once, runs the checks of tools/check-pages.py on the result, and prints each file's size
and which values are still empty. It never prints a value.

Usage:  python3 tools/make-live.py [--config PATH] [--src DIR] [--out DIR]
  Defaults: live-config.json, funnel/ and live/ at the repo root. Python 3 standard library only.
"""
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (page file, config object on the window, key inside it, live-config.json key)
TARGETS = [
    ('01-giveaway-ghl.html', 'GHL_CONFIG', 'webhook', 'webhook'),
    ('06-book-ghl.html', 'GW_BOOK', 'bookingUrl', 'interview_calendar'),
    ('02-thankyou-ghl.html', 'GW_TY', 'nominateWebhook', 'nominate_webhook'),
    ('04-referral-ghl.html', 'GHL_CONFIG', 'webhook', 'webhook'),
    ('03-claim-ghl.html', 'GW_CLAIM', 'bookingUrl', 'claim_calendar'),
    ('05-claim-third-ghl.html', 'GW_CLAIM3', 'bookingUrl', 'third_place_calendar'),
] + [(name, 'GW_PREVIEW', 'map', 'preview_pages') for name in (
    '01-giveaway-ghl.html', '02-thankyou-ghl.html', '03-claim-ghl.html',
    '04-referral-ghl.html', '05-claim-third-ghl.html', '06-book-ghl.html')]
KEYS = ['webhook', 'nominate_webhook', 'interview_calendar', 'claim_calendar', 'third_place_calendar', 'preview_pages']
FALLBACK = {'claim_calendar': 'interview_calendar'}


def fail(msg):
    sys.exit(f'make-live: {msg}')


def load_checker():
    spec = importlib.util.spec_from_file_location('check_pages', os.path.join(ROOT, 'tools', 'check-pages.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mask_comments(text):
    """Same length as text, with every /* ... */ comment blanked, so searches skip comments."""
    return re.sub(r'/\*.*?\*/', lambda m: re.sub(r'[^\n]', ' ', m.group(0)), text, flags=re.S)


def js_string(value):
    """A double-quoted JavaScript string holding value: ASCII only, safe inside a <script> element."""
    out = json.dumps(value, ensure_ascii=True)
    return out.replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')


def set_config_value(page, obj, key, value, label):
    """Write key: "value" into window.obj = {...}. Tolerant of the current value; fails unless it matches exactly once."""
    masked = mask_comments(page)
    blocks = list(re.finditer(r'window\.' + re.escape(obj) + r'\s*=\s*\{(.*?)\n?\s*\};', masked, flags=re.S))
    if len(blocks) != 1:
        fail(f'{label}: found {len(blocks)} "window.{obj} = {{...}};" blocks, expected exactly 1')
    b0, b1 = blocks[0].start(1), blocks[0].end(1)
    keyrx = re.compile(r'''(?<![\w$])(["']?)''' + re.escape(key) + r'''\1\s*:\s*(?:"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')''')
    hits = list(keyrx.finditer(masked, b0, b1))
    if len(hits) != 1:
        fail(f'{label}: key {key} matched {len(hits)} times inside window.{obj}, expected exactly 1 (is it missing, or no longer a string?)')
    m = hits[0]
    new = f'{m.group(1)}{key}{m.group(1)}: {js_string(value)}'
    return page[:m.start()] + new + page[m.end():]


def main(argv):
    opts = {'--config': os.path.join(ROOT, 'live-config.json'),
            '--src': os.path.join(ROOT, 'funnel'),
            '--out': os.path.join(ROOT, 'live')}
    i = 0
    while i < len(argv):
        if argv[i] in ('-h', '--help'):
            print(__doc__)
            return 0
        if argv[i] not in opts or i + 1 >= len(argv):
            sys.exit(f'unknown or incomplete option {argv[i]}\n{__doc__}')
        opts[argv[i]] = os.path.abspath(argv[i + 1])
        i += 2
    cfg_path, src, out = opts['--config'], opts['--src'], opts['--out']
    if os.path.realpath(src) == os.path.realpath(out):
        fail('--out must not be the same folder as --src')
    if not os.path.isfile(cfg_path):
        fail(f'no config at {cfg_path}. Copy tools/live-config.example.json to live-config.json (git-ignored) and fill it in.')
    try:
        cfg = json.load(open(cfg_path, encoding='utf-8'))
    except ValueError as e:
        fail(f'{cfg_path} is not valid JSON: {e}')
    if not isinstance(cfg, dict):
        fail('the config must be a JSON object')
    unknown = [k for k in cfg if k not in KEYS]
    if unknown:
        fail('unknown config keys: ' + ', '.join(unknown) + '. Allowed: ' + ', '.join(KEYS))
    for k in KEYS:
        if not isinstance(cfg.get(k, ''), str):
            fail(f'config key {k} must be a string')
    # resolve values (a missing key counts as ""), apply the one-calendar fallbacks, validate the shapes
    val = {k: cfg.get(k, '').strip() for k in KEYS}
    for k in FALLBACK:
        if not val[k]:
            val[k] = val[FALLBACK[k]]
    for k in ('webhook', 'nominate_webhook'):
        if val[k] and not val[k].startswith('https://'):
            fail(f'config key {k} must start with https:// (value not shown)')
    for k in ('interview_calendar', 'claim_calendar', 'third_place_calendar'):
        if val[k] and not (val[k].startswith('https://') and '/widget/booking/' in val[k]):
            fail(f'config key {k} must be an https:// widget link containing /widget/booking/ (value not shown)')
    if val['preview_pages'] and not re.fullmatch(r'(/[a-z0-9-]+=[A-Za-z0-9_-]+)(,/[a-z0-9-]+=[A-Za-z0-9_-]+)*', val['preview_pages']):
        fail('config key preview_pages must look like "/path=ID,/path=ID" (value not shown)')
    os.makedirs(out, exist_ok=True)
    sizes, pages = {}, {}
    for name, obj, key, ck in TARGETS:        # a page can take more than one value: each one is written into the same copy
        if name not in pages:
            path = os.path.join(src, name)
            if not os.path.isfile(path):
                fail(f'{name} is missing from {src}')
            with open(path, encoding='utf-8') as fh:
                pages[name] = fh.read()
        pages[name] = set_config_value(pages[name], obj, key, val[ck], name)
    for name, page in pages.items():
        with open(os.path.join(out, name), 'w', encoding='utf-8', newline='') as fh:
            fh.write(page)
        sizes[name] = len(page.encode('utf-8'))
    # report: per file, size and what is still empty (names only, never values)
    print(f'wrote {len(pages)} pages to {out}')
    for name, obj, key, ck in TARGETS:
        note = f'still empty: {ck}' if not val[ck] else 'values set'
        print(f'  {name}: {sizes[name]} bytes, {obj}.{key} <- {ck}: {note}')
    empty = sorted({ck for _, _, _, ck in TARGETS if not val[ck]})
    if empty:
        print('Still empty in the live pages (preview mode there): ' + ', '.join(empty))
    # same checks as check-pages.py, on the output
    checker = load_checker()
    print(f'checking {out}')
    failed = checker.check_dir(out)
    print('RESULT: FAIL' if failed else 'RESULT: live pages built and pass the checks')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
