"""Probe candidate public URLs (lead discovery only; not evidence)."""
import sys, urllib.request, concurrent.futures as cf

URLS = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip() and not l.startswith("#")]

def probe(u):
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 composio-research-probe"})
        with urllib.request.urlopen(req, timeout=15) as r:
            b = r.read(400000)
            return u, r.status, len(b), r.headers.get("content-type", "")[:30]
    except Exception as e:
        return u, getattr(e, "code", "ERR"), 0, str(e)[:50]

with cf.ThreadPoolExecutor(8) as ex:
    for res in ex.map(probe, URLS):
        print(*res, sep=" | ")
