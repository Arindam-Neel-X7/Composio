import json
import pathlib
import re
import sys

RUN = pathlib.Path("work/research-runs/task10-capture-004")
caps = json.loads((RUN / "captures.json").read_text(encoding="utf-8"))
app_ids = [int(x) for x in sys.argv[1:]]

PAT = re.compile(
    r"(oauth|api[ _-]?key|bearer|basic|token|auth|scope|free|trial|sandbox|paid|pricing|plan|\$|review|approv|tier|access level|limited access|full access|standard access|development tier|mcp|model context|rest|graphql|grpc|rpc|sdk|endpoint|rate limit|campaign|ad set|contact|audience|email|pin|board|thread|funnel|webhook|template|insight|report|partner|vendor|admin|self-serve|developer|test account|explorer|business verification|system user)",
    re.I,
)

for aid in app_ids:
    print(f"================ APP {aid} ================")
    for c in [x for x in caps if x["spec"]["app_id"] == aid]:
        url = c["spec"]["url"]
        snap = c["snapshot_ref"]
        lines = (RUN / snap).read_text(encoding="utf-8", errors="replace").splitlines()
        print(f"\n--- [{c['spec']['kind']}] {url} ({len(lines)}L) ---")
        shown = 0
        for idx, line in enumerate(lines, 1):
            s = line.strip()
            if not s:
                continue
            if idx <= 12 or PAT.search(s):
                if shown < 95:
                    print(f"L{idx}: {s[:200]}")
                    shown += 1
        if shown >= 95:
            print(f"... (truncated after 95 matching lines; total {len(lines)}L)")
