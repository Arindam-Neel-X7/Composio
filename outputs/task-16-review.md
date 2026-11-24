# Task 16: Independent AI Review Report (AI, Research and Media-native, IDs 91–100)

- **Final Verdict**: **PASS**
- **Reviewed on**: 2026-11-24
- **Auditor**: Independent read-only AI review agent (context-isolated; shared model family disclosed). **AI review only; not human review and not Task 17 formal blind scoring.**
- **Target & Accepted Run**: `work/research-runs/task16-first-pass-001` (parent: `task16-capture-007`)
  - `records.json` SHA-256: `56aba7c2e67ec24fcd831307c856fb5c2a7d6ebddecd66fc8dbd7623d266429a`
  - `seal.json` SHA-256: `fc2dbb794eb2f3c80ae95202e02bdbe0f85b419b0c520feffd99e6ee7b66dbdb`
  - `manifest.json` SHA-256: `d7e23a40486e083c847347e093d9434b8510f600cb7ac41b2bc406ed49eea12d`
- **Target Deliverables**: `outputs/task-16/{records.json, metrics.json, findings-matrix.md, source-index.md, batch-report.md, exceptions-for-reviewer.md}`
- **Scope & Boundaries**: Line-by-line inspection of all `10` records (IDs `91–100`, `186` eligible research assertions + `10` identity claims; `424` evidence observations) against `work/research-runs/task16-first-pass-001/snapshots/`, `docs/evidence-rules.md` v1.1, and `schemas/record.json` v1.1. No shared code, sampling, prior tasks' files, or `data/apps.json` were modified. Formal blind scoring of frozen sample apps `97` (higgsfield) and `98` (Mermaid CLI) remains deferred to Task 17 (`accuracy: null`, `review_coverage: 0.0%`).

---

## 1. Core Verification Checks (All PASS)

| Area | Status | Verified Evidence |
| --- | --- | --- |
| Baseline & sealed-run immutability | **PASS** | `pilot-first-pass-001` (`records.json` `10ff5bdb...`, `seal.json` `eaebd62d...`), `task05-review-002` (`seal.json` `9713538d...`), `outputs/task-06/sampling-manifest.json` (`7f8a6111...`), and `data/apps.json` (`6e3aada1...`) all verified byte-for-byte unchanged. |
| Schema & pipeline validation | **PASS** | `research_pipeline.py validate --run-id task16-first-pass-001` passed (`Python jsonschema Draft202012Validator`, contract `v1.1`, `10/10` records matching `data/apps.json` IDs `91–100`, `synthetic: false`). Offline test suite `test_research_pipeline.py` passed `23/23` tests. |
| Evidence links & locator grounding | **PASS** | All `424/424` evidence references resolve to local snapshot files with `0` SHA-256 digest mismatches. All `424` line ranges (`lines:N-M`) are valid within snapshot boundaries. Direct text matching confirmed `0` ungrounded citations or off-by-one errors. |
| Auth taxonomy, MCP provenance & operational checks | **PASS** | Valid auth enums across all 10 apps (including `none` for local MIT-licensed Mermaid CLI, `OAuth2`, `API_key`, and `Bearer_token`). All 8 MCP entries have verified callable server direction and URLs (`https://mcp.otter.ai/mcp`, `https://api.fathom.ai/mcp`, `https://mcp.consensus.app/mcp`, `https://mcp.reducto.ai/mcp`, `https://mcp.devin.ai/mcp`, `https://mcp.higgsfield.ai/mcp`, `https://transcriptapi.com/mcp`, `https://api.grain.com/_/mcp`). All `8/8` nested `operational_check` claims remain `not_researched`. Bounded searches for NotebookLM (Enterprise) and Mermaid CLI (official repo) correctly assert `not_found_in_checked_sources`. |
| Credential scoping & path separation | **PASS** | Conflicting credential paths are strictly separated without collapsing: NotebookLM personal preview is excluded from Enterprise; Otter MCP OAuth is separated from Enterprise API keys; Fathom user keys are separated from vendor-reviewed OAuth; Consensus self-serve REST & MCP DCR are separated from manual enterprise OAuth; Reducto Studio roles are distinguished while free page quota remains `unknown`; Devin service users vs. PATs vs. legacy keys are distinguished; Higgsfield prepaid USD API is separated from plan-credit CLI & MCP; Mermaid CLI local free MIT execution has `trial_access`/`sandbox_access` marked `not_applicable`; YouTube Transcript 100 free credits vs. paid plans are separated; Grain personal PAT (Free+) is separated from workspace tokens (admin-only, rejected by MCP). |
| Breadth & buildability dependencies | **PASS** | `breadth` classifications (`narrow` for 98 Mermaid CLI and 99 YouTube Transcript; `broad` for 96 Devin; `moderate` for 91, 92, 93, 94, 95, 97, 100) are justified under `docs/evidence-rules.md` line 63 with valid supporting resource-group refs. All 10 `buildability` claims resolve valid supporting refs and declare grounded blockers and next steps. |
| Deliverables consistency (`outputs/task-16/`) | **PASS** | `outputs/task-16/records.json` is byte-identical to `work/research-runs/task16-first-pass-001/records.json` (`56aba7c2...`). `outputs/task-16/metrics.json` matches pipeline `metrics` output. `source-index.md`, `findings-matrix.md`, `batch-report.md`, and `exceptions-for-reviewer.md` are complete, consistent, and disclose all exceptions and AI-only review status. |

