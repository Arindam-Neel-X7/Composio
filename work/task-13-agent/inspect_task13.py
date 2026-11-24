import json
from pathlib import Path

d = Path("work/research-runs/task13-first-pass-002")
caps = json.loads((d / "captures.json").read_text(encoding="utf-8"))
recs = json.loads((d / "records.json").read_text(encoding="utf-8"))
print(f"Total captures: {len(caps)}")
for i, c in enumerate(caps):
    sp = c["spec"]
    print(f"[{i:02d}] app={sp['app_id']} kind={sp['kind']} lines={c['line_count']} url={sp['url']}")

ck = {(c["spec"]["app_id"], c["spec"]["url"]) for c in caps}
print("\n--- Uncaptured / Failed fetches ---")
for r in recs:
    aid = r["identity"]["id"]
    seen = set()
    for f in r["fetches"]:
        u = f["source_url"]
        if (aid, u) not in ck and u not in seen:
            latest = [x for x in r["fetches"] if x["source_url"] == u][-1]
            seen.add(u)
            print(f"app={aid} status={latest['status']} http={latest['http_status']} url={u} err={latest['error']}")
