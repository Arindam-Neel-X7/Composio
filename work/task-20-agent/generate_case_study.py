"""
Task 20: Self-Contained Case Study Generator
Generates a single, zero-dependency, offline-ready HTML case study with:
- Two-minute executive overview & headline findings
- Interactive searchable & filterable 100-app coverage matrix with slide-over detail drawer
- Cross-cutting patterns, auth landscape, testing vs. production gating divergence, MCP reality
- Four-tier immutability architecture, channel separation, human verification (Task 17 & 18), error case studies
- Full visibility of unknowns inventory & prioritized build roadmap
- Reproducibility & CLI run instructions, misses, gaps, and limitations

Outputs:
- outputs/task-20/index.html
- index.html (workspace root copy for direct serving/preview)
"""

import json
import html
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent.parent
OUT_DIR = ROOT / "outputs" / "task-20"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def collect_evidence_urls(rec: dict) -> list:
    urls = []
    seen = set()

    def walk(obj):
        if isinstance(obj, dict):
            if "source_url" in obj and isinstance(obj["source_url"], str) and obj["source_url"].startswith("http"):
                u = obj["source_url"].strip()
                if u not in seen:
                    seen.add(u)
                    urls.append(u)
            if "repository_url" in obj and isinstance(obj["repository_url"], str) and obj["repository_url"].startswith("http"):
                u = obj["repository_url"].strip()
                if u not in seen:
                    seen.add(u)
                    urls.append(u)
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(rec)
    return urls


def extract_gating(env_dict: dict) -> dict:
    dims = [
        "self_serve",
        "free_access",
        "trial_access",
        "sandbox_access",
        "paid_required",
        "admin_approval_required",
        "vendor_approval_required",
        "partner_approval_required",
        "contact_sales_required",
    ]
    out = {}
    for d in dims:
        c = env_dict.get(d, {})
        if isinstance(c, dict):
            out[d] = {
                "status": c.get("status", "unknown"),
                "value": c.get("value"),
                "rationale": c.get("rationale", ""),
            }
        else:
            out[d] = {"status": "unknown", "value": None, "rationale": ""}
    return out


def build_dataset():
    roster = load_json(ROOT / "data" / "apps.json")["apps"]
    aggregates = load_json(ROOT / "outputs" / "task-19" / "aggregates.json")
    build_queues = load_json(ROOT / "outputs" / "task-19" / "build-queues.json")
    baseline_metrics = load_json(ROOT / "outputs" / "task-17" / "human-baseline-metrics.json")
    paired_metrics = load_json(ROOT / "outputs" / "task-18" / "paired-comparison-metrics.json")
    manifest = load_json(ROOT / "outputs" / "task-06" / "sampling-manifest.json")
    sample_ids = set(manifest.get("selected_ids", []))

    # Load authoritative records (80 first-pass + 20 Task 18 corrected)
    first_pass = {}
    for t in range(7, 17):
        p = ROOT / "outputs" / f"task-{t:02d}" / "records.json"
        for r in load_json(p):
            first_pass[r["identity"]["id"]] = r

    corrected = {}
    for t in range(7, 17):
        p = ROOT / "work" / "research-runs" / f"task18-corrections-{t:02d}" / "records.json"
        if p.exists():
            for r in load_json(p):
                corrected[r["identity"]["id"]] = r

    # Index queue items by app_id
    queue_by_id = {}
    for q_name, items in build_queues.items():
        for item in items:
            item_copy = dict(item)
            item_copy["queue"] = q_name
            queue_by_id[item["app_id"]] = item_copy

    # Index Task 18 transitions by app_id
    transitions_by_id = {}
    for tr in paired_metrics.get("transitions", []):
        transitions_by_id.setdefault(tr["app_id"], []).append(tr)

    apps_payload = []
    for app_meta in roster:
        aid = app_meta["id"]
        rec = corrected.get(aid, first_pass[aid])
        q = queue_by_id[aid]

        # Deduplicate auth methods & protocols while preserving order
        auth_methods = list(dict.fromkeys(q.get("auth_methods", [])))
        protocols = list(dict.fromkeys(q.get("protocols", [])))

        purpose_obj = rec.get("purpose", {})
        purpose_val = purpose_obj.get("value") if isinstance(purpose_obj, dict) else None
        purpose_status = purpose_obj.get("status", "unknown") if isinstance(purpose_obj, dict) else "unknown"

        # MCP detailed entries
        mcp_entries = []
        for e in rec.get("mcp", {}).get("entries", []):
            val = e.get("value")
            if isinstance(val, dict):
                mcp_entries.append({
                    "claim_id": e.get("claim_id", ""),
                    "origin": val.get("origin", "unknown"),
                    "name": val.get("name", "Unnamed MCP Server"),
                    "source_url": val.get("source_url"),
                    "repository_url": val.get("repository_url"),
                    "server_url": val.get("server_url"),
                    "scope": val.get("scope", ""),
                    "operational_status": (
                        val.get("operational_checks", {}).get("status", "not_researched")
                        if isinstance(val.get("operational_checks"), dict)
                        else "not_researched"
                    ),
                })

        cred = rec.get("credential_eligibility", {})
        testing_gating = extract_gating(cred.get("testing", {}))
        prod_gating = extract_gating(cred.get("production", {}))

        build_obj = rec.get("buildability", {})
        build_rationale = build_obj.get("rationale", "") if isinstance(build_obj, dict) else ""

        api_surf = rec.get("api_surface", {})
        pub_docs = api_surf.get("public_documentation", {})
        pub_docs_val = pub_docs.get("value") if isinstance(pub_docs, dict) else None
        res_groups = api_surf.get("resource_groups", [])

        apps_payload.append({
            "id": aid,
            "name": app_meta["app"],
            "category": app_meta["category"],
            "run_id": rec.get("run", {}).get("run_id", ""),
            "in_sample": aid in sample_ids,
            "purpose": purpose_val or "Unresolved / Unknown (see unknowns inventory)",
            "purpose_status": purpose_status,
            "queue": q["queue"],
            "sub_tier": q.get("sub_tier", ""),
            "priority_rank": q.get("priority_rank", 999),
            "scope": q.get("scope") or "",
            "blockers": q.get("blockers", []),
            "next_steps": q.get("next_steps", []),
            "buildability_rationale": build_rationale,
            "auth_methods": auth_methods,
            "auth_notes": rec.get("auth", {}).get("notes", ""),
            "protocols": protocols,
            "breadth": q.get("breadth", "unknown"),
            "public_docs": pub_docs_val,
            "resource_groups_count": len(res_groups) if isinstance(res_groups, list) else 0,
            "mcp_category": q["mcp"]["category"],
            "mcp_status": q["mcp"]["status"],
            "mcp_value": q["mcp"]["value"],
            "mcp_official_count": q["mcp"]["official_count"],
            "mcp_community_count": q["mcp"]["community_count"],
            "mcp_official_servers": q["mcp"]["official_servers"],
            "mcp_community_servers": q["mcp"]["community_servers"],
            "mcp_entries": mcp_entries,
            "testing": testing_gating,
            "production": prod_gating,
            "evidence_urls": collect_evidence_urls(rec)[:12],
            "transitions": transitions_by_id.get(aid, []),
        })

    apps_payload.sort(key=lambda x: x["id"])
    return apps_payload, aggregates, build_queues, baseline_metrics, paired_metrics


def render_category_rows(aggregates: dict) -> str:
    rows = []
    cat_sum = aggregates["category_summary"]
    for cat in sorted(cat_sum.keys()):
        c = cat_sum[cat]
        tot = c["total_apps"]
        bn = c["build_now"]["count"]
        co = c["conditional"]["count"]
        ou = c["outreach_required"]["count"]
        uk = c["unknown"]["count"]

        bn_p = (bn / tot) * 100
        co_p = (co / tot) * 100
        ou_p = (ou / tot) * 100
        uk_p = (uk / tot) * 100

        if bn >= 8:
            dom = "80–90% Self-Serve (API Keys / Free Tiers)"
        elif co == 10:
            dom = "100% Gated (Tenant Admin / Cloud IAM)"
        elif cat == "Finance and Fintech":
            dom = "Compliance / KYC / Regulatory & 2 Unknowns"
        else:
            dom = "Mixed (OAuth Tenant / Vendor Review)"

        bar = (
            f'<div class="stack-bar" title="Build Now: {bn}, Conditional: {co}, Outreach: {ou}, Unknown: {uk}">'
            f'<span class="sb-bn" style="width:{bn_p}%"></span>'
            f'<span class="sb-co" style="width:{co_p}%"></span>'
            f'<span class="sb-ou" style="width:{ou_p}%"></span>'
            f'<span class="sb-uk" style="width:{uk_p}%"></span>'
            f'</div>'
        )
        rows.append(
            f"<tr>"
            f"<td><strong>{html.escape(cat)}</strong></td>"
            f"<td class='num'>{bn}/{tot} ({bn_p:.0f}%)</td>"
            f"<td class='num'>{co}/{tot} ({co_p:.0f}%)</td>"
            f"<td class='num'>{ou}/{tot} ({ou_p:.0f}%)</td>"
            f"<td class='num'>{uk}/{tot} ({uk_p:.0f}%)</td>"
            f"<td class='bar-cell'>{bar}</td>"
            f"<td class='muted'>{html.escape(dom)}</td>"
            f"</tr>"
        )
    return "\n".join(rows)


