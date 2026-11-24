# Task 12: Batch 6 Research Report (Data, SEO and Scraping, IDs 51–60)

- **Date**: 2026-11-23
- **Category**: Data, SEO and Scraping (`data/apps.json` IDs `51–60`)
- **Final Sealed Run ID**: `task12-first-pass-005` (`work/research-runs/task12-first-pass-005`)
- **Records SHA-256**: `5479079465cbf07d14ad0bee2421378644f8013ae04634f3e0cc7c42f7984815`
- **Seal SHA-256**: `c817cccdd03046f9ef91276a288fbe15a4ada8809ed28b75bff4da54b21c2ad3`
- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`
- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy.

## 1. Run Lineage & Validation Results

| Run ID | Parent | Role | Status | Notes |
| --- | --- | --- | --- | --- |
| `task12-capture-001` | `null` | Initial live capture | Sealed (`126` captures) | Approved-network HTTP capture across IDs 51–60 (including 72,341-line Ahrefs OpenAPI 3.2.0 JSON spec). |
| `task12-capture-002` | `task12-capture-001` | Expanded capture (v2) | Sealed (`141` captures) | Added 15 official `developers.clay.com` Markdown pages (`index.md`, `quickstart.md`, `public-api/authentication.md`, `tables.md`, `searches.md`, `routines/api.md`, `llms.txt`, etc.). |
| `task12-capture-003` | `task12-capture-002` | Final capture (v3) | Sealed (`146` captures) | Added official `seranking/openapi` and `seranking/seo-skills` READMEs, `developers.clay.com/routines/custom-functions.md`, and `clay-run/agent-plugins`. |
| `task12-first-pass-001` | `task12-capture-003` | Initial ingest attempt | Rejected (preserved) | Rejected by MCP URL presence check (`MCP URL not present in cited content` for 3 `repository_url` strings on hosted MCP entries); preserved untouched. |
| `task12-first-pass-002` | `task12-capture-003` | Second ingest attempt | Rejected (preserved) | Rejected by MCP callable-direction wording check on `60.mcp.official_clay_mcp` (`connector` without `server`); preserved untouched. |
| `task12-first-pass-003` | `task12-capture-003` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent read-only AI reviewers (`NEEDS FIXES`); preserved untouched. |
| `task12-first-pass-004` | `task12-first-pass-003` | Second sealed pass (superseded) | Sealed (preserved) | Remediated 15 internal audit locator/attachment items; preserved untouched. |
| `task12-first-pass-005` | `task12-first-pass-004` | **Final Task 12 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`Python jsonschema Draft202012Validator`, `10` records, `synthetic: false`, `681` verified evidence refs, all 15 internal audit findings and all 18 Codex review checkpoint items in `outputs/task-12-review.md` remediated). |

## 2. Source-Capture and Claim-Coverage Counts

- **Selected Apps**: `10 / 100` (IDs `51–60`, all 10 present with asserted non-identity research)
- **Captured Snapshots**: `146` live public snapshots (`0` synthetic fixtures; 1 PyPI client-challenge page excluded from citations); `0` uncaptured fetch declarations in the final run
- **Eligible Research Assertions (Frozen Inventory)**: `207` total (`187` observed documentary, `20` inferred; excludes 10 identity claims)
- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `207` pending, `accuracy: null`

| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `identity` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `purpose` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `auth` | 21 | 0 | 0 | 0 | 0 | 10/10 |
| `credentials` | 68 | 0 | 112 | 0 | 0 | 10/10 |
| `api` | 68 | 10 | 0 | 0 | 0 | 10/10 |
| `mcp` | 20 | 0 | 0 | 12 | 2 | 8/10 |
| `buildability` | 0 | 10 | 0 | 0 | 0 | 10/10 |

## 3. Pilot Overlap (Sherlock ID 58), Sample Integrity & Baseline Verification

- **Pilot Overlap (App 58 — Sherlock)**:
  - Inspected `work/task-04-runs/pilot-first-pass-001`, `work/task-04-runs/task05-review-002`, and `outputs/task-05/verification-report.md` before researching Sherlock.
  - In Task 05, Sherlock scored `13/13` (`100.0%`), with two notes: (a) `58.mcp` (`not_found_in_checked_sources`) was verified accurate for official sources, and (b) `sherlockproject.xyz/usage` lines 76–77 had leaked Mintlify JSON/MDX hydration payload in v0.1.0, which Task 06 fixed in `research_pipeline.py` v0.2.0 (`test_22_html_hydration_json_stripping`).
  - In `task12-capture-003` and `task12-first-pass-005`, `sherlockproject.xyz/usage` (75 clean lines), `sherlockproject.xyz/installation` (92 clean lines), `github.com/sherlock-project/sherlock`, `pyproject.toml` (v0.16.2), and `LICENSE` (MIT) were freshly captured under pipeline v0.2.0 and contract v1.1 (including `vendor_approval_required=false`), while preserving `pilot-first-pass-001` and `task05-review-002` byte-for-byte untouched.
- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in Data, SEO and Scraping were researched to the same documentary standard without preferential treatment for sample apps (`52` SE Ranking, `60` Clay).
- **Baseline Hash Verification**: `pilot-first-pass-001/records.json`, `pilot-first-pass-001/seal.json`, `task05-review-002/seal.json`, `outputs/task-06/sampling-manifest.json`, and `data/apps.json` all verified byte-for-byte unchanged.

## 4. Reproduction Instructions

Offline validation and metrics replay (no network or API keys required):

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task12-first-pass-005
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task12-first-pass-005 --target task12-first-pass-005
```

Rebuild extraction JSON from sealed capture `task12-capture-003`:

```powershell
.venv\Scripts\python.exe -B work/task-12-agent/build_extraction.py
.venv\Scripts\python.exe -B work/task-12-agent/generate_deliverables.py
```
