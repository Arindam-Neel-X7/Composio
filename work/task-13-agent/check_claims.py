"""Spot-check cited line ranges for key claims in task13-first-pass-002."""
import json
from pathlib import Path

RUN_DIR = Path("D:/Composio/work/research-runs/task13-first-pass-002")
recs = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))

# Check for any suspicious patterns: empty observations, bad locators, or questionable eligibility flags
for r in recs:
    aid = r["identity"]["id"]
    app = r["identity"]["app"]
    print(f"=== {aid} {app} ===")
    print(f"  identity: {r['identity']['resolution']['value']}")
    print(f"  purpose:  {r['purpose']['value']}")
    print(f"  auth ({len(r['auth']['items'])}): " + ", ".join(f"{a['claim_id']}={a['value']['method']}" for a in r["auth"]["items"]))
    for env in ("testing", "production"):
        obs = {k: v["value"] for k, v in r["credential_eligibility"][env].items() if isinstance(v, dict) and v["status"] == "observed"}
        print(f"  {env}: {obs}")
    protos = [p["value"] for p in r["api_surface"]["protocols"]["items"]]
    groups = [g["value"] for g in r["api_surface"]["resource_groups"]["items"]]
    print(f"  api: protos={protos}, breadth={r['api_surface']['breadth']['value']}, groups={len(groups)}")
    mcp_e = [(e["value"]["origin"], e["value"]["name"], e["value"]["server_url"], e["value"]["repository_url"], e["value"]["operational_check"]["status"]) for e in r["mcp"]["entries"]]
    print(f"  mcp ({r['mcp']['discovery']['status']}): {mcp_e}")
    print(f"  buildability: {r['buildability']['value']['verdict']} | scope={r['buildability']['value']['scope']}")
