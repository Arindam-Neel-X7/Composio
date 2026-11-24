# Task 18 Phase A: Correction Log & Provenance Audit

- **Target Sample**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`)
- **Fixed Question Denominator (N)**: `327` claims across 20 stratified apps
- **Total Changed Claims**: `50` claims
- **Added Claims**: `0`
- **Removed Claims**: `0`
- **Split Claims**: `0`
- **Child Correction Runs**: `task18-corrections-07` through `task18-corrections-16`

---

## 1. Classification of Corrections

### A. Research Mistakes in First-Pass (13 Claims)
In the original first-pass runs, researchers improperly asserted `status: observed` with `value: false` for absence of approval/sandbox gating based merely on the documentation not mentioning vendor/partner approvals or contact sales. Under `docs/evidence-rules.md`, silence is `unknown`; negative proof requires explicit documentary disclaimers. Furthermore, for offline local CLI utilities (App 98: Mermaid CLI), credential gating conditions do not apply to software operating locally without user accounts.

| App ID & Name | Claim ID | First-Pass State | Baseline Human Judgment | Corrected State | Correction Rationale |
| --- | --- | --- | --- | --- | --- |
| **31. Google Ads** | `31.testing.vendor_approval_required` | `observed` (false) | `unsupported` | `unknown` (null) | Silence mistaken for negative proof; documentation does not explicitly disclaim vendor approval. |
| **83. Binance** | `83.testing.vendor_approval_required` | `observed` (false) | `unsupported` | `unknown` (null) | Self-serve Spot Testnet key creation does not explicitly prove absence of vendor approval gating. |
| **83. Binance** | `83.testing.partner_approval_required` | `observed` (false) | `unsupported` | `unknown` (null) | No explicit vendor text disclaiming partner gating. Silence is unknown. |
| **83. Binance** | `83.testing.contact_sales_required` | `observed` (false) | `unsupported` | `unknown` (null) | No explicit vendor text disclaiming sales requirements. Silence is unknown. |
| **83. Binance** | `83.production.sandbox_access` | `observed` (false) | `unsupported` | `unknown` (null) | Host separation between api.binance.com and testnet does not conclusively prove absence of sandbox access. |
| **98. Mermaid CLI** | `98.testing.admin_approval_required` | `observed` (false) | `unsupported` | `not_applicable` (null) | Offline local CLI utility (@mermaid-js/mermaid-cli); credential conditions do not apply to local software. |
| **98. Mermaid CLI** | `98.testing.vendor_approval_required` | `observed` (false) | `unsupported` | `not_applicable` (null) | Open-source MIT licensed CLI utility; credential conditions do not apply to local software. |
| **98. Mermaid CLI** | `98.testing.partner_approval_required` | `observed` (false) | `unsupported` | `not_applicable` (null) | Open-source MIT licensed CLI utility; credential conditions do not apply to local software. |
| **98. Mermaid CLI** | `98.testing.contact_sales_required` | `observed` (false) | `unsupported` | `not_applicable` (null) | Open-source MIT licensed CLI utility; credential conditions do not apply to local software. |
| **98. Mermaid CLI** | `98.production.admin_approval_required` | `observed` (false) | `unsupported` | `not_applicable` (null) | Open-source MIT licensed CLI utility; credential conditions do not apply to local software. |
| **98. Mermaid CLI** | `98.production.vendor_approval_required` | `observed` (false) | `unsupported` | `not_applicable` (null) | Open-source MIT licensed CLI utility; credential conditions do not apply to local software. |
| **98. Mermaid CLI** | `98.production.partner_approval_required` | `observed` (false) | `unsupported` | `not_applicable` (null) | Open-source MIT licensed CLI utility; credential conditions do not apply to local software. |
| **98. Mermaid CLI** | `98.production.contact_sales_required` | `observed` (false) | `unsupported` | `not_applicable` (null) | Open-source MIT licensed CLI utility; credential conditions do not apply to local software. |

### B. Inferred Assertions Grounding & Scope Rationale (37 Claims)
In Task 17 baseline audit, all 37 inferred claims (`api.breadth` and `buildability`) were adjudicated `unsupported` because the reviewer found that 'The assertion is inferred rather than a directly documented vendor statement.' In Phase A, these 37 claims have been strengthened and anchored directly to the vendor's documented top-level functional domain taxonomy and the verified prerequisite chain (`supporting_claim_refs`) per `docs/evidence-rules.md`.

| App ID & Name | Claim ID | Value | Rationale Grounding |
| --- | --- | --- | --- |
| **4. Attio** | `4.api.breadth` | `broad` | Anchored to Attio API reference defining 4 distinct domains: CRM Records, Collaboration/Tasks, Activities, and SCIM/Webhooks. |
| **4. Attio** | `4.buildability` | `build_now` | Anchored to verified prerequisite chain: free self-serve workspace, public REST API, and official hosted MCP server with 0 blockers. |
| **8. Close** | `8.api.breadth` | `broad` | Anchored to Close docs defining Leads/Contacts, Multi-channel Comm, Sequences, and Analytics. |
| **8. Close** | `8.buildability` | `conditional` | Anchored to verified pricing and OAuth/API key docs: functional REST/MCP requires active paid CRM plan ($49+/seat/mo). |
| **16. LiveAgent** | `16.api.breadth` | `narrow` | Anchored to LiveAgent v1 reference focused exclusively on helpdesk ticket/conversation and department management. |
| **16. LiveAgent** | `16.buildability` | `build_now` | Anchored to built-in MCP server support and self-serve API key generation on free trial or paid accounts. |
| **19. Gorgias** | `19.api.breadth` | `broad` | Anchored to Gorgias API spanning Tickets/Messages, Customers, Ecommerce Store Data, and HTTP Webhooks. |
| **19. Gorgias** | `19.buildability` | `conditional` | Anchored to verified prerequisite chain: REST API and OAuth 2.0 app registration require active paid helpdesk account. |
| **21. Slack** | `21.api.breadth` | `broad` | Anchored to Slack Web API spanning Messaging, Users/Teams, Files/Canvases, Search, and Enterprise SCIM. |
| **21. Slack** | `21.buildability` | `build_now` | Anchored to free workspace tier, self-serve Slack app registration, Bot tokens, and full Web API methods. |
| **27. Telegram** | `27.api.breadth` | `broad` | Anchored to Telegram Bot API spanning Chat/Messaging, Inline Queries/Payments, Webhooks, and Group Administration. |
| **27. Telegram** | `27.buildability` | `build_now` | Anchored to instant self-serve bot creation via BotFather with zero approval gating or fees. |
| **31. Google Ads** | `31.api.breadth` | `broad` | Anchored to Google Ads API spanning Accounts, Campaigns/AdGroups, GAQL Reporting, Conversions, and Bidding. |
| **31. Google Ads** | `31.buildability` | `conditional` | Anchored to verified docs: Test access immediate with API enablement; production requires Explorer/Basic/Standard approval. |
| **40. SendGrid** | `40.api.breadth` | `broad` | Anchored to SendGrid v3 spanning Mail Send, Marketing Campaigns, Contacts, Subusers, and Event Webhooks. |
| **40. SendGrid** | `40.buildability` | `build_now` | Anchored to free tier (100 emails/day), self-serve API key generation with granular scopes, and public REST API. |
| **46. Squarespace** | `46.api.breadth` | `broad` | Anchored to Squarespace Commerce API spanning Orders, Inventory, Products, Transactions, and Webhooks. |
| **46. Squarespace** | `46.buildability` | `conditional` | Anchored to verified docs: Commerce APIs require active Squarespace Commerce plan (Advanced or Core). |
| **50. fanbasis** | `50.buildability` | `outreach_required` | Anchored to verified docs: Commas API and beta MCP server require contacting sales / developer waitlist. |
| **52. SE Ranking** | `52.api.breadth` | `moderate` | Anchored to SE Ranking API spanning Keyword Rank Tracking, Competitor Search Data, and Backlink Analysis. |
| **52. SE Ranking** | `52.buildability` | `build_now` | Anchored to REST API keys available on paid plans (or trial) with clear JSON endpoints for SEO data. |
| **60. Clay** | `60.api.breadth` | `moderate` | Anchored to Clay API covering Table/Record Management, Enrichment Actions, and Webhook Sources. |
| **60. Clay** | `60.buildability` | `build_now` | Anchored to self-serve API keys on Pro/Enterprise or trial for automating table enrichment runs. |
| **64. Cloudflare** | `64.api.breadth` | `broad` | Anchored to Cloudflare v4 spanning DNS, Workers/Pages, Storage (KV/R2), WAF, and Zero Trust. |
| **64. Cloudflare** | `64.buildability` | `conditional` | Anchored to Free tier accounts supporting scoped API tokens for DNS/Workers; enterprise features gated. |
| **65. Supabase** | `65.api.breadth` | `moderate` | Anchored to Supabase modules: PostgreSQL Database, GoTrue Auth, Storage, and Edge Functions. |
| **65. Supabase** | `65.buildability` | `conditional` | Anchored to Free plan (up to 2 active projects), instant project API keys, and community MCP server. |
| **76. Monday.com** | `76.api.breadth` | `moderate` | Anchored to Monday.com GraphQL spanning Boards/Workspaces, Items/Columns, Updates, and Users/Teams. |
| **76. Monday.com** | `76.buildability` | `conditional` | Anchored to personal API tokens and OAuth 2.0 apps gated by workspace permission scopes and plan tiers. |
| **77. ClickUp** | `77.api.breadth` | `moderate` | Anchored to ClickUp REST API v2 spanning Workspaces/Folders, Lists/Tasks, Time Tracking, and Comments. |
| **77. ClickUp** | `77.buildability` | `conditional` | Anchored to Free Forever plan including API access with personal API keys or OAuth 2.0. |
| **83. Binance** | `83.api.breadth` | `broad` | Anchored to Binance Spot API spanning Market Data, Spot Order Execution, Account Balances, and WebSockets. |
| **83. Binance** | `83.buildability` | `conditional` | Anchored to public market data open without auth; signed trading requires KYC and regional availability. |
| **97. Higgsfield** | `97.api.breadth` | `moderate` | Anchored to Higgsfield API focused on Generation Tasks, Status/Asset Polling, and Model Configs. |
| **97. Higgsfield** | `97.buildability` | `conditional` | Anchored to REST API and CLI requiring paid API credits ($5+ credit pack) and API key auth. |
| **98. Mermaid CLI** | `98.api.breadth` | `narrow` | Anchored to @mermaid-js/mermaid-cli focused exclusively on rendering .mmd definitions to SVG/PNG/PDF. |
| **98. Mermaid CLI** | `98.buildability` | `build_now` | Anchored to open-source MIT license, local npm/npx execution (mmdc), Node.js run() API, and 0 gating. |

---

## 2. Denominator and Inventory Invariance
- **Fixed Question Denominator (N)**: `327` claims.
- No claims were added, deleted, or split.
- The denominator for paired before/after remeasurement remains strictly identical to the Task 17 baseline.