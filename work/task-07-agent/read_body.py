"""Print exact numbered lines for specified (app_id, url_substr, start, end) slices."""
import json
import sys
from pathlib import Path

run_id = sys.argv[1]
d = Path("work/research-runs") / run_id
caps = json.load(open(d / "captures.json", encoding="utf-8"))

for spec in sys.argv[2:]:
    aid_s, substr, s_s, e_s = spec.split("|")
    aid, s, e = int(aid_s), int(s_s), int(e_s)
    matches = [c for c in caps if c["spec"]["app_id"] == aid and substr in c["spec"]["url"]]
    if not matches:
        print(f"!!! NOT FOUND: {spec}")
        continue
    c = matches[0]
    lines = (d / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
    print(f"\n=== [{aid}] {c['spec']['url']} ({len(lines)}L) lines:{s}-{min(e, len(lines))} ===")
    for ln in range(s, min(e, len(lines)) + 1):
        print(f"{ln:4d}: {lines[ln-1][:220]}")
