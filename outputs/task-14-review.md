# Task 14: Independent AI Review Report (Productivity and Project Management, IDs 71–80)

- **Final Verdict**: **PASS** *(initial independent audit of `task14-first-pass-002` returned `NEEDS FIXES` for 36 per-claim attachment, locator-range, omitted Monday.com OAuth 2.0, and v1.1 line-59 credential-scoping defects across Apps 71–80; all 36 remediated in immutable child run `task14-first-pass-003` and independently re-verified on disk → `PASS`)*
- **Reviewed on**: 2026-11-24
- **Auditors** *(context-isolated, read-only AI research subagents; shared model family disclosed; **AI review only, not human review**)*:
  - Initial audit (IDs 71–75): `b8bacf67-4ab7-4f72-a4ab-9f429907cde7`
  - Initial audit (IDs 76–80 & deliverables): `61e1dc32-7cb8-42be-ae8b-c317f0d5c875`
  - Re-review audit (`task14-first-pass-003`): `92f097aa-69f7-4ae3-837c-821db8b52b46`
- **Accepted Run**: `work/research-runs/task14-first-pass-003` (`records.json` SHA-256 `661013f357d38ff4e725705ff269441daabab68bc33bd9ebbac68d5544d39d17`, `seal.json` SHA-256 `416e8f822365e0cbac3f86fbc524e27f0e2b1f6249b4c17fb0177a70cbf64dc9`)
- **Superseded Run Preserved Untouched**: `work/research-runs/task14-first-pass-002` (`records.json` SHA-256 `5cf1177abceef0aa711d583dbb6cc03d5ddbaad028290e480358299d920eb184`, `seal.json` SHA-256 `86f83326e26090feb7fc03212b68ba00bde2287b978eccafbb1a353a5582ce58`)
- **Formal Blind Scoring**: Deferred to Task 17 (20-app stratified sample, which includes App `76` Monday.com and App `77` ClickUp); `task14-first-pass-003` keeps `review.status == "pending"` and `accuracy: null` (`138` eligible assertions: `117` observed, `21` inferred; `328` verified evidence observations).

---

## 1. Core Verification Checks (All PASS)

| Area | Status | Verified Evidence |
| --- | --- | --- |
| Baseline & prior-run immutability | **PASS** | `pilot-first-pass-001` (`records.json` `10ff5bdb...`, `seal.json` `eaebd62d...`), `task05-review-002` (`seal.json` `9713538d...`), `outputs/task-06/sampling-manifest.json` (`7f8a6111...`), `data/apps.json` (`6e3aada1...`), and superseded `task14-first-pass-002` (`records.json` `5cf1177a...`, `seal.json` `86f83326...`) all verified byte-for-byte unchanged. |
| Schema & grounding validation | **PASS** | `research_pipeline.py validate --run-id task14-first-pass-003` passed (`Python jsonschema Draft202012Validator`, contract `v1.1`, `10/10` records matching `data/apps.json` IDs 71–80, `synthetic: false`). |
| Evidence-link & claim grounding | **PASS** | Direct line-by-line re-verification of all `36/36` initial findings against `task14-first-pass-003/snapshots/*.txt` confirmed **36/36 RESOLVED** with **0 regressions**. All `328/328` evidence refs resolve with 0 SHA-256 or locator errors; `0` claims cite the 2 excluded Airtable 1-line SPA shells; all `10/10` nested MCP `operational_check` claims remain `not_researched`; Harvest's community MCP (`southleft/harvest-mcp`) is restricted to MCP claims. |
| Deliverables consistency | **PASS** | `outputs/task-14/{records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json}` match `task14-first-pass-003` hashes (`661013f3...`, seal `416e8f82...`), counts (`52` captures, `138` eligible, `328` evidence refs, `accuracy: null`), and 5 minor stale prose lines in `exceptions-for-reviewer.md` flagged during re-review were synchronized without touching the sealed run. |

---

## 2. Remediations Verified on Re-Review (36/36 RESOLVED, 0 Regressions)

