"""Inspect capture results and fetch failures for a Task 11 capture run."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "task11-capture-002"
RUN_DIR = ROOT / "work/research-runs" / RUN_ID

captures = json.loads((RUN_DIR / "captures.json").read_text(encoding="utf-8"))
records = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))

print(f"=== {RUN_ID}: {len(captures)} captures ===")
by_app = {}
for c in captures:
    aid = c["spec"]["app_id"]
    by_app.setdefault(aid, []).append(c)

for r in records:
    aid = r["identity"]["id"]
    app = r["identity"]["app"]
    caps = by_app.get(aid, [])
    cap_urls = {c["spec"]["url"] for c in caps}
    fails = [f for f in r["fetches"] if f["source_url"] not in cap_urls]
    print(f"\n[{aid}] {app}: {len(caps)} captured, {len(fails)} failed fetches")
    for c in caps:
        print(f"  OK  lines={c['line_count']:4d}  {c['spec']['url']}  -> {c['snapshot_ref']}")
    seen = set()
    for f in fails:
        u = f["source_url"]
        if u in seen:
            continue
        seen.add(u)
        print(f"  ERR {f['status']} http={f['http_status']} {u} :: {f['error']}")
