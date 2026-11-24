# Task 13: Batch 7 Research Report (Developer, Infra and Data platforms, IDs 61–70)

- **Date**: 2026-11-23 / 2026-11-24
- **Category**: Developer, Infra and Data platforms (`data/apps.json` IDs `61–70`)
- **Final Sealed Run ID**: `task13-first-pass-003` (`work/research-runs/task13-first-pass-003`)
- **Records SHA-256**: `2289c227f083cd20f9a130035e412b538cfda981578f72901b7cb6da3f9c95cf`
- **Seal SHA-256**: `896c8460c8ed34c43ea64d0315c1df86df01744382b7cf38a2ce6d984bfda8a1`
- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`
- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy.

## 1. Run Lineage & Validation Results

| Run ID | Parent | Role | Status | Notes |
| --- | --- | --- | --- | --- |
| `task13-capture-001` | `null` | Initial live capture | Sealed (`41` captures) | Initial public documentation and official repository captures across IDs 61–70. |
| `task13-capture-002` | `task13-capture-001` | Expanded capture (v2) | Sealed (`45` captures) | Added Vercel auth/welcome docs, Netlify pricing, and Datadog identity check. |
| `task13-capture-003` | `task13-capture-002` | Expanded capture (v3) | Sealed (`51` captures) | Added Vercel deployment/account pages and readable Datadog `.md` sources (`api-app-keys.md`, `mcp_server.md`, `mcp_server/setup.md`) replacing gzip-corrupt HTML captures. |
| `task13-capture-004` | `task13-capture-003` | Final capture (v4) | Sealed (`52` captures) | Added `vercel.com/docs/limits/fair-use-guidelines`; attempted `mongodb.com/docs/atlas/api/api-resources/` (HTTP 404, recorded in `fetches`). |
| `task13-first-pass-001` | `task13-capture-004` | Initial ingest attempt | Incomplete / Rejected (preserved) | Rejected during pipeline intake validation; preserved untouched. |
| `task13-first-pass-002` | `task13-capture-004` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent read-only AI reviewer (`NEEDS FIXES`, 7 Contract v1.1 defects); preserved untouched. |
| `task13-first-pass-003` | `task13-first-pass-002` | **Final Task 13 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`Python jsonschema Draft202012Validator`, `10` records, `synthetic: false`, `245` verified evidence refs; all 7 independent review defects and 2 polish items in `outputs/task-13-review.md` remediated). |

## 2. Source-Capture and Claim-Coverage Counts

- **Selected Apps**: `10 / 100` (IDs `61–70`, all 10 present with asserted non-identity research)
- **Captured Snapshots**: `52` live public snapshots (`0` synthetic fixtures; 3 gzip-corrupt Datadog HTML snapshots preserved in archive and excluded from claim citations); `7` uncaptured fetch declarations recorded in `fetches` telemetry
- **Eligible Research Assertions (Frozen Inventory)**: `145` total (`125` observed documentary, `20` inferred; excludes 10 identity claims)
- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `145` pending, `accuracy: null`

| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `identity` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `purpose` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `auth` | 24 | 0 | 0 | 0 | 0 | 10/10 |
| `credentials` | 24 | 0 | 156 | 0 | 0 | 10/10 |
| `api` | 47 | 10 | 0 | 0 | 0 | 10/10 |
| `mcp` | 20 | 0 | 0 | 10 | 0 | 10/10 |
| `buildability` | 0 | 10 | 0 | 0 | 0 | 10/10 |

## 3. Sample Integrity & Shared Baseline Verification

- **Shared Baseline Status**: Task 06 (`outputs/task-06-review.md` PASS, pipeline `v0.2.0`, contract `v1.1`) confirmed accepted with no shared pipeline blockers encountered.
- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in Developer, Infra and Data platforms were researched to the same documentary standard without preferential treatment for sample apps (`64` Cloudflare, `65` Supabase).
- **Baseline Hash Verification**: `pilot-first-pass-001/records.json`, `pilot-first-pass-001/seal.json`, `task05-review-002/seal.json`, `outputs/task-06/sampling-manifest.json`, and `data/apps.json` all verified byte-for-byte unchanged.

## 4. Reproduction Instructions

Offline validation and metrics replay (no network or API keys required):

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task13-first-pass-003
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task13-first-pass-003 --target task13-first-pass-003
```

Rebuild extraction JSON from sealed capture `task13-capture-004` and regenerate `outputs/task-13/` deliverables:

```powershell
.venv\Scripts\python.exe -B work/task-13-agent/build_extraction.py
.venv\Scripts\python.exe -B work/task-13-agent/generate_deliverables.py
```