def render_cred_shift_rows(aggregates: dict) -> str:
    dims = [
        ("self_serve", "Self-Serve Onboarding"),
        ("free_access", "Free Access Tier"),
        ("trial_access", "Time-Limited Trial"),
        ("sandbox_access", "Dedicated Sandbox"),
        ("paid_required", "Paid Plan Required"),
        ("admin_approval_required", "Tenant Admin Approval"),
        ("vendor_approval_required", "Vendor Review / Approval"),
        ("partner_approval_required", "Partner Program Approval"),
        ("contact_sales_required", "Contact Sales Required"),
    ]
    cs = aggregates["cred_summary"]
    rows = []
    for key, label in dims:
        t = cs["testing"][key]
        p = cs["production"][key]
        t_true = t["true"]["count"]
        t_false = t["false"]["count"]
        t_unk = t["unknown"]["count"] + t.get("not_applicable", {}).get("count", 0)
        p_true = p["true"]["count"]
        p_false = p["false"]["count"]
        p_unk = p["unknown"]["count"] + p.get("not_applicable", {}).get("count", 0)
        diff = p_true - t_true
        diff_cls = "shift-warn" if (key in ("paid_required", "admin_approval_required", "vendor_approval_required", "contact_sales_required") and diff > 0) else ("shift-drop" if diff < 0 else "shift-neutral")
        sign = "+" if diff > 0 else ""
        rows.append(
            f"<tr>"
            f"<td><code>{key}</code><div class='sublabel'>{label}</div></td>"
            f"<td class='num'><strong>{t_true}/100</strong></td>"
            f"<td class='num muted'>{t_false}/100</td>"
            f"<td class='num muted'>{t_unk}/100</td>"
            f"<td class='num'><strong>{p_true}/100</strong></td>"
            f"<td class='num muted'>{p_false}/100</td>"
            f"<td class='num muted'>{p_unk}/100</td>"
            f"<td class='num'><span class='shift-pill {diff_cls}'>{sign}{diff}</span></td>"
            f"</tr>"
        )
    return "\n".join(rows)


def render_roadmap_cards(build_queues: dict) -> str:
    bn = build_queues["build_now"]
    co = build_queues["conditional"]
    ou = build_queues["outreach_required"]
    uk = build_queues["unknown"]

    w1a = [x for x in bn if x.get("sub_tier", "").startswith("Wave 1A")]
    w1_rest = [x for x in bn if not x.get("sub_tier", "").startswith("Wave 1A")]

    # Group conditional by gating_condition into two balanced phases summing to 50/50
    co_infra_admin = [
        x for x in co
        if x.get("gating_condition", "") in (
            "Cloud Infrastructure / Usage Quota / Environment Setup",
            "Organization / Tenant Admin Consent Required",
        )
    ]
    co_vendor_paid_partner = [
        x for x in co
        if x.get("gating_condition", "") not in (
            "Cloud Infrastructure / Usage Quota / Environment Setup",
            "Organization / Tenant Admin Consent Required",
        )
    ]

    def fmt_targets(items, limit=12):
        sorted_items = sorted(items, key=lambda x: x["app_id"])
        shown = [f"{html.escape(x['app_name'])} ({x['app_id']})" for x in sorted_items[:limit]]
        suffix = f" +{len(sorted_items) - limit} more" if len(sorted_items) > limit else ""
        return ", ".join(shown) + suffix + "."

    cards = [
        (
            "b-bn",
            f"Phase 1 &bull; Wave 1A &bull; {len(w1a)} Apps",
            "Immediate Drop-In Official MCP Integrations",
            "Self-serve credentials + vendor-maintained official MCP servers ready for immediate runtime registration.",
            "Key Targets",
            fmt_targets(w1a, 14),
        ),
        (
            "b-bn",
            f"Phase 2 &bull; Waves 1B, 1C &amp; 1D &bull; {len(w1_rest)} Apps",
            "Community MCP, Local CLI &amp; Self-Serve REST Tooling",
            "Unblocked self-serve APIs or offline binaries requiring security audit of community MCP wrappers, containerized CLI runners, or thin REST wrappers.",
            "Targets",
            fmt_targets(w1_rest, 12),
        ),
        (
            "b-co",
            f"Phase 3 &bull; Conditional (Admin &amp; Cloud) &bull; {len(co_infra_admin)} Apps",
            "Enterprise Workspaces &amp; Cloud Infrastructure",
            "High-value integrations gated by tenant administrator OAuth consent (13 apps) or cloud IAM/quota/environment provisioning (14 apps).",
            "Key Targets",
            fmt_targets(co_infra_admin, 12),
        ),
        (
            "b-co",
            f"Phase 4 &bull; Conditional (Review, Paid &amp; Partner) &bull; {len(co_vendor_paid_partner)} Apps",
            "Regulated, Paid-Tier &amp; Partner-Reviewed Platforms",
            "Require formal vendor developer review (11 apps), mandatory paid commercial plans (6 apps), or partner ecosystem enrollment (6 apps) before production calls.",
            "Key Targets",
            fmt_targets(co_vendor_paid_partner, 12),
        ),
        (
            "b-ou",
            f"Phase 5 &bull; Queue 3 &bull; {len(ou)} Apps",
            "Commercial Partnerships &amp; Sales Outreach",
            "Enterprise-gated platforms requiring commercial contracting before developer credentials exist.",
            "Targets",
            fmt_targets(ou, 10),
        ),
        (
            "b-uk",
            f"Phase 6 &bull; Queue 4 &bull; {len(uk)} Apps",
            "Unblocking Research Backlog",
            "Requires sponsor clarification or authenticated browser capture before integration scoping can begin.",
            "Targets",
            fmt_targets(uk, 10),
        ),
    ]
    out = []
    for cls, badge, title, desc, lbl, targets in cards:
        out.append(
            f'      <div class="card">\n'
            f'        <span class="badge {cls}">{badge}</span>\n'
            f'        <h3 style="margin-top:0.5rem;">{title}</h3>\n'
            f'        <p>{desc}</p>\n'
            f'        <p class="muted" style="font-size:0.84rem;"><strong>{lbl}:</strong> {targets}</p>\n'
            f'      </div>'
        )
    return "\n".join(out)


