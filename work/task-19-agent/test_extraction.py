"""
Comprehensive field audit test across all 100 apps.
Verifies every field extractor works without errors and prints exact tallies.
"""

import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent.parent

def run_audit():
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

    print("--- 1. Identity Resolution ---")
    id_statuses = Counter()
    unresolved_apps = []
    for aid in range(1, 101):
        r = auth_records[aid]
        res = r["identity"].get("resolution", {})
        status = res.get("status")
        val = res.get("value")
        id_statuses[status] += 1
        if status != "observed" or val is None:
            unresolved_apps.append((aid, r["identity"]["app"], status, val))
    print(f"Identity resolution statuses: {dict(id_statuses)}")
    print(f"Unresolved apps ({len(unresolved_apps)}): {unresolved_apps}")

    print("\n--- 2. Purpose ---")
    purpose_statuses = Counter()
    for aid in range(1, 101):
        r = auth_records[aid]
        p = r.get("purpose", {})
        purpose_statuses[p.get("status")] += 1
    print(f"Purpose statuses: {dict(purpose_statuses)}")

    print("\n--- 3. Auth Methods ---")
    auth_methods = Counter()
    apps_by_auth_type = defaultdict(set)
    for aid in range(1, 101):
        r = auth_records[aid]
        items = r.get("auth", {}).get("items", [])
        if not items:
            apps_by_auth_type["none_or_missing"].add(aid)
        for it in items:
            st = it.get("status")
            val = it.get("value")
            if isinstance(val, dict):
                m = val.get("method")
            elif isinstance(val, str):
                m = val
            else:
                m = it.get("method")
            auth_methods[f"{st}:{m}"] += 1
            if st == "observed" and m:
                m_str = str(m).lower()
                if "oauth" in m_str:
                    apps_by_auth_type["oauth"].add(aid)
                elif "api_key" in m_str or "apikey" in m_str or "api key" in m_str:
                    apps_by_auth_type["api_key"].add(aid)
                elif "bearer" in m_str or "token" in m_str:
                    apps_by_auth_type["token"].add(aid)
                elif "basic" in m_str:
                    apps_by_auth_type["basic"].add(aid)
                elif "cli" in m_str or "none" in m_str or "local" in m_str:
                    apps_by_auth_type["cli_or_none"].add(aid)
                else:
                    apps_by_auth_type["other"].add(aid)
            elif st == "unknown":
                apps_by_auth_type["unknown"].add(aid)
    print(f"Raw auth method counts: {dict(auth_methods)}")
    print("Unique apps by auth category:")
    for k, s in sorted(apps_by_auth_type.items()):
        print(f"  {k}: {len(s)}/100 apps ({len(s)/100*100:.1f}%)")

    print("\n--- 4. Credential Eligibility ---")
    cred_summary = {}
    for env in ["testing", "production"]:
        cred_summary[env] = {}
        for field in [
            "free_access", "trial_access", "sandbox_access",
            "paid_required", "admin_approval_required", "vendor_approval_required",
            "partner_approval_required", "contact_sales_required", "self_serve"
        ]:
            counts = Counter()
            for aid in range(1, 101):
                claim = auth_records[aid].get("credential_eligibility", {}).get(env, {}).get(field, {})
                st = claim.get("status")
                val = claim.get("value")
                if st == "unknown" or val is None:
                    counts["unknown"] += 1
                elif val is True:
                    counts["true"] += 1
                elif val is False:
                    counts["false"] += 1
                else:
                    counts[str(val)] += 1
            cred_summary[env][field] = dict(counts)
            print(f"  [{env}] {field}: true={counts['true']}, false={counts['false']}, unknown={counts['unknown']} (Total: {sum(counts.values())})")

    print("\n--- 5. API Surface (Protocols & Breadth) ---")
    proto_counts = Counter()
    apps_by_proto = defaultdict(set)
    for aid in range(1, 101):
        api = auth_records[aid].get("api_surface", {})
        for p in api.get("protocols", []):
            if isinstance(p, dict):
                proto = p.get("value", {}).get("protocol") if isinstance(p.get("value"), dict) else p.get("protocol")
                st = p.get("status")
            else:
                proto = str(p)
                st = "observed"
            if proto:
                proto_counts[f"{st}:{proto}"] += 1
                if st == "observed":
                    p_lower = proto.lower()
                    if "rest" in p_lower:
                        apps_by_proto["REST"].add(aid)
                    elif "graphql" in p_lower:
                        apps_by_proto["GraphQL"].add(aid)
                    elif "grpc" in p_lower:
                        apps_by_proto["gRPC"].add(aid)
                    elif "sdk" in p_lower or "cli" in p_lower:
                        apps_by_proto["SDK/CLI"].add(aid)
                    elif "webhook" in p_lower:
                        apps_by_proto["Webhook"].add(aid)
                    elif "soap" in p_lower:
                        apps_by_proto["SOAP"].add(aid)
                    else:
                        apps_by_proto[proto].add(aid)

    print(f"Raw protocol counts: {dict(proto_counts)}")
    print("Unique apps by protocol:")
    for k, s in sorted(apps_by_proto.items()):
        print(f"  {k}: {len(s)}/100 apps ({len(s)/100*100:.1f}%)")

    breadth_counts = Counter()
    for aid in range(1, 101):
        b = auth_records[aid].get("api_surface", {}).get("breadth", {})
        st = b.get("status")
        val = b.get("value")
        if st == "unknown" or val is None:
            breadth_counts["unknown"] += 1
        else:
            breadth_counts[val] += 1
    print(f"API Breadth: {dict(breadth_counts)}")

    print("\n--- 6. MCP Discovery ---")
    mcp_disc = Counter()
    mcp_official = set()
    mcp_community = set()
    mcp_any = set()
    for aid in range(1, 101):
        mcp = auth_records[aid].get("mcp", {})
        d = mcp.get("discovery", {})
        st = d.get("status")
        val = d.get("value")
        mcp_disc[f"{st}:{val}"] += 1
        
        entries = mcp.get("entries", [])
        for e in entries:
            kind = e.get("kind") or (e.get("value", {}).get("kind") if isinstance(e.get("value"), dict) else None)
            if kind == "official":
                mcp_official.add(aid)
            elif kind == "community":
                mcp_community.add(aid)
        if st == "observed" and val == "found":
            mcp_any.add(aid)
        if len(entries) > 0:
            mcp_any.add(aid)

    print(f"MCP discovery claims: {dict(mcp_disc)}")
    print(f"Apps with Official MCP: {len(mcp_official)}/100 ({len(mcp_official)/100*100:.1f}%)")
    print(f"Apps with Community MCP: {len(mcp_community)}/100 ({len(mcp_community)/100*100:.1f}%)")
    print(f"Apps with Any MCP (Official or Community or Found): {len(mcp_any)}/100 ({len(mcp_any)/100*100:.1f}%)")

    print("\n--- 7. Buildability Verdicts ---")
    b_counts = Counter()
    for aid in range(1, 101):
        b = auth_records[aid].get("buildability", {})
        st = b.get("status")
        val = b.get("value")
        if st == "unknown" or val is None:
            verdict = "unknown"
        elif isinstance(val, dict):
            verdict = val.get("verdict", "unknown")
        else:
            verdict = str(val)
        b_counts[verdict] += 1
    print(f"Buildability counts: {dict(b_counts)}")

if __name__ == "__main__":
    run_audit()
