# Task 15: Independent AI Review Report (Finance and Fintech, IDs 81–90)

- **Final Verdict**: **PASS**
- **Reviewed on**: 2026-11-24
- **Auditor**: Independent read-only AI reviewer (`f96f88d5-e553-4c4b-91ac-3f769ec0a95a`, context-isolated; shared model family disclosed). **AI review only; not human review and not Task 17 formal blind scoring.**
- **Accepted Run**: `work/research-runs/task15-first-pass-002` (`records.json` SHA-256 `3a82fb00f79ed6bde41e66ad29d34a01e8a1dbd2d92ffa8d52a302bffcdd3f8f`, `seal.json` SHA-256 `ca7e91ab10379502c65d5102b9d97b930234b61cecfd2a3b481f61a61544c65b`)
- **Parent Capture Run**: `work/research-runs/task15-capture-005` (`62` captured snapshots, `15` failed fetches)
- **Superseded / Unused Runs Preserved Untouched**:
  - `work/research-runs/task15-capture-004` (network-isolated sandbox capture attempt, unused branch preserved)
  - `work/research-runs/task15-first-pass-001` (initial ingest attempt rejected by community-source guard; preserved untouched)
- **Formal Blind Scoring**: Deferred to Task 17 (20-app stratified sample includes App `83` Binance and App `84` Paygent Connect); `task15-first-pass-002` keeps `review.status == "pending"` and `accuracy: null` (`168` eligible assertions: `153` observed, `15` inferred; `212` verified evidence citations).

---

## 1. Core Verification Checks (All PASS)

| Area | Status | Verified Evidence |
| --- | --- | --- |
| Baseline & prior-run immutability | **PASS** | `pilot-first-pass-001` (`records.json` `10ff5bdb...`, `seal.json` `eaebd62d...`), `task05-review-002` (`seal.json` `9713538d...`), `outputs/task-06/sampling-manifest.json` (`7f8a6111...`), and `data/apps.json` (`6e3aada1...`) all verified byte-for-byte unchanged. All `66/66` sealed files in `task15-first-pass-002/seal.json` verified with `0` hash mismatches. |
| Schema & grounding validation | **PASS** | `research_pipeline.py validate --run-id task15-first-pass-002` passed (`Python jsonschema Draft202012Validator`, contract `v1.1`, `10/10` records matching `data/apps.json` IDs 81–90, `synthetic: false`, `parent_run_id: task15-capture-005`). |
| Evidence-link & claim grounding | **PASS** | All `212` evidence citations independently verified against local snapshot files in `task15-first-pass-002/snapshots/`. Verified `0` missing snapshots, `0` out-of-bounds locator line ranges, and `0` empty snippets. All `10/10` nested MCP `operational_check` claims strictly remain `not_researched` with `value: null`. `0` citations point to the `15` failed fetches (HTTP 403, timeouts, 1-line SPA shells). |
| Community source restriction | **PASS** | Community repositories (`mujeeb8/Binance-MCP` and `iPAYX-Technologies/mcp-fx-audit`) are cited strictly under `mcp.entries` (`origin: "community"`). Verified `0` citations of community sources in product identity, auth, API, or buildability claims (satisfying the community-source isolation rule). |
| Credential boolean scoping | **PASS** | No credential boolean path-collapsing. Where credential access differed between developer sandboxes vs live production, personal keys vs organization admin approval, or own-account vs commercial partner onboarding, booleans are honestly scoped or preserved as `unknown` with detailed rationales citing the exact distinctions. |
| Honest preservation of unknowns | **PASS** | ID `84` (Paygent Connect) is honestly preserved as an unresolved identity (`identity_status: "unresolved"` in `data/apps.json`) with all product claims set to `unknown`. ID `90` (PitchBook) had all 7 official URLs blocked with HTTP 403, and all claims are honestly preserved as `unknown`. ID `85` (iPayX) primary docs returned 1-line SPA shells, leaving REST API/credentials as `unknown`. |
| Deliverables consistency | **PASS** | `outputs/task-15/{records.json, findings-matrix.md, source-index.md, batch-report.md, exceptions-for-reviewer.md, metrics.json}` all match `task15-first-pass-002` hashes (`3a82fb00...`, seal `ca7e91ab...`) and metrics (`168` eligible assertions, `168` pending, `accuracy: null`, `review_coverage: 0.0%`). No human attestation or accuracy claims. |

---

## 2. Detailed App-by-App Audit (IDs 81–90)

