"""Dump numbered lines of captured snapshots for one app ID, with optional keyword filter."""
import json
import sys
from pathlib import Path

run_id = sys.argv[1]
app_id = int(sys.argv[2])
max_lines = int(sys.argv[3]) if len(sys.argv) > 3 else 120
keywords = [k.lower() for k in sys.argv[4:]]

d = Path("work/research-runs") / run_id
caps = [c for c in json.load(open(d / "captures.json", encoding="utf-8")) if c["spec"]["app_id"] == app_id]
print(f"=== APP {app_id} ({len(caps)} captures) ===")
for i, c in enumerate(caps):
    snap = d / c["snapshot_ref"]
    lines = snap.read_text(encoding="utf-8").splitlines()
    print(f"\n--- [{i}] ({len(lines)}L) {c['spec']['url']} ({c['spec']['kind']}, envs={c['spec']['environments']}) ---")
    if keywords:
        matched = set()
        for idx, line in enumerate(lines, 1):
            low = line.lower()
            if any(k in low for k in keywords):
                for j in range(max(1, idx - 1), min(len(lines), idx + 2) + 1):
                    matched.add(j)
        shown = sorted(matched)[:max_lines]
        for ln in shown:
            print(f"{ln:4d}: {lines[ln-1][:200]}")
    else:
        for ln in range(1, min(len(lines), max_lines) + 1):
            print(f"{ln:4d}: {lines[ln-1][:200]}")
