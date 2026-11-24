"""
Task 19: Pattern Calculation and Build Priority Engine.
Processes all 100 applications from outputs/task-07..16 and work/research-runs/task18-corrections-*.
Calculates reproducible aggregates with explicit numerators and denominators,
surfaces all unknowns, and prioritizes build_now, conditional, outreach, and unknown queues.
"""

import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent.parent

def load_all_records():
    apps_data = json.load(open(ROOT / "data" / "apps.json", "r", encoding="utf-8"))
    roster = apps_data["apps"]
    
    # First-pass records (100 apps)
    first_pass_records = {}
    for t in range(7, 17):
        rec_path = ROOT / "outputs" / f"task-{t:02d}" / "records.json"
        data = json.load(open(rec_path, "r", encoding="utf-8"))
        recs = data if isinstance(data, list) else data.get("records", [])
        for r in recs:
            first_pass_records[r["identity"]["id"]] = r
            
    # Task 18 corrected records (20 sampled apps)
    corr_records = {}
    for t in range(7, 17):
        rec_path = ROOT / "work" / "research-runs" / f"task18-corrections-{t:02d}" / "records.json"
        if rec_path.exists():
            data = json.load(open(rec_path, "r", encoding="utf-8"))
            recs = data if isinstance(data, list) else data.get("records", [])
            for r in recs:
                corr_records[r["identity"]["id"]] = r

    # Sampling manifest
    manifest = json.load(open(ROOT / "outputs" / "task-06" / "sampling-manifest.json", "r", encoding="utf-8"))
    sample_ids = set(manifest.get("selected_ids", []))

    # Authoritative merged records: use corrected record if available, else first-pass
    auth_records = {}
    for aid in range(1, 101):
        if aid in corr_records:
            auth_records[aid] = corr_records[aid]
        else:
            auth_records[aid] = first_pass_records[aid]

    return roster, first_pass_records, corr_records, auth_records, sample_ids

def get_buildability(r):
    b = r.get("buildability", {})
    status = b.get("status")
    val = b.get("value")
    if status == "unknown" or val is None:
        return {
            "verdict": "unknown",
            "scope": None,
            "blockers": b.get("rationale", "Unknown buildability due to unresolved identity/surface"),
            "next_steps": []
        }
    if isinstance(val, dict):
        return {
            "verdict": val.get("verdict", "unknown"),
            "scope": val.get("scope"),
            "blockers": val.get("blockers", []),
            "next_steps": val.get("next_steps", [])
        }
    return {
        "verdict": str(val),
        "scope": None,
        "blockers": [],
        "next_steps": []
    }

