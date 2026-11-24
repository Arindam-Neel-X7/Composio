"""
Generate the Human Review Packet for the frozen 20-app verification sample.
Preserves original first-pass answers, extracts locator snapshots, and creates:
1. outputs/task-17/human_review_packet.json
2. outputs/task-17/human_review_worksheet.md
3. outputs/task-17/human_review_form.html (interactive local HTML form)
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

TASK_RUNS = {
    7: "task07-first-pass-003",
    8: "task08-first-pass-003",
    9: "task09-first-pass-004",
    10: "task10-first-pass-003",
    11: "task11-first-pass-004",
    12: "task12-first-pass-005",
    13: "task13-first-pass-003",
    14: "task14-first-pass-003",
    15: "task15-first-pass-002",
    16: "task16-first-pass-001",
}


def extract_snapshot_lines(file_path: Path, locator: str) -> str:
    if not file_path.exists():
        return ""
    try:
        lines = file_path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return ""
    m = re.match(r"lines:(\d+)(?:-(\d+))?", locator)
    if not m:
        return ""
    start = int(m.group(1))
    end = int(m.group(2)) if m.group(2) else start
    # 1-based indexing
    excerpt_lines = lines[start - 1 : end]
    return "\n".join(f"{i}: {line}" for i, line in enumerate(excerpt_lines, start=start))


def main():
    manifest_path = ROOT / "outputs/task-06/sampling-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    selected_apps = manifest["selected_apps"]
    selected_ids = {a["id"]: a for a in selected_apps}

    from research_pipeline import claims

    packet_apps = []
    total_claims = 0

    for app_meta in selected_apps:
        app_id = app_meta["id"]
        # Find which task batch contains this app
        batch_num = None
        for b in range(7, 17):
            if (b - 7) * 10 < app_id <= (b - 6) * 10:
                batch_num = b
                break
        if batch_num is None:
            raise ValueError(f"Could not map app {app_id} to batch")

        run_id = TASK_RUNS[batch_num]
        run_dir = ROOT / f"work/research-runs/{run_id}"
        records = json.loads((run_dir / "records.json").read_text(encoding="utf-8"))
        record = next((r for r in records if r["identity"]["id"] == app_id), None)
        if not record:
            raise ValueError(f"App {app_id} not found in {run_id}")

        app_claims = []
        for path, c in claims(record):
            if c["status"] in ("observed", "inferred") and path[0] != "identity":
                evidence_list = []
                for ev in c.get("evidence", []):
                    snap_ref = ev.get("snapshot_ref")
                    snap_path = run_dir / snap_ref if snap_ref else None
                    locator = ev.get("locator", "")
                    excerpt = extract_snapshot_lines(snap_path, locator) if snap_path else ""
                    evidence_list.append(
                        {
                            "source_url": ev.get("source_url"),
                            "source_kind": ev.get("source_kind"),
                            "locator": locator,
                            "observation": ev.get("observation"),
                            "captured_on": ev.get("captured_on"),
                            "capture_method": ev.get("capture_method"),
                            "content_sha256": ev.get("content_sha256"),
                            "snapshot_ref": snap_ref,
                            "snapshot_excerpt": excerpt,
                        }
                    )

                app_claims.append(
                    {
                        "claim_id": c["claim_id"],
                        "path": list(path),
                        "section": path[0],
                        "status": c["status"],
                        "context": c.get("context"),
                        "value": c.get("value"),
                        "rationale": c.get("rationale"),
                        "supporting_claim_refs": c.get("supporting_claim_refs", []),
                        "original_evidence": evidence_list,
                        "human_judgment": None,
                        "human_reason": None,
                        "human_evidence": [],
                    }
                )

        total_claims += len(app_claims)
        packet_apps.append(
            {
                "id": app_id,
                "app": app_meta["app"],
                "category": app_meta["category"],
                "rank_hash": app_meta.get("rank_hash"),
                "in_task04_pilot": app_meta.get("in_task04_pilot", False),
                "original_run_id": run_id,
                "identity_status": (
                    "unresolved"
                    if record.get("identity", {}).get("resolution", {}).get("status") == "unknown"
                    else "resolved"
                ),
                "claims_count": len(app_claims),
                "claims": app_claims,
            }
        )

    packet = {
        "manifest_id": manifest["manifest_id"],
        "sampling_manifest_ref": "outputs/task-06/sampling-manifest.json",
        "sample_size": len(packet_apps),
        "total_eligible_claims": total_claims,
        "selection_seed": manifest.get("seed"),
        "created_for": "Task 17 Human Baseline Audit",
        "instructions": (
            "Independent human review of first-pass research assertions. "
            "Read each claim and attached primary source documentation. "
            "Assign one of correct, incorrect, unsupported, unresolved, or not_applicable. "
            "Record human reviewer ID, date, explanation, and evidence."
        ),
        "apps": packet_apps,
    }

    out_dir = ROOT / "outputs/task-17"
    out_dir.mkdir(parents=True, exist_ok=True)
    work_dir = ROOT / "work/task-17-human-review"
    work_dir.mkdir(parents=True, exist_ok=True)

    # 1. Save JSON packet
    json_path = out_dir / "human_review_packet.json"
    json_path.write_text(json.dumps(packet, indent=2, ensure_ascii=False), encoding="utf-8")
    (work_dir / "human_review_packet.json").write_text(
        json.dumps(packet, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Saved JSON packet to {json_path} ({total_claims} claims across {len(packet_apps)} apps)")

    # 2. Save Markdown Worksheet
    md_lines = [
        "# Task 17: Human Review Worksheet (Frozen 20-App Verification Sample)",
        "",
        "- **Sampling Manifest**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`)",
        f"- **Sample Size**: {len(packet_apps)} apps across 10 categories",
        f"- **Total Scored Claims**: {total_claims} eligible first-pass research assertions (`path[0] != 'identity'`, `status in ['observed', 'inferred']`)",
        "- **Review Mode**: Actual human audit (`reviewer_type: 'human'`, `--actual-human-attestation`)",
        "- **AI Reviewer Conclusions**: Hidden during baseline review to prevent anchoring/bias.",
        "",
        "---",
        "",
        "## Reviewer Metadata",
        "",
        "- **Reviewer Identity**: `[Enter Name / Email / ID]`",
        "- **Review Date**: `[YYYY-MM-DD]`",
        "- **Actual Human Attestation**: `[ ] Checked (I confirm that these adjudications represent an actual human audit of primary documentation)`",
        "",
        "---",
        "",
        "## Claim Adjudication Instructions",
        "",
        "For each claim below, inspect the primary source documentation URL and local snapshot excerpt, then assign one judgment:",
        "1. **`correct`**: All material details hold for the declared scope and are anchored in primary evidence.",
        "2. **`incorrect`**: Contradicted by primary documentation or factually false for stated scope.",
        "3. **`unsupported`**: Fails to substantiate one or more material details (citation missing, broken scope, edition conflation).",
        "4. **`unresolved`**: Could not be adjudicated due to capture failure (must reference fetch error).",
        "5. **`not_applicable`**: Claim does not apply to the declared scope, backed by evidence.",
        "",
        "---",
        "",
    ]

    for app in packet_apps:
        md_lines.append(f"## App {app['id']}: {app['app']} ({app['category']})")
        md_lines.append(f"- **Original Run**: `{app['original_run_id']}`")
        md_lines.append(f"- **Eligible Assertions**: {app['claims_count']}")
        if app["claims_count"] == 0:
            md_lines.append(
                "- *Note*: App has unresolved identity / 0 asserted claims (all preserved as unknown). Excluded from accuracy denominator."
            )
            md_lines.append("")
            continue

        md_lines.append("")
        for idx, cl in enumerate(app["claims"], 1):
            md_lines.append(f"### Claim {app['id']}.{idx}: `{cl['claim_id']}` ({cl['section']})")
            md_lines.append(f"- **Section / Path**: `{' -> '.join(str(p) for p in cl['path'])}`")
            md_lines.append(f"- **Basis**: `{cl['status']}`")
            md_lines.append(f"- **Context / Scope**: {cl['context']}")
            md_lines.append(
                f"- **First-Pass Answer**: `{json.dumps(cl['value'], ensure_ascii=False)}`"
            )
            if cl.get("rationale"):
                md_lines.append(f"- **Rationale**: {cl['rationale']}")
            if cl.get("supporting_claim_refs"):
                md_lines.append(
                    f"- **Supporting Claim Refs**: `{', '.join(cl['supporting_claim_refs'])}`"
                )

            md_lines.append("- **Primary Evidence Cited**:")
            for ev_idx, ev in enumerate(cl["original_evidence"], 1):
                md_lines.append(
                    f"  {ev_idx}. [{ev['source_url']}]({ev['source_url']}) (`{ev['source_kind']}`, `{ev['locator']}`)"
                )
                md_lines.append(f"     - *Observation*: {ev['observation']}")
                if ev.get("snapshot_excerpt"):
                    md_lines.append(f"     - *Local Snapshot Excerpt* (`{ev['snapshot_ref']}`):")
                    md_lines.append("       ```text")
                    for s_line in ev["snapshot_excerpt"].splitlines()[:10]:
                        md_lines.append(f"       {s_line}")
                    if len(ev["snapshot_excerpt"].splitlines()) > 10:
                        md_lines.append("       ... [truncated in markdown; full in HTML form]")
                    md_lines.append("       ```")

            md_lines.append("- **Human Judgment** (leave blank until reviewed): `[ ] correct | [ ] incorrect | [ ] unsupported | [ ] unresolved | [ ] not_applicable`")
            md_lines.append("- **Human Explanation / Reason**: `[Enter human explanation]`")
            md_lines.append("- **Review Evidence / Citation**: `[Same as original / Enter custom evidence]`")
            md_lines.append("")

        md_lines.append("---")
        md_lines.append("")

    worksheet_path = out_dir / "human_review_worksheet.md"
    worksheet_path.write_text("\n".join(md_lines), encoding="utf-8")
    (work_dir / "human_review_worksheet.md").write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Saved Markdown worksheet to {worksheet_path}")

    # 3. Save Interactive Local HTML Form
    html_content = generate_html_form(packet)
    html_path = out_dir / "human_review_form.html"
    html_path.write_text(html_content, encoding="utf-8")
    (work_dir / "human_review_form.html").write_text(html_content, encoding="utf-8")
    print(f"Saved Interactive HTML form to {html_path}")


def generate_html_form(packet: dict) -> str:
    packet_json_str = json.dumps(packet, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Task 17: Human Review Form (Frozen 20-App Sample)</title>
<style>
  :root {{
    --bg: #f8fafc;
    --card-bg: #ffffff;
    --text: #0f172a;
    --text-muted: #64748b;
    --primary: #2563eb;
    --primary-hover: #1d4ed8;
    --border: #e2e8f0;
    --success: #16a34a;
    --danger: #dc2626;
    --warning: #d97706;
    --info: #0284c7;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.5;
    padding-bottom: 80px;
  }}
  header {{
    background: #1e293b;
    color: white;
    padding: 20px 32px;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
  }}
  .header-content {{
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }}
  h1 {{ font-size: 1.4rem; font-weight: 700; }}
  .badge {{
    background: #334155;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 500;
  }}
  .container {{
    max-width: 1400px;
    margin: 24px auto;
    padding: 0 24px;
    display: grid;
    grid-template-columns: 320px 1fr;
    gap: 24px;
  }}
  @media (max-width: 900px) {{
    .container {{ grid-template-columns: 1fr; }}
  }}
  .sidebar {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    height: fit-content;
    position: sticky;
    top: 100px;
  }}
  .sidebar h3 {{
    font-size: 1rem;
    margin-bottom: 12px;
    color: var(--text);
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
  }}
  .stat-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 20px;
  }}
  .stat-card {{
    background: var(--bg);
    padding: 10px;
    border-radius: 8px;
    text-align: center;
    border: 1px solid var(--border);
  }}
  .stat-val {{ font-size: 1.3rem; font-weight: 700; color: var(--primary); }}
  .stat-lbl {{ font-size: 0.75rem; color: var(--text-muted); }}
  .reviewer-box {{
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .reviewer-box label {{ font-size: 0.85rem; font-weight: 600; color: var(--text); }}
  .reviewer-box input {{
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: 6px;
    font-size: 0.9rem;
  }}
  .attestation-box {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    padding: 10px;
    border-radius: 8px;
    font-size: 0.8rem;
    margin-bottom: 16px;
  }}
  .filter-group {{
    margin-bottom: 16px;
  }}
  .filter-group label {{
    display: block;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 6px;
  }}
  .filter-group select {{
    width: 100%;
    padding: 8px;
    border: 1px solid var(--border);
    border-radius: 6px;
    font-size: 0.85rem;
  }}
  .app-list {{
    max-height: 240px;
    overflow-y: auto;
    border: 1px solid var(--border);
    border-radius: 6px;
    margin-bottom: 16px;
  }}
  .app-nav-item {{
    padding: 8px 12px;
    font-size: 0.85rem;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .app-nav-item:hover, .app-nav-item.active {{
    background: #eff6ff;
    color: var(--primary);
    font-weight: 600;
  }}
  .btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 10px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    border-radius: 6px;
    cursor: pointer;
    border: none;
    transition: all 0.2s;
    width: 100%;
    margin-bottom: 8px;
  }}
  .btn-primary {{ background: var(--primary); color: white; }}
  .btn-primary:hover {{ background: var(--primary-hover); }}
  .btn-secondary {{ background: #f1f5f9; color: #334155; border: 1px solid var(--border); }}
  .btn-secondary:hover {{ background: #e2e8f0; }}
  .btn-success {{ background: var(--success); color: white; }}
  .btn-success:hover {{ background: #15803d; }}

  .main-content {{
    display: flex;
    flex-direction: column;
    gap: 20px;
  }}
  .notice-banner {{
    background: #fef3c7;
    border: 1px solid #fde68a;
    color: #92400e;
    padding: 14px 18px;
    border-radius: 10px;
    font-size: 0.9rem;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }}
  .claim-card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    transition: border-color 0.2s;
  }}
  .claim-card.judged {{
    border-left: 6px solid var(--success);
  }}
  .claim-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1px solid var(--border);
    padding-bottom: 14px;
    margin-bottom: 16px;
    gap: 12px;
    flex-wrap: wrap;
  }}
  .claim-title {{
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--text);
  }}
  .claim-meta {{
    display: flex;
    gap: 8px;
    font-size: 0.8rem;
    flex-wrap: wrap;
  }}
  .tag {{
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 600;
    font-size: 0.75rem;
  }}
  .tag-observed {{ background: #dcfce7; color: #166534; }}
  .tag-inferred {{ background: #e0e7ff; color: #3730a3; }}
  .tag-section {{ background: #f1f5f9; color: #475569; }}
  
  .claim-section-title {{
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-muted);
    margin-bottom: 6px;
    margin-top: 14px;
  }}
  .answer-box {{
    background: #f8fafc;
    border: 1px solid var(--border);
    padding: 12px;
    border-radius: 8px;
    font-family: monospace;
    font-size: 0.9rem;
    white-space: pre-wrap;
    word-break: break-all;
    max-height: 180px;
    overflow-y: auto;
  }}
  .evidence-item {{
    background: #f8fafc;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px;
    margin-top: 8px;
    font-size: 0.85rem;
  }}
  .evidence-url {{
    font-weight: 600;
    color: var(--primary);
    text-decoration: none;
    word-break: break-all;
  }}
  .evidence-url:hover {{ text-decoration: underline; }}
  .evidence-obs {{
    margin-top: 6px;
    font-style: italic;
    color: #334155;
  }}
  .snapshot-accordion {{
    margin-top: 8px;
    border-top: 1px dashed var(--border);
    padding-top: 8px;
  }}
  .snapshot-summary {{
    font-size: 0.8rem;
    color: var(--text-muted);
    cursor: pointer;
    font-weight: 600;
  }}
  .snapshot-text {{
    background: #0f172a;
    color: #f8fafc;
    padding: 10px;
    border-radius: 6px;
    font-family: monospace;
    font-size: 0.8rem;
    white-space: pre-wrap;
    max-height: 200px;
    overflow-y: auto;
    margin-top: 6px;
  }}
  .ai-lock-banner {{
    background: #f1f5f9;
    border: 1px dashed #cbd5e1;
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 0.8rem;
    color: #64748b;
    margin-top: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .decision-panel {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 8px;
    padding: 16px;
    margin-top: 18px;
  }}
  .decision-title {{
    font-size: 0.95rem;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .judgment-options {{
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 14px;
  }}
  .judgment-label {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: white;
    padding: 6px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    font-size: 0.85rem;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.15s;
  }}
  .judgment-label:hover {{ border-color: var(--primary); }}
  .judgment-label input[type="radio"]:checked + span {{
    color: var(--primary);
  }}
  .reason-input {{
    width: 100%;
    padding: 10px;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    font-size: 0.85rem;
    min-height: 60px;
    font-family: inherit;
  }}
  .custom-evidence-box {{
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .custom-evidence-box input {{
    width: 100%;
    padding: 8px;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    font-size: 0.8rem;
  }}
  .sticky-footer {{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #ffffff;
    border-top: 1px solid var(--border);
    padding: 12px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    z-index: 90;
  }}
</style>
</head>
<body>

<header>
  <div class="header-content">
    <div>
      <h1>Task 17: Human Baseline Review</h1>
      <span style="font-size: 0.85rem; color: #94a3b8;">Stratified 20-App Sample (composio-20app-sample-v1)</span>
    </div>
    <div style="display: flex; gap: 12px; align-items: center;">
      <span class="badge" id="header-progress">0 / 327 Judged (0%)</span>
      <button class="btn btn-primary" style="margin: 0; width: auto; padding: 6px 16px;" onclick="exportJudgmentsJSON()">Export JSON</button>
    </div>
  </div>
</header>

<div class="container">
  <!-- Sidebar -->
  <aside class="sidebar">
    <h3>Reviewer Information</h3>
    <div class="reviewer-box">
      <label for="reviewer-id">Reviewer ID / Name</label>
      <input type="text" id="reviewer-id" placeholder="e.g. human-auditor-1" oninput="saveMetadata()">
      <label for="review-date">Date</label>
      <input type="date" id="review-date" onchange="saveMetadata()">
    </div>
    <div class="attestation-box">
      <label style="display: flex; gap: 8px; cursor: pointer; font-weight: 500;">
        <input type="checkbox" id="human-attestation" onchange="saveMetadata()">
        <span><strong>Actual Human Attestation</strong>: I confirm these adjudications represent real human audit of primary sources.</span>
      </label>
    </div>

    <h3>Progress & Metrics</h3>
    <div class="stat-grid">
      <div class="stat-card">
        <div class="stat-val" id="stat-total">327</div>
        <div class="stat-lbl">Eligible Claims</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" id="stat-judged" style="color: var(--success);">0</div>
        <div class="stat-lbl">Completed</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" id="stat-pending" style="color: var(--warning);">327</div>
        <div class="stat-lbl">Pending</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" id="stat-accuracy">--</div>
        <div class="stat-lbl">Current Acc</div>
      </div>
    </div>

    <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 16px;" id="stat-breakdown">
      Correct: 0 | Incorrect: 0 | Unsupported: 0 | Unresolved: 0
    </div>

    <h3>Navigation & Filter</h3>
    <div class="filter-group">
      <label>Filter by Status</label>
      <select id="filter-status" onchange="renderClaims()">
        <option value="all">All Claims (327)</option>
        <option value="pending">Pending Only</option>
        <option value="completed">Completed Only</option>
      </select>
    </div>
    <div class="filter-group">
      <label>Filter by Section</label>
      <select id="filter-section" onchange="renderClaims()">
        <option value="all">All Sections</option>
        <option value="purpose">Purpose (19)</option>
        <option value="auth">Auth (38)</option>
        <option value="credential_eligibility">Credentials (90)</option>
        <option value="api_surface">API Surface (126)</option>
        <option value="mcp">MCP (35)</option>
        <option value="buildability">Buildability (19)</option>
      </select>
    </div>

    <label style="font-size: 0.85rem; font-weight: 600; margin-bottom: 6px; display: block;">Select App</label>
    <div class="app-list" id="app-nav-list"></div>

    <button class="btn btn-primary" onclick="exportJudgmentsJSON()">Export Pipeline JSON</button>
    <button class="btn btn-secondary" onclick="document.getElementById('import-file').click()">Load Progress JSON</button>
    <input type="file" id="import-file" style="display: none;" accept=".json" onchange="importJudgmentsJSON(event)">
    <button class="btn btn-secondary" onclick="resetProgress()">Reset Progress</button>
  </aside>

  <!-- Main Claims Area -->
  <main class="main-content">
    <div class="notice-banner">
      <div style="font-size: 1.5rem;">🔒</div>
      <div>
        <strong>Unbiased Baseline Policy</strong>: AI reviewer conclusions from Tasks 07–16 are hidden to prevent anchoring.
        Evaluate each claim solely against the attached primary vendor documentation URL, source locator, and snapshot text.
        Your judgments will be recorded as the ground-truth baseline for Task 17.
      </div>
    </div>

    <div id="claims-container"></div>
  </main>
</div>

<footer class="sticky-footer">
  <div>
    <span id="footer-status" style="font-size: 0.9rem; font-weight: 600; color: #334155;">Ready</span>
    <span id="auto-save-status" style="font-size: 0.8rem; color: var(--text-muted); margin-left: 12px;">Auto-saved locally</span>
  </div>
  <div style="display: flex; gap: 12px;">
    <button class="btn btn-secondary" style="width: auto; margin: 0;" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})">Top</button>
    <button class="btn btn-primary" style="width: auto; margin: 0;" onclick="exportJudgmentsJSON()">Export Judgments JSON</button>
  </div>
</footer>

<script>
const PACKET = {packet_json_str};

// State: stored in localStorage
let judgments = {{}};
let metadata = {{
  reviewerId: "",
  reviewDate: new Date().toISOString().split("T")[0],
  humanAttestation: false
}};
let activeAppFilter = "all";

function init() {{
  const savedMeta = localStorage.getItem("composio_task17_meta");
  if (savedMeta) {{
    try {{ metadata = JSON.parse(savedMeta); }} catch(e) {{}}
  }}
  document.getElementById("reviewer-id").value = metadata.reviewerId || "";
  document.getElementById("review-date").value = metadata.reviewDate || new Date().toISOString().split("T")[0];
  document.getElementById("human-attestation").checked = !!metadata.humanAttestation;

  const savedJudgments = localStorage.getItem("composio_task17_judgments");
  if (savedJudgments) {{
    try {{ judgments = JSON.parse(savedJudgments); }} catch(e) {{}}
  }}

  renderAppNav();
  renderClaims();
  updateStats();
}}

function saveMetadata() {{
  metadata.reviewerId = document.getElementById("reviewer-id").value.trim();
  metadata.reviewDate = document.getElementById("review-date").value;
  metadata.humanAttestation = document.getElementById("human-attestation").checked;
  localStorage.setItem("composio_task17_meta", JSON.stringify(metadata));
  showAutoSave();
}}

function showAutoSave() {{
  const el = document.getElementById("auto-save-status");
  el.textContent = "Saved to local storage at " + new Date().toLocaleTimeString();
}}

function renderAppNav() {{
  const nav = document.getElementById("app-nav-list");
  nav.innerHTML = "";
  
  const allItem = document.createElement("div");
  allItem.className = "app-nav-item" + (activeAppFilter === "all" ? " active" : "");
  allItem.innerHTML = "<span>All Apps (20)</span><span>327</span>";
  allItem.onclick = () => {{ activeAppFilter = "all"; renderAppNav(); renderClaims(); }};
  nav.appendChild(allItem);

  PACKET.apps.forEach(app => {{
    const item = document.createElement("div");
    item.className = "app-nav-item" + (activeAppFilter === app.id ? " active" : "");
    item.innerHTML = `<span>#${{app.id}} ${{app.app}}</span><span>${{app.claims_count}}</span>`;
    item.onclick = () => {{ activeAppFilter = app.id; renderAppNav(); renderClaims(); }};
    nav.appendChild(item);
  }});
}}

function renderClaims() {{
  const container = document.getElementById("claims-container");
  container.innerHTML = "";

  const statusFilter = document.getElementById("filter-status").value;
  const sectionFilter = document.getElementById("filter-section").value;

  let displayed = 0;

  PACKET.apps.forEach(app => {{
    if (activeAppFilter !== "all" && activeAppFilter !== app.id) return;

    if (app.claims.length === 0) {{
      const card = document.createElement("div");
      card.className = "claim-card";
      card.innerHTML = `
        <div class="claim-header">
          <div>
            <div class="claim-title">App #${{app.id}}: ${{app.app}} (${{app.category}})</div>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Status: Identity Unresolved / 0 Eligible Assertions</div>
          </div>
        </div>
        <p style="font-size: 0.85rem; color: var(--text-muted);">This app has unresolved identity; all product fields are preserved as unknown and excluded from the scored assertion denominator.</p>
      `;
      container.appendChild(card);
      return;
    }}

    app.claims.forEach(cl => {{
      const jKey = `${{app.id}}::${{cl.claim_id}}`;
      const currentJ = judgments[jKey];
      const isJudged = !!(currentJ && currentJ.judgment);

      if (statusFilter === "pending" && isJudged) return;
      if (statusFilter === "completed" && !isJudged) return;
      if (sectionFilter !== "all" && cl.section !== sectionFilter) return;

      displayed++;
      const card = document.createElement("div");
      card.className = "claim-card" + (isJudged ? " judged" : "");
      card.id = `card-${{app.id}}-${{cl.claim_id.replace(/[^a-zA-Z0-9]/g, '_')}}`;

      const evHtml = cl.original_evidence.map((ev, i) => `
        <div class="evidence-item">
          <div><strong>Evidence #${{i+1}}</strong>: <a class="evidence-url" href="${{ev.source_url}}" target="_blank" rel="noopener">${{ev.source_url}}</a></div>
          <div style="color: var(--text-muted); font-size: 0.75rem; margin-top: 2px;">Kind: ${{ev.source_kind}} | Locator: ${{ev.locator}} | Method: ${{ev.capture_method}}</div>
          <div class="evidence-obs">"${{ev.observation}}"</div>
          ${{ev.snapshot_excerpt ? `
            <details class="snapshot-accordion">
              <summary class="snapshot-summary">View local snapshot excerpt (${{ev.snapshot_ref}})</summary>
              <pre class="snapshot-text">${{ev.snapshot_excerpt}}</pre>
            </details>
          ` : ''}}
        </div>
      `).join("");

      card.innerHTML = `
        <div class="claim-header">
          <div>
            <div class="claim-title">App #${{app.id}} ${{app.app}}: <code>${{cl.claim_id}}</code></div>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Scope: <strong>${{cl.context || 'General'}}</strong></div>
          </div>
          <div class="claim-meta">
            <span class="tag tag-${{cl.status}}">${{cl.status}}</span>
            <span class="tag tag-section">${{cl.section}}</span>
            <span class="tag" style="background: #e2e8f0;">${{app.original_run_id}}</span>
          </div>
        </div>

        <div class="claim-section-title">First-Pass Answer / Extracted Value</div>
        <div class="answer-box">${{typeof cl.value === 'object' ? JSON.stringify(cl.value, null, 2) : cl.value}}</div>

        ${{cl.rationale ? `<div style="font-size: 0.85rem; margin-top: 8px;"><strong>Rationale</strong>: ${{cl.rationale}}</div>` : ''}}
        ${{cl.supporting_claim_refs && cl.supporting_claim_refs.length ? `<div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Supporting refs: ${{cl.supporting_claim_refs.join(', ')}}</div>` : ''}}

        <div class="claim-section-title">Primary Document Links & Attached Evidence (${{cl.original_evidence.length}})</div>
        ${{evHtml}}

        <div class="ai-lock-banner">
          <span>🔒</span>
          <span><strong>AI conclusions locked</strong>: First-pass AI auditor notes are withheld until human baseline is exported.</span>
        </div>

        <div class="decision-panel">
          <div class="decision-title">
            <span>Human Adjudication</span>
            ${{isJudged ? '<span style="color: var(--success); font-size: 0.8rem;">✓ Judged: ' + currentJ.judgment.toUpperCase() + '</span>' : '<span style="color: var(--warning); font-size: 0.8rem;">Pending Review</span>'}}
          </div>
          <div class="judgment-options">
            ${{['correct', 'incorrect', 'unsupported', 'unresolved', 'not_applicable'].map(val => `
              <label class="judgment-label">
                <input type="radio" name="j-${{jKey}}" value="${{val}}" ${{currentJ && currentJ.judgment === val ? 'checked' : ''}} onchange="recordJudgment(${{app.id}}, '${{cl.claim_id}}', '${{val}}')">
                <span>${{val}}</span>
              </label>
            `).join('')}}
          </div>
          <div>
            <textarea class="reason-input" placeholder="Explain judgment reason (required)..." oninput="recordReason(${{app.id}}, '${{cl.claim_id}}', this.value)">${{currentJ && currentJ.reason ? currentJ.reason : ''}}</textarea>
          </div>
        </div>
      `;

      container.appendChild(card);
    }});
  }});

  if (displayed === 0) {{
    container.innerHTML = '<div class="claim-card" style="text-align: center; color: var(--text-muted); padding: 40px;">No claims match the active filters.</div>';
  }}
}}

function recordJudgment(appId, claimId, val) {{
  const jKey = `${{appId}}::${{claimId}}`;
  if (!judgments[jKey]) judgments[jKey] = {{ appId, claimId, evidence: [] }};
  judgments[jKey].judgment = val;
  if (!judgments[jKey].reason) {{
    judgments[jKey].reason = val === 'correct' ? 'Verified against primary documentation and snapshot excerpt.' : '';
  }}
  saveJudgments();
  updateStats();
  renderClaims();
}}

function recordReason(appId, claimId, reasonVal) {{
  const jKey = `${{appId}}::${{claimId}}`;
  if (!judgments[jKey]) judgments[jKey] = {{ appId, claimId, evidence: [] }};
  judgments[jKey].reason = reasonVal;
  saveJudgments();
}}

function saveJudgments() {{
  localStorage.setItem("composio_task17_judgments", JSON.stringify(judgments));
  showAutoSave();
}}

function updateStats() {{
  let total = PACKET.total_eligible_claims;
  let judgedCount = 0;
  let correct = 0, incorrect = 0, unsupported = 0, unresolved = 0, na = 0;

  Object.values(judgments).forEach(j => {{
    if (j && j.judgment) {{
      judgedCount++;
      if (j.judgment === 'correct') correct++;
      else if (j.judgment === 'incorrect') incorrect++;
      else if (j.judgment === 'unsupported') unsupported++;
      else if (j.judgment === 'unresolved') unresolved++;
      else if (j.judgment === 'not_applicable') na++;
    }}
  }});

  const pending = total - judgedCount;
  const denom = correct + incorrect + unsupported;
  const acc = denom > 0 ? ((correct / denom) * 100).toFixed(1) + "%" : "--";
  const pct = ((judgedCount / total) * 100).toFixed(0);

  document.getElementById("stat-total").textContent = total;
  document.getElementById("stat-judged").textContent = judgedCount;
  document.getElementById("stat-pending").textContent = pending;
  document.getElementById("stat-accuracy").textContent = acc;
  document.getElementById("header-progress").textContent = `${{judgedCount}} / ${{total}} Judged (${{pct}}%)`;
  document.getElementById("stat-breakdown").textContent = `Correct: ${{correct}} | Incorrect: ${{incorrect}} | Unsupported: ${{unsupported}} | Unresolved: ${{unresolved}} | N/A: ${{na}}`;
}}

function exportJudgmentsJSON() {{
  saveMetadata();
  if (!metadata.reviewerId) {{
    alert("Please enter a Reviewer ID / Name in the sidebar before exporting.");
    return;
  }}
  if (!metadata.humanAttestation) {{
    if (!confirm("Actual Human Attestation is unchecked. Are you sure you want to export without human attestation?")) {{
      return;
    }}
  }}

  // Build pipeline-compatible structure
  const recordsMap = {{}};
  PACKET.apps.forEach(app => {{
    const appJudgments = [];
    app.claims.forEach(cl => {{
      const jKey = `${{app.id}}::${{cl.claim_id}}`;
      const j = judgments[jKey];
      if (j && j.judgment) {{
        // Evidence: if user didn't specify custom evidence, inherit original primary evidence
        let ev = (j.evidence && j.evidence.length > 0) ? j.evidence : cl.original_evidence.map(e => ({{
          source_url: e.source_url,
          source_kind: e.source_kind,
          locator: e.locator,
          observation: e.observation,
          captured_on: e.captured_on,
          capture_method: e.capture_method,
          content_sha256: e.content_sha256,
          snapshot_ref: e.snapshot_ref,
          hash_unavailable_reason: null,
          document_version: null,
          document_date: null
        }}));

        if (j.judgment === 'unresolved') {{
          ev = [];
        }}

        appJudgments.push({{
          claim_id: cl.claim_id,
          original_run_id: app.original_run_id,
          judgment: j.judgment,
          reason: j.reason || 'Human audit decision',
          evidence: ev
        }});
      }}
    }});
    if (appJudgments.length > 0) {{
      recordsMap[String(app.id)] = appJudgments;
    }}
  }});

  const exportPayload = {{
    reviewer: {{
      id: metadata.reviewerId,
      type: "human",
      human_attestation: !!metadata.humanAttestation,
      reviewed_on: metadata.reviewDate || new Date().toISOString().split("T")[0]
    }},
    sample_manifest_ref: PACKET.sampling_manifest_ref,
    records: recordsMap
  }};

  const blob = new Blob([JSON.stringify(exportPayload, null, 2)], {{ type: "application/json" }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `human-baseline-judgments-${{metadata.reviewerId || 'export'}}.json`;
  a.click();
  URL.revokeObjectURL(url);
}}

function importJudgmentsJSON(evt) {{
  const file = evt.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (e) => {{
    try {{
      const data = JSON.parse(e.target.result);
      if (data.reviewer) {{
        metadata.reviewerId = data.reviewer.id || "";
        metadata.reviewDate = data.reviewer.reviewed_on || "";
        metadata.humanAttestation = !!data.reviewer.human_attestation;
        document.getElementById("reviewer-id").value = metadata.reviewerId;
        document.getElementById("review-date").value = metadata.reviewDate;
        document.getElementById("human-attestation").checked = metadata.humanAttestation;
      }}
      if (data.records) {{
        Object.entries(data.records).forEach(([appId, list]) => {{
          list.forEach(adj => {{
            const jKey = `${{appId}}::${{adj.claim_id}}`;
            judgments[jKey] = {{
              appId: parseInt(appId),
              claimId: adj.claim_id,
              judgment: adj.judgment,
              reason: adj.reason,
              evidence: adj.evidence || []
            }};
          }});
        }});
        saveJudgments();
        saveMetadata();
        renderClaims();
        updateStats();
        alert("Judgments imported successfully!");
      }}
    }} catch(err) {{
      alert("Failed to parse JSON file: " + err.message);
    }}
  }};
  reader.readAsText(file);
}}

function resetProgress() {{
  if (confirm("Are you sure you want to clear all locally saved judgments? This cannot be undone.")) {{
    judgments = {{}};
    localStorage.removeItem("composio_task17_judgments");
    renderClaims();
    updateStats();
  }}
}}

window.onload = init;
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
