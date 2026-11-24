"""
Generate the Task 18 Human Recheck Packet and Interactive Review Form.
Presents side-by-side:
- Original Answer & Task 17 Baseline Judgment (unsupported / correct) & Notes
- Corrected Answer & What Changed explanation
- Primary Documentation links, exact line locators, and snapshot excerpts
- Blank Human Recheck Judgment fields (judgment, explanation, reviewer, date)
Ensures proposed AI approval is hidden from judgment fields.
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from research_pipeline import read_json, run_path

TASK_RUNS = {
    7: ("task07-first-pass-003", "task18-corrections-07"),
    8: ("task08-first-pass-003", "task18-corrections-08"),
    9: ("task09-first-pass-004", "task18-corrections-09"),
    10: ("task10-first-pass-003", "task18-corrections-10"),
    11: ("task11-first-pass-004", "task18-corrections-11"),
    12: ("task12-first-pass-005", "task18-corrections-12"),
    13: ("task13-first-pass-003", "task18-corrections-13"),
    14: ("task14-first-pass-003", "task18-corrections-14"),
    15: ("task15-first-pass-002", "task18-corrections-15"),
    16: ("task16-first-pass-001", "task18-corrections-16"),
}

STORE = ROOT / "work/research-runs"


def extract_snapshot_lines(file_path: Path, locator: str) -> str:
    if not file_path.exists():
        return ""
    try:
        lines = file_path.read_text(encoding="utf-8").splitlines()
        m = re.match(r"lines:(\d+)-(\d+)", locator)
        if m:
            start, end = int(m.group(1)) - 1, int(m.group(2))
            start = max(0, start)
            end = min(len(lines), end)
            return "\n".join(lines[start:end])
        return ""
    except Exception:
        return ""


def build_recheck_packet():
    manifest = read_json(ROOT / "outputs/task-06/sampling-manifest.json")
    base_judgments_raw = read_json(ROOT / "outputs/task-17/human-baseline-judgments.json")
    base_records = base_judgments_raw.get("records", {})

    baseline_map = {}
    for aid_str, items in base_records.items():
        aid = int(aid_str)
        for it in items:
            baseline_map[(aid, it["claim_id"])] = it

    selected_apps = {a["id"]: a for a in manifest["selected_apps"]}

    packet_records = {}
    total_claims = 0
    total_corrected = 0

    for b, (parent_rid, child_rid) in sorted(TASK_RUNS.items()):
        p_records = read_json(STORE / parent_rid / "records.json")
        c_records = read_json(STORE / child_rid / "records.json")
        changes = read_json(STORE / child_rid / "changes.json")
        changed_claims = {(c["app_id"], c["claim_id"]): c for c in changes}

        c_rec_map = {r["identity"]["id"]: r for r in c_records}
        p_rec_map = {r["identity"]["id"]: r for r in p_records}

        for aid, app_info in selected_apps.items():
            if aid not in c_rec_map:
                continue

            c_rec = c_rec_map[aid]
            p_rec = p_rec_map[aid]

            app_claims = []

            from research_pipeline import claims
            p_claim_map = {c["claim_id"]: c for _, c in claims(p_rec)}
            c_claim_map = {c["claim_id"]: c for _, c in claims(c_rec)}

            for cid, c_claim in sorted(c_claim_map.items()):
                b_adj = baseline_map.get((aid, cid))
                if not b_adj:
                    continue  # not in audited sample

                total_claims += 1
                p_claim = p_claim_map.get(cid, {})
                ch = changed_claims.get((aid, cid))
                is_corrected = bool(ch)
                if is_corrected:
                    total_corrected += 1

                evidence_list = []
                for ev in c_claim.get("evidence", []):
                    snap_ref = ev.get("snapshot_ref")
                    snap_path = STORE / child_rid / snap_ref if snap_ref else None
                    snap_text = extract_snapshot_lines(snap_path, ev.get("locator", "")) if snap_path else ""

                    evidence_list.append({
                        "source_url": ev.get("source_url"),
                        "source_kind": ev.get("source_kind"),
                        "locator": ev.get("locator"),
                        "observation": ev.get("observation"),
                        "captured_on": ev.get("captured_on"),
                        "content_sha256": ev.get("content_sha256"),
                        "snapshot_ref": snap_ref,
                        "snapshot_excerpt": snap_text,
                    })

                app_claims.append({
                    "app_id": aid,
                    "app_name": app_info.get("app") or app_info.get("name"),
                    "category": app_info["category"],
                    "claim_id": cid,
                    "is_corrected": is_corrected,
                    "original_run_id": parent_rid,
                    "correction_run_id": child_rid,
                    "baseline_judgment": b_adj.get("judgment"),
                    "baseline_reason": b_adj.get("reason", "").strip(),
                    "original_answer": {
                        "status": p_claim.get("status"),
                        "value": p_claim.get("value"),
                        "context": p_claim.get("context"),
                        "rationale": p_claim.get("rationale"),
                    },
                    "corrected_answer": {
                        "status": c_claim.get("status"),
                        "value": c_claim.get("value"),
                        "context": c_claim.get("context"),
                        "rationale": c_claim.get("rationale"),
                    },
                    "what_changed": ch.get("reason", "") if ch else "Unchanged from verified baseline.",
                    "evidence": evidence_list,
                    "human_recheck": {
                        "judgment": "",
                        "reason": "",
                        "reviewer_id": "",
                        "reviewed_on": "",
                        "human_attestation": False,
                    }
                })

            if app_claims:
                packet_records[str(aid)] = app_claims

    packet = {
        "manifest_id": manifest["manifest_id"],
        "created_on": "2026-11-24",
        "description": "Task 18 Human Recheck Packet for Frozen 20-App Verification Sample",
        "total_eligible_assertions": total_claims,
        "total_corrected_assertions": total_corrected,
        "total_unchanged_baseline_assertions": total_claims - total_corrected,
        "reviewer_prompt": (
            "Please review each corrected claim against the primary documentation and record your independent human judgment. "
            "Proposed AI approval is strictly withheld from the judgment fields."
        ),
        "records": packet_records,
    }
    return packet


def generate_markdown_worksheet(packet: dict) -> str:
    md = [
        "# Task 18: Human Recheck Worksheet (Frozen 20-App Sample)",
        "",
        f"- **Sampling Manifest**: `{packet['manifest_id']}`",
        f"- **Date**: `{packet['created_on']}`",
        f"- **Total Eligible Assertions**: `{packet['total_eligible_assertions']}`",
        f"- **Corrected Assertions (Action Required)**: `{packet['total_corrected_assertions']}`",
        f"- **Unchanged Baseline Assertions**: `{packet['total_unchanged_baseline_assertions']}`",
        "",
        "> [!IMPORTANT]",
        "> Reviewer instructions: For each corrected claim below, open the primary documentation link, inspect the cited excerpt, ",
        "> and record your human recheck judgment (`correct`, `incorrect`, `unsupported`, `unresolved`, `not_applicable`) ",
        "> along with an explanation. Human attestation is required for all submitted decisions.",
        "",
        "---",
        "",
    ]

    for aid_str, claims in packet["records"].items():
        aid = int(aid_str)
        app_name = claims[0]["app_name"]
        cat = claims[0]["category"]
        corrected_count = sum(1 for c in claims if c["is_corrected"])

        md.append(f"## App {aid}: {app_name} ({cat})")
        md.append(f"- Total claims: {len(claims)} | Corrected: {corrected_count}")
        md.append("")

        for c in claims:
            cid = c["claim_id"]
            corr_badge = "**[CORRECTED - ACTION REQUIRED]**" if c["is_corrected"] else "[UNCHANGED - BASELINE VERIFIED]"
            md.append(f"### Claim: `{cid}` {corr_badge}")
            md.append(f"- **Baseline Human Judgment**: `{c['baseline_judgment']}`")
            md.append(f"- **Baseline Reason**: {c['baseline_reason']}")
            md.append("")
            if c["is_corrected"]:
                md.append("#### Before / After Comparison")
                md.append(f"- **What Changed**: {c['what_changed']}")
                md.append(f"- **Original Answer**: `status: {c['original_answer']['status']}`, `value: {json.dumps(c['original_answer']['value'])}`")
                md.append(f"  - Original Rationale: {c['original_answer']['rationale']}")
                md.append(f"- **Corrected Answer**: `status: {c['corrected_answer']['status']}`, `value: {json.dumps(c['corrected_answer']['value'])}`")
                md.append(f"  - Corrected Rationale: {c['corrected_answer']['rationale']}")
                md.append("")

            md.append("#### Primary Evidence & Excerpts")
            for ev in c["evidence"]:
                md.append(f"- **URL**: [{ev['source_url']}]({ev['source_url']}) (locator: `{ev['locator']}`)")
                md.append(f"  - *Observation*: {ev['observation']}")
                if ev.get("snapshot_excerpt"):
                    md.append("  ```text")
                    for line in ev["snapshot_excerpt"].splitlines()[:10]:
                        md.append(f"  {line}")
                    md.append("  ```")
            md.append("")

            md.append("#### Human Recheck Decision (Applicant Input)")
            md.append("- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`")
            md.append("- **Explanation**: `____________________________________________________________________`")
            md.append("- **Reviewer Identity**: `________________________`")
            md.append("- **Date**: `____________________`")
            md.append("- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*")
            md.append("")
            md.append("---")
            md.append("")

    return "\n".join(md)


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Task 18: Human Recheck Form (Frozen 20-App Sample)</title>
<style>
  :root {
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
    --corrected-bg: #fefce8;
    --corrected-border: #fde047;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.5;
    padding-bottom: 80px;
  }
  header {
    background: #0f172a;
    color: white;
    padding: 20px 32px;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
  }
  .header-content {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }
  h1 { font-size: 1.35rem; font-weight: 700; }
  .badge {
    background: #334155;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 500;
  }
  .badge-warn {
    background: #b45309;
    color: white;
  }
  .container {
    max-width: 1400px;
    margin: 24px auto;
    padding: 0 24px;
    display: grid;
    grid-template-columns: 320px 1fr;
    gap: 24px;
  }
  @media (max-width: 1024px) {
    .container { grid-template-columns: 1fr; }
  }
  .sidebar {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
    height: fit-content;
    position: sticky;
    top: 96px;
  }
  .main-content {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .form-group { margin-bottom: 16px; }
  label { display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 6px; color: var(--text-muted); }
  input[type="text"], input[type="date"], select, textarea {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: 6px;
    font-size: 0.9rem;
    color: var(--text);
  }
  input:focus, select:focus, textarea:focus {
    outline: 2px solid var(--primary);
    border-color: transparent;
  }
  .checkbox-group {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    font-size: 0.85rem;
    margin-top: 10px;
  }
  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 10px 16px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 0.9rem;
    cursor: pointer;
    border: none;
    transition: background 0.15s ease;
    width: 100%;
  }
  .btn-primary { background: var(--primary); color: white; }
  .btn-primary:hover { background: var(--primary-hover); }
  .btn-secondary { background: #e2e8f0; color: #1e293b; margin-top: 8px; }
  .btn-secondary:hover { background: #cbd5e1; }
  
  .filter-bar {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
    display: flex;
    gap: 12px;
    align-items: center;
    flex-wrap: wrap;
  }
  .filter-btn {
    padding: 6px 12px;
    border-radius: 6px;
    border: 1px solid var(--border);
    background: #f1f5f9;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: 500;
  }
  .filter-btn.active {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
  }
  
  .claim-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .claim-card.is-corrected {
    border-left: 4px solid var(--warning);
    background: #fffdf5;
  }
  .claim-card.is-unchanged {
    border-left: 4px solid var(--success);
  }
  .claim-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
  }
  .claim-id { font-family: monospace; font-size: 1rem; font-weight: 700; color: var(--primary); }
  .app-tag { font-size: 0.85rem; color: var(--text-muted); }
  
  .baseline-banner {
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 14px;
    font-size: 0.85rem;
  }
  .baseline-banner strong { color: var(--danger); }
  
  .diff-box {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 14px;
  }
  @media (max-width: 768px) {
    .diff-box { grid-template-columns: 1fr; }
  }
  .diff-col {
    background: #f8fafc;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 12px;
    font-size: 0.85rem;
  }
  .diff-col.corrected {
    background: #f0fdf4;
    border-color: #bbf7d0;
  }
  .diff-title { font-weight: 700; margin-bottom: 6px; color: var(--text-muted); font-size: 0.75rem; text-transform: uppercase; }
  
  .evidence-box {
    background: #f1f5f9;
    border-radius: 6px;
    padding: 12px;
    font-size: 0.85rem;
    margin-bottom: 14px;
  }
  .evidence-item { margin-bottom: 8px; }
  .evidence-item:last-child { margin-bottom: 0; }
  .evidence-link { color: var(--primary); text-decoration: none; word-break: break-all; font-weight: 500; }
  .evidence-link:hover { text-decoration: underline; }
  .snapshot-excerpt {
    background: #1e293b;
    color: #e2e8f0;
    padding: 8px 12px;
    border-radius: 4px;
    font-family: monospace;
    font-size: 0.75rem;
    white-space: pre-wrap;
    margin-top: 6px;
    max-height: 140px;
    overflow-y: auto;
  }
  
  .recheck-inputs {
    background: #ffffff;
    border: 2px dashed #94a3b8;
    border-radius: 6px;
    padding: 14px;
  }
  .recheck-inputs label { color: #0f172a; font-size: 0.9rem; }
  .judgment-radios {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin: 8px 0 12px 0;
  }
  .radio-label {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    padding: 4px 10px;
    border-radius: 6px;
    border: 1px solid var(--border);
    background: #f8fafc;
  }
  .radio-label:hover { background: #f1f5f9; }
  .status-saved { color: var(--success); font-weight: 600; font-size: 0.8rem; margin-top: 6px; display: none; }
</style>
</head>
<body>

<header>
  <div class="header-content">
    <div>
      <h1>Task 18: Human Recheck Form</h1>
      <span style="font-size: 0.85rem; color: #94a3b8;">Frozen 20-App Sample &bull; Error Corrections Review</span>
    </div>
    <div style="display: flex; gap: 8px; align-items: center;">
      <span class="badge badge-warn" id="corrected-count-badge">50 Corrected Claims</span>
      <span class="badge" id="total-count-badge">327 Total Claims</span>
      <span class="badge" style="background: #16a34a;" id="completed-count-badge">0 / 50 Rechecked</span>
    </div>
  </div>
</header>

<div class="container">
  <!-- Sidebar -->
  <aside class="sidebar">
    <h2 style="font-size: 1.1rem; margin-bottom: 14px;">Reviewer Identity</h2>
    
    <div class="form-group">
      <label for="reviewer-id">Reviewer Identifier / Name *</label>
      <input type="text" id="reviewer-id" value="ARINDAM KARMAKAR" placeholder="e.g., ARINDAM KARMAKAR">
    </div>

    <div class="form-group">
      <label for="review-date">Review Date *</label>
      <input type="date" id="review-date">
    </div>

    <div class="form-group">
      <label>Actual Human Attestation *</label>
      <div class="checkbox-group">
        <input type="checkbox" id="human-attestation" checked>
        <span style="font-size: 0.8rem; color: #334155;">
          I confirm these adjudications represent my actual human examination of primary vendor documentation.
        </span>
      </div>
    </div>

    <hr style="margin: 16px 0; border: none; border-top: 1px solid var(--border);">

    <div style="margin-bottom: 16px;">
      <div style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 4px;">Progress</div>
      <div style="background: #e2e8f0; border-radius: 9999px; height: 10px; overflow: hidden;">
        <div id="progress-bar" style="background: var(--primary); width: 0%; height: 100%; transition: width 0.3s ease;"></div>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">
        <span id="progress-text">0 / 50 rechecked</span>
        <span id="progress-pct">0%</span>
      </div>
    </div>

    <button class="btn btn-primary" id="export-json-btn">Export Pipeline JSON</button>
    <button class="btn btn-secondary" id="save-local-btn">Save Progress Locally</button>
    
    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 14px; line-height: 1.4;">
      Progress auto-saves to your browser local storage. When done, click <strong>Export Pipeline JSON</strong> and save to:<br>
      <code style="word-break: break-all; font-weight: 600;">outputs/task-18/human-recheck-judgments.json</code>
    </div>
  </aside>

  <!-- Main Content -->
  <main class="main-content">
    <div class="filter-bar">
      <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted);">View:</span>
      <button class="filter-btn active" data-filter="corrected">Corrected Only (50)</button>
      <button class="filter-btn" data-filter="all">All Fixed Claims (327)</button>
      <button class="filter-btn" data-filter="pending">Pending Recheck</button>
      
      <span style="margin-left: auto; font-size: 0.85rem; color: var(--text-muted);">
        App:
        <select id="app-filter" style="width: auto; padding: 4px 8px; font-size: 0.8rem; margin-left: 4px;">
          <option value="all">All Apps (20)</option>
        </select>
      </span>
    </div>

    <div id="claims-container">
      <!-- Dynamic claim cards will render here -->
    </div>
  </main>
</div>

<script>
const PACKET = %%PACKET_DATA%%;

let currentFilter = 'corrected';
let currentAppFilter = 'all';

// Populate review date with today
document.getElementById('review-date').value = new Date().toISOString().split('T')[0];

// Load local storage if available
const STORAGE_KEY = 'composio_task18_recheck_v1';
let userDecisions = {};

try {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {
    userDecisions = JSON.parse(saved);
  }
} catch (e) {
  console.error("Could not load local storage", e);
}

// Populate App dropdown
const appSelect = document.getElementById('app-filter');
const seenApps = new Set();
for (const [aid, claims] of Object.entries(PACKET.records)) {
  if (!seenApps.has(aid) && claims.length > 0) {
    seenApps.add(aid);
    const opt = document.createElement('option');
    opt.value = aid;
    opt.textContent = `App ${aid}: ${claims[0].app_name}`;
    appSelect.appendChild(opt);
  }
}

appSelect.addEventListener('change', (e) => {
  currentAppFilter = e.target.value;
  renderClaims();
});

document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentFilter = btn.dataset.filter;
    renderClaims();
  });
});

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function renderClaims() {
  const container = document.getElementById('claims-container');
  container.innerHTML = '';

  let visibleCount = 0;
  let recheckedCount = 0;
  let totalTarget = 0;

  for (const [aid, claims] of Object.entries(PACKET.records)) {
    if (currentAppFilter !== 'all' && currentAppFilter !== aid) continue;

    for (const c of claims) {
      const key = `${aid}:${c.claim_id}`;
      const dec = userDecisions[key] || { judgment: '', reason: '' };
      const hasDecision = Boolean(dec.judgment);

      if (c.is_corrected) {
        totalTarget++;
        if (hasDecision) recheckedCount++;
      }

      // Apply Filter
      if (currentFilter === 'corrected' && !c.is_corrected) continue;
      if (currentFilter === 'pending' && (!c.is_corrected || hasDecision)) continue;

      visibleCount++;

      const safeId = `${aid}_${c.claim_id.replace(/[^a-zA-Z0-9]/g, '_')}`;
      const card = document.createElement('div');
      card.className = `claim-card ${c.is_corrected ? 'is-corrected' : 'is-unchanged'}`;
      card.id = `card_${safeId}`;

      let diffHtml = '';
      if (c.is_corrected) {
        diffHtml = `
          <div class="diff-box">
            <div class="diff-col">
              <div class="diff-title">Original Answer (Task 17 Baseline)</div>
              <div><strong>Status:</strong> <code>${escapeHtml(c.original_answer.status)}</code></div>
              <div><strong>Value:</strong> <code>${escapeHtml(JSON.stringify(c.original_answer.value))}</code></div>
              <div style="margin-top: 4px;"><strong>Rationale:</strong> ${escapeHtml(c.original_answer.rationale || '')}</div>
            </div>
            <div class="diff-col corrected">
              <div class="diff-title">Corrected Answer (Task 18 Phase A)</div>
              <div><strong>Status:</strong> <code>${escapeHtml(c.corrected_answer.status)}</code></div>
              <div><strong>Value:</strong> <code>${escapeHtml(JSON.stringify(c.corrected_answer.value))}</code></div>
              <div style="margin-top: 4px;"><strong>Rationale:</strong> ${escapeHtml(c.corrected_answer.rationale || '')}</div>
            </div>
          </div>
          <div style="font-size: 0.85rem; margin-bottom: 12px; padding: 8px 12px; background: #e0f2fe; border-radius: 6px;">
            <strong>What Changed:</strong> ${escapeHtml(c.what_changed)}
          </div>
        `;
      } else {
        diffHtml = `
          <div style="font-size: 0.85rem; margin-bottom: 12px; padding: 8px 12px; background: #f0fdf4; border-radius: 6px;">
            <strong>Baseline Answer:</strong> <code>${escapeHtml(c.corrected_answer.status)}</code> &bull; Value: <code>${escapeHtml(JSON.stringify(c.corrected_answer.value))}</code> &bull; Rationale: ${escapeHtml(c.corrected_answer.rationale)}
          </div>
        `;
      }

      let evidenceHtml = '';
      for (const ev of c.evidence) {
        evidenceHtml += `
          <div class="evidence-item">
            <div>
              <a href="${escapeHtml(ev.source_url)}" target="_blank" class="evidence-link">${escapeHtml(ev.source_url)}</a>
              <span style="font-family: monospace; font-size: 0.75rem; color: #475569; margin-left: 6px;">[${escapeHtml(ev.locator)}]</span>
            </div>
            <div style="font-size: 0.8rem; color: #334155; margin-top: 2px;">
              <strong>Observation:</strong> ${escapeHtml(ev.observation)}
            </div>
            ${ev.snapshot_excerpt ? `<pre class="snapshot-excerpt">${escapeHtml(ev.snapshot_excerpt)}</pre>` : ''}
          </div>
        `;
      }

      card.innerHTML = `
        <div class="claim-header">
          <div>
            <div class="claim-id">${escapeHtml(c.claim_id)}</div>
            <div class="app-tag">App ${aid}: ${escapeHtml(c.app_name)} &bull; ${escapeHtml(c.category)}</div>
          </div>
          <div>
            ${c.is_corrected ? '<span class="badge badge-warn">CORRECTED</span>' : '<span class="badge" style="background:#16a34a;">UNCHANGED BASELINE</span>'}
          </div>
        </div>

        <div class="baseline-banner">
          <strong>Task 17 Baseline Audit:</strong> <code>${escapeHtml(c.baseline_judgment)}</code> &bull; <em>"${escapeHtml(c.baseline_reason)}"</em>
        </div>

        ${diffHtml}

        <div class="evidence-box">
          <div style="font-weight: 700; font-size: 0.8rem; margin-bottom: 6px; color: #475569; text-transform: uppercase;">
            Primary Evidence & Locator Excerpt
          </div>
          ${evidenceHtml}
        </div>

        <div class="recheck-inputs">
          <label><strong>Human Recheck Judgment (Applicant Evaluation) *</strong></label>
          <div class="judgment-radios">
            ${['correct', 'incorrect', 'unsupported', 'unresolved', 'not_applicable'].map(val => `
              <label class="radio-label">
                <input type="radio" class="claim-judgment-radio" name="judgment_${safeId}" value="${val}" ${dec.judgment === val ? 'checked' : ''}>
                ${val}
              </label>
            `).join('')}
          </div>
          
          <div class="form-group" style="margin-bottom: 0;">
            <label>Recheck Reason / Explanation *</label>
            <textarea class="claim-reason-input" rows="2" placeholder="Explain your independent assessment of the corrected claim against primary docs...">${escapeHtml(dec.reason || '')}</textarea>
          </div>
          <div class="status-saved" id="saved_${safeId}">&#10004; Saved to local storage</div>
        </div>
      `;

      // Event listeners for inputs using scoped class selectors within card
      const radios = card.querySelectorAll('.claim-judgment-radio');
      const reasonInput = card.querySelector('.claim-reason-input');

      radios.forEach(radio => {
        radio.addEventListener('change', (e) => {
          saveClaimInput(aid, c.claim_id, e.target.value, reasonInput ? reasonInput.value : '');
        });
      });

      if (reasonInput) {
        reasonInput.addEventListener('input', (e) => {
          const checkedRadio = card.querySelector('.claim-judgment-radio:checked');
          const jVal = checkedRadio ? checkedRadio.value : '';
          saveClaimInput(aid, c.claim_id, jVal, e.target.value);
        });
      }

      container.appendChild(card);
    }
  }

  // Update progress
  document.getElementById('completed-count-badge').textContent = `${recheckedCount} / 50 Rechecked`;
  const pct = Math.round((recheckedCount / 50) * 100);
  document.getElementById('progress-bar').style.width = `${pct}%`;
  document.getElementById('progress-text').textContent = `${recheckedCount} / 50 rechecked`;
  document.getElementById('progress-pct').textContent = `${pct}%`;
}

function saveClaimInput(aid, claimId, judgment, reason) {
  const key = `${aid}:${claimId}`;
  userDecisions[key] = {
    judgment: judgment,
    reason: reason,
    updated_at: new Date().toISOString()
  };
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(userDecisions));
  } catch (e) {
    console.error("Local storage save error", e);
  }

  const safeId = `${aid}_${claimId.replace(/[^a-zA-Z0-9]/g, '_')}`;
  const indicator = document.getElementById(`saved_${safeId}`);
  if (indicator) {
    indicator.style.display = 'block';
    setTimeout(() => { indicator.style.display = 'none'; }, 1500);
  }

  // Update progress bar
  let recheckedCount = 0;
  for (const [aidStr, claims] of Object.entries(PACKET.records)) {
    for (const c of claims) {
      if (c.is_corrected && userDecisions[`${aidStr}:${c.claim_id}`]?.judgment) {
        recheckedCount++;
      }
    }
  }
  document.getElementById('completed-count-badge').textContent = `${recheckedCount} / 50 Rechecked`;
  const pct = Math.round((recheckedCount / 50) * 100);
  document.getElementById('progress-bar').style.width = `${pct}%`;
  document.getElementById('progress-text').textContent = `${recheckedCount} / 50 rechecked`;
  document.getElementById('progress-pct').textContent = `${pct}%`;
}

document.getElementById('save-local-btn').addEventListener('click', () => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(userDecisions));
  alert('All progress saved to browser localStorage.');
});

document.getElementById('export-json-btn').addEventListener('click', () => {
  const reviewerId = document.getElementById('reviewer-id').value.trim();
  const reviewDate = document.getElementById('review-date').value;
  const humanAttestation = document.getElementById('human-attestation').checked;

  if (!reviewerId) {
    alert('Please enter your Reviewer Identifier / Name.');
    return;
  }
  if (!humanAttestation) {
    alert('Actual Human Attestation checkbox is required.');
    return;
  }

  const exportRecords = {};

  for (const [aidStr, claims] of Object.entries(PACKET.records)) {
    const outList = [];
    for (const c of claims) {
      const key = `${aidStr}:${c.claim_id}`;
      const dec = userDecisions[key];

      let judgment = dec ? dec.judgment : '';
      let reason = dec ? dec.reason : '';

      if (!c.is_corrected && !judgment) {
        judgment = c.baseline_judgment;
        reason = c.baseline_reason;
      }

      outList.push({
        claim_id: c.claim_id,
        original_run_id: c.correction_run_id,
        judgment: judgment || 'pending',
        reason: reason || '',
        evidence: c.evidence.map(e => ({
          source_url: e.source_url,
          source_kind: e.source_kind,
          locator: e.locator,
          observation: e.observation,
          captured_on: e.captured_on,
          capture_method: 'http_content',
          content_sha256: e.content_sha256,
          snapshot_ref: e.snapshot_ref,
          hash_unavailable_reason: null,
          document_version: null,
          document_date: null
        }))
      });
    }
    exportRecords[aidStr] = outList;
  }

  const exportPayload = {
    manifest_id: PACKET.manifest_id,
    reviewer: {
      id: reviewerId,
      type: "human",
      human_attestation: humanAttestation,
      reviewed_on: reviewDate
    },
    records: exportRecords
  };

  const blob = new Blob([JSON.stringify(exportPayload, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'human-recheck-judgments.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});

// Initial render
renderClaims();
</script>

</body>
</html>
"""