def analyze():
    roster, first_pass_records, corr_records, auth_records, sample_ids = load_all_records()
    print(f"Loaded {len(roster)} roster apps, {len(first_pass_records)} first-pass records, {len(auth_records)} authoritative records.")

    # 1. Buildability breakdown
    queues = defaultdict(list)
    for aid in range(1, 101):
        r = auth_records[aid]
        b_info = get_buildability(r)
        verdict = b_info["verdict"]
        queues[verdict].append({
            "app_id": aid,
            "app_name": r["identity"]["app"],
            "category": r["identity"]["category"],
            "buildability": b_info,
            "in_sample": aid in sample_ids
        })

    print("\n--- Buildability Verdicts (Authoritative N=100) ---")
    for v in ["build_now", "conditional", "outreach_required", "unknown"]:
        apps = queues[v]
        print(f"  {v}: {len(apps)}/100 ({len(apps)/100*100:.1f}%)")
        for item in apps:
            if v in ("outreach_required", "unknown"):
                print(f"    - [{item['app_id']:02d}] {item['app_name']} ({item['category']}): {item['buildability']['scope'] or 'N/A'}")

    # 2. Category distribution across queues
    categories = sorted(list(set(r["category"] for r in roster)))
    cat_breakdown = {}
    for cat in categories:
        cat_apps = [auth_records[aid] for aid in range(1, 101) if auth_records[aid]["identity"]["category"] == cat]
        counts = Counter(get_buildability(r)["verdict"] for r in cat_apps)
        cat_breakdown[cat] = {
            "total": len(cat_apps),
            "build_now": counts.get("build_now", 0),
            "conditional": counts.get("conditional", 0),
            "outreach_required": counts.get("outreach_required", 0),
            "unknown": counts.get("unknown", 0),
        }

    # 3. Auth methods analysis
    auth_method_counts = Counter()
    apps_with_oauth = set()
    apps_with_apikey = set()
    apps_with_basic = set()
    apps_with_token = set()
    apps_with_none_or_cli = set()
    apps_with_auth_unknown = set()

    for aid in range(1, 101):
        r = auth_records[aid]
        auth = r.get("auth", {})
        items = auth.get("items", [])
        if not items:
            apps_with_auth_unknown.add(aid)
        for it in items:
            method = it.get("method")
            status = it.get("status")
            if status == "unknown":
                apps_with_auth_unknown.add(aid)
            elif status == "observed":
                auth_method_counts[method] += 1
                m_lower = str(method).lower()
                if "oauth" in m_lower:
                    apps_with_oauth.add(aid)
                elif "api_key" in m_lower or "apikey" in m_lower or "api key" in m_lower:
                    apps_with_apikey.add(aid)
                elif "basic" in m_lower:
                    apps_with_basic.add(aid)
                elif "bearer" in m_lower or "token" in m_lower:
                    apps_with_token.add(aid)
                elif "none" in m_lower or "cli" in m_lower or "local" in m_lower:
                    apps_with_none_or_cli.add(aid)

    # 4. Credential Eligibility Analysis (Testing vs Production)
    cred_stats = {
        "testing": defaultdict(lambda: {"true": 0, "false": 0, "unknown": 0}),
        "production": defaultdict(lambda: {"true": 0, "false": 0, "unknown": 0})
    }
    
    for aid in range(1, 101):
        r = auth_records[aid]
        creds = r.get("credential_eligibility", {})
        for env in ["testing", "production"]:
            env_creds = creds.get(env, {})
            for field in [
                "free_access", "trial_access", "sandbox_access",
                "paid_required", "admin_approval_required", "vendor_approval_required",
                "partner_approval_required", "contact_sales_required", "self_serve"
            ]:
                claim = env_creds.get(field, {})
                status = claim.get("status")
                val = claim.get("value")
                if status == "unknown" or val is None:
                    cred_stats[env][field]["unknown"] += 1
                elif val is True:
                    cred_stats[env][field]["true"] += 1
                elif val is False:
                    cred_stats[env][field]["false"] += 1

    # 5. API Surface Analysis (Protocols & Breadth)
    protocol_counts = Counter()
    breadth_counts = Counter()
    for aid in range(1, 101):
        r = auth_records[aid]
        api = r.get("api_surface", {})
        # protocols
        for p in api.get("protocols", []):
            if isinstance(p, dict):
                if p.get("status") == "observed":
                    protocol_counts[p.get("protocol")] += 1
                elif "protocol" in p:
                    protocol_counts[p.get("protocol")] += 1
            elif isinstance(p, str):
                protocol_counts[p] += 1
        # breadth
        b_claim = api.get("breadth", {})
        b_status = b_claim.get("status")
        b_val = b_claim.get("value")
        if b_status == "unknown" or b_val is None:
            breadth_counts["unknown"] += 1
        else:
            breadth_counts[b_val] += 1

    # 6. MCP Discovery Analysis
    mcp_discovery_counts = Counter()
    apps_with_official_mcp = set()
    apps_with_community_mcp = set()
    apps_with_any_mcp = set()
    
    for aid in range(1, 101):
        r = auth_records[aid]
        mcp = r.get("mcp", {})
        disc = mcp.get("discovery", {})
        status = disc.get("status")
        val = disc.get("value")
        key = f"{status}:{val}"
        mcp_discovery_counts[key] += 1
        
        # Check entries
        entries = mcp.get("entries", [])
        has_official = False
        has_community = False
        for entry in entries:
            kind = entry.get("kind")
            if kind == "official":
                has_official = True
            elif kind == "community":
                has_community = True
        if has_official:
            apps_with_official_mcp.add(aid)
        if has_community:
            apps_with_community_mcp.add(aid)
        if has_official or has_community or val == "found":
            apps_with_any_mcp.add(aid)

    # 7. Unknowns Inventory
    unknowns_inventory = {
        "identity_unresolved": [],
        "purpose_unknown": [],
        "auth_unknown": [],
        "testing_credentials_unknown": defaultdict(list),
        "production_credentials_unknown": defaultdict(list),
        "api_breadth_unknown": [],
        "mcp_unknown": [],
        "mcp_not_found_bounded": [],
        "buildability_unknown": []
    }

    for aid in range(1, 101):
        r = auth_records[aid]
        app_name = r["identity"]["app"]
        
        # Identity
        id_res = r["identity"].get("resolution", {})
        if id_res.get("status") in ("unknown", "disputed") or id_res.get("product_identity") is None:
            unknowns_inventory["identity_unresolved"].append({"id": aid, "app": app_name, "reason": id_res.get("rationale")})
            
        # Purpose
        purp = r.get("purpose", {})
        if purp.get("status") == "unknown":
            unknowns_inventory["purpose_unknown"].append({"id": aid, "app": app_name})
            
        # Auth
        auth_items = r.get("auth", {}).get("items", [])
        if any(it.get("status") == "unknown" for it in auth_items) or not auth_items:
            unknowns_inventory["auth_unknown"].append({"id": aid, "app": app_name})
            
        # Creds
        creds = r.get("credential_eligibility", {})
        for env in ["testing", "production"]:
            env_creds = creds.get(env, {})
            for field in [
                "free_access", "trial_access", "sandbox_access",
                "paid_required", "admin_approval_required", "vendor_approval_required",
                "partner_approval_required", "contact_sales_required", "self_serve"
            ]:
                claim = env_creds.get(field, {})
                if claim.get("status") == "unknown" or claim.get("value") is None:
                    unknowns_inventory[f"{env}_credentials_unknown"][field].append(aid)
                    
        # Breadth
        if r.get("api_surface", {}).get("breadth", {}).get("status") == "unknown":
            unknowns_inventory["api_breadth_unknown"].append({"id": aid, "app": app_name})
            
        # MCP
        mcp_disc = r.get("mcp", {}).get("discovery", {})
        if mcp_disc.get("status") == "unknown":
            unknowns_inventory["mcp_unknown"].append({"id": aid, "app": app_name})
        elif mcp_disc.get("status") == "not_found_in_checked_sources":
            unknowns_inventory["mcp_not_found_bounded"].append({"id": aid, "app": app_name})
            
        # Buildability
        if get_buildability(r)["verdict"] == "unknown":
            unknowns_inventory["buildability_unknown"].append({"id": aid, "app": app_name, "rationale": r.get("buildability", {}).get("rationale")})

    print(f"\nUnknowns Summary:")
    print(f"  Identity unresolved: {len(unknowns_inventory['identity_unresolved'])}/100")
    print(f"  Buildability unknown: {len(unknowns_inventory['buildability_unknown'])}/100")
    print(f"  API Breadth unknown: {len(unknowns_inventory['api_breadth_unknown'])}/100")
    print(f"  MCP unknown: {len(unknowns_inventory['mcp_unknown'])}/100")
    print(f"  MCP not found in checked sources: {len(unknowns_inventory['mcp_not_found_bounded'])}/100")

    return {
        "queues": queues,
        "cat_breakdown": cat_breakdown,
        "auth_methods": {
            "method_counts": dict(auth_method_counts),
            "apps_with_oauth": len(apps_with_oauth),
            "apps_with_apikey": len(apps_with_apikey),
            "apps_with_basic": len(apps_with_basic),
            "apps_with_token": len(apps_with_token),
            "apps_with_none_or_cli": len(apps_with_none_or_cli),
            "apps_with_auth_unknown": len(apps_with_auth_unknown),
        },
        "cred_stats": {env: {f: dict(counts) for f, counts in fields.items()} for env, fields in cred_stats.items()},
        "api_surface": {
            "protocol_counts": dict(protocol_counts),
            "breadth_counts": dict(breadth_counts)
        },
        "mcp_stats": {
            "discovery_counts": dict(mcp_discovery_counts),
            "apps_with_official_mcp": len(apps_with_official_mcp),
            "apps_with_community_mcp": len(apps_with_community_mcp),
            "apps_with_any_mcp": len(apps_with_any_mcp),
            "official_mcp_app_ids": sorted(list(apps_with_official_mcp)),
            "community_mcp_app_ids": sorted(list(apps_with_community_mcp)),
        },
        "unknowns_inventory": {
            k: (v if not isinstance(v, defaultdict) else {f: len(ids) for f, ids in v.items()})
            for k, v in unknowns_inventory.items()
        }
    }

if __name__ == "__main__":
    analyze()
