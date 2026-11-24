# Task 21: Reproduction Testing & Page Presentation QA Report

**Date**: 2026-11-24  
**Status**: COMPLETED (PASS with explicit live-Chrome DevTools environment limitation noted)  
**Scope**: Fresh offline replay verification, SHA-256 seal integrity audit, live-research prerequisites verification, page-to-output data agreement audit, link/asset validation, JavaScript runtime testing, and desktop/mobile responsive CSS QA.

---

## 1. Executive QA Summary

| QA Pillar | Result | Evidence / Key Metrics |
| --- | --- | --- |
| **Offline Pipeline Test Suite** | **PASS** | `23/23` tests passing (`unittest discover -s tests -v`, 6.86s) |
| **Fresh Zero-Network Offline Replay** | **PASS** | `task21-offline-replay-001` (from `task07-first-pass-003`) and `task21-offline-replay-t18-001` (from `task18-corrections-07`) created and validated via Draft 2020-12 JSON Schema |
| **SHA-256 Seal Integrity** | **PASS** | `42/42` sealed runs verified (10 first-pass + 10 Task 17 reviews + 10 Task 18 corrections + 10 Task 18 rechecks + 2 Task 21 replays); `0` missing files, `0` hash mismatches |
| **Page-to-Output Data Agreement** | **PASS** (after 3 QA fixes) | `100/100` embedded apps, `44/50/4/2` queues, `66/15/4/11/4` MCP counts, `N=327` (`84.71% → 100.00%`) human metrics, and dynamically generated Build Roadmap match authoritative JSON outputs |
| **Links, Anchors & Zero-External-Asset Check** | **PASS** | `0` external `<script>/<link>/<img>` assets; `0` broken internal anchors (`9` refs / `8` unique); `0` duplicate IDs; `770` unique embedded evidence/MCP URLs (`0` invalid syntax) |
| **JavaScript Syntax & Functional Runtime** | **PASS** | `node --check` passed; Node.js v26.7.0 DOM-shim harness verified all filters, search, sorting, XSS escaping, and `openDrawer(id)` across `100/100` apps (`0` runtime errors) |
| **Desktop / Mobile Responsive QA** | **PASS (Static + Runtime) / BLOCKED (Live Chrome DevTools)** | Responsive CSS, breakpoints, mobile `.hide-sm`, `.table-wrap` scroll, narrow-viewport grid guard (`min(340px, 100%)`), drawer `min(680px, 100vw)`, dark mode, and ARIA verified. Live Chrome DevTools connection unavailable (`DevToolsActivePort` `ENOENT`). |

---

## 2. Offline Replay & Seal Verification

### A. Pipeline Unit Test Suite
Executed offline in `.venv`:
```powershell
.venv\Scripts\python.exe -B -m unittest discover -s tests -v
```
Result: **23/23 tests OK** (covering capture/extract/packet, external adapter CLI, evidence-free assertion rejection, roster/identity gate, dependency cycles, SHA-256/locator/quote anchoring, credential environment scoping, MCP guards, immutable parent-child replay, failure receipts, tamper detection, v1.1 vendor vs. partner approval, hydration-blob stripping, and deterministic stratified sampling).

### B. Fresh Offline Replays (Zero Network Calls)
1. **First-Pass Batch Replay**:
   - Command: `.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs collect --run-id task21-offline-replay-001 --parent task07-first-pass-003 --replay`
   - Validation: `validate --run-id task21-offline-replay-001` → `structure_and_grounding: passed`, `backend: Python jsonschema Draft202012Validator`, `records: 10`, `synthetic: false`.
2. **Task 18 Correction Child Replay**:
   - Command: `.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs collect --run-id task21-offline-replay-t18-001 --parent task18-corrections-07 --replay`
   - Validation: `validate --run-id task21-offline-replay-t18-001` → `structure_and_grounding: passed`, `records: 10`, `synthetic: false`.
3. **Paired Metrics Replay**:
   - Command: `.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task18-human-recheck-07 --target task18-corrections-07`
   - Result: `34/34` sampled batch-7 claims `correct` (`accuracy: 1.0`, `0` incorrect, `0` unsupported, `0` unresolved), preserving frozen inventory and sample-reuse notice.

