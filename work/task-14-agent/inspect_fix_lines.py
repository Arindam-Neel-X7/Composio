import json, pathlib

d = pathlib.Path("work/research-runs/task14-first-pass-002")
caps = json.loads((d / "captures.json").read_text(encoding="utf-8"))

def show(aid, url_part, lo, hi):
    for c in caps:
        if c["spec"]["app_id"] == aid and url_part in c["spec"]["url"]:
            lines = (d / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
            print(f"=== {aid} {c['spec']['url']} L{lo}-{hi} ===")
            for i in range(max(1, lo), min(len(lines), hi) + 1):
                print(f"  {i:3d}: {lines[i-1][:120]}")

show(71, "reference/intro", 78, 86)
show(71, "docs/authorization", 118, 126)
show(76, "apps/docs/oauth", 175, 228)
show(77, "What-is-ClickUp-MCP", 39, 59)
show(77, "reference/gettasks", 8, 15)
show(79, "smartsheet/introduction", 75, 82)
show(79, "basics/authentication", 98, 104)
show(80, "overview/general", 11, 22)
show(80, "authentication/authentication", 33, 42)
show(80, "authentication/authentication", 90, 108)