---

## 2. App-by-App Review Audit (IDs 91–100)

### App 91 — NotebookLM (`PASS`)
- **Identity & Purpose**: Matched to Google Cloud Gemini Notebook Enterprise (`discoveryengine.googleapis.com` v1alpha REST API). Reconciles the roster hint `cloud.google.com/gemini (Enterprise API)` and documents the rename from NotebookLM Enterprise to Gemini Notebook Enterprise (`set-up-licensing` lines 140–144). Personal `developers.google.com/notebook` Public Preview is explicitly excluded (`91.auth.notes`).
- **Auth**: `91.auth.licensed_user` (`Bearer_token` via `gcloud auth print-access-token`, requiring active Enterprise license and Cloud NotebookLM User IAM role).
- **Credentials**: `testing.trial_access=true`, `testing.free_access=true`, `testing.paid_required=false` (14-day free trial tier with 5,000 licenses); `production.paid_required=true`; `admin_approval_required=true` and `self_serve=true` across both envs (tenant admin setup).
- **API & MCP**: REST protocol; 2 resource groups (`notebooks`, `sources`); `moderate` breadth; `mcp.discovery=not_found_in_checked_sources` (no Enterprise MCP documented).
- **Buildability**: `conditional` (Preview/Pre-GA terms, licensed user IAM, Google Drive authorization).

### App 92 — Otter AI (`PASS`)
- **Identity & Purpose**: Matched to Otter AI meeting knowledge platform (`help.otter.ai`).
- **Auth**: Cleanly separates `92.auth.mcp_oauth` (`OAuth2` for `https://mcp.otter.ai/mcp`) from `92.auth.enterprise_api_key` (`API_key` for Enterprise Public API `https://api.otter.ai/v1/`).
- **Credentials**: `self_serve=true` on MCP path; other credential booleans properly left `unknown` because captured docs do not settle MCP plan eligibility, and Enterprise API requires account-manager enablement.
- **API & MCP**: REST and other (MCP); 3 resource groups (`meeting_content`, `channels_workspace`, `mcp_profile`); `moderate` breadth; `mcp.discovery=found` with official server `https://mcp.otter.ai/mcp` (`operational_check=not_researched`). Single-line Zendesk JSON API capture (`36130822688279.json`) is properly cited with exact JSON/HTML anchors.
- **Buildability**: `conditional` (MCP OAuth authorization and shared-meeting prerequisites).

### App 93 — Fathom (`PASS`)
- **Identity & Purpose**: Matched to Fathom video meeting assistant (`fathom.video` / `developers.fathom.ai`), reconciling help page `8368641` link.
- **Auth**: Cleanly separates `93.auth.api_key` (`API_key`, user-level `X-Api-Key` in User Settings) from `93.auth.oauth` (`OAuth2`, `public_api` scope for multi-user public apps).
- **Credentials**: `self_serve=true` for user API keys; other credential booleans properly left `unknown` (public OAuth apps require vendor review; plan costs unresolved).
- **API & MCP**: REST and SDK; 2 resource groups (`meeting_recordings`, `teams_webhooks`); `moderate` breadth; `mcp.discovery=found` with official server `https://api.fathom.ai/mcp` (`operational_check=not_researched`).
- **Buildability**: `conditional` (user-level sharing constraints and plan entitlements).