### C. Full 42-Run Seal Audit
Executed via `work/task-21-agent/qa_audit.py` (results saved in `work/task-21-agent/qa_audit_results.json`):
- **42/42 runs passed** every SHA-256 digest check in `seal.json`.
- Original sealed runs, snapshots, inventories, and manifests remain completely untouched.

---

## 3. Page-to-Output Agreement Audit & QA Remediations

The automated agreement audit (`work/task-21-agent/qa_audit.py`) compared `outputs/task-20/index.html` and root `index.html` against:
- `data/apps.json` (100 authoritative identities)
- `outputs/task-17/human-baseline-metrics.json`
- `outputs/task-18/paired-comparison-metrics.json`
- `outputs/task-19/aggregates.json`
- `outputs/task-19/build-queues.json`

### Defects Identified & Remediated During Task 21
1. **Section 5 (Build Roadmap) Hardcoded App IDs & Wave Counts (FIXED)**:
   - *Finding*: The initial Task 20 HTML had hardcoded Phase 1–4 prose containing 30 mismatched app-ID/name citations (e.g., citing `Supabase (64)` instead of `Cloudflare (64)` / `Supabase (65)`, and non-roster names like `Resend`, `Tavily`, `Perplexity`) and stale wave counts (`32 / 12 / 27 / 17` instead of exact `build-queues.json` counts).
   - *Fix*: Refactored `work/task-20-agent/generate_case_study.py` to add `render_roadmap_cards(build_queues)`, dynamically rendering all 6 roadmap phases directly from `outputs/task-19/build-queues.json`:
     - Phase 1 (Wave 1A Official MCP): **34 apps**
     - Phase 2 (Waves 1B, 1C & 1D): **10 apps** (7 Community MCP + 2 Local CLI + 1 Self-Serve REST)
     - Phase 3 (Conditional — Admin & Cloud): **27 apps** (13 Admin Consent + 14 Cloud/Quota)
     - Phase 4 (Conditional — Review, Paid & Partner): **23 apps** (11 Vendor Review + 6 Paid Plan + 6 Partner Program)
     - Phase 5 (Outreach Required): **4 apps**
     - Phase 6 (Unknown Backlog): **2 apps**
     - Total: **34 + 10 + 27 + 23 + 4 + 2 = 100/100 apps** with 100% roster-verified names and IDs.
2. **Hero Two-Minute Overview Official MCP Count (FIXED)**:
   - *Finding*: Overview card 1 stated `32 already ship official MCP servers` (counting only `official_only` and omitting the `2` `official_and_community` apps in `build_now`).
   - *Fix*: Updated to `34 already ship official MCP servers` to match Wave 1A (`34` apps) in `outputs/task-19/build-queues.json`.
3. **Narrow-Mobile CSS Grid Overflow Guard (FIXED)**:
   - *Finding*: `.grid-2` used `minmax(320px, 1fr)` and `.case-grid` used `minmax(340px, 1fr)`, which would overflow horizontally on `<380px` mobile screens after container padding.
   - *Fix*: Updated both to `minmax(min(320px, 100%), 1fr)` and `minmax(min(340px, 100%), 1fr)`.

After regeneration, `outputs/task-20/index.html` and root `index.html` are byte-for-byte identical (`737,590` bytes) and pass `verify_case_study.py`, `qa_audit.py`, and `qa_js_and_css.py` with **0 data agreement errors** and **0 prose app-ID mismatches**.

---

## 4. Interactive Runtime, Link & Presentation QA

### A. JavaScript Syntax & Functional Execution (`work/task-21-agent/qa_js_and_css.py`)
- `node --check` (Node.js v26.7.0): **PASS** (0 syntax errors).
- Functional DOM-shim execution across the embedded `APPS` array:
  - `totalApps`: `100`, `categoriesPopulated`: `10`
  - Search filter: `"HubSpot"` → `1`, `"Paygent"` → `1`
  - Queue pills: `build_now: 44`, `conditional: 50`, `outreach_required: 4`, `unknown: 2`
  - Sample-only toggle: `20`
  - Auth filter: `OAuth2: 79`, `API_key: 39`, `Bearer_token: 35`, `Basic: 15`, `none: 5`, `other: 8`, `JWT: 2`, `session_cookie: 1`
  - MCP filter: `official_only: 66`, `community_only: 15`, `official_and_community: 4`, `not_found_bounded: 11`, `unknown: 4`
  - Sorting (`name` ascending): `"Ahrefs"` → `"Zoho CRM"`
  - Slide-over inspector (`openDrawer(id)`): **100/100 apps rendered cleanly with 0 exceptions**
  - XSS escaping (`esc()`): **PASS**

