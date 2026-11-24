# Task 07: Batch 1 Research Report (CRM and Sales, IDs 1–10)

- **Date**: 2026-11-23
- **Category**: CRM and Sales (`data/apps.json` IDs `1–10`)
- **Final Sealed Run ID**: `task07-first-pass-003` (`work/research-runs/task07-first-pass-003`)
- **Records SHA-256**: `e22d6ce79075aa0cef21928ad30f6d61f4c32d024fd98ada2428dff1a70c57b7`
- **Seal SHA-256**: `0fe78d44c22f228294eb6592b7f2790c44d70a6e1417d6aaa94cc49c35069118`
- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`
- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy.

## 1. Run Lineage & Validation Results

| Run ID | Parent | Role | Status | Notes |
| --- | --- | --- | --- | --- |
| `task07-capture-001` | `null` | Initial capture (sandboxed) | Sealed (`0` captures) | Preserves initial sandbox DNS failures per immutable-run rules. |
| `task07-capture-002` | `task07-capture-001` | Network capture recovery (v1) | Sealed (`32` captures) | Approved-network HTTP capture of initial 39 public URLs. |
| `task07-capture-003` | `task07-capture-002` | Expanded capture (v2) | Sealed (`53` captures) | Added Trailhead/forcedotcom, HubSpot OAuth, Pipedrive `.md`, Attio/Close/Twenty `llms.txt`, Zoho v8, Copper auth, DealCloud MCP. |
| `task07-capture-004` | `task07-capture-003` | Final capture (v3) | Sealed (`58` captures) | Added exact Attio OAuth/MCP `.md` and Close OAuth/MCP `.md` pages discovered from `llms.txt`. |
| `task07-first-pass-001` | `task07-capture-004` | Initial ingest attempt | Rejected (preserved) | Rejected by validator (`MCP scope must explicitly identify callable server direction`); preserved untouched. |
| `task07-first-pass-002` | `task07-capture-004` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent AI reviewer; superseded by `task07-first-pass-003` to tighten claim-level citations/locators and null Zoho `server_url`. |
| `task07-first-pass-003` | `task07-capture-004` | **Final Task 07 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`Python jsonschema Draft202012Validator`, `10` records, `synthetic: false`). |

## 2. Source-Capture and Claim-Coverage Counts

- **Selected Apps**: `10 / 100` (IDs `1–10`, all 10 present with asserted non-identity research)
- **Captured Snapshots**: `58` live public snapshots (`0` synthetic fixtures); `19` distinct URLs failed in network runs (preserved in `fetches`, never promoted into claims)
- **Eligible Research Assertions (Frozen Inventory)**: `164` total (`142` observed documentary, `22` inferred; excludes 10 identity claims)
- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `164` pending, `accuracy: null`

| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `identity` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `purpose` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `auth` | 21 | 0 | 0 | 0 | 0 | 10/10 |
| `credentials` | 43 | 2 | 135 | 0 | 0 | 10/10 |
| `api` | 52 | 10 | 0 | 0 | 0 | 10/10 |
| `mcp` | 16 | 0 | 0 | 8 | 2 | 8/10 |
| `buildability` | 0 | 10 | 0 | 0 | 0 | 10/10 |

## 3. Pilot Continuity & Integrity Verification

- **HubSpot (ID 2) Pilot Provenance**: HubSpot was previously researched in `work/task-04-runs/pilot-first-pass-001` and verified `22/22` in `task05-review-002` with a Task 05 caveat that `2.production.*` relied on sunset legacy private apps (new creation ended 2026-10-26). In Task 07, all 5 HubSpot pilot URLs were freshly captured on `2026-11-23` alongside `working-with-oauth`, so `2.production.admin_approval_required` now cites current OAuth installation requirements (Super Admin or HubSpot Marketplace Access) in addition to legacy private apps, while `2.production.free_access` / `paid_required` remain explicitly scoped to existing legacy private apps. Original Task 04/05 sealed runs remain byte-for-byte unchanged.
- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps (including sampled IDs `4 Attio` and `8 Close`) were researched to the same documentary standard.
- **Baseline Hash Verification**: `pilot-first-pass-001` (`records.json` & `seal.json`), `task05-review-002` (`seal.json`), `outputs/task-06/sampling-manifest.json`, and `data/apps.json` all verified byte-for-byte unchanged.

## 4. Reproduction Instructions

Offline validation and metrics replay (no network or API keys required):

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task07-first-pass-003
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task07-first-pass-003 --target task07-first-pass-003
```

Rebuild extraction JSON from sealed capture `task07-capture-004`:

```powershell
.venv\Scripts\python.exe -B work/task-07-agent/build_extraction.py
```
