# Task 08: Exceptions List for Independent Reviewer

Prepared for independent review of `work/research-runs/task08-first-pass-003` (Support and Helpdesk, IDs 11–20). No correctness judgments are made here.

1. **Help Scout (ID 18) — Compressed Binary Responses on `developer.helpscout.com` & MCP Blog 404**:
   - All four `developer.helpscout.com` URLs (`/`, `/mailbox-api/`, `/mailbox-api/overview/authentication/`, `/docs-api/`) returned HTTP `200` with compressed binary payloads that `research_pipeline.py`'s `urllib` collector did not decompress, yielding unreadable snapshots. None of those 4 snapshots are cited in any claim.
   - `www.helpscout.com/blog/mcp-server/` returned HTTP `404`. Consequently, only readable `www.helpscout.com/pricing/` evidence is cited (`18.identity`, `18.purpose`, `18.auth.oauth_apps`, `18.api.protocol.api_access`, pricing/trial eligibility, and `conditional` buildability), while `api.public_docs`, `resource_groups`, `api.breadth`, and `mcp.discovery` remain `unknown`. This is a collector/content-encoding limitation to flag for future pipeline handling.
2. **Zendesk (ID 11) — Official MCP Client Article 404 & Community MCP Server Scope**:
   - `support.zendesk.com/hc/en-us/articles/8244243105178-...` (Zendesk MCP client) returned HTTP `404` and `4408828617370-Testing-changes-in-your-sandbox` returned a 14-line shell. Zendesk's sandbox availability is cited from `www.zendesk.com/pricing/` (Suite Enterprise + Copilot), and MCP discovery cites community repo `github.com/reminia/zendesk-mcp-server` (`origin: community`, not vendor-endorsed). No official Zendesk MCP server claim was promoted.
3. **Intercom (ID 12) — Vendor App Store Review vs. Private Self-Serve Scope**:
   - `12.production.vendor_approval_required=true` (contract v1.1) applies specifically to public multi-tenant OAuth apps submitted to the Intercom App Store, whereas private workspace Access Token apps are self-serve without review (`12.production.self_serve=true`). Reviewer should verify this dual-path scope clarity.
4. **Freshdesk (ID 13) — Pilot Refresh & Tenant-Templated MCP URL**:
   - Resolves the Task 04 pilot capture gap by capturing `developers.freshdesk.com/api/` (31,897 lines) under `--max-bytes 10000000`. Because the official Freshdesk MCP endpoint is tenant-templated (`https://<subdomain>.freshdesk.com/mcp`), `server_url` is set to `null` (to satisfy strict URI format validation) with the exact template documented in `scope`.
5. **Front (ID 14) — Dual Official MCP Servers & No DCR**:
   - Records two distinct official hosted MCP servers (`https://mcp.frontapp.com/mcp` for user-scoped conversations and `https://mcp.frontapp.com/admin-mcp` open beta for admin configuration), both requiring confidential OAuth 2.1 + PKCE (no Dynamic Client Registration).
6. **Pylon (ID 15) — No Public Free Trial / Self-Serve Checkout Captured**:
   - `usepylon.com/pricing` lists annual per-seat contracts ($89/$139/Enterprise) without a public free tier or cardless trial CTA; testing `free_access` / `trial_access` / `self_serve` remain `unknown`, leading to `conditional` buildability.
7. **LiveAgent (ID 16) — `liveagent.com/api/` 404 & v1 vs. Tenant-Hosted v3 Docs**:
   - `www.liveagent.com/api/` returned HTTP `404`. The captured `support.liveagent.com/061754-Complete-API-reference` reflects REST API v1 PHP examples (`narrow` breadth from captured public text), while LiveAgent's v3 Swagger/OpenAPI reference is tenant-hosted. Built-in MCP server (`https://<your-liveagent-domain>/api/mcp`) is captured from `support.liveagent.com/647358-MCP-Integration-for-Agents` with `server_url: null` (tenant-templated).
8. **Gorgias (ID 19) — Partner Approval for Sandbox/OAuth & Community MCP Only**:
   - `19.testing.partner_approval_required=true` and `19.production.partner_approval_required=true` reflect explicit `techpartners@gorgias.com` Sandbox conversion and tech partnership team review. MCP records community repo `github.com/mattcoatsworth/Gorgias-MCP-Server` (`origin: community`); no official Gorgias MCP doc was captured in `developers.gorgias.com/llms.txt`.
9. **Gladly (ID 20) — Help Subpage 404s & Bounded MCP Not Found**:
   - `developer.gladly.com/lookup/` and two `help.gladly.com` articles returned HTTP `404`, but the 5,595-line `developer.gladly.com/rest/` ReDoc snapshot fully documents REST API, Lookup API, `.gladly.qa` sandbox, and Admin-gated API User Basic auth. `20.mcp` is `not_found_in_checked_sources` (bounded to checked Gladly docs; does not prove no MCP exists).
10. **Operational Checks Unresearched**:
   - All 9 nested MCP `operational_check` claims across IDs 11–20 remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).
