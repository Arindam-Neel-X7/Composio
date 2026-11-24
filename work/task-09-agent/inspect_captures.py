"""Inspect captured snapshots, detect unreadable/binary/shell files, and list failures."""
import json
import sys
from pathlib import Path

run_id = sys.argv[1] if len(sys.argv) > 1 else "task09-capture-002"
d = Path("work/research-runs") / run_id
caps = json.loads((d / "captures.json").read_text(encoding="utf-8"))
recs = json.loads((d / "records.json").read_text(encoding="utf-8"))

print(f"=== {run_id}: {len(caps)} CAPTURES ===")
for c in sorted(caps, key=lambda x: (x["spec"]["app_id"], x["spec"]["url"])):
    snap = d / c["snapshot_ref"]
    txt = snap.read_text(encoding="utf-8", errors="replace")
    non_ascii = sum(1 for ch in txt[:500] if ord(ch) > 127)
    flag = " [BINARY/GARBLED?]" if non_ascii > 150 else (" [SHORT]" if c["line_count"] < 20 else "")
    print(f"{c['spec']['app_id']:2d} | {c['line_count']:5d} lines | {c['snapshot_ref']:25s} | {c['spec']['url']}{flag}")

cap_keys = {(c["spec"]["app_id"], c["spec"]["url"]) for c in caps}
print("\n=== FAILED ===")
for r in recs:
    aid = r["identity"]["id"]
    urls = sorted({f["source_url"] for f in r["fetches"]})
    for u in urls:
        if (aid, u) not in cap_keys:
            latest = [f for f in r["fetches"] if f["source_url"] == u][-1]
            print(f"{aid:2d} | {latest['status']:10s} | {str(latest['http_status']):4s} | {u} | {latest['error']}")
