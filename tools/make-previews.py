#!/usr/bin/env python3
"""Build preview copies of the funnel pages that need query-string data to show their real state.

A preview host (for example a Claude artifact) passes no query string, so the referral page would show
its plain variant, the thank-you page its no-code state, and the claim pages no countdown. This script
writes copies with sample parameters and a distinct <title>. The files in funnel/ are never changed.

Usage:  python3 tools/make-previews.py OUTPUT_DIR
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'funnel')
SOON = "('?first=Dana&until=' + encodeURIComponent(new Date(Date.now()+71*3600e3).toISOString()))"
PAGES = [
    ('04-referral-ghl.html', 'referral-page-preview.html', 'Giveaway Referral Page',
     "'?ref=MIKSMI1234&from=Mike&co=Summit%20Roofing'"),
    ('02-thankyou-ghl.html', 'thank-you-page-preview.html', 'Giveaway Thank-You Page', "'?c=DANREY0142'"),
    ('03-claim-ghl.html', 'second-place-claim-preview.html', 'Second-Place Claim Page', SOON),
    ('05-claim-third-ghl.html', 'third-place-claim-preview.html', 'Third-Place Claim Page', SOON),
]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for src, dst, title, demo in PAGES:
        with open(os.path.join(SRC, src), encoding='utf-8') as fh:
            page = fh.read()
        reads = page.count('new URLSearchParams(location.search)')
        if not reads:
            sys.exit(f'{src}: no "new URLSearchParams(location.search)" to patch')
        page = page.replace('new URLSearchParams(location.search)',
                            f'new URLSearchParams(location.search || {demo})')
        page, swapped = re.subn(r'<title>.*?</title>', f'<title>{title}</title>', page, count=1)
        if swapped != 1:
            sys.exit(f'{src}: no <title> found')
        with open(os.path.join(out, dst), 'w', encoding='utf-8') as fh:
            fh.write(page)
        print(f'{dst}: {len(page)} bytes')


if __name__ == '__main__':
    main()