1. **Per-claim attachment & locator-range precision (`docs/evidence-rules.md` v1.1 lines 8, 45)**:
   - **App 71 (Notion)**: Attached `get-started-with-mcp` `lines:83-99` to `71.identity`; attached `reference/intro` `lines:80-83` (`Authorization: Bearer`) and `authorization` `lines:120-122` (`team-owned`) to `71.auth.internal`; attached `create-a-notion-integration` `lines:72-82` and `71.mcp.server` ref to `71.buildability`.
   - **App 72 (Airtable)**: Attached Web API and MCP evidence to `72.identity`; attached API-key deprecation (`lines:58-64`) to `72.auth.pat`; aligned `72.api.protocol.rest` observation/rationale; removed fetch telemetry from `72.api.public_docs` and SPA-shell blocker from `72.buildability` (added `72.mcp.server`, `72.testing.free_access` refs).
   - **App 73 (Linear)**: Attached MCP evidence to `73.identity` and GraphQL mutation `lines:124-126` to `73.purpose`; aligned `lines:87-101` observation; trimmed out-of-range wording in `73.api.public_docs`; added `73.mcp.server` ref to `73.buildability`.
   - **App 74 (Jira)**: Attached remote MCP `lines:1-18` to `74.purpose`; attached `basic-auth-for-rest-apis` `lines:82-91` (`distributable 3LO app`) to `74.auth.oauth`; added `74.mcp.server` ref to `74.buildability`.
   - **App 75 (Asana)**: Attached MCP `lines:89-93` to `75.identity`; fixed off-by-one locator on `75.auth.oauth` (`lines:128-146` covering `tasks:delete` on L146); attached `overview` `lines:108-110`, removed redundant `EV[2]`, and added `75.mcp.server`, `75.testing.free_access`, `75.testing.sandbox_access` refs to `75.buildability`.
   - **App 76 (Monday.com — Frozen Sample Member)**: Attached MCP evidence to `76.identity` and workspace/integration evidence to `76.purpose`; **added `76.auth.oauth`** (`method: OAuth2`, Platform API OAuth 2.0 authorization-code flow & scopes `boards:read/write`, `docs:read/write`, `workspaces:read/write`) anchored verbatim to `developer.monday.com/apps/docs/oauth` `lines:175-218`.
   - **App 77 (ClickUp — Frozen Sample Member)**: Attached `reference/gettasks` `lines:8-12` (`ClickUp API v2 Reference`) to `77.identity`; expanded `What-is-ClickUp-MCP` locators to `lines:39-58` (covering `rolling` L39/L57-58 and `per-minute` L43-46); added `77.mcp.server` ref to `77.buildability`.
   - **App 78 (Coda)**: Attached `Connect-to-the-Coda-MCP?output=1` `lines:27-42` (OAuth 2 supported-clients table) to `78.mcp.server` and `78.mcp.discovery`.
   - **App 79 (Smartsheet)**: Attached `introduction` `lines:76-81` (`/2.0` and regional base URLs) and `authentication` `lines:99-100` (separate regional tokens) to `79.identity`.
   - **App 80 (Harvest)**: Expanded `80.identity` locator to `lines:11-20` (covering `api.harvestapp.com` on L20); attached OAuth2 app registration (`lines:33-41`) alongside PAT creation (`lines:17-24`) to `80.{testing,production}.self_serve`; removed non-verbatim `"legacy"` wording from `80.auth.oauth_implicit`.
2. **Credential-eligibility path scoping (`docs/evidence-rules.md` v1.1 lines 55–59)**:
   - All path-conflicting app-wide booleans (`admin_approval_required`, `vendor_approval_required`, `paid_required` where free/paid or tenant/sandbox paths diverge, and `self_serve` where PAT vs. admin/vendor-gated paths diverge) were moved to `unknown` (`value: null`) with full captured evidence and explicit path-by-path rationales preserved.
   - Retained `13` strictly valid `observed` credential booleans: availability booleans (`free_access`, `trial_access`, `sandbox_access`) where documented paths exist (`72`, `75`, `76`, `78`, `79`), uniform `79.production.paid_required=true` (both REST 2.0 and hosted MCP require Business/Enterprise/AWM), and uniform `80.{testing,production}.self_serve=true` (both PAT and OAuth2 app creation are self-serve in Harvest ID Developers).

---

## 3. Disposition

- **Task 14 status**: Accepted (**PASS**) after remediation in `work/research-runs/task14-first-pass-003` (AI review only; no human review; formal blind scoring of frozen sample apps `76` and `77` deferred to Task 17; `HANDOFF.md` and `outputs/execution-plan.json` remain owned by the coordinator and were not modified).
