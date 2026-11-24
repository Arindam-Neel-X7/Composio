import json
import pathlib
import sys

run_id = sys.argv[1] if len(sys.argv) > 1 else "task10-capture-002"
run = pathlib.Path("work/research-runs") / run_id
caps = json.loads((run / "captures.json").read_text(encoding="utf-8"))
recs = json.loads((run / "records.json").read_text(encoding="utf-8"))
cap_map = {(c["spec"]["app_id"], c["spec"]["url"]): c for c in caps}
print(f"RUN: {run_id} | TOTAL CAPTURED: {len(caps)}")
for r in recs:
    aid = r["identity"]["id"]
    name = r["identity"]["app"]
    print(f"\n=== {aid}: {name} ===")
    seen = set()
    for f in r["fetches"]:
        u = f["source_url"]
        if u in seen:
            continue
        seen.add(u)
        if (aid, u) in cap_map:
            c = cap_map[(aid, u)]
            txt = (run / c["snapshot_ref"]).read_text(encoding="utf-8", errors="replace")
            lines = txt.splitlines()
            first = lines[0][:90] if lines else ""
            # Check for replacement chars / binary garbage
            bad = txt.count("\ufffd")
            flag = f" [BAD_CHARS:{bad}]" if bad > 10 else ""
            print(f"  OK   [{c['line_count']:4d}L]{flag} {u} -> {c['snapshot_ref']} | {first}")
        else:
            last = [x for x in r["fetches"] if x["source_url"] == u][-1]
            print(f"  FAIL [{last['status']}:{last['http_status']}] {u} | {last['error']}")