### App 81 — Stripe (`PASS`)
- **Identity & Purpose**: Accurately identified as Stripe financial infrastructure platform API (`https://api.stripe.com`) and Stripe MCP server (`https://mcp.stripe.com`). Grounded in `docs.stripe.com/api` and `docs.stripe.com/mcp`.
- **Auth Methods**: 4 distinct auth methods documented and grounded: `API_key` (`81.auth.api_keys` for restricted/secret keys), `Bearer_token` (`81.auth.workload_identity_federation`), `OAuth2` (`81.auth.connect_oauth2` for multi-tenant Connect platforms), and `OAuth2` (`81.auth.mcp_oauth2` for hosted MCP server).
- **Credentials**: Testing sandbox is self-serve and free (`free_access=true`, `sandbox_access=true`, `paid_required=false`, `self_serve=true`). Production requires business KYC verification (`vendor_approval_required=true`, `sandbox_access=false`, `self_serve=true` subject to KYC).
- **API & MCP**: REST API, official multi-language SDKs, Stripe CLI. Breadth is accurately classified **`broad`** (`inferred`), supported by 4 distinct multi-domain groups (Core Payments, Billing & Products, Connect Platforms, Financial Services / Risk / Data). Official hosted MCP server (`https://mcp.stripe.com`) verified; operational check is `not_researched`.
- **Buildability**: **`build_now`** (`inferred`), with KYC activation, country prerequisites, and upcoming 2027 MCP key migration noted as scoped caveats.

### App 82 — Plaid (`PASS`)
- **Identity & Purpose**: Financial account connectivity API for bank auth, transactions, balances, identity, and payments, plus Sandbox and Dashboard MCP servers. Grounded in `plaid.com/docs/api/` and `plaid.com/docs/resources/mcp/`.
- **Auth Methods**: `API_key` (`82.auth.client_id_secret` with `client_id` + `secret`) and `OAuth2` (`82.auth.oauth2_dashboard_mcp` with `mcp:dashboard` scope).
- **Credentials**: Sandbox is free, self-serve, and persistent (`free_access=true`, `sandbox_access=true`, `paid_required=false`). Limited 10-Item Production Trial available in US/CA (`trial_access=true`). Full Production requires Plaid approval and paid plan (`vendor_approval_required=true`, `paid_required=true`, `free_access=false`).
- **API & MCP**: REST/JSON API and client libraries; breadth is **`broad`** (`inferred`) across 4 distinct financial data and money movement domains. Two official MCP servers documented: official remote hosted Dashboard MCP (`https://api.dashboard.plaid.com/mcp/`) and official local stdio Sandbox MCP (`plaid/ai-coding-toolkit/mcp-server-plaid`). Both operational checks are `not_researched`.
- **Buildability**: **`conditional`** (`inferred`), citing production approval, OAuth security questionnaires, and paid plan requirements.

### App 83 — Binance (`PASS` — Sample Member)
- **Identity & Purpose**: Cryptocurrency exchange Spot trading and market data API. Grounded in official vendor GitHub repository `binance/binance-spot-api-docs` (rest-api.md, testnet/general-info.md).
- **Auth Methods**: `none` (`83.auth.public_none` for public market data) and `API_key` (`83.auth.signed_api_key` with HMAC/RSA/Ed25519 signatures).
- **Credentials**: Spot Testnet is free, isolated, and self-serve (`free_access=true`, `sandbox_access=true`, `paid_required=false`, `self_serve=true`). Production live mode is separate; global KYC/jurisdictional eligibility is honestly marked `unknown`.
- **API & MCP**: REST API, WebSocket/FIX streams, official SDKs. Breadth is **`broad`** (`inferred`) across 4 groups (Market Data, Spot Trading, User Data / Account Management, User Stream). Community MCP server (`mujeeb8/Binance-MCP`) is correctly tagged `origin: "community"` and cited strictly for MCP claims. Operational check is `not_researched`.
- **Buildability**: **`conditional`** (`inferred`), citing jurisdictional KYC uncertainties and lack of an official vendor-published MCP.

