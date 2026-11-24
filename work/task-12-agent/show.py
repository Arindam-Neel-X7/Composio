"""Read helper: show.py APP URLSUBSTR [FIRST LAST] | grep.py via 'g' mode: show.py APP g REGEX [maxwidth]"""
import json, re, sys
from pathlib import Path
R = Path(__file__).resolve().parents[2] / "work/research-runs/task12-capture-003"
caps = json.load(open(R / "captures.json", encoding="utf8"))
app = int(sys.argv[1]); mode = sys.argv[2]
mine = [c for c in caps if c["spec"]["app_id"] == app]
def lines(c): return (R / c["snapshot_ref"]).read_text(encoding="utf8").splitlines()
if mode == "g":
    rx = re.compile(sys.argv[3], re.I); w = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    import os
    flt = os.environ.get("URLFLT")
    for c in mine:
        if c["spec"]["url"].endswith("openapi.json") or (flt and flt not in c["spec"]["url"]): continue
        tail = c["spec"]["url"].split("//")[1][-45:]
        for i, l in enumerate(lines(c), 1):
            if rx.search(l): print(f"[{tail}] {i}: {l[:w]}")
else:
    m = [c for c in mine if mode in c["spec"]["url"]]
    c = [x for x in m if x["spec"]["url"].endswith(mode)] or m
    c = c[0]; L = lines(c)
    a = int(sys.argv[3]) if len(sys.argv) > 3 else 1; b = int(sys.argv[4]) if len(sys.argv) > 4 else len(L)
    w = int(sys.argv[5]) if len(sys.argv) > 5 else 300
    print("##", c["spec"]["url"], len(L))
    for i in range(a, min(b, len(L)) + 1): print(f"{i}: {L[i-1][:w]}")
