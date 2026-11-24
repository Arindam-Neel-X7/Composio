# Task 06: Pipeline Repairs, Contract v1.1 & Frozen Evaluation Method

- **Date**: 2026-11-23
- **Pipeline version**: `0.2.0` (upgraded from `0.1.0`)
- **Contract version**: `1.1` (`schemas/record.json`, `docs/evidence-rules.md`, `examples/unresearched-record.json`)
- **Preserved baseline runs**: `pilot-first-pass-001` (`records.json` SHA-256 `10ff5bdb556920e5fd0c692e6a3694c219ee98011c6244d9cf796203505d8f90`, `seal.json` SHA-256 `eaebd62d4f63c52465b15d5d94aa708db3a2140f25b120ca28b704ac38e03ca2`) and `task05-review-002` (`seal.json` SHA-256 `9713538d659d4d56d5a980d96eb58cf78669715fb8dcd5343203f02776d5a94f`) remain completely unchanged and validate against their own frozen v1.0 contract snapshots.
- **No manufactured accuracy improvement**: No pilot claims were silently edited or re-scored; Task 05's first-pass pilot AI score remains 87/92 (94.57%).

---

## 1. Pipeline & Contract Repairs Implemented

| Pilot Finding (Task 05) | Root Cause | Task 06 Repair | Files Changed |
| --- | --- | --- | --- |
| Google Ads `31.production.partner_approval_required` (`unsupported`) | Schema lacked a field for vendor/platform API-access review distinct from commercial partnership gating. | Versioned contract to **v1.1**: added `vendor_approval_required` boolean claim to `credential_eligibility.{testing,production}` and defined `vendor_approval_required` vs `partner_approval_required` vs `admin_approval_required`. | `schemas/record.json`, `docs/evidence-rules.md`, `examples/unresearched-record.json`, `research_pipeline.py` |
| Freshdesk `developers.freshdesk.com/api/` failed with opaque `Capture failed: ValueError` | Collector swallowed guard reasons into `ValueError` and hard-coded a 2 MB cap. | Added `CaptureError` with sanitized diagnostic codes (`size_limit_exceeded`, `unsupported_content_type`, `empty_readable_content`, `time_budget_exceeded`, `non_success_status`) and configurable `--max-bytes` (100 KB–10 MB, default 2 MB, logged in `manifest.config.max_bytes`). | `research_pipeline.py`, `docs/pipeline-usage.md` |
| Sherlock `sherlockproject.xyz/usage` lines 76–77 leaked Mintlify JSON/MDX hydration payload | HTML parser only skipped `script`/`style`/`noscript`. | Added `template` to `SKIP_TAGS` and stripped large (>500 char) HTML-embedded framework hydration JSON lines (`compiledSource`, `mdxSource`, `__NEXT_DATA__`, `docsConfig`, `pageProps`) while preserving `application/json` responses untouched. | `research_pipeline.py` |
| NotebookLM `91.mcp` edition conflation & `91.purpose` / `91.mcp.personal_community` citation gaps | Rules did not explicitly block cross-edition community MCP from setting Enterprise `mcp.discovery="found"`. | Clarified edition-matching rule for `mcp.discovery` and reinforced per-claim locator/attachment discipline in `docs/evidence-rules.md` v1.1. | `docs/evidence-rules.md` |
| Missing reproducible 20-app sampling CLI | No sampling command existed in v0.1.0. | Added `research_pipeline.py sample` implementing `stratified-sha256-v1` (deterministic, language-independent SHA-256 ranking per category, exclusive write via `write_new`). | `research_pipeline.py`, `docs/pipeline-usage.md` |

**Traceability note on remaining Task 05 proposals**: Task 05 Proposed Fix #4 (scope-specific context granularity) is already supported by supplying distinct source specs per scope on the same URL (verified by `test_17_same_page_multiple_scopes`). Task 05 Proposed Fix #6 (pilot child correction run) was intentionally deferred rather than creating a corrected pilot run here, to avoid manufacturing accuracy improvement and because the 5 pilot apps will be researched under contract v1.1 within their respective full-run batches.

---

## 2. Regression Test & Backward-Compatibility Results

- **Unit tests**: `python -B -m unittest discover -s tests -p test_research_pipeline.py -v` → **23 / 23 tests passed** (`OK` in 7.25s), including 4 new Task 06 tests:
  - `test_20_vendor_vs_partner_approval_v1_1`
  - `test_21_collector_guard_codes_and_max_bytes`
  - `test_22_html_hydration_json_stripping`
  - `test_23_reproducible_stratified_sampling`
- **Sealed run backward compatibility**:
  - `validate --run-id pilot-first-pass-001` → `passed` (`Python jsonschema Draft202012Validator`)
  - `validate --run-id task05-review-002` → `passed` (`Python jsonschema Draft202012Validator`)
  - `metrics --run-id task05-review-002 --target pilot-first-pass-001` → unchanged (`87/92 = 94.57%`, `observed 62/66`, `inferred 25/26`)

---

## 3. Frozen 20-App Stratified Sample & Rubric

- **Manifest**: `outputs/task-06/sampling-manifest.json` (`manifest_id: composio-20app-sample-v1`, frozen)
- **Rubric**: `outputs/task-06/evaluation-rubric.md`
- **Algorithm**: `stratified-sha256-v1` (`sha256("{seed}:{category}:{app_id}")` ascending, 2 apps per category without replacement across all 10 categories)
- **Seed**: `composio-eval-2026-11-23-v1`
- **Roster SHA-256**: `6e3aada149102c2e5539c126aa556c1ceaca3d9d25ca6e0a8f56b3a569f81c19`
- **Selected 20 apps**:
  - **AI, Research and Media-native**: 98 Mermaid CLI, 97 higgsfield
  - **CRM and Sales**: 4 Attio, 8 Close
  - **Communications and Messaging**: 27 Telegram, 21 Slack
  - **Data, SEO and Scraping**: 60 Clay, 52 SE Ranking
  - **Developer, Infra and Data platforms**: 65 Supabase, 64 Cloudflare
  - **Ecommerce**: 46 Squarespace, 50 fanbasis
  - **Finance and Fintech**: 84 Paygent Connect, 83 Binance
  - **Marketing, Ads, Email and Social**: 40 SendGrid, 31 Google Ads *(pilot overlap disclosed)*
  - **Productivity and Project Management**: 77 ClickUp, 76 Monday.com
  - **Support and Helpdesk**: 19 Gorgias, 16 LiveAgent
- **Pilot overlap disclosure**: App `31` (Google Ads) overlaps with the 5-app pilot; the seed was not re-rolled, and Task 04/05 pilot reviews remain preserved separately.

---

## 4. Next Step

Task 06 is complete. **Task 07 (Research batch 1: CRM and Sales, IDs 1–10)** is next and has not started.
