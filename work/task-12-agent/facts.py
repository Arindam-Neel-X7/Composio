"""Compact topic grep: facts.py APP [topics comma] [per_topic] [width]"""
import json, re, sys, os
from pathlib import Path
R = Path(__file__).resolve().parents[2] / "work/research-runs/task12-capture-003"
caps = json.load(open(R / "captures.json", encoding="utf8"))
T = {
 "auth": r"api[ _-]?key|bearer|oauth|basic auth|authorization:|access token|api token|x-api-key|login.*password|client[_ ]id",
 "free": r"free (tier|plan|credit|trial|account|forever)|trial|sandbox|no credit card|\$0|free usage|test mode",
 "paid": r"pay[- ]as[- ]you[- ]go|paid plan|subscription|minimum (deposit|payment|spend)|per month|/mo\b|starting (at|from)|credits? (are|is)",
 "gate": r"contact (sales|us)|talk to sales|book a (call|demo)|enterprise (plan|only|customers)|approval|apply|verification|kyc|waitlist|request access|available (on|for|only)",
 "mcp": r"mcp|model context protocol",
 "api": r"rest(ful)? api|graphql|openapi|swagger|sdk|webhook|endpoint|cli\b|command[- ]line|postman",
}
app = int(sys.argv[1]); topics = (sys.argv[2] if len(sys.argv) > 2 else ",".join(T)).split(",")
per = int(sys.argv[3]) if len(sys.argv) > 3 else 4; w = int(sys.argv[4]) if len(sys.argv) > 4 else 150
flt = os.environ.get("URLFLT")
for t in topics:
    rx = re.compile(T.get(t, t), re.I); n = 0; print("==", t)
    for c in caps:
        if c["spec"]["app_id"] != app or c["spec"]["url"].endswith("openapi.json"): continue
        if flt and flt not in c["spec"]["url"]: continue
        for i, l in enumerate((R / c["snapshot_ref"]).read_text(encoding="utf8").splitlines(), 1):
            if rx.search(l) and len(l) > 25:
                print(f"[{c['spec']['url'].split('//')[1][-38:]}] {i}: {l[:w]}"); n += 1
                if n >= per: break
        if n >= per: break
