"""
Analysis script to examine gating blockers, MCP details, and queue rankings across all 100 apps.
"""

import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent.parent

def load_data():
    first_pass_records = {}
    for t in range(7, 17):
        rec_path = ROOT / "outputs" / f"task-{t:02d}" / "records.json"
        for r in json.load(open(rec_path, "r", encoding="utf-8")):
            first_pass_records[r["identity"]["id"]] = r
            
    corr_records = {}
    for t in range(7, 17):
        rec_path = ROOT / "work" / "research-runs" / f"task18-corrections-{t:02d}" / "records.json"
        if rec_path.exists():
            for r in json.load(open(rec_path, "r", encoding="utf-8")):
                corr_records[r["identity"]["id"]] = r

    auth_records = {}
    for aid in range(1, 101):
        auth_records[aid] = corr_records.get(aid, first_pass_records[aid])

    return auth_records

def inspect_queues_and_blockers():
    auth_records = load_data()
    
    queues = defaultdict(list)
    for aid in range(1, 101):
        r = auth_records[aid]
        b = r.get("buildability", {})
        val = b.get("value")
        status = b.get("status")
        if status == "unknown" or val is None:
            verdict = "unknown"
            scope = None
            blockers = [b.get("rationale", "")]
            next_steps = []
        else:
            verdict = val.get("verdict", "unknown")
            scope = val.get("scope")
            blockers = val.get("blockers", [])
            next_steps = val.get("next_steps", [])
            
        queues[verdict].append({
            "id": aid,
            "app": r["identity"]["app"],
            "category": r["identity"]["category"],
            "scope": scope,
            "blockers": blockers,
            "next_steps": next_steps,
            "record": r
        })
        
    print(f"Queues summary: build_now={len(queues['build_now'])}, conditional={len(queues['conditional'])}, outreach={len(queues['outreach_required'])}, unknown={len(queues['unknown'])}")
    
    # Analyze blockers in 'conditional'
    blocker_categories = defaultdict(list)
    for item in queues["conditional"]:
        b_texts = " ".join(item["blockers"]).lower()
        creds = item["record"].get("credential_eligibility", {})
        prod = creds.get("production", {})
        test = creds.get("testing", {})
        
        # Classify main gating condition
        if prod.get("partner_approval_required", {}).get("value") is True or "partner" in b_texts:
            blocker_categories["partner_approval_or_program"].append(item["id"])
        elif prod.get("vendor_approval_required", {}).get("value") is True or "vendor approval" in b_texts or "app review" in b_texts or "verification" in b_texts:
            blocker_categories["vendor_or_platform_approval"].append(item["id"])
        elif prod.get("admin_approval_required", {}).get("value") is True or "admin" in b_texts or "workspace" in b_texts or "organization" in b_texts:
            blocker_categories["tenant_admin_or_org_scope"].append(item["id"])
        elif prod.get("paid_required", {}).get("value") is True or "paid" in b_texts or "subscription" in b_texts:
            blocker_categories["paid_subscription_required"].append(item["id"])
        else:
            blocker_categories["other_or_rate_limit"].append(item["id"])
            
    print("\nConditional Gating Conditions Breakdown:")
    for k, ids in blocker_categories.items():
        print(f"  {k}: {len(ids)} apps (IDs: {ids})")
        
    # Analyze build_now sub-tiering (e.g. MCP available vs Clean REST)
    mcp_build_now = []
    rest_build_now = []
    cli_build_now = []
    
    for item in queues["build_now"]:
        mcp = item["record"].get("mcp", {})
        mcp_val = mcp.get("discovery", {}).get("value")
        entries = mcp.get("entries", [])
        has_mcp = mcp_val == "found" or len(entries) > 0
        
        # Check CLI
        auth_items = item["record"].get("auth", {}).get("items", [])
        is_cli = any("cli" in str(it.get("method")).lower() or "none" in str(it.get("method")).lower() for it in auth_items)
        
        if has_mcp:
            mcp_build_now.append(item["id"])
        elif is_cli:
            cli_build_now.append(item["id"])
        else:
            rest_build_now.append(item["id"])
            
    print("\nBuild Now Sub-Tiering:")
    print(f"  Tier 1A (Existing MCP Server ready): {len(mcp_build_now)} apps (IDs: {mcp_build_now})")
    print(f"  Tier 1B (Standard REST / API Key / OAuth2 wrapper): {len(rest_build_now)} apps (IDs: {rest_build_now})")
    print(f"  Tier 1C (Local CLI / Tool execution): {len(cli_build_now)} apps (IDs: {cli_build_now})")

if __name__ == "__main__":
    inspect_queues_and_blockers()