### App 94 — Consensus (`PASS`)
- **Identity & Purpose**: Matched to Consensus (`consensus.app`), reconciling the roster hint `consensus.app (OAuth requested)`.
- **Auth**: Captures `94.auth.rest_key` (`API_key`, `x-api-key`), `94.auth.mcp_oauth` (`OAuth2`, PKCE S256 with Dynamic Client Registration), and `94.auth.mcp_key` (`API_key` Bearer gateway).
- **Credentials**: `testing.free_access=true`, `testing.paid_required=false`, `self_serve=true` (recurring Free plan: 30 calls/mo, max 20 papers/req); pagination, full text, and citation beta endpoints are paid. Confidential enterprise OAuth requires manual sales provisioning.
- **API & MCP**: REST and other (MCP); 4 resource groups (`search`, `full_text`, `threads`, `citations`); `moderate` breadth; `mcp.discovery=found` with official server `https://mcp.consensus.app/mcp` (`operational_check=not_researched`).
- **Buildability**: `build_now` for basic first-page REST search.

### App 95 — Reducto (`PASS`)
- **Identity & Purpose**: Matched to Reducto document processing API (`reducto.ai` / `docs.reducto.ai`).
- **Auth**: `95.auth.api_key` (`API_key`, `REDUCTO_API_KEY` Bearer) and `95.auth.local_mcp_oauth_device` (`OAuth2`, `uvx mcp-server-reducto --login`).
- **Credentials**: `self_serve=true` and `admin_approval_required=false` (all roles create keys); `production.paid_required=true` ($1–$60 per 1,000 pages list pricing). Testing free access/paid requirements properly left `unknown` because captured docs do not specify a free starter page quota.
- **API & MCP**: REST, SDK, CLI, and other (MCP); 3 resource groups (`parse_upload`, `extract_split_classify_edit`, `usage_export`); `moderate` breadth; `mcp.discovery=found` with official hosted server `https://mcp.reducto.ai/mcp` (`operational_check=not_researched`). Local vs. hosted MCP constraints documented.
- **Buildability**: `build_now` for self-serve API and hosted MCP public URL parsing.

### App 96 — Devin (`PASS`)
- **Identity & Purpose**: Matched to Devin autonomous AI software engineering platform (`devin.ai` / `docs.devin.ai`).
- **Auth**: Distinguishes `96.auth.service_user_key` (`API_key`, non-human `cog_` prefix), `96.auth.personal_access_token` (`Bearer_token`, human `cog_` prefix), and `96.auth.legacy_api_key` (`API_key`, `apk_`/`apk_user_` deprecated, limited to repo wiki tools).
- **Credentials**: `admin_approval_required=true` (service users provisioned by Admin; Enterprise PATs disabled by default pending admin policy); `self_serve=true` for authorized org admins. Account pricing/free tiers left `unknown`.
- **API & MCP**: REST and other (MCP); 4 resource groups (`sessions`, `knowledge_playbooks_secrets`, `automations_schedules_scans`, `enterprise_governance`); `broad` breadth (autonomous sessions, knowledge/skills, CI snapshot builds/code scans, enterprise governance); `mcp.discovery=found` with official callable server `https://mcp.devin.ai/mcp` (`operational_check=not_researched`). Outgoing MCP client management (`devin_mcp_server_manage`) and free DeepWiki MCP (`https://mcp.deepwiki.com/`) are cleanly distinguished.
- **Buildability**: `conditional` (requires active Devin account and admin key provisioning).

### App 97 — higgsfield (*Frozen 20-App Sample Member*, `PASS`)
- **Identity & Purpose**: Matched to Higgsfield AI video/image creative suite (`higgsfield.ai`).
- **Auth**: Strictly separates `97.auth.api_key` (`API_key` from `open.higgsfield.ai` for `api.higgsfield.ai`), `97.auth.cli_browser_oauth` (`OAuth2` for `@higgsfield/cli`), and `97.auth.mcp_browser_signin` (`OAuth2` for `https://mcp.higgsfield.ai/mcp`).
- **Credentials**: `free_access=false` and `paid_required=true` across testing and production (CLI/MCP require a paid subscription with plan credits; API requires a prepaid USD balance with a $5 minimum top-up; web Unlimited and free generations explicitly do not apply); `self_serve=true`.
- **API & MCP**: REST, SDK, CLI, and other (MCP); 3 resource groups (`media_generation`, `soul_characters_workflows`, `account_workspace_assets`); `moderate` breadth; `mcp.discovery=found` with official hosted server `https://mcp.higgsfield.ai/mcp` (`operational_check=not_researched`).
- **Buildability**: `conditional` (prepaid USD balance for API or paid subscription credits for CLI/MCP).