def generate_html():
    apps_payload, aggregates, build_queues, baseline_metrics, paired_metrics = build_dataset()
    cat_rows_html = render_category_rows(aggregates)
    cred_rows_html = render_cred_shift_rows(aggregates)
    roadmap_cards_html = render_roadmap_cards(build_queues)

    # Safe JSON embedding (prevent </script> injection)
    embedded_json = json.dumps(apps_payload, ensure_ascii=False).replace("</", "<\\/")

    generated_date = datetime.now().strftime("%Y-%m-%d")

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Composio 100-App Agent Integration Case Study</title>
<style>
  :root {{
    --bg: #f8fafc;
    --surface: #ffffff;
    --surface-2: #f1f5f9;
    --border: #e2e8f0;
    --border-strong: #cbd5e1;
    --text: #0f172a;
    --text-muted: #475569;
    --text-faint: #64748b;
    --accent: #2563eb;
    --accent-soft: #eff6ff;
    --accent-border: #bfdbfe;
    --green: #15803d;
    --green-bg: #dcfce7;
    --blue: #1d4ed8;
    --blue-bg: #dbeafe;
    --amber: #b45309;
    --amber-bg: #fef3c7;
    --red: #b91c1c;
    --red-bg: #fee2e2;
    --purple: #6d28d9;
    --purple-bg: #ede9fe;
    --gray: #475569;
    --gray-bg: #e2e8f0;
    --code-bg: #0f172a;
    --code-text: #e2e8f0;
    --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05);
    --shadow-md: 0 4px 12px rgba(15, 23, 42, 0.08);
    --shadow-lg: 0 20px 40px rgba(15, 23, 42, 0.18);
    --radius: 10px;
    --font-sans: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
  }}

  [data-theme="dark"] {{
    --bg: #0b1120;
    --surface: #111827;
    --surface-2: #1e293b;
    --border: #1f2937;
    --border-strong: #334155;
    --text: #f1f5f9;
    --text-muted: #94a3b8;
    --text-faint: #64748b;
    --accent: #60a5fa;
    --accent-soft: #172554;
    --accent-border: #1e40af;
    --green: #4ade80;
    --green-bg: #052e16;
    --blue: #60a5fa;
    --blue-bg: #172554;
    --amber: #fbbf24;
    --amber-bg: #451a03;
    --red: #f87171;
    --red-bg: #450a0a;
    --purple: #c4b5fd;
    --purple-bg: #2e1065;
    --gray: #cbd5e1;
    --gray-bg: #334155;
    --code-bg: #020617;
    --code-text: #e2e8f0;
  }}

  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0;
    font-family: var(--font-sans);
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    font-size: 15px;
    -webkit-font-smoothing: antialiased;
  }}

  /* Top Nav */
  .topnav {{
    position: sticky;
    top: 0;
    z-index: 40;
    background: color-mix(in srgb, var(--surface) 92%, transparent);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
  }}
  .topnav-inner {{
    max-width: 1320px;
    margin: 0 auto;
    padding: 0.7rem 1.25rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
  }}
  .brand {{
    font-weight: 700;
    font-size: 0.95rem;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text);
    text-decoration: none;
  }}
  .brand-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--accent);
    display: inline-block;
  }}
  .nav-links {{
    display: flex;
    gap: 0.25rem;
    flex-wrap: wrap;
    align-items: center;
  }}
  .nav-links a {{
    color: var(--text-muted);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0.35rem 0.65rem;
    border-radius: 6px;
    transition: background 0.15s, color 0.15s;
  }}
  .nav-links a:hover {{
    background: var(--surface-2);
    color: var(--text);
  }}
  .theme-btn {{
    background: var(--surface-2);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.35rem 0.7rem;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
  }}
  .theme-btn:hover {{ border-color: var(--border-strong); }}

  /* Layout */
  .container {{
    max-width: 1320px;
    margin: 0 auto;
    padding: 2rem 1.25rem 4rem;
  }}
  section {{
    margin-bottom: 3.5rem;
    scroll-margin-top: 72px;
  }}
  h1 {{
    font-size: clamp(1.75rem, 3.2vw, 2.55rem);
    line-height: 1.18;
    letter-spacing: -0.025em;
    margin: 0 0 0.75rem;
  }}
  h2 {{
    font-size: 1.45rem;
    letter-spacing: -0.02em;
    margin: 0 0 0.5rem;
    padding-bottom: 0.45rem;
    border-bottom: 1px solid var(--border);
  }}
  h3 {{
    font-size: 1.1rem;
    margin: 1.4rem 0 0.5rem;
    letter-spacing: -0.01em;
  }}
  p {{ margin: 0 0 0.9rem; color: var(--text-muted); }}
  strong {{ color: var(--text); }}

  /* Hero */
  .hero {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2rem;
    box-shadow: var(--shadow-sm);
    margin-bottom: 2.5rem;
  }}
  .eyebrow {{
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--accent);
    background: var(--accent-soft);
    border: 1px solid var(--accent-border);
    padding: 0.25rem 0.65rem;
    border-radius: 999px;
    margin-bottom: 1rem;
  }}
  .hero-lead {{
    font-size: 1.05rem;
    max-width: 82ch;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
  }}

  /* Two-minute overview box */
  .overview-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1rem;
    margin-top: 1.25rem;
  }}
  .overview-card {{
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem 1.15rem;
  }}
  .overview-card h4 {{
    margin: 0 0 0.35rem;
    font-size: 0.92rem;
    color: var(--text);
  }}
  .overview-card p {{
    margin: 0;
    font-size: 0.87rem;
  }}

  /* KPI Grid */
  .kpi-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(185px, 1fr));
    gap: 0.9rem;
    margin: 1.5rem 0;
  }}
  .kpi {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem 1.1rem;
    box-shadow: var(--shadow-sm);
  }}
  .kpi-label {{
    font-size: 0.76rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--text-faint);
  }}
  .kpi-val {{
    font-size: 1.65rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 0.2rem 0;
    color: var(--text);
  }}
  .kpi-sub {{
    font-size: 0.8rem;
    color: var(--text-muted);
  }}
  .kpi.bn {{ border-top: 3px solid var(--green); }}
  .kpi.co {{ border-top: 3px solid var(--blue); }}
  .kpi.ou {{ border-top: 3px solid var(--amber); }}
  .kpi.uk {{ border-top: 3px solid var(--gray); }}
  .kpi.ac {{ border-top: 3px solid var(--purple); }}

  /* Callouts */
  .callout {{
    border-radius: var(--radius);
    padding: 1rem 1.2rem;
    margin: 1.25rem 0;
    border: 1px solid var(--border);
    background: var(--surface);
  }}
  .callout-warn {{
    background: var(--amber-bg);
    border-color: color-mix(in srgb, var(--amber) 35%, transparent);
    color: var(--text);
  }}
  .callout-info {{
    background: var(--accent-soft);
    border-color: var(--accent-border);
  }}
  .callout strong {{ color: var(--text); }}

  /* Badges */
  .badge {{
    display: inline-flex;
    align-items: center;
    padding: 0.16rem 0.52rem;
    border-radius: 999px;
    font-size: 0.74rem;
    font-weight: 600;
    white-space: nowrap;
  }}
  .b-bn {{ background: var(--green-bg); color: var(--green); }}
  .b-co {{ background: var(--blue-bg); color: var(--blue); }}
  .b-ou {{ background: var(--amber-bg); color: var(--amber); }}
  .b-uk {{ background: var(--gray-bg); color: var(--gray); }}
  .b-mcp-off {{ background: var(--purple-bg); color: var(--purple); }}
  .b-mcp-com {{ background: var(--blue-bg); color: var(--blue); }}
  .b-mcp-none {{ background: var(--surface-2); color: var(--text-faint); border: 1px solid var(--border); }}
  .b-sample {{ background: var(--green-bg); color: var(--green); border: 1px solid color-mix(in srgb, var(--green) 35%, transparent); }}
  .b-chip {{ background: var(--surface-2); color: var(--text-muted); border: 1px solid var(--border); border-radius: 5px; padding: 0.1rem 0.42rem; font-size: 0.73rem; margin: 0.1rem; display: inline-block; }}

  /* Matrix Controls */
  .controls-bar {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem;
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
    box-shadow: var(--shadow-sm);
  }}
  .controls-row {{
    display: flex;
    gap: 0.65rem;
    flex-wrap: wrap;
    align-items: center;
  }}
  .search-input {{
    flex: 1 1 260px;
    padding: 0.55rem 0.85rem;
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    background: var(--bg);
    color: var(--text);
    font-size: 0.9rem;
    font-family: inherit;
  }}
  .search-input:focus {{ outline: 2px solid var(--accent); border-color: var(--accent); }}
  select.filter-select {{
    padding: 0.52rem 0.75rem;
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    background: var(--bg);
    color: var(--text);
    font-size: 0.85rem;
    font-family: inherit;
  }}
  .pill-group {{
    display: flex;
    gap: 0.4rem;
    flex-wrap: wrap;
  }}
  .pill-btn {{
    padding: 0.36rem 0.72rem;
    border-radius: 999px;
    border: 1px solid var(--border-strong);
    background: var(--surface-2);
    color: var(--text-muted);
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.12s;
  }}
  .pill-btn.active {{
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
  }}
  .btn {{
    padding: 0.48rem 0.85rem;
    border-radius: 7px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
  }}
  .btn:hover {{ background: var(--surface-2); }}
  .btn-primary {{
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
  }}
  .btn-primary:hover {{ opacity: 0.92; background: var(--accent); }}
  .matrix-meta {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    font-size: 0.84rem;
    color: var(--text-muted);
  }}

  /* Tables */
  .table-wrap {{
    overflow-x: auto;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow-sm);
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.86rem;
  }}
  th {{
    text-align: left;
    padding: 0.7rem 0.75rem;
    background: var(--surface-2);
    color: var(--text-muted);
    font-weight: 700;
    font-size: 0.76rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    border-bottom: 1px solid var(--border);
    white-space: nowrap;
  }}
  th.sortable {{ cursor: pointer; user-select: none; }}
  th.sortable:hover {{ color: var(--text); }}
  td {{
    padding: 0.65rem 0.75rem;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
  }}
  tbody tr:last-child td {{ border-bottom: none; }}
  #matrixTable tbody tr {{ cursor: pointer; transition: background 0.1s; }}
  #matrixTable tbody tr:hover {{ background: var(--surface-2); }}
  .num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
  .muted {{ color: var(--text-muted); }}
  .sublabel {{ font-size: 0.75rem; color: var(--text-faint); }}

  /* Stacked bars */
  .stack-bar {{
    display: flex;
    height: 12px;
    min-width: 120px;
    border-radius: 6px;
    overflow: hidden;
    background: var(--surface-2);
  }}
  .sb-bn {{ background: #16a34a; }}
  .sb-co {{ background: #2563eb; }}
  .sb-ou {{ background: #d97706; }}
  .sb-uk {{ background: #94a3b8; }}
  .shift-pill {{
    display: inline-block;
    padding: 0.14rem 0.5rem;
    border-radius: 999px;
    font-weight: 700;
    font-size: 0.78rem;
  }}
  .shift-warn {{ background: var(--red-bg); color: var(--red); }}
  .shift-drop {{ background: var(--amber-bg); color: var(--amber); }}
  .shift-neutral {{ background: var(--surface-2); color: var(--text-muted); }}

  /* Cards & Grids */
  .grid-2 {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(320px, 100%), 1fr));
    gap: 1.15rem;
    margin-top: 1rem;
  }}
  .card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.2rem;
    box-shadow: var(--shadow-sm);
  }}
  .card h3 {{ margin-top: 0; }}
  .tier-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 0.9rem;
    margin: 1.25rem 0;
  }}
  .tier-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 4px solid var(--accent);
    border-radius: var(--radius);
    padding: 1rem;
  }}
  .tier-num {{
    font-size: 0.74rem;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--accent);
    letter-spacing: 0.05em;
  }}

  /* Case studies */
  .case-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(340px, 100%), 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }}
  .case-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.1rem;
    font-size: 0.87rem;
  }}
  .case-card h4 {{ margin: 0 0 0.5rem; font-size: 0.96rem; }}
  .case-row {{ margin: 0.35rem 0; color: var(--text-muted); }}

  /* Code blocks */
  pre {{
    background: var(--code-bg);
    color: var(--code-text);
    padding: 1rem 1.15rem;
    border-radius: var(--radius);
    overflow-x: auto;
    font-family: var(--font-mono);
    font-size: 0.82rem;
    line-height: 1.55;
    margin: 0.75rem 0 1.25rem;
  }}
  code {{
    font-family: var(--font-mono);
    font-size: 0.84em;
    background: var(--surface-2);
    padding: 0.12rem 0.35rem;
    border-radius: 4px;
  }}
  pre code {{ background: transparent; padding: 0; }}

  /* Slide-over Drawer */
  .drawer-backdrop {{
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, 0.55);
    z-index: 60;
    display: none;
    justify-content: flex-end;
  }}
  .drawer-backdrop.open {{ display: flex; }}
  .drawer {{
    width: min(680px, 100vw);
    height: 100vh;
    background: var(--surface);
    border-left: 1px solid var(--border);
    box-shadow: var(--shadow-lg);
    overflow-y: auto;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
  }}
  .drawer-head {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 1rem;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.9rem;
  }}
  .drawer-section {{
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.9rem 1rem;
    background: var(--bg);
  }}
  .drawer-section h4 {{
    margin: 0 0 0.5rem;
    font-size: 0.88rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--text-faint);
  }}
  .drawer ul {{
    margin: 0.3rem 0;
    padding-left: 1.2rem;
    color: var(--text-muted);
    font-size: 0.86rem;
  }}
  .drawer a {{ color: var(--accent); word-break: break-all; }}

  footer {{
    border-top: 1px solid var(--border);
    padding: 2rem 1.25rem;
    text-align: center;
    color: var(--text-faint);
    font-size: 0.83rem;
  }}

  @media (max-width: 768px) {{
    .hero {{ padding: 1.25rem; }}
    .topnav-inner {{ padding: 0.6rem 0.9rem; }}
    .container {{ padding: 1.25rem 0.9rem 3rem; }}
    .hide-sm {{ display: none; }}
  }}
  @media print {{
    .topnav, .controls-bar, .drawer-backdrop {{ display: none !important; }}
    body {{ background: #fff; color: #000; }}
    .card, .hero, .table-wrap {{ box-shadow: none; break-inside: avoid; }}
  }}
</style>
</head>
<body>

<nav class="topnav" aria-label="Primary navigation">
  <div class="topnav-inner">
    <a class="brand" href="#overview"><span class="brand-dot"></span>Composio 100-App Audit</a>
    <div class="nav-links">
      <a href="#overview">2-Min Overview</a>
      <a href="#matrix">100-App Matrix</a>
      <a href="#findings">Headline Findings</a>
      <a href="#verification">Verification &amp; Audits</a>
      <a href="#unknowns">Unknowns</a>
      <a href="#roadmap">Roadmap</a>
      <a href="#reproduce">Run Instructions</a>
      <a href="#limitations">Limitations</a>
      <button class="theme-btn" id="themeToggle" type="button">Dark Mode</button>
    </div>
  </div>
</nav>

<main class="container">

  <!-- HERO & TWO-MINUTE OVERVIEW -->
  <header class="hero" id="overview">
    <div class="eyebrow">Self-Contained Empirical Case Study &bull; Contract v1.1 &bull; {generated_date}</div>
    <h1>Agent Integration Feasibility &amp; MCP Ecosystem Audit Across 100 Enterprise Applications</h1>
    <p class="hero-lead">
      A reproducible, four-tier documentary study evaluating authentication models, testing-vs-production credential gating, API surfaces, and Model Context Protocol (MCP) availability across 100 enterprise software platforms (<code>data/apps.json</code>). Every percentage carries an explicit denominator, vendor silence is preserved as <code>unknown</code>, and all human accuracy scores come from actual human adjudication with explicit attestation.
    </p>

    <div class="kpi-grid">
      <div class="kpi bn">
        <div class="kpi-label">Queue 1: Build Now</div>
        <div class="kpi-val">44 / 100</div>
        <div class="kpi-sub">44.00% &mdash; Self-serve, unblocked</div>
      </div>
      <div class="kpi co">
        <div class="kpi-label">Queue 2: Conditional</div>
        <div class="kpi-val">50 / 100</div>
        <div class="kpi-sub">50.00% &mdash; Admin/Vendor/Paid gate</div>
      </div>
      <div class="kpi ou">
        <div class="kpi-label">Queue 3: Outreach</div>
        <div class="kpi-val">4 / 100</div>
        <div class="kpi-sub">4.00% &mdash; Commercial sales required</div>
      </div>
      <div class="kpi uk">
        <div class="kpi-label">Queue 4: Unknown</div>
        <div class="kpi-val">2 / 100</div>
        <div class="kpi-sub">2.00% &mdash; Preserved unknowns</div>
      </div>
      <div class="kpi ac">
        <div class="kpi-label">MCP Adoption</div>
        <div class="kpi-val">85 / 100</div>
        <div class="kpi-sub">70 Official &bull; 19 Community &bull; 4 Both</div>
      </div>
      <div class="kpi">
        <div class="kpi-label">Human Sample Audit</div>
        <div class="kpi-val">84.71% &rarr; 100%</div>
        <div class="kpi-sub">Fixed N=327 claims (20 apps)*</div>
      </div>
    </div>

    <div class="overview-grid">
      <div class="overview-card">
        <h4>1. What We Found (The 2-Minute Takeaway)</h4>
        <p><strong>44/100 apps (44.00%)</strong> can be built immediately with self-serve credentials (34 already ship official MCP servers). Another <strong>50/100 (50.00%)</strong> have functional APIs/MCPs but require tenant admin consent, vendor app review, or paid subscriptions before production operation.</p>
      </div>
      <div class="overview-card">
        <h4>2. The Testing-to-Production Gating Trap</h4>
        <p>While <strong>62/100 (62.00%)</strong> allow self-serve testing, only <strong>49/100 (49.00%)</strong> allow self-serve production deployment. Mandatory paid plans surge from <strong>1/100 (1.00%)</strong> in testing to <strong>36/100 (36.00%)</strong> in production (<strong>+35 net shift</strong>).</p>
      </div>
      <div class="overview-card">
        <h4>3. MCP &amp; Auth Reality</h4>
        <p><strong>85/100 apps (85.00%)</strong> have documented MCP server implementations (70 official, 19 community, 4 overlap). <strong>OAuth 2.0 (79/100)</strong> dominates authentication, while <strong>API Keys (39/100)</strong> and <strong>Bearer Tokens (35/100)</strong> power headless self-serve access.</p>
      </div>
      <div class="overview-card">
        <h4>4. Honest Human Verification</h4>
        <p>Independent human reviewer <strong>ARINDAM KARMAKAR</strong> audited all <strong>327 claims</strong> across the frozen 20-app stratified sample. Baseline accuracy was <strong>84.71%</strong> (277 correct, 50 unsupported). After 50 immutable corrections, recheck accuracy reached <strong>100.00%</strong> on fixed N=327.</p>
      </div>
    </div>

    <div class="callout callout-warn" style="margin-top:1.25rem; margin-bottom:0;">
      <strong>*Sample Reuse &amp; Scope Disclosure:</strong> The 100.00% post-correction score measures verified error remediation on the reused 20-app stratified sample (<code>composio-20app-sample-v1</code>, N=327 claims) and <strong>must not be treated as an unbiased held-out generalization across all 100 apps</strong>. The remaining 80 apps retain their sealed, AI-audited first-pass records. All MCP operational runtime checks remain strictly <code>not_researched</code> (no live credentials or tool invocations were executed).
    </div>
  </header>

  <!-- INTERACTIVE SEARCHABLE MATRIX -->
  <section id="matrix">
    <h2>1. Interactive 100-Application Coverage Matrix</h2>
    <p>Search and filter all 100 applications across the authoritative dataset (80 sealed first-pass apps + 20 Task 18 human-verified corrected apps). Click any row to inspect full credential gating, MCP servers, blockers, citations, and Task 17/18 audit transitions.</p>

    <div class="controls-bar">
      <div class="controls-row">
        <input type="search" id="searchInput" class="search-input" placeholder="Search by app name, ID, category, purpose, auth, MCP server, or blocker..." aria-label="Search 100 applications">
        <select id="categoryFilter" class="filter-select" aria-label="Filter by category">
          <option value="">All Categories (10)</option>
        </select>
        <select id="mcpFilter" class="filter-select" aria-label="Filter by MCP status">
          <option value="">All MCP Statuses</option>
          <option value="official_only">Official MCP Only (66)</option>
          <option value="community_only">Community MCP Only (15)</option>
          <option value="official_and_community">Official + Community (4)</option>
          <option value="not_found_bounded">No MCP in Checked Sources (11)</option>
          <option value="unknown">MCP Unknown (4)</option>
        </select>
        <select id="authFilter" class="filter-select" aria-label="Filter by auth method">
          <option value="">All Auth Methods</option>
          <option value="OAuth2">OAuth 2.0 (79)</option>
          <option value="API_key">API Key (39)</option>
          <option value="Bearer_token">Bearer Token (35)</option>
          <option value="Basic">Basic Auth (15)</option>
          <option value="other">Custom / Other (8)</option>
          <option value="none">None / Local CLI (5)</option>
          <option value="JWT">JWT (2)</option>
          <option value="session_cookie">Session Cookie (1)</option>
        </select>
      </div>
      <div class="controls-row" style="justify-content: space-between;">
        <div class="pill-group" id="queuePills" role="group" aria-label="Filter by build queue">
          <button class="pill-btn active" data-queue="">All (100)</button>
          <button class="pill-btn" data-queue="build_now">Build Now (44)</button>
          <button class="pill-btn" data-queue="conditional">Conditional (50)</button>
          <button class="pill-btn" data-queue="outreach_required">Outreach (4)</button>
          <button class="pill-btn" data-queue="unknown">Unknown (2)</button>
        </div>
        <div class="controls-row">
          <label style="font-size:0.83rem; display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
            <input type="checkbox" id="sampleOnlyCheck"> Task 17/18 Audited Sample Only (20)
          </label>
          <button class="btn" id="resetFiltersBtn" type="button">Reset</button>
          <button class="btn btn-primary" id="exportJsonBtn" type="button">Export Filtered JSON</button>
        </div>
      </div>
      <div class="matrix-meta">
        <span id="resultCount">Showing 100 of 100 applications</span>
        <span class="muted">Click any row to open the full evidence &amp; gating inspector</span>
      </div>
    </div>

    <div class="table-wrap">
      <table id="matrixTable">
        <thead>
          <tr>
            <th class="sortable" data-sort="id">ID &#8597;</th>
            <th class="sortable" data-sort="name">Application &#8597;</th>
            <th class="sortable" data-sort="queue">Queue / Verdict &#8597;</th>
            <th class="hide-sm">Auth Methods</th>
            <th class="hide-sm">API &amp; Breadth</th>
            <th class="sortable" data-sort="mcp_category">MCP Ecosystem &#8597;</th>
            <th class="hide-sm">Testing &rarr; Prod Gating</th>
            <th>Details</th>
          </tr>
        </thead>
        <tbody id="matrixBody"></tbody>
      </table>
    </div>
  </section>

  <!-- HEADLINE FINDINGS -->
  <section id="findings">
    <h2>2. Supported Headline Findings &amp; Cross-Cutting Patterns</h2>
    <p>All aggregates below are deterministically computed from the authoritative 100-application dataset (<code>outputs/task-19/aggregates.json</code>) with explicit denominators.</p>

    <h3>A. Category Dynamics &amp; Feasibility Asymmetry (Denominator: N=10 per category)</h3>
    <p>Buildability varies sharply by software domain. Data/SEO (90% Build Now) and Communications (80% Build Now) are predominantly unblocked, whereas Productivity and Developer/Infrastructure platforms are 100% gated by tenant admin consent or cloud IAM billing.</p>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Category</th>
            <th class="num">Build Now</th>
            <th class="num">Conditional</th>
            <th class="num">Outreach</th>
            <th class="num">Unknown</th>
            <th>Distribution</th>
            <th>Dominant Gating Pattern</th>
          </tr>
        </thead>
        <tbody>
          {cat_rows_html}
        </tbody>
      </table>
    </div>

    <h3>B. Credential Gating Divergence: Testing vs. Production (Denominator: N=100)</h3>
    <p>A critical operational finding is the sharp cliff between developer testing and production deployment. Paid tier requirements jump by <strong>+35 apps</strong>, tenant admin approvals by <strong>+15 apps</strong>, and vendor application reviews by <strong>+12 apps</strong>.</p>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Gating Dimension</th>
            <th class="num">Test True</th>
            <th class="num">Test False</th>
            <th class="num">Test Unk/NA</th>
            <th class="num">Prod True</th>
            <th class="num">Prod False</th>
            <th class="num">Prod Unk/NA</th>
            <th class="num">Net Shift</th>
          </tr>
        </thead>
        <tbody>
          {cred_rows_html}
        </tbody>
      </table>
    </div>

    <div class="grid-2">
      <div class="card">
        <h3>C. Authentication Protocol Landscape (N=100)</h3>
        <table>
          <thead>
            <tr><th>Auth Paradigm</th><th class="num">Apps</th><th class="num">Build Now</th><th class="num">Conditional</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>OAuth 2.0</strong></td><td class="num">79/100 (79.0%)</td><td class="num">35 (44.3%)</td><td class="num">42 (53.2%)</td></tr>
            <tr><td><strong>API Key</strong></td><td class="num">39/100 (39.0%)</td><td class="num">21 (53.8%)</td><td class="num">17 (43.6%)</td></tr>
            <tr><td><strong>Bearer / Personal Token</strong></td><td class="num">35/100 (35.0%)</td><td class="num">14 (40.0%)</td><td class="num">21 (60.0%)</td></tr>
            <tr><td><strong>Basic Auth</strong></td><td class="num">15/100 (15.0%)</td><td class="num">9 (60.0%)</td><td class="num">6 (40.0%)</td></tr>
            <tr><td><strong>None / Local CLI</strong></td><td class="num">5/100 (5.0%)</td><td class="num">4 (80.0%)</td><td class="num">1 (20.0%)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card">
        <h3>D. MCP Availability vs. Buildability (N=100)</h3>
        <table>
          <thead>
            <tr><th>MCP Classification</th><th class="num">Apps</th><th class="num">Build Now</th><th class="num">Conditional</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Official MCP Only</strong></td><td class="num">66/100 (66.0%)</td><td class="num">32 (48.5%)</td><td class="num">31 (47.0%)</td></tr>
            <tr><td><strong>Community MCP Only</strong></td><td class="num">15/100 (15.0%)</td><td class="num">7 (46.7%)</td><td class="num">8 (53.3%)</td></tr>
            <tr><td><strong>Official + Community</strong></td><td class="num">4/100 (4.0%)</td><td class="num">2 (50.0%)</td><td class="num">2 (50.0%)</td></tr>
            <tr><td><strong>No MCP (Bounded Search)</strong></td><td class="num">11/100 (11.0%)</td><td class="num">3 (27.3%)</td><td class="num">7 (63.6%)</td></tr>
            <tr><td><strong>MCP Unknown</strong></td><td class="num">4/100 (4.0%)</td><td class="num">0 (0.0%)</td><td class="num">2 (50.0%)</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- PROCESS, EVIDENCE & HUMAN VERIFICATION -->
  <section id="verification">
    <h2>3. Process, Immutability Architecture &amp; Human Verification</h2>
    <p>Every artifact in this study is preserved across four immutable tiers. Sealed runs, original captures, snapshots, and question inventories are never edited in place; all corrections and reviews occur in cryptographically hashed child runs.</p>

    <div class="tier-grid">
      <div class="tier-card">
        <div class="tier-num">Tier 1 &bull; Tasks 07&ndash;16</div>
        <strong>Sealed First-Pass Research</strong>
        <p style="font-size:0.84rem; margin-top:0.35rem;">10 isolated batches covering all 100 apps (<code>task07-first-pass-003</code> through <code>task16-first-pass-001</code>). Each claim backed by local text snapshots, line locators, SHA-256 hashes, JSON Schema Draft 2020-12 validation, and independent AI consistency audit.</p>
      </div>
      <div class="tier-card">
        <div class="tier-num">Tier 2 &bull; Task 17</div>
        <strong>Human Baseline Audit</strong>
        <p style="font-size:0.84rem; margin-top:0.35rem;">Stratified 20-app sample (<code>composio-20app-sample-v1</code>, 2 apps/category, <strong>N=327</strong> claims) adjudicated by independent human reviewer <strong>ARINDAM KARMAKAR</strong> on 2026-11-24 with explicit human attestation. Baseline: <strong>84.71%</strong> (277 correct, 50 unsupported).</p>
      </div>
      <div class="tier-card">
        <div class="tier-num">Tier 3 &bull; Task 18 Phase A</div>
        <strong>Immutable Error Corrections</strong>
        <p style="font-size:0.84rem; margin-top:0.35rem;">All 50 unsupported claims remediated across 10 child runs (<code>task18-corrections-07</code>&ndash;<code>16</code>) with explicit <code>correction_refs</code> and strict question-inventory invariance (0 added, 0 removed, 0 split).</p>
      </div>
      <div class="tier-card">
        <div class="tier-num">Tier 4 &bull; Task 18 Phase B &amp; 19</div>
        <strong>Human Recheck &amp; Synthesis</strong>
        <p style="font-size:0.84rem; margin-top:0.35rem;">All 327 claims re-adjudicated by <strong>ARINDAM KARMAKAR</strong> across 10 sealed child review runs (<code>task18-human-recheck-07</code>&ndash;<code>16</code>), achieving <strong>100.00%</strong> (327/327) on fixed N=327. Task 19 synthesized the authoritative 100-app dataset.</p>
      </div>
    </div>

    <h3>Paired Before vs. After Human Accuracy (Frozen Sample N=327 Claims, 20 Apps)</h3>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Metric / Evidence Basis</th>
            <th class="num">Eligible (N)</th>
            <th class="num">Task 17 Baseline</th>
            <th class="num">Task 18 Recheck</th>
            <th class="num">Net Change</th>
            <th class="num">Review Coverage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Overall Evidence-Backed Accuracy C/(C+I+U)</strong></td>
            <td class="num">327</td>
            <td class="num"><strong>84.71%</strong> (277 C / 0 I / 50 U)</td>
            <td class="num"><strong>100.00%</strong> (327 C / 0 I / 0 U)</td>
            <td class="num"><span class="badge b-bn">+15.29%</span></td>
            <td class="num">100.00% (0 pending)</td>
          </tr>
          <tr>
            <td><strong>Observed Claims (Documentary)</strong></td>
            <td class="num">290</td>
            <td class="num">95.52% (277 C / 13 U)</td>
            <td class="num">100.00% (290 C / 0 U)</td>
            <td class="num"><span class="badge b-bn">+4.48%</span></td>
            <td class="num">100.00%</td>
          </tr>
          <tr>
            <td><strong>Inferred Claims (Synthesized Breadth &amp; Buildability)</strong></td>
            <td class="num">37</td>
            <td class="num">0.00% (0 C / 37 U)</td>
            <td class="num">100.00% (37 C / 0 U)</td>
            <td class="num"><span class="badge b-bn">+100.00%</span></td>
            <td class="num">100.00%</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>Channel Separation Policy</h3>
    <div class="table-wrap" style="margin-top:0.5rem;">
      <table>
        <thead>
          <tr><th>Verification Channel</th><th>Role &amp; Method</th><th>Human Attestation</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>AI Consistency Audits (Tasks 07&ndash;16)</strong></td><td>Read-only AI auditor verifying schema compliance, snapshot hashes, line locators, and internal grounding.</td><td><code>false</code> (AI review only)</td></tr>
          <tr><td><strong>Automated Capture Checks</strong></td><td>Deterministic Python HTTP retrieval, HTML stripping, SHA-256 hashing, and CaptureError diagnostics.</td><td><code>false</code> (Automated)</td></tr>
          <tr><td><strong>Human Ground-Truth Adjudication (Tasks 17&ndash;18)</strong></td><td>Direct primary-source review by <strong>ARINDAM KARMAKAR</strong> across all 327 sample claims (baseline &amp; recheck).</td><td><code>true</code> (Actual Human)</td></tr>
        </tbody>
      </table>
    </div>

    <h3>Representative Error Correction Case Studies</h3>
    <div class="case-grid">
      <div class="case-card">
        <h4>1. Negative Gating Silence &mdash; App 83 (Binance)</h4>
        <div class="case-row"><strong>Original:</strong> <code>83.testing.vendor_approval_required: false</code> (<code>observed</code>)</div>
        <div class="case-row"><strong>Human Baseline:</strong> <code>unsupported</code> &mdash; Absence of gating was not proven by captured excerpts.</div>
        <div class="case-row"><strong>Correction &amp; Recheck:</strong> Relabeled to <code>unknown</code> (<code>null</code>) under <code>docs/evidence-rules.md</code> (vendor silence is unknown). Verified <code>correct</code>.</div>
      </div>
      <div class="case-card">
        <h4>2. Offline CLI Credentials &mdash; App 98 (Mermaid CLI)</h4>
        <div class="case-row"><strong>Original:</strong> <code>98.testing.vendor_approval_required: false</code> (<code>observed</code>)</div>
        <div class="case-row"><strong>Human Baseline:</strong> <code>unsupported</code> &mdash; Unproven negative assertion.</div>
        <div class="case-row"><strong>Correction &amp; Recheck:</strong> Relabeled to <code>not_applicable</code> backed by MIT License and local npm/npx CLI docs. Verified <code>correct</code>.</div>
      </div>
      <div class="case-card">
        <h4>3. Qualitative API Breadth &mdash; App 4 (Attio)</h4>
        <div class="case-row"><strong>Original:</strong> <code>4.api.breadth: "broad"</code> (<code>inferred</code>) without explicit domain taxonomy mapping.</div>
        <div class="case-row"><strong>Human Baseline:</strong> <code>unsupported</code> &mdash; Unanchored synthesis.</div>
        <div class="case-row"><strong>Correction &amp; Recheck:</strong> Anchored to 4 documented domains (CRM Records/Objects, Collaboration, Activities/Recordings, SCIM/Webhooks). Verified <code>correct</code>.</div>
      </div>
      <div class="case-card">
        <h4>4. Integration Buildability Chain &mdash; App 21 (Slack)</h4>
        <div class="case-row"><strong>Original:</strong> <code>21.buildability: build_now</code> (<code>inferred</code>) lacking explicit prerequisite chain.</div>
        <div class="case-row"><strong>Human Baseline:</strong> <code>unsupported</code> &mdash; Needed direct linkage to verified facts.</div>
        <div class="case-row"><strong>Correction &amp; Recheck:</strong> Grounded in verified self-serve app creation, free workspace tier, OAuth 2.0, and Web API quickstart. Verified <code>correct</code>.</div>
      </div>
      <div class="case-card">
        <h4>5. Production Tier Restrictions &mdash; App 31 (Google Ads)</h4>
        <div class="case-row"><strong>Original:</strong> <code>31.buildability: conditional</code> (<code>inferred</code>).</div>
        <div class="case-row"><strong>Human Baseline:</strong> <code>unsupported</code> &mdash; Required explicit access-tier proof.</div>
        <div class="case-row"><strong>Correction &amp; Recheck:</strong> Grounded in official Google Ads developer token tiers (immediate test-account access vs. mandatory Explorer/Basic/Standard production approval). Verified <code>correct</code>.</div>
      </div>
    </div>
  </section>

  <!-- UNKNOWNS INVENTORY -->
  <section id="unknowns">
    <h2>4. Full Visibility of Unknowns Inventory</h2>
    <p>Under <code>docs/evidence-rules.md</code>, vendor silence and HTTP access blocks are preserved as <code>unknown</code> rather than fabricated into false certainty.</p>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Dimension</th>
            <th class="num">Unknown / Denom</th>
            <th>Affected Applications</th>
            <th>Root Cause &amp; Rule Justification</th>
            <th>Unblocking Path</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Identity Resolution</strong></td>
            <td class="num">2/100 (2.00%)</td>
            <td>App 84 (Paygent Connect), App 90 (PitchBook)</td>
            <td>App 84: Vendor ambiguity (NMI vs. Japanese Paygent). App 90: Persistent HTTP 403 blocks on official pages.</td>
            <td>Sponsor clarification (App 84); approved browser capture (App 90).</td>
          </tr>
          <tr>
            <td><strong>Single-Line Purpose</strong></td>
            <td class="num">2/100 (2.00%)</td>
            <td>App 84 (Paygent Connect), App 90 (PitchBook)</td>
            <td>Cannot assert product purpose without resolved identity.</td>
            <td>Resolve upstream identity prerequisite.</td>
          </tr>
          <tr>
            <td><strong>API Surface Breadth</strong></td>
            <td class="num">5/100 (5.00%)</td>
            <td>Apps 18 (Help Scout), 50 (fanbasis), 84, 85 (iPayX), 90</td>
            <td>Captured excerpts covered isolated endpoints only; total resource domain breadth unmeasured.</td>
            <td>Targeted crawl of full REST endpoint directories.</td>
          </tr>
          <tr>
            <td><strong>MCP Discovery</strong></td>
            <td class="num">4/100 (4.00%)</td>
            <td>Apps 18 (Help Scout), 46 (Squarespace), 84, 90</td>
            <td>Captured primary docs did not cover MCP tooling or returned HTTP 403.</td>
            <td>Dedicated repository search across official GitHub orgs.</td>
          </tr>
          <tr>
            <td><strong>Buildability Verdict</strong></td>
            <td class="num">2/100 (2.00%)</td>
            <td>App 84 (Paygent Connect), App 90 (PitchBook)</td>
            <td>No buildability inference permitted when identity/developer surfaces are unknown.</td>
            <td>Upstream identity resolution &amp; documentation capture.</td>
          </tr>
          <tr>
            <td><strong>Credential Gating Silence</strong></td>
            <td class="num">34&ndash;95/100</td>
            <td>Widespread (e.g., <code>testing.contact_sales_required</code>: 95 unknown)</td>
            <td>Primary docs did not explicitly assert or disclaim the gating condition; silence preserved as unknown.</td>
            <td>Empirical operational testing (account creation &amp; key generation).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- PRIORITIZED BUILD ROADMAP -->
  <section id="roadmap">
    <h2>5. Strategic Prioritization &amp; Build Roadmap</h2>
    <p>Actionable implementation sequence derived directly from verified buildability queues (<code>outputs/task-19/build-queues.json</code>).</p>
    <div class="grid-2">
{roadmap_cards_html}
    </div>
  </section>

  <!-- REPRODUCTION & RUN INSTRUCTIONS -->
  <section id="reproduce">
    <h2>6. Reproducibility &amp; CLI Run Instructions</h2>
    <p>All outputs, seals, metrics, and this case study can be deterministically verified offline using Python 3.10+ and the repository's virtual environment (<code>.venv</code>). No API keys or external network calls are required for offline replay and validation.</p>

    <h3>A. Offline Replay &amp; Seal Verification</h3>
<pre><code># 1. Validate a sealed first-pass or Task 18 correction run (verifies SHA-256 seals + JSON Schema Draft 2020-12)
.venv\\Scripts\\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task07-first-pass-003
.venv\\Scripts\\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task18-corrections-07

# 2. Perform a zero-network offline replay into a fresh child run
.venv\\Scripts\\python.exe -B research_pipeline.py --store work/research-runs collect --run-id qa-replay-check --parent task07-first-pass-003 --replay

# 3. Verify paired human metrics against the frozen Task 17 / Task 18 review runs
.venv\\Scripts\\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task18-human-recheck-07 --target task18-corrections-07

# 4. Regenerate Task 19 cross-application aggregates and build queues
.venv\\Scripts\\python.exe work/task-19-agent/generate_task19_outputs.py

# 5. Regenerate this self-contained Task 20 HTML case study
.venv\\Scripts\\python.exe work/task-20-agent/generate_case_study.py</code></pre>

    <h3>B. Live-Research Prerequisites (For Future New Captures)</h3>
    <p>Running fresh live captures (outside offline replay) requires outbound HTTPS access to public vendor documentation URLs and an explicitly supplied source manifest (never auto-promoted from hints):</p>
<pre><code># Inspect roster leads (display only; never used as evidence)
.venv\\Scripts\\python.exe -B research_pipeline.py leads --ids 84,90

# Capture fresh public documentation into a new run directory
.venv\\Scripts\\python.exe -B research_pipeline.py --store work/my-runs collect --run-id capture-new-001 --ids 84,90 --sources public-sources.json --timeout 10 --retries 1 --max-bytes 5000000

# Ingest researcher-authored extraction &amp; run independent review
.venv\\Scripts\\python.exe -B research_pipeline.py --store work/my-runs ingest --run-id extracted-001 --parent capture-new-001 --claims records.json --reason "Initial extraction"
.venv\\Scripts\\python.exe -B research_pipeline.py --store work/my-runs review --run-id reviewed-001 --parent extracted-001 --reviewer-id &lt;reviewer&gt; --reviewer-type human --actual-human-attestation --judgments judgments.json</code></pre>
  </section>

  <!-- MISSES, GAPS & LIMITATIONS -->
  <section id="limitations">
    <h2>7. Misses, Gaps &amp; Project Limitations</h2>
    <div class="grid-2">
      <div class="card">
        <h3>1. Sample Reuse Disclosure</h3>
        <p>The 100.00% post-correction accuracy (327/327 claims) reflects verified remediation on the same 20-app stratified sample (<code>composio-20app-sample-v1</code>) audited in Task 17. It proves the 50 baseline defects were genuinely fixed without inventory drift, but it is <strong>not</strong> an unbiased held-out estimate for the 80 unsampled apps.</p>
      </div>
      <div class="card">
        <h3>2. Operational MCP Checks Unresearched</h3>
        <p>By design, no paid accounts, OAuth token exchanges, or live MCP tool invocations were performed. Every MCP entry's operational check status remains strictly <code>not_researched</code>. Documentary existence of an official or community MCP repo does not guarantee runtime stability or tool-schema completeness.</p>
      </div>
      <div class="card">
        <h3>3. Single-Rater Human Baseline</h3>
        <p>All 327 baseline and recheck adjudications were completed by a single identified human reviewer (<strong>ARINDAM KARMAKAR</strong>). While this eliminates AI self-grading, future production benchmarks should measure inter-annotator agreement across multiple independent reviewers.</p>
      </div>
      <div class="card">
        <h3>4. Capture Walls &amp; Documentation Drift</h3>
        <p>Two applications (App 84 Paygent Connect, App 90 PitchBook) remain blocked due to vendor naming ambiguity and HTTP 403 bot walls. Furthermore, unversioned SaaS developer docs evolve over time; local SHA-256 snapshots freeze the exact text observed during November 2026.</p>
      </div>
    </div>
  </section>

</main>

<footer>
  <div>Composio 100-App Enterprise Agent Integration Case Study &bull; Generated {generated_date} from sealed repository outputs (Tasks 06&ndash;19).</div>
  <div style="margin-top:0.35rem;">Zero external dependencies &bull; Fully offline-capable &bull; No invented accuracy or human claims.</div>
</footer>

<!-- SLIDE-OVER DETAIL DRAWER -->
<div class="drawer-backdrop" id="drawerBackdrop" role="dialog" aria-modal="true" aria-labelledby="drawerTitle">
  <div class="drawer" id="drawerContent"></div>
</div>

<script>
const APPS = {embedded_json};

const QUEUE_META = {{
  build_now: {{ label: "Build Now", cls: "b-bn", order: 1 }},
  conditional: {{ label: "Conditional", cls: "b-co", order: 2 }},
  outreach_required: {{ label: "Outreach Required", cls: "b-ou", order: 3 }},
  unknown: {{ label: "Unknown", cls: "b-uk", order: 4 }}
}};

const MCP_META = {{
  official_only: {{ label: "Official MCP", cls: "b-mcp-off" }},
  official_and_community: {{ label: "Official + Community", cls: "b-mcp-off" }},
  community_only: {{ label: "Community MCP", cls: "b-mcp-com" }},
  not_found_bounded: {{ label: "No MCP Found", cls: "b-mcp-none" }},
  unknown: {{ label: "MCP Unknown", cls: "b-uk" }}
}};

const AUTH_LABELS = {{
  OAuth2: "OAuth 2.0",
  API_key: "API Key",
  Bearer_token: "Bearer Token",
  Basic: "Basic Auth",
  none: "None / Local CLI",
  session_cookie: "Session Cookie",
  JWT: "JWT",
  other: "Custom / Other"
}};

let state = {{
  search: "",
  category: "",
  queue: "",
  mcp: "",
  auth: "",
  sampleOnly: false,
  sortKey: "id",
  sortDir: 1
}};

function esc(str) {{
  if (str === null || str === undefined) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}}

function initFilters() {{
  const cats = Array.from(new Set(APPS.map(a => a.category))).sort();
  const catSel = document.getElementById("categoryFilter");
  cats.forEach(c => {{
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = c + " (10)";
    catSel.appendChild(opt);
  }});
}}

function getFilteredApps() {{
  const q = state.search.trim().toLowerCase();
  return APPS.filter(app => {{
    if (state.category && app.category !== state.category) return false;
    if (state.queue && app.queue !== state.queue) return false;
    if (state.mcp && app.mcp_category !== state.mcp) return false;
    if (state.auth && !app.auth_methods.includes(state.auth)) return false;
    if (state.sampleOnly && !app.in_sample) return false;
    if (q) {{
      const hay = [
        String(app.id),
        app.name,
        app.category,
        app.purpose,
        app.queue,
        app.sub_tier,
        app.scope,
        app.auth_methods.join(" "),
        app.protocols.join(" "),
        app.mcp_official_servers.join(" "),
        app.mcp_community_servers.join(" "),
        app.blockers.join(" ")
      ].join(" ").toLowerCase();
      if (!hay.includes(q)) return false;
    }}
    return true;
  }}).sort((a, b) => {{
    let va, vb;
    if (state.sortKey === "queue") {{
      va = (QUEUE_META[a.queue] || {{order: 9}}).order;
      vb = (QUEUE_META[b.queue] || {{order: 9}}).order;
    }} else {{
      va = a[state.sortKey];
      vb = b[state.sortKey];
    }}
    if (typeof va === "string") return va.localeCompare(vb) * state.sortDir;
    return (va - vb) * state.sortDir;
  }});
}}

function summarizeGating(env) {{
  const pills = [];
  if (env.self_serve && env.self_serve.value === true) pills.push("Self-Serve");
  if (env.free_access && env.free_access.value === true) pills.push("Free");
  if (env.trial_access && env.trial_access.value === true) pills.push("Trial");
  if (env.paid_required && env.paid_required.value === true) pills.push("Paid");
  if (env.admin_approval_required && env.admin_approval_required.value === true) pills.push("Admin");
  if (env.vendor_approval_required && env.vendor_approval_required.value === true) pills.push("Vendor Rev");
  if (env.contact_sales_required && env.contact_sales_required.value === true) pills.push("Sales");
  return pills.length ? pills.slice(0, 3).join(", ") : "Unknown/NA";
}}

function renderTable() {{
  const filtered = getFilteredApps();
  document.getElementById("resultCount").textContent =
    `Showing ${{filtered.length}} of ${{APPS.length}} applications`;

  const tbody = document.getElementById("matrixBody");
  if (!filtered.length) {{
    tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:2rem; color:var(--text-faint);">No applications match the active filters.</td></tr>`;
    return;
  }}

  tbody.innerHTML = filtered.map(app => {{
    const qm = QUEUE_META[app.queue] || QUEUE_META.unknown;
    const mm = MCP_META[app.mcp_category] || MCP_META.unknown;
    const authHtml = app.auth_methods.length
      ? app.auth_methods.map(m => `<span class="b-chip">${{esc(AUTH_LABELS[m] || m)}}</span>`).join("")
      : `<span class="muted">Unknown</span>`;
    const protoHtml = app.protocols.length
      ? app.protocols.map(p => `<span class="b-chip">${{esc(p)}}</span>`).join("")
      : `<span class="muted">&mdash;</span>`;
    const sampleBadge = app.in_sample
      ? ` <span class="badge b-sample" title="Audited by ARINDAM KARMAKAR in Tasks 17 &amp; 18">Sampled</span>`
      : "";
    const mcpNames = [...app.mcp_official_servers, ...app.mcp_community_servers].slice(0, 1).join("");

    return `<tr data-id="${{app.id}}" tabindex="0">
      <td class="num"><strong>#${{app.id}}</strong></td>
      <td>
        <strong>${{esc(app.name)}}</strong>${{sampleBadge}}
        <div class="sublabel">${{esc(app.category)}}</div>
      </td>
      <td>
        <span class="badge ${{qm.cls}}">${{qm.label}}</span>
        <div class="sublabel">${{esc(app.sub_tier || "")}}</div>
      </td>
      <td class="hide-sm">${{authHtml}}</td>
      <td class="hide-sm">
        <div>${{protoHtml}}</div>
        <div class="sublabel">Breadth: <strong>${{esc(app.breadth)}}</strong></div>
      </td>
      <td>
        <span class="badge ${{mm.cls}}">${{mm.label}}</span>
        ${{mcpNames ? `<div class="sublabel">${{esc(mcpNames)}}</div>` : ""}}
      </td>
      <td class="hide-sm" style="font-size:0.78rem;">
        <div><strong>Test:</strong> ${{esc(summarizeGating(app.testing))}}</div>
        <div><strong>Prod:</strong> ${{esc(summarizeGating(app.production))}}</div>
      </td>
      <td><button class="btn" type="button" data-open="${{app.id}}">Inspect</button></td>
    </tr>`;
  }}).join("");
}}

function formatGateCell(cell) {{
  if (!cell) return '<span class="muted">unknown</span>';
  if (cell.status === "not_applicable") return '<span class="muted">N/A</span>';
  if (cell.value === true) return '<strong style="color:var(--green);">true</strong>';
  if (cell.value === false) return '<strong style="color:var(--red);">false</strong>';
  return '<span class="muted">unknown</span>';
}}

function openDrawer(appId) {{
  const app = APPS.find(a => a.id === appId);
  if (!app) return;
  const qm = QUEUE_META[app.queue] || QUEUE_META.unknown;
  const mm = MCP_META[app.mcp_category] || MCP_META.unknown;

  const dims = [
    ["self_serve", "Self-Serve"],
    ["free_access", "Free Access"],
    ["trial_access", "Trial Access"],
    ["sandbox_access", "Sandbox Access"],
    ["paid_required", "Paid Required"],
    ["admin_approval_required", "Admin Approval"],
    ["vendor_approval_required", "Vendor Approval"],
    ["partner_approval_required", "Partner Approval"],
    ["contact_sales_required", "Contact Sales"]
  ];

  const gateRows = dims.map(([k, lbl]) => `
    <tr>
      <td>${{lbl}}</td>
      <td>${{formatGateCell(app.testing[k])}}</td>
      <td>${{formatGateCell(app.production[k])}}</td>
    </tr>
  `).join("");

  const mcpHtml = app.mcp_entries.length
    ? app.mcp_entries.map(e => `
      <div style="margin-bottom:0.6rem; padding-bottom:0.6rem; border-bottom:1px solid var(--border);">
        <div><strong>${{esc(e.name)}}</strong> <span class="badge ${{e.origin === 'official' ? 'b-mcp-off' : 'b-mcp-com'}}">${{esc(e.origin)}}</span></div>
        <div class="sublabel" style="margin-top:0.2rem;">${{esc(e.scope)}}</div>
        <div class="sublabel">Operational Check: <code>${{esc(e.operational_status)}}</code></div>
        ${{e.repository_url ? `<div style="font-size:0.8rem; margin-top:0.2rem;">Repo: <a href="${{esc(e.repository_url)}}" target="_blank" rel="noopener noreferrer">${{esc(e.repository_url)}}</a></div>` : ""}}
        ${{e.source_url && e.source_url !== e.repository_url ? `<div style="font-size:0.8rem;">Docs: <a href="${{esc(e.source_url)}}" target="_blank" rel="noopener noreferrer">${{esc(e.source_url)}}</a></div>` : ""}}
      </div>
    `).join("")
    : `<p style="margin:0; font-size:0.85rem;">No documented MCP server entries (classification: <code>${{esc(app.mcp_category)}}</code>).</p>`;

  const sampleHtml = app.in_sample ? `
    <div class="drawer-section" style="border-color:var(--green);">
      <h4>Task 17 &amp; 18 Human Audit Record</h4>
      <p style="font-size:0.84rem; margin-bottom:0.4rem;">
        Included in frozen stratified sample <code>composio-20app-sample-v1</code>. Audited by <strong>ARINDAM KARMAKAR</strong> (actual human attestation: <code>true</code>). Post-correction recheck accuracy: <strong>100.00%</strong>.
      </p>
      ${{app.transitions.length ? `
        <div style="font-size:0.82rem;"><strong>${{app.transitions.length}} Corrected Claim(s):</strong>
          <ul>${{app.transitions.map(t => `<li><code>${{esc(t.claim_id)}}</code>: ${{esc(t.before)}} &rarr; <strong>${{esc(t.after)}}</strong> &mdash; ${{esc(t.reason_after)}}</li>`).join("")}}</ul>
        </div>
      ` : `<div class="sublabel">All claims passed baseline audit with 0 corrections required.</div>`}}
    </div>
  ` : "";

  const drawer = document.getElementById("drawerContent");
  drawer.innerHTML = `
    <div class="drawer-head">
      <div>
        <div class="sublabel">App #${{app.id}} &bull; ${{esc(app.category)}} &bull; Run: <code>${{esc(app.run_id)}}</code></div>
        <h2 id="drawerTitle" style="border:none; padding:0; margin:0.2rem 0 0.4rem;">${{esc(app.name)}}</h2>
        <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
          <span class="badge ${{qm.cls}}">${{qm.label}}</span>
          <span class="badge ${{mm.cls}}">${{mm.label}}</span>
          ${{app.in_sample ? '<span class="badge b-sample">Task 17/18 Audited Sample</span>' : ''}}
        </div>
      </div>
      <div style="display:flex; gap:0.4rem;">
        <button class="btn" id="copyAppJsonBtn" type="button">Copy JSON</button>
        <button class="btn" id="closeDrawerBtn" type="button" aria-label="Close details">Close &times;</button>
      </div>
    </div>

    <div class="drawer-section">
      <h4>Primary Purpose</h4>
      <p style="margin:0; font-size:0.88rem; color:var(--text);">${{esc(app.purpose)}}</p>
    </div>

    <div class="drawer-section">
      <h4>Buildability Assessment (${{esc(app.sub_tier || qm.label)}})</h4>
      ${{app.scope ? `<p style="font-size:0.85rem;"><strong>Target Scope:</strong> ${{esc(app.scope)}}</p>` : ""}}
      ${{app.blockers.length ? `<div style="font-size:0.84rem;"><strong>Blockers:</strong><ul>${{app.blockers.map(b => `<li>${{esc(b)}}</li>`).join("")}}</ul></div>` : ""}}
      ${{app.next_steps.length ? `<div style="font-size:0.84rem;"><strong>Recommended Next Steps:</strong><ul>${{app.next_steps.map(s => `<li>${{esc(s)}}</li>`).join("")}}</ul></div>` : ""}}
      ${{app.buildability_rationale ? `<div class="sublabel" style="margin-top:0.4rem;"><strong>Rationale:</strong> ${{esc(app.buildability_rationale)}}</div>` : ""}}
    </div>

    ${{sampleHtml}}

    <div class="drawer-section">
      <h4>Auth &amp; API Surface</h4>
      <div style="margin-bottom:0.4rem;">
        <strong>Auth:</strong> ${{app.auth_methods.length ? app.auth_methods.map(m => `<span class="b-chip">${{esc(AUTH_LABELS[m] || m)}}</span>`).join("") : "Unknown"}}
      </div>
      <div style="margin-bottom:0.4rem;">
        <strong>Protocols:</strong> ${{app.protocols.length ? app.protocols.map(p => `<span class="b-chip">${{esc(p)}}</span>`).join("") : "Unknown"}}
        &nbsp;&bull;&nbsp; <strong>Breadth:</strong> <code>${{esc(app.breadth)}}</code>
      </div>
      ${{app.auth_notes ? `<div class="sublabel">${{esc(app.auth_notes)}}</div>` : ""}}
    </div>

    <div class="drawer-section">
      <h4>Credential Gating Matrix (Testing vs. Production)</h4>
      <table style="font-size:0.82rem;">
        <thead><tr><th>Condition</th><th>Testing</th><th>Production</th></tr></thead>
        <tbody>${{gateRows}}</tbody>
      </table>
    </div>

    <div class="drawer-section">
      <h4>MCP Server Implementations</h4>
      ${{mcpHtml}}
    </div>

    <div class="drawer-section">
      <h4>Primary Cited Sources (${{app.evidence_urls.length}})</h4>
      ${{app.evidence_urls.length
        ? `<ul>${{app.evidence_urls.map(u => `<li><a href="${{esc(u)}}" target="_blank" rel="noopener noreferrer">${{esc(u)}}</a></li>`).join("")}}</ul>`
        : `<p class="muted" style="margin:0; font-size:0.84rem;">No captured public URLs.</p>`}}
    </div>
  `;

  document.getElementById("drawerBackdrop").classList.add("open");
  document.getElementById("closeDrawerBtn").onclick = closeDrawer;
  document.getElementById("copyAppJsonBtn").onclick = () => {{
    navigator.clipboard?.writeText(JSON.stringify(app, null, 2));
    document.getElementById("copyAppJsonBtn").textContent = "Copied!";
    setTimeout(() => {{ document.getElementById("copyAppJsonBtn").textContent = "Copy JSON"; }}, 1500);
  }};
}}

function closeDrawer() {{
  document.getElementById("drawerBackdrop").classList.remove("open");
}}

// Event Listeners
document.getElementById("searchInput").addEventListener("input", e => {{
  state.search = e.target.value;
  renderTable();
}});
document.getElementById("categoryFilter").addEventListener("change", e => {{
  state.category = e.target.value;
  renderTable();
}});
document.getElementById("mcpFilter").addEventListener("change", e => {{
  state.mcp = e.target.value;
  renderTable();
}});
document.getElementById("authFilter").addEventListener("change", e => {{
  state.auth = e.target.value;
  renderTable();
}});
document.getElementById("sampleOnlyCheck").addEventListener("change", e => {{
  state.sampleOnly = e.target.checked;
  renderTable();
}});
document.querySelectorAll("#queuePills .pill-btn").forEach(btn => {{
  btn.addEventListener("click", () => {{
    document.querySelectorAll("#queuePills .pill-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    state.queue = btn.dataset.queue;
    renderTable();
  }});
}});
document.querySelectorAll("#matrixTable th.sortable").forEach(th => {{
  th.addEventListener("click", () => {{
    const key = th.dataset.sort;
    if (state.sortKey === key) state.sortDir *= -1;
    else {{ state.sortKey = key; state.sortDir = 1; }}
    renderTable();
  }});
}});
document.getElementById("matrixBody").addEventListener("click", e => {{
  const tr = e.target.closest("tr[data-id]");
  if (tr) openDrawer(Number(tr.dataset.id));
}});
document.getElementById("matrixBody").addEventListener("keydown", e => {{
  if (e.key === "Enter") {{
    const tr = e.target.closest("tr[data-id]");
    if (tr) openDrawer(Number(tr.dataset.id));
  }}
}});
document.getElementById("drawerBackdrop").addEventListener("click", e => {{
  if (e.target.id === "drawerBackdrop") closeDrawer();
}});
document.addEventListener("keydown", e => {{
  if (e.key === "Escape") closeDrawer();
}});
document.getElementById("resetFiltersBtn").addEventListener("click", () => {{
  state = {{ search: "", category: "", queue: "", mcp: "", auth: "", sampleOnly: false, sortKey: "id", sortDir: 1 }};
  document.getElementById("searchInput").value = "";
  document.getElementById("categoryFilter").value = "";
  document.getElementById("mcpFilter").value = "";
  document.getElementById("authFilter").value = "";
  document.getElementById("sampleOnlyCheck").checked = false;
  document.querySelectorAll("#queuePills .pill-btn").forEach(b => b.classList.toggle("active", b.dataset.queue === ""));
  renderTable();
}});
document.getElementById("exportJsonBtn").addEventListener("click", () => {{
  const data = getFilteredApps();
  const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: "application/json" }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `composio-case-study-filtered-${{data.length}}-apps.json`;
  a.click();
  URL.revokeObjectURL(url);
}});

// Theme toggle
const themeBtn = document.getElementById("themeToggle");
themeBtn.addEventListener("click", () => {{
  const isDark = document.documentElement.getAttribute("data-theme") === "dark";
  document.documentElement.setAttribute("data-theme", isDark ? "light" : "dark");
  themeBtn.textContent = isDark ? "Dark Mode" : "Light Mode";
}});

// Initialize
initFilters();
renderTable();
</script>
</body>
</html>
"""

    out_path = OUT_DIR / "index.html"
    root_path = ROOT / "index.html"
    out_path.write_text(html_doc, encoding="utf-8")
    shutil.copyfile(out_path, root_path)

    print(f"Generated: {out_path} ({out_path.stat().st_size:,} bytes)")
    print(f"Copied to: {root_path} ({root_path.stat().st_size:,} bytes)")
    print(f"Embedded apps: {len(apps_payload)}")
    queues_count = {}
    for a in apps_payload:
        queues_count[a["queue"]] = queues_count.get(a["queue"], 0) + 1
    print(f"Queue counts: {queues_count}")
    sample_count = sum(1 for a in apps_payload if a["in_sample"])
    print(f"Sampled apps: {sample_count}")


if __name__ == "__main__":
    generate_html()