def generate_html_form(packet: dict) -> str:
    packet_json_str = json.dumps(packet, ensure_ascii=False)
    return HTML_TEMPLATE.replace("%%PACKET_DATA%%", packet_json_str)


def main():
    print("=" * 60)
    print("TASK 18: GENERATING HUMAN RECHECK PACKET & FORM")
    print("=" * 60)

    packet = build_recheck_packet()
    print(f"Total eligible assertions in frozen sample: {packet['total_eligible_assertions']}")
    print(f"Total corrected assertions requiring recheck: {packet['total_corrected_assertions']}")
    print(f"Total unchanged baseline assertions: {packet['total_unchanged_baseline_assertions']}")

    out_dir = ROOT / "outputs/task-18"
    work_dir = ROOT / "work/task-18-agent"
    out_dir.mkdir(parents=True, exist_ok=True)
    work_dir.mkdir(parents=True, exist_ok=True)

    packet_json_path = out_dir / "human_recheck_packet.json"
    packet_json_path.write_text(json.dumps(packet, indent=2, ensure_ascii=False), encoding="utf-8")
    (work_dir / "human_recheck_packet.json").write_text(json.dumps(packet, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] Wrote human_recheck_packet.json to {packet_json_path}")

    worksheet_md = generate_markdown_worksheet(packet)
    worksheet_path = out_dir / "human_recheck_worksheet.md"
    worksheet_path.write_text(worksheet_md, encoding="utf-8")
    (work_dir / "human_recheck_worksheet.md").write_text(worksheet_md, encoding="utf-8")
    print(f"[OK] Wrote human_recheck_worksheet.md to {worksheet_path}")

    html_content = generate_html_form(packet)
    html_path = out_dir / "human_recheck_form.html"
    html_path.write_text(html_content, encoding="utf-8")
    (work_dir / "human_recheck_form.html").write_text(html_content, encoding="utf-8")
    print(f"[OK] Wrote human_recheck_form.html to {html_path}")

    print("All Task 18 artifacts successfully generated!")


if __name__ == "__main__":
    main()
