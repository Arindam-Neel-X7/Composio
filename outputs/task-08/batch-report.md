# Task 08: Batch 2 Research Report (Support and Helpdesk, IDs 11–20)

- **Date**: 2026-11-23
- **Category**: Support and Helpdesk (`data/apps.json` IDs `11–20`)
- **Final Sealed Run ID**: `task08-first-pass-003` (`work/research-runs/task08-first-pass-003`)
- **Records SHA-256**: `b8c75b62b3e4f13478cca5d079e07dc50c4f6faa437d72d3d4cc1749eb23b861`
- **Seal SHA-256**: `e3fe4e7ded6cd1ac8dcd69ff551d209833afa812a40116023862e4cbec3e44d7`
- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`
- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy.

## 1. Run Lineage & Validation Results

| Run ID | Parent | Role | Status | Notes |
| --- | --- | --- | --- | --- |
| `task08-capture-001` | `null` | Initial capture (sandboxed) | Sealed (`0` captures) | Preserves initial sandbox DNS failures per immutable-run rules. |
| `task08-capture-002` | `task08-capture-001` | Network capture recovery (v1) | Sealed (`37` captures) | Approved-network HTTP capture including 31,897-line `developers.freshdesk.com/api/` via `--max-bytes 10000000`. |
| `task08-capture-003` | `task08-capture-002` | Expanded capture (v2) | Sealed (`54` captures) | Added Zendesk community MCP, Intercom OAuth, Front `.md` auth/MCP/Admin MCP, Pylon `.md` auth/API/MCP, LiveAgent MCP, Plain `developer.txt`, Gorgias OAuth/review/community MCP. |
| `task08-capture-004` | `task08-capture-003` | Final capture (v3) | Sealed (`58` captures) | Added exact Plain GraphQL `introduction.md`, `authentication.md`, `oauth.md`, and `integrations/mcp-server.md`. |
| `task08-first-pass-001` | `task08-capture-004` | Initial ingest attempt | Rejected (preserved) | Rejected by JSON Schema validator (lowercase auth/protocol enums); preserved untouched. |
| `task08-first-pass-002` | `task08-capture-004` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent AI reviewer; superseded by `task08-first-pass-003` to tighten per-claim attachments/locators and downgrade `20.production.contact_sales_required` to `unknown`. |
| `task08-first-pass-003` | `task08-capture-004` | **Final Task 08 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`Python jsonschema Draft202012Validator`, `10` records, `synthetic: false`). |

## 2. Source-Capture and Claim-Coverage Counts

- **Selected Apps**: `10 / 100` (IDs `11–20`, all 10 present with asserted non-identity research)
- **Captured Snapshots**: `58` live public snapshots (`0` synthetic fixtures; 4 `developer.helpscout.com` snapshots returned compressed binary bytes and were not cited); `10` distinct URLs failed in network runs (preserved in `fetches`, never promoted into claims)
- **Eligible Research Assertions (Frozen Inventory)**: `152` total (`133` observed documentary, `19` inferred; excludes 10 identity claims)
- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `152` pending, `accuracy: null`

| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `identity` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `purpose` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `auth` | 21 | 0 | 0 | 0 | 0 | 10/10 |
| `credentials` | 45 | 0 | 135 | 0 | 0 | 10/10 |
| `api` | 40 | 9 | 2 | 0 | 0 | 10/10 |
| `mcp` | 17 | 0 | 1 | 9 | 1 | 8/10 |
| `buildability` | 0 | 10 | 0 | 0 | 0 | 10/10 |

## 3. Pilot Continuity & Integrity Verification

- **Freshdesk (ID 13) Pilot Provenance**: Freshdesk was previously researched in `work/task-04-runs/pilot-first-pass-001` and verified `20/20` in `task05-review-002`, with one disclosed capture gap: `developers.freshdesk.com/api/` failed under the v0.1.0 2 MB cap. Using pipeline v0.2.0 (`--max-bytes 10000000`), Task 08 freshly captured all 5 pilot URLs plus `developers.freshdesk.com/api/` (31,897 lines) and `www.freshworks.com/freshdesk/pricing/`, directly grounding Freshdesk's HTTP Basic (`apikey:X`) wire format, plan-tiered rate limits, and GA MCP allowances. Original Task 04/05 sealed runs remain byte-for-byte unchanged.
- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in Support and Helpdesk were researched to the same documentary standard.
- **Baseline Hash Verification**: `pilot-first-pass-001` (`records.json` & `seal.json`), `task05-review-002` (`seal.json`), `outputs/task-06/sampling-manifest.json`, `data/apps.json`, and `task07-first-pass-003` (`records.json` & `seal.json`) all verified byte-for-byte unchanged.

## 4. Reproduction Instructions

Offline validation and metrics replay (no network or API keys required):

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task08-first-pass-003
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task08-first-pass-003 --target task08-first-pass-003
```

Rebuild extraction JSON from sealed capture `task08-capture-004`:

```powershell
.venv\Scripts\python.exe -B work/task-08-agent/build_extraction.py
```