### App 98 — Mermaid CLI (*Frozen 20-App Sample Member*, `PASS`)
- **Identity & Purpose**: Matched to official `@mermaid-js/mermaid-cli` (`github.com/mermaid-js/mermaid-cli`).
- **Auth**: `98.auth.local_none` (`none`, local CLI / Node.js library / container execution).
- **Credentials**: `free_access=true`, `paid_required=false`, `admin_approval_required=false`, `vendor_approval_required=false`, `partner_approval_required=false`, `contact_sales_required=false`, `self_serve=true`; `trial_access` and `sandbox_access` properly marked `not_applicable` with explanatory evidence.
- **API & MCP**: CLI and SDK; 2 resource groups (`diagram_rendering`, `markdown_transformation`); `narrow` breadth; `mcp.discovery=not_found_in_checked_sources` (bounded check of official repo and README found no official MCP server).
- **Buildability**: `build_now` for local `mmdc` CLI or Node.js `run()` API (noting non-semver Node.js API status).

### App 99 — YouTube Transcript (`PASS`)
- **Identity & Purpose**: Matched to TranscriptAPI.com (`transcriptapi.com`), reconciling the roster hint.
- **Auth**: `99.auth.api_key` (`API_key`, `sk_` Bearer) and `99.auth.mcp_oauth21` (`OAuth2`, OAuth 2.1 `mcp:access` scope, supporting DCR for Claude and Static registration for ChatGPT).
- **Credentials**: `testing.free_access=true`, `testing.paid_required=false`, `self_serve=true` (100 free starter credits, no card required, plus 2 zero-credit tools); `production.paid_required=true` ($5/mo for 1,000 credits beyond starter pool).
- **API & MCP**: REST and other (MCP); 2 resource groups (`transcripts_metadata`, `search_channels_playlists`); `narrow` breadth; `mcp.discovery=found` with official hosted server `https://transcriptapi.com/mcp` (`operational_check=not_researched`).
- **Buildability**: `build_now` for self-serve free signup and REST/MCP transcript extraction.

### App 100 — Grain (`PASS`)
- **Identity & Purpose**: Matched to Grain (`grain.com` / `developers.grain.com`).
- **Auth**: Strictly separates `100.auth.personal_access_token` (`Bearer_token`, Free+ plans, accepted by REST v2 and headless MCP), `100.auth.workspace_access_token` (`Bearer_token`, Business/Enterprise admin-only, full workspace access, **rejected by MCP**), and `100.auth.oauth2` (`OAuth2` PKCE with Client ID Metadata Document support).
- **Credentials**: `testing.free_access=true`, `testing.paid_required=false`, `self_serve=true` (Personal Access Tokens and core MCP tools are free and self-serve); `admin_approval_required` and `vendor_approval_required` properly left `unknown` across mixed paths (workspace tokens need admin; OAuth workspace scope needs Grain verification).
- **API & MCP**: REST and other (MCP); 2 resource groups (`recordings_transcripts_highlights`, `mcp_meetings_contacts_deals_coaching`); `moderate` breadth; `mcp.discovery=found` with official hosted server `https://api.grain.com/_/mcp` (`operational_check=not_researched`).
- **Buildability**: `build_now` for Personal Access Token REST v2 and headless MCP meeting data access.

---

## 3. Disposition

- **Task 16 Review Status**: **PASS** (Accepted as `completed` pending coordinator review; AI review only, not human review).
- **Baseline Integrity**: Preserved byte-for-byte (`pilot-first-pass-001`, `task05-review-002`, `outputs/task-06/sampling-manifest.json`, and `data/apps.json`).
- **Next Steps**: With all research batches (Tasks 07–16) completed, proceed to coordinator reconciliation and preparation for **Task 17 (Audit the frozen 20-app sample)**.
