"""Inspect captures and failed fetches for a run."""
import json
import sys
from pathlib import Path

run_id = sys.argv[1]
d = Path("work/research-runs") / run_id
caps = json.load(open(d / "captures.json", encoding="utf-8"))
recs = json.load(open(d / "records.json", encoding="utf-8"))

print(f"RUN: {run_id} | CAPTURES: {len(caps)}")
by_app = {}
for c in caps:
    by_app.setdefault(c["spec"]["app_id"], []).append(c)

cap_urls = {(c["spec"]["app_id"], c["spec"]["url"]) for c in caps}
for r in recs:
    aid = r["identity"]["id"]
    app = r["identity"]["app"]
    print(f"\n=== [{aid}] {app} ===")
    for c in by_app.get(aid, []):
        snap = d / c["snapshot_ref"]
        lines = snap.read_text(encoding="utf-8").splitlines()
        preview = " | ".join(lines[:2])[:110]
        print(f"  OK  ({len(lines):4d}L) {c['spec']['url']}  [{c['snapshot_ref']}]")
        print(f"      -> {preview}")
    seen_err = set()
    for f in r["fetches"]:
        u = f["source_url"]
        if (aid, u) not in cap_urls and u not in seen_err:
            # Find the latest fetch for this URL
            latest = [x for x in r["fetches"] if x["source_url"] == u][-1]
            seen_err.add(u)
            print(f"  ERR ({latest['http_status']}) {latest['status']} {u} -> {latest['error']}")
