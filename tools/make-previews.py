#!/usr/bin/env python3
"""Build preview copies of the funnel pages that need query-string data to show their real state.

A preview host (for example a Claude artifact) passes no query string, so the referral page would show
its plain variant, the thank-you page its no-code state, the interview page its "apply first" state, and the claim
pages their no-link state ("This page is for ... winners", no countdown, no calendar). This script
writes copies with sample parameters and a distinct <title>. The thank-you preview shows the booked state; the
interview preview gets sample entry data in sessionStorage (key gw_entry) and shows its calendar placeholder, because
the repo pages carry no booking link. The files in funnel/ are never changed.

Usage:  python3 tools/make-previews.py OUTPUT_DIR [--src DIR]
  --src   read the pages from another folder (default: funnel/ at the repo root)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'funnel')
SOON = "('?first=Dana&until=' + encodeURIComponent(new Date(Date.now()+71*3600e3).toISOString()))"
# Sample entry, written to sessionStorage by the interview and thank-you previews (fake name, example.com, 555 number).
ENTRY = ('{"first":"Dana","last":"Reynolds","email":"dana@example.com","phone":"+15015550142",'
         '"company":"Summit Roofing","code":"DANREY0142"}')
SEED = ("<script>try{if(!sessionStorage.getItem('gw_entry'))sessionStorage.setItem('gw_entry',"
        + repr(ENTRY) + ")}catch(e){}</script>\n")
PAGES = [
    ('04-referral-ghl.html', 'referral-page-preview.html', 'Giveaway Referral Page',
     "'?ref=MIKSMI1234&from=Mike&co=Summit%20Roofing'"),
    ('02-thankyou-ghl.html', 'thank-you-page-preview.html', 'Giveaway Thank-You Page', "'?c=DANREY0142&booked=1'"),
    ('06-book-ghl.html', 'interview-page-preview.html', 'Giveaway Interview Page', "'?c=DANREY0142'"),
    ('03-claim-ghl.html', 'second-place-claim-preview.html', 'Second-Place Claim Page', SOON),
    ('05-claim-third-ghl.html', 'third-place-claim-preview.html', 'Third-Place Claim Page', SOON),
]


SEEDED = ('02-thankyou-ghl.html', '06-book-ghl.html')


def main():
    args = sys.argv[1:]
    src_dir = SRC
    if '--src' in args:
        i = args.index('--src')
        if i + 1 >= len(args):
            sys.exit(__doc__)
        src_dir = os.path.abspath(args[i + 1])
        del args[i:i + 2]
    if len(args) != 1 or args[0].startswith('-'):
        sys.exit(__doc__)
    out = args[0]
    os.makedirs(out, exist_ok=True)
    for src, dst, title, demo in PAGES:
        path = os.path.join(src_dir, src)
        if not os.path.isfile(path):
            sys.exit(f'{src}: not found in {src_dir}')
        with open(path, encoding='utf-8') as fh:
            page = fh.read()
        reads = page.count('new URLSearchParams(location.search)')
        if not reads:
            sys.exit(f'{src}: no "new URLSearchParams(location.search)" to patch')
        page = page.replace('new URLSearchParams(location.search)',
                            f'new URLSearchParams(location.search || {demo})')
        page, swapped = re.subn(r'<title>.*?</title>', f'<title>{title}</title>', page, count=1)
        if swapped != 1:
            sys.exit(f'{src}: no <title> found')
        if src in SEEDED:
            page = SEED + page
        with open(os.path.join(out, dst), 'w', encoding='utf-8') as fh:
            fh.write(page)
        print(f'{dst}: {len(page)} bytes')


if __name__ == '__main__':
    main()
