# Task 09: Exceptions List for Independent Reviewer

Prepared for independent review of `work/research-runs/task09-first-pass-004` (Communications and Messaging, IDs 21–30). No correctness judgments are made here.

1. **Lark / Larksuite (ID 24) — 1-Line JS Shells on `open.larksuite.com` and `larksuite.com/en_us/plans`**:
   - `open.larksuite.com/document/home/index`, `open.larksuite.com/.../tenant_access_token_internal`, and `www.larksuite.com/en_us/plans` returned 1-line client-side JS shells to HTTP capture. None of those 3 snapshots are cited.
   - All Lark claims are grounded in official `github.com/larksuite/*` repositories (`lark-openapi-mcp`, `oapi-sdk-python`, `node-sdk`). Because the pricing page was a JS shell, `free_access`, `trial_access`, and `paid_required` remain `unknown`.
2. **Pumble (ID 25) — `pumble.com/pricing/` 404 & Product-Page-Only Official MCP Announcement**:
   - `https://pumble.com/pricing/` and `https://github.com/CAKE-com/pumble-sdk` returned HTTP `404` (replaced by `pumble.com/`, `pumble.com/help/`, and `github.com/CAKE-com/pumble-node-sdk`).
   - `25.mcp.official` records the official MCP server announcement on `pumble.com/` (`server_url: null`, `repository_url: null` since no endpoint URL or technical spec was captured) alongside community server `github.com/infralayers/pumble-mcp` (`origin: community`).
3. **Aircall (ID 29) — Outbound MCP Client vs. Callable MCP Server Distinction**:
   - Checked Aircall developer docs (`developer.aircall.io/`, `developer.aircall.io/tutorials/oauth/`, `developer.aircall.io/docs/aircall-ai/llms.txt`) document outbound MCP client integration (Aircall AI Virtual Agents calling external partner MCP servers, marked 'Coming soon') rather than a callable Aircall MCP server. Per Contract v1.1, `29.mcp` is recorded as `not_found_in_checked_sources` rather than promoting an outbound MCP client as a callable server.
   - `29.testing.partner_approval_required=true` and `29.production.partner_approval_required=true` reflect Aircall's form-gated Technology Partner onboarding for OAuth `client_id`/`client_secret` and developer sandboxes (whereas single-company customer Basic Auth is self-serve on paid accounts).
4. **WhatsApp Business (ID 28) — Dual-Path App Review & Community-Only MCP Capture**:
   - `28.production.vendor_approval_required=true` applies to multi-tenant Tech Provider apps needing Advanced Access via Meta App Review (plus template approval), while Direct Developers receive automatic Standard Access (`28.production.self_serve=true`).
   - No official Meta WhatsApp MCP doc page appeared in the captured `whatsapp/llms.txt` index; `28.mcp` cites community Cloud API repo `github.com/tkhattar14/whatsapp-business-mcp` (`origin: community`, targeting `graph.facebook.com`).
5. **Slack (ID 21) — Dual-Path Marketplace Approval & No DCR on Official MCP**:
   - `21.production.vendor_approval_required=true` reflects Slack Marketplace review for published multi-tenant apps (and Slack's rule that unlisted apps cannot use `https://mcp.slack.com/mcp`), while internal workspace apps are self-serve (`21.production.self_serve=true`).
6. **Discord (ID 26) — Partner-Only OAuth2 Scopes & No Dedicated Pricing Page Captured**:
   - `26.production.partner_approval_required=true` reflects Discord's documented partner-only OAuth2 scopes (`dm_channels.read`, `rpc.*`, `voice`, etc.), while standard bot/OAuth2 scopes are self-serve. `free_access` / `paid_required` remain `unknown` because no dedicated Discord developer billing/pricing page was captured.
7. **Zoho Cliq (ID 23) — `oauth.html` 404 & Multi-Datacenter Routing**:
   - `www.zoho.com/cliq/help/restapi/v2/oauth.html` returned HTTP `404`, but the 10,572-line `www.zoho.com/cliq/help/restapi/v2/` page contains the full OAuth 2.0 specification and OAS 3.0 YAML links across 9 regional Zoho domains. MCP records community repo `github.com/rohansen856/cliq-mcp` (`origin: community`).
8. **Telegram (ID 27) — Bot API vs. MTProto Dual Surface & Community MCPs**:
   - Captures both Bot API v10.5 (`core.telegram.org/bots/api`, 14,067 lines) and MTProto/TDLib (`core.telegram.org/api`) with separate community MCP servers for each (`node2flow-th/telegram-bot-mcp-community` for Bot API; `sparfenyuk/mcp-telegram` for MTProto user-account read/draft).
9. **Vonage (ID 30) — Official API Bindings + Docs MCP & Beta Messages API Label**:
   - Captures both `github.com/Vonage-Community/vonage-mcp-server-api-bindings` and `github.com/Vonage/vonage-kiro-power` (referencing `vonage-api` and `vonage-docs` MCP servers). Notes `developer.vonage.com/en/api` still labels Messages API as Beta while SMS API is stable.
10. **Operational Checks Unresearched**:
    - All 12 nested MCP `operational_check` claims across IDs 21–30 remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).
