#!/usr/bin/env python3
"""A tiny local server for testing the funnel with its real paths.

  /lead-engine   01-giveaway-ghl.html      /interview     06-book-ghl.html
  /entered     02-thankyou-ghl.html      /refer         04-referral-ghl.html
  /claim-second  03-claim-ghl.html         /claim-third   05-claim-third-ghl.html
  /rules         07-rules-ghl.html (review draft)   /privacy  /terms   one-line stubs

The file names (/01-giveaway-ghl.html ...) keep working too. Each paste file is served as text/html; charset=utf-8
inside a minimal <!doctype html><html><head><meta charset="utf-8"></head><body> shell, which is roughly what
GoHighLevel's custom-code element does with it.

Usage:  python3 tools/dev-server.py [--live] [--port 8792] [--dir DIR]
  --live   serve from live/ (built by make-live.py) instead of funnel/
  --dir    serve from another folder (overrides --live)
Binds to 127.0.0.1 only. Python 3 standard library only.
"""
import argparse
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROUTES = {
    '/lead-engine': '01-giveaway-ghl.html',
    '/interview': '06-book-ghl.html',
    '/entered': '02-thankyou-ghl.html',
    '/refer': '04-referral-ghl.html',
    '/claim-second': '03-claim-ghl.html',
    '/claim-third': '05-claim-third-ghl.html',
    '/rules': '07-rules-ghl.html',
}
STUBS = {
    '/privacy': 'Privacy Policy (stub: the real page is a separate GoHighLevel page).',
    '/terms': 'Terms of Service (stub: the real page is a separate GoHighLevel page).',
}
SHELL_HEAD = '<!doctype html><html><head><meta charset="utf-8"></head><body>'
SHELL_FOOT = '</body></html>'


def make_handler(folder):
    class Handler(BaseHTTPRequestHandler):
        server_version = 'gw-dev'

        def _send(self, code, body, ctype='text/html; charset=utf-8', head=False, extra=None):
            data = body.encode('utf-8')
            self.send_response(code)
            self.send_header('Content-Type', ctype)
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()
            if not head:
                self.wfile.write(data)

        def _serve(self, head):
            path = urlsplit(self.path).path
            if len(path) > 1:
                path = path.rstrip('/')
            if path in ('', '/'):
                return self._send(302, '', head=head, extra={'Location': '/lead-engine'})
            name = ROUTES.get(path) or (path[1:] if path[1:] in ROUTES.values() else None)
            if name:
                f = os.path.join(folder, name)
                if not os.path.isfile(f):
                    return self._send(404, f'{name} is not in {folder}', 'text/plain; charset=utf-8', head)
                with open(f, encoding='utf-8') as fh:
                    return self._send(200, SHELL_HEAD + fh.read() + SHELL_FOOT, head=head)
            if path in STUBS:
                return self._send(200, f'{SHELL_HEAD}<p style="font:16px sans-serif;padding:24px">{STUBS[path]}</p>{SHELL_FOOT}', head=head)
            self._send(404, 'Not found. Paths: ' + ' '.join(sorted(ROUTES) + sorted(STUBS)), 'text/plain; charset=utf-8', head)

        def do_GET(self):
            self._serve(False)

        def do_HEAD(self):
            self._serve(True)

        def log_message(self, fmt, *args):
            print('%s %s' % (self.address_string(), fmt % args))

    return Handler


def main():
    ap = argparse.ArgumentParser(description='Serve the giveaway funnel pages with their real paths.')
    ap.add_argument('--live', action='store_true', help='serve from live/ instead of funnel/')
    ap.add_argument('--port', type=int, default=8792)
    ap.add_argument('--dir', help='serve from this folder (overrides --live)')
    a = ap.parse_args()
    folder = os.path.abspath(a.dir) if a.dir else os.path.join(ROOT, 'live' if a.live else 'funnel')
    if not os.path.isdir(folder):
        raise SystemExit(f'dev-server: {folder} does not exist' + (' (run tools/make-live.py first)' if a.live else ''))
    srv = ThreadingHTTPServer(('127.0.0.1', a.port), make_handler(folder))
    print(f'Serving {folder} at http://127.0.0.1:{a.port}/  (Ctrl-C to stop)')
    for p in ROUTES:
        print(f'  http://127.0.0.1:{a.port}{p}')
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