### App 84 — Paygent Connect (`PASS` — Sample Member, Unresolved Identity)
- **Identity & Resolution**: Grounded in `data/apps.json` where Paygent Connect is flagged `identity_status: "unresolved"` with original hint `paygent (NMI-powered)`. Captured `nmi.com` pages confirm NMI is a white-label gateway with no documented "Paygent Connect" product, and Japanese Paygent Co., Ltd. (NTT DATA / MUFG NICOS) is a separate gateway that is not assumed.
- **Claims**: In accordance with `docs/evidence-rules.md`, `84.identity.resolution` and all product-specific claims (purpose, auth, testing, production, api, mcp, buildability) are honestly preserved as **`unknown`**.
- **Audit Finding**: Correctly prevents hallucination or unauthorized substitution of unverified third-party entities.

### App 85 — iPayX (`PASS`)
- **Identity & Purpose**: FINTRAC-registered FX forensic audit layer (`iPayX Protocol`). Grounded in `www.ipayx.ai/` (lines:1-1).
- **Auth & API Surface**: Primary vendor pages (`ipayx.ai/docs`, `/docs/api`, `/docs/mcp`, `/api-terms`) rendered single-line JS SPA shells, and `/pricing` timed out. These fetch failures were recorded in `records.json` `fetches` and `exceptions-for-reviewer.md`. Primary REST API and credentials remain **`unknown`**.
- **MCP**: GitHub repository `iPAYX-Technologies/mcp-fx-audit` documents a remote streamable-HTTP MCP server at `https://mcp.ipayx.ai/mcp` (v1.4.0, Bearer token for `full_forensic_fx_report`). Because the SPA shell lacked an org ownership link, this repository is conservatively classified `origin: "community"` and cited **strictly** for MCP claims. Operational check is `not_researched`.
- **Buildability**: **`conditional`** (`inferred`), citing JS SPA shell capture blockers and unverified vendor-domain linkage.

### App 86 — QuickBooks (`PASS`)
- **Identity & Purpose**: Cloud accounting API for QuickBooks Online companies with OAuth 2.0 and an official local MCP server. Grounded in `static.developer.intuit.com` and `intuit/quickbooks-online-mcp-server`.
- **Auth Methods**: `OAuth2` (`86.auth.oauth2_auth_code` with realmId and 100-day refresh tokens).
- **Credentials**: Developer sandbox companies are self-serve and free (`sandbox_access=true`, `self_serve=true`). Production access requires Intuit review of the App Assessment Questionnaire and compliance verification (`vendor_approval_required=true`, `sandbox_access=false`, `self_serve=false`).
- **API & MCP**: REST API, official multi-language SDKs. Resource groups grounded in the official MCP README (29 CRUD entities + 11 financial reports); breadth is **`broad`** (`inferred`) across 4 major accounting/ERP domains. Official local stdio MCP server (`intuit/quickbooks-online-mcp-server`) verified; operational check is `not_researched`.
- **Buildability**: **`conditional`** (`inferred`), citing Intuit App Assessment Questionnaire approval and company-realm OAuth consent.

### App 87 — Xero (`PASS`)
- **Identity & Purpose**: Cloud accounting and business API suite with OAuth 2.0, OpenAPI 3.0 specs, SDKs, and official hosted Remote MCP and local MCP servers. Grounded in `developer.xero.com` FAQs/pricing, `XeroAPI/Xero-OpenAPI`, and `XeroAPI/xero-mcp-server`.
- **Auth Methods**: `OAuth2` (`87.auth.oauth2_auth_code_pkce` for multi-org apps and Remote MCP) and `OAuth2` (`87.auth.oauth2_client_credentials_custom` for Custom Connections). Upcoming deprecation (new Custom Connections closing 1 December 2026) is explicitly documented.
- **Credentials**: Starter tier is free for <= 5 connections and includes Demo Company access (`free_access=true`, `sandbox_access=true`). Real-org Remote MCP or > 5 connections requires paid Core ($35 AUD/mo) or higher.
- **API & MCP**: OpenAPI 3.0 REST API and SDKs; breadth is **`broad`** (`inferred`) across 3 multi-domain accounting suites. Two official MCP servers documented: official remote hosted MCP (`https://api.xero.com/mcp/v1`) and official local stdio MCP (`@xeroapi/xero-mcp-server`). Both operational checks are `not_researched`.
- **Buildability**: **`build_now`** (`inferred`), with connection tier caps, Demo org restrictions for free Remote MCP, and paid Core plan requirements clearly disclosed.