### B. Links, Anchors & Offline Self-Containment
- External asset references (`<script src>`, `<link href>`, `<img src>`): **0** (100% offline-capable).
- Internal navigation anchors (`href="#..."`): **9 links / 8 unique targets, 0 broken**.
- Duplicate HTML `id` attributes: **0**.
- Embedded citation & MCP URLs: **770 unique `http`/`https` URLs, 0 malformed URLs**. (Note: Live HTTP reachability of all 770 third-party vendor URLs was intentionally not re-probed during offline QA; original capture receipts and hashes are sealed in `work/research-runs/`.)

### C. Desktop & Mobile Presentation Checks + Explicit Environment Blocker
- **Verified in CSS/HTML**: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`, sticky responsive `.topnav`, `@media (max-width: 768px)` mobile rules, `.hide-sm` secondary column collapsing, `.table-wrap` horizontal scroll container, `.drawer` `width: min(680px, 100vw)`, dark-mode CSS custom properties (`[data-theme="dark"]`), `role="dialog" aria-modal="true"`, and 7 `aria-label` attributes.
- **Explicit Environment Blocker (Live Chrome Visual Inspection)**: Attempting live desktop (`1440x900`) and mobile (`390x844`) rendering via Chrome DevTools failed because Chrome remote debugging was not active on the host (`Could not find DevToolsActivePort for chrome at C:\Users\User\AppData\Local\Google\Chrome\User Data\DevToolsActivePort (ENOENT)`), and neither `playwright` nor `selenium` is installed in `.venv`. No fabricated screenshot or live-pixel claims are made; when the user opens `index.html` in a browser or enables Chrome remote debugging, live visual verification can be run directly.

---

## 5. Live-Research Prerequisites (Verified Against `docs/pipeline-usage.md`)

To perform **new live captures** (beyond offline replay of sealed runs), a researcher or operator requires:
1. **Runtime**: Python 3.10+ with `.venv` containing `jsonschema` (Draft 2020-12) or PowerShell 7 (`Test-Json`). No other external Python packages are required.
2. **Network Access**: Outbound HTTPS access to public, credential-free vendor documentation URLs (userinfo and credential-like query parameters are rejected by `research_pipeline.py`).
3. **Explicit Source Manifest**: A JSON file (`{"sources": [...]}`) specifying `app_id`, `url`, `kind` (`primary_docs`, `official_repository`, `official_product_page`, `community_repository`, `community_docs`), `scope`, `environments`, `attribution_basis`, and `attribution_by`. Roster hints are never auto-promoted.
4. **Collector Bounds**: Configure `--timeout` (default 10s), `--retries` (default 1, max 3), and `--max-bytes` (default 2 MB, allowed 100 KB–10 MB). Static HTTP capture cannot execute JS-only SPAs or bypass HTTP 403 bot walls (e.g., App 90 PitchBook).
5. **Extraction & Review**: No model backend is embedded. Provide researcher-authored records via `ingest` or an explicit trusted adapter via `extract --extractor-command-json`. Independent review requires a distinct `--reviewer-id`; `--reviewer-type human --actual-human-attestation` may only be used when an identified human personally verifies primary sources.

---

## 6. Task 21 Artifacts Created
- `outputs/task-21/qa-report.md` (this report)
- `work/task-21-agent/qa_audit.py` & `work/task-21-agent/qa_audit_results.json`
- `work/task-21-agent/qa_js_and_css.py` & `work/task-21-agent/qa_js_css_results.json`
- `work/research-runs/task21-offline-replay-001/` (sealed offline replay of `task07-first-pass-003`)
- `work/research-runs/task21-offline-replay-t18-001/` (sealed offline replay of `task18-corrections-07`)
- Updated `work/task-20-agent/generate_case_study.py`, `outputs/task-20/index.html`, and root `index.html` (QA remediations applied and re-verified)
