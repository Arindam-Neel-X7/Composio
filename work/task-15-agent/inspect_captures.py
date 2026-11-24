import json
from pathlib import Path

RUN_DIR = Path("work/research-runs/task15-capture-003")
captures = json.loads((RUN_DIR / "captures.json").read_text(encoding="utf-8"))
records = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))

for r in records:
    aid = r["identity"]["id"]
    app = r["identity"]["app"]
    cs = [x for x in captures if x["spec"]["app_id"] == aid]
    fails = [f for f in r["fetches"] if f["status"] != "fetched"]
    print(f"\n[{aid}] {app}: {len(cs)} captures, {len(fails)} failed fetches")
    for x in cs:
        print(f"  OK ({x['line_count']:5d}L) [{x['spec']['kind']}] env={x['spec']['environments']} {x['spec']['url']} -> {x['snapshot_ref']}")
    for f in fails:
        print(f"  FAIL ({f['status']} {f['http_status']}) {f['source_url']} err={f['error']}")