### App 88 — Brex (`PASS`)
- **Identity & Purpose**: Corporate card, expense, bill pay, and banking spend-management REST API with an official hosted MCP server. Grounded in `developer.brex.com/` and `developer.brex.com/docs/mcp.md`.
- **Auth Methods**: 4 distinct auth methods documented: `Bearer_token` (`88.auth.own_account_user_token` for production user tokens), `OAuth2` (`88.auth.partner_oauth2_auth_code` for multi-tenant customer access), `OAuth2` (`88.auth.partner_oauth2_client_credentials` for partner onboarding), and `OAuth2` (`88.auth.mcp_oauth2_dcr` for hosted MCP with Dynamic Client Registration).
- **Credentials**: Own-account customers have no sandbox (`sandbox_access=false`, production `api.brex.com` only, requiring Account/Card Admin approval). Third-party partner staging (`api-staging.brex.com`) requires partner review and a signed Unilateral API Access Agreement (`vendor_approval_required=true`, `partner_approval_required=true`, `self_serve=false`).
- **API & MCP**: REST API; breadth is **`broad`** (`inferred`) across 3 spend-management domains. Official hosted MCP server (`https://api.brex.com/mcp`) verified; operational check is `not_researched`.
- **Buildability**: **`conditional`** (`inferred`), citing no-sandbox own-account access and partner agreement/demo requirements.

### App 89 — Ramp (`PASS`)
- **Identity & Purpose**: Corporate spend-management, card, bill pay, and accounting REST API with official hosted MCP servers and CLI. Grounded in `docs.ramp.com/llms.txt`, `llms-api.txt`, and `llms-guides/*.txt`.
- **Auth Methods**: 3 distinct auth methods documented: `OAuth2` (`89.auth.oauth2_client_credentials` for own-business apps), `OAuth2` (`89.auth.oauth2_auth_code` for third-party partners), and `OAuth2` (`89.auth.mcp_cli_oauth2` for MCP server and CLI).
- **Credentials**: Sandbox access form body was empty in capture (`sandbox-access.txt` 4 lines), so sandbox approval terms are honestly marked `unknown`. Production own-business apps require Ramp business account Admin/Owner approval (`admin_approval_required=true`).
- **API & MCP**: OpenAPI REST API (`llms-api.txt`, 35,019 lines) and Ramp CLI; breadth is **`broad`** (`inferred`) across 5 distinct commercial spend domains. Official hosted MCP server (`https://mcp.ramp.com/mcp`) verified; operational check is `not_researched`.
- **Buildability**: **`conditional`** (`inferred`), citing Ramp business account requirement, Admin approval, and unverified sandbox form policy.

### App 90 — PitchBook (`PASS`)
- **Identity & Resolution**: All 7 official PitchBook URLs (`pitchbook.com` and `www.pitchbook.com` help and product pages) returned HTTP 403 (`blocked`) across `task15-capture-001` through `task15-capture-003` (`fetches[0..6]`).
- **Claims**: In accordance with `docs/evidence-rules.md` (HTTP 403 does not prove absence of API/MCP and search snippets cannot establish vendor claims), all product-specific claims (purpose, auth, testing, production, api, mcp, buildability) are honestly preserved as **`unknown`**.
- **Audit Finding**: Exemplary fidelity to evidence standards; avoids unevidenced positive claims.

---

## 3. Deliverables & Reproduction Audit (All PASS)

- **`outputs/task-15/records.json`**: Byte-identical copy of `work/research-runs/task15-first-pass-002/records.json` (`3a82fb00...`).
- **`outputs/task-15/findings-matrix.md`**: Complete 10-app matrix faithfully summarizing identity, auth methods, testing vs production credentials, API surface, MCP provenance and direction, and buildability.
- **`outputs/task-15/source-index.md`**: Indexes all 62 captured snapshots and clearly documents all 15 failed fetches.
- **`outputs/task-15/batch-report.md`**: Discloses run lineage, claim coverage counts, baseline hash verification, and offline reproduction commands.
- **`outputs/task-15/exceptions-for-reviewer.md`**: Thoroughly details unresolved identity on App 84, HTTP 403 blocks on App 90, JS SPA shells on App 85, and partial capture gaps on Apps 83, 86, 87, 88, and 89.
- **`outputs/task-15/metrics.json`**: Matches frozen claim inventory counts (`168` eligible assertions: `153` observed, `15` inferred; `168` pending; `accuracy: null`; `review_coverage: 0.0%`).

---

## 4. Disposition & Recommendation

- **Task 15 Status**: **PASS** (Accepted as completed for first-pass batch research and independent AI review).
- **Formal Evaluation Note**: Independent AI review only; human verification and Task 17 formal blind scoring (including sample apps `83` Binance and `84` Paygent Connect) remain pending.
