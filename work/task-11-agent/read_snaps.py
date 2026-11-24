"""Helper to inspect numbered lines of captured snapshots in task11-capture-004."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_DIR = ROOT / "work/research-runs/task11-capture-004"
captures = json.loads((RUN_DIR / "captures.json").read_text(encoding="utf-8"))

mode = sys.argv[1]
app_id = int(sys.argv[2])

app_caps = [c for c in captures if c["spec"]["app_id"] == app_id]

if mode == "list":
    for idx, c in enumerate(app_caps):
        print(f"[{idx}] lines={c['line_count']:5d}  {c['spec']['url']}  ({c['snapshot_ref']})")
elif mode == "head":
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 60
    for idx, c in enumerate(app_caps):
        print(f"\n=== [{idx}] {c['spec']['url']} (lines={c['line_count']}) ===")
        lines = (RUN_DIR / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines[:n], 1):
            print(f"{i:5d}: {line[:220]}")
elif mode == "grep":
    pattern = sys.argv[3]
    rx = re.compile(pattern, re.I)
    for idx, c in enumerate(app_caps):
        lines = (RUN_DIR / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
        hits = [(i, line) for i, line in enumerate(lines, 1) if rx.search(line)]
        if hits:
            print(f"\n=== [{idx}] {c['spec']['url']} ({len(hits)} hits) ===")
            for i, line in hits[:45]:
                print(f"{i:5d}: {line[:220]}")
elif mode == "range":
    idx = int(sys.argv[3])
    start = int(sys.argv[4])
    end = int(sys.argv[5])
    c = app_caps[idx]
    print(f"=== [{idx}] {c['spec']['url']} lines {start}-{end} ===")
    lines = (RUN_DIR / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
    for i in range(max(1, start), min(len(lines), end) + 1):
        print(f"{i:5d}: {lines[i-1]}")
