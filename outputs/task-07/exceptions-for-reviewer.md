# Task 07: Exceptions List for Independent Reviewer

Prepared for independent review of `work/research-runs/task07-first-pass-003` (CRM and Sales, IDs 1–10). No correctness judgments are made here.

1. **Salesforce (ID 1) — HTTP 403 Bot-Block on `developer.salesforce.com` & Local MCP EOL**:
   - Five `developer.salesforce.com` / `salesforce.com/form/developer-signup/` URLs returned HTTP `403` (`blocked`), and `help.salesforce.com` returned a 5-line JS loading shell. Consequently, Salesforce OAuth 2.0 Connected App / External Client App flows and exact edition-level API gating (e.g., Professional add-on vs. Enterprise/Developer Edition) could not be cited from captured primary docs and remain `unknown`.
   - Captured `github.com/salesforcecli/mcp` documents that the official local Salesforce DX MCP server (`@salesforce/mcp`) reached **End of Life on November 2, 2026**; Salesforce hosted MCP server documentation was not capturable due to the `developer.salesforce.com` 403.
2. **HubSpot (ID 2) — Pricing JS Shell & Legacy Private App Sunset**:
   - `www.hubspot.com/pricing/crm` returned a 1-line JS shell (`Free Tools | HubSpot`). `2.production.admin_approval_required` is now grounded in current `working-with-oauth` (Super Admin / Marketplace Access) plus legacy private apps, while `2.production.free_access` and `2.production.paid_required` remain explicitly scoped to existing legacy private apps (new creation ended 2026-10-26).
3. **Pipedrive (ID 3) — Pricing HTTP 403 & Native MCP Doc Not Captured**:
   - `www.pipedrive.com/en/pricing` returned HTTP `403` (`blocked`), so production paid/free tier thresholds remain `unknown`.
   - Community MCP repository `github.com/Wirasm/pipedrive-mcp` was captured (`origin: community`). Although search leads indicate a native Pipedrive MCP connector, no primary vendor MCP doc URL was captured in `task07-capture-004`, so no official Pipedrive MCP claim was promoted.
4. **Twenty (ID 5) — Community MCP Only & Self-Hosted vs. Cloud Scope**:
   - `github.com/jezweb/twenty-mcp` (`origin: community`) is recorded for MCP; no official Twenty MCP doc page was captured in `task07-capture-004`.
   - Production `free_access=true` / `paid_required=false` explicitly reflect open-source self-hosting (`github.com/twentyhq/twenty`), whereas Twenty Cloud production plans are paid (Pro `$9/user/mo+`). Reviewer should verify scope clarity.
5. **Podio (ID 6) — Bounded MCP Not Found**:
   - `6.mcp` is `not_found_in_checked_sources` across official Podio developer/pricing docs; reviewer should confirm this bounded negative is not over-claimed as universal absence.
6. **Zoho CRM (ID 7) — Sandbox KB Capture Failure**:
   - `help.zoho.com/.../sandbox-overview` failed with `Capture failed: empty_readable_content`, so `7.testing.sandbox_access` remains `unknown` (testing is supported via Free Edition and paid-edition trials).
7. **Close (ID 8) — Paid Production & Vendor Public-OAuth Approval**:
   - `8.production.vendor_approval_required=true` uses the new v1.1 field for Close's public OAuth app publication process (`create-an-oauth-app.md` lines 20–21: private by default; making public requires requesting publication). Reviewer should verify this distinction against `partner_approval_required`.
8. **Copper (ID 9) — OAuth & MCP Blog 404s**:
   - `developer.copper.com/oauth/overview.html` and `www.copper.com/blog/copper-mcp-server` returned HTTP `404`. OAuth 2.0 existence is confirmed from `introduction/authentication.html`, while `9.mcp` remains `not_found_in_checked_sources`.
9. **DealCloud (ID 10) — REST Auth Subpage 404s & Enterprise Gating**:
   - `api.docs.dealcloud.com` REST `api-keys` and `authorization-token` subpages returned HTTP `404`, so REST token-exchange details remain `unknown` while MCP OAuth 2.0 (`.well-known` discovery, user-scoped permissions, Celeste license + admin capability) is observed from `mcp/getting-started` and `mcp/authentication`.
10. **Operational Checks Unresearched**:
   - All 8 nested MCP `operational_check` claims remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).
