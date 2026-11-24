"""Task 15 researcher-authored extraction (Finance and Fintech, IDs 81-90, contract v1.1).

Every claim and paraphrase was authored after directly reading the captured snapshots in
work/research-runs/task15-capture-005. No model API, synthetic fixture, authenticated account
operation, independent review, or accuracy measurement occurs here.
"""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import research_pipeline as p

SCOPES_RAW = json.loads((ROOT / "work/task-15-agent/scopes.json").read_text(encoding="utf-8"))
SCOPES = {int(k): v for k, v in SCOPES_RAW.items()}


def build(capture_run: str, destination: Path):
    directory = ROOT / "work/research-runs" / capture_run
    p.verify_seal(directory)
    records = copy.deepcopy(p.read_json(directory / "records.json"))
    captures = p.read_json(directory / "captures.json")

    by_app_url = {}
    for c in captures:
        by_app_url[(c["spec"]["app_id"], c["spec"]["url"])] = c

    def find_cap(app_id: int, substr: str):
        exact = [c for (aid, u), c in by_app_url.items() if aid == app_id and u.endswith(substr)]
        if len(exact) == 1:
            return exact[0]
        matches = [c for (aid, u), c in by_app_url.items() if aid == app_id and substr in u]
        assert len(matches) == 1, f"Expected 1 match for ({app_id}, {substr!r}), got {len(matches)}: {[c['spec']['url'] for c in matches]}"
        return matches[0]

    for r in records:
        app = r["identity"]["id"]
        scope = SCOPES[app]

        def E(substr: str, first: int, last: int, para: str):
            c = find_cap(app, substr)
            lines = (directory / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
            assert 1 <= first <= last <= len(lines), (app, substr, first, last, len(lines))
            e = p.evidence_for(c, first, lines[first - 1])
            e.update(locator=f"lines:{first}-{last}", observation="paraphrase: " + para)
            return e

        def claim(key, value, ev=(), status="observed", refs=(),
                  rationale="Documentary observation only; independent review pending."):
            return {
                "claim_id": f"{app}.{key}",
                "status": status,
                "value": value,
                "context": scope,
                "evidence": list(ev),
                "supporting_claim_refs": [f"{app}.{x}" for x in refs],
                "rationale": rationale,
            }

        def auth(key, method, details, ev, subcontext, scopes=(), status="observed", refs=()):
            return claim(
                "auth." + key,
                {"method": method, "context": subcontext, "scopes": list(scopes), "details": details},
                ev,
                status,
                refs,
                "Scoped authentication mechanism from primary documentation; no credentials obtained or authenticated calls executed.",
            )

        def items(target, entries, notes, cov="checked_sources"):
            target.update(coverage_status=cov, items=entries, notes=notes)

        def elig(env, key, val, ev, rationale, status="observed", refs=()):
            r["credential_eligibility"][env][key] = claim(f"{env}.{key}", val, ev, status, refs, rationale)

        def unknown_elig(env, key, rationale):
            r["credential_eligibility"][env][key] = claim(f"{env}.{key}", None, (), "unknown", (), rationale)

        def group(key, value, ev):
            return claim("api.group." + key, value, ev)

        def breadth(value, groups, ev, reason):
            r["api_surface"]["breadth"] = claim(
                "api.breadth", value, ev, "inferred", ["api.group." + g for g in groups], reason
            )

        def set_mcp_entries(entries_spec, discovery_ev):
            out = []
            for key, origin, name, ev, substr, tool_scope, server, repo in entries_spec:
                op = claim(
                    f"mcp.{key}.operational",
                    None,
                    status="not_researched",
                    rationale="No MCP connection or tool call was attempted.",
                )
                c = find_cap(app, substr)
                out.append(claim(
                    "mcp." + key,
                    {
                        "origin": origin,
                        "name": name,
                        "source_url": c["spec"]["url"],
                        "repository_url": repo,
                        "server_url": server,
                        "scope": tool_scope,
                        "operational_check": op,
                    },
                    ev,
                    "observed",
                    (),
                    "Documentary MCP server listing only; operational execution remains not_researched.",
                ))
            r["mcp"]["discovery"] = claim("mcp.discovery", "found", discovery_ev, "observed")
            r["mcp"]["entries"] = out

        def set_build(verdict, bscope, blockers, next_steps, refs, ev, rationale):
            r["buildability"] = claim(
                "buildability",
                {"verdict": verdict, "scope": bscope, "blockers": blockers, "next_steps": next_steps},
                ev,
                "inferred",
                refs,
                rationale,
            )

        r["credential_eligibility"]["testing"]["context"] = scope
        r["credential_eligibility"]["production"]["context"] = scope

        # =====================================================================
        # 81: Stripe
        # =====================================================================
        if app == 81:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                "Stripe payments and financial infrastructure platform API (https://api.stripe.com) and Stripe MCP server (https://mcp.stripe.com).",
                [
                    E("/api", 155, 165, "Stripe API Reference documents the REST API at https://api.stripe.com."),
                    E("/mcp", 69, 100, "Stripe MCP docs describe the official hosted MCP server at https://mcp.stripe.com."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Payments, billing, Connect marketplace, and financial infrastructure platform with REST API, SDKs, CLI, and hosted MCP server.",
                [
                    E("/api", 17, 156, "Stripe API Reference covers core payments, billing, Connect, Issuing, Treasury, and REST endpoints."),
                    E("/mcp", 69, 99, "Stripe provides a hosted MCP server for AI agents to interact with the Stripe API."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "api_keys",
                        "API_key",
                        "Secret (sk_test_/sk_live_), Restricted (rk_test_/rk_live_, including agent-tagged RAKs with approval rules), Publishable (pk_*), and Organisation (sk_org_*) API keys passed via HTTP Basic Auth username or Authorization: Bearer header.",
                        [
                            E("/api/authentication", 155, 161, "Stripe API uses API keys (sk_test_, rk_live_, sk_live_) via HTTP Basic Auth or Bearer header over HTTPS."),
                            E("/keys", 97, 120, "Documents publishable, restricted, secret, organisation, and agent-tagged restricted API keys."),
                        ],
                        "Account-level or organisation-level server-side and client-side REST API requests.",
                    ),
                    auth(
                        "workload_identity_federation",
                        "Bearer_token",
                        "Workload Identity Federation exchanges a short-lived cloud provider identity token for a 1-hour Stripe access token.",
                        [E("/api/authentication", 158, 158, "Workload Identity Federation exchanges a cloud identity token for a 1-hour Stripe access token.")],
                        "Server-to-server cloud workloads avoiding long-lived API keys.",
                    ),
                    auth(
                        "connect_oauth2",
                        "OAuth2",
                        "Stripe Connect OAuth 2.0 Authorization Code and Refresh Token grants at connect.stripe.com/oauth/authorize and /oauth/token for platform access to Standard connected accounts.",
                        [E("/connect/oauth-reference", 44, 51, "Documents Connect OAuth authorize endpoint with response_type=code and read_write/read_only scopes."),
                         E("/connect/oauth-reference", 101, 137, "Documents Connect OAuth token exchange for authorization_code and refresh_token grants.")],
                        "Multi-tenant Connect platforms linking Standard connected Stripe accounts.",
                        scopes=["read_write", "read_only"],
                    ),
                    auth(
                        "mcp_oauth2",
                        "OAuth2",
                        "Interactive OAuth user consent for Stripe MCP server with 14-day refresh token session expiry; autonomous MCP clients use agent API keys as Bearer tokens.",
                        [E("/mcp", 103, 108, "Stripe MCP supports OAuth for user-delegated access (14-day session expiry) and agent API keys."),
                         E("/mcp", 126, 129, "Interactive MCP clients use OAuth; autonomous clients use agent API keys as Bearer tokens.")],
                        "Hosted Stripe MCP server (https://mcp.stripe.com); connected-account MCP requires agent API key plus Stripe-Account header.",
                    ),
                ],
                "Checked official Stripe API authentication, keys, Connect OAuth, and MCP docs.",
            )
            # Testing eligibility
            elig("testing", "free_access", True, [E("/testing", 73, 75, "Sandboxes simulate transactions with test values without moving funds."), E("/get-started/account/activate", 66, 66, "After creating a Stripe account, users can test Stripe services in a sandbox.")], "Free sandbox testing available immediately after creating a Stripe account.")
            unknown_elig("testing", "trial_access", "Stripe uses persistent free sandboxes rather than a time-limited API trial; trial applicability not separately stated.")
            elig("testing", "sandbox_access", True, [E("/api", 156, 156, "Stripe API supports isolated sandboxes without affecting live data."), E("/keys", 97, 97, "Sandboxes provide pk_test_, rk_test_, and sk_test_ keys.")], "Dedicated sandbox environments with isolated test keys.")
            elig("testing", "paid_required", False, [E("/testing", 73, 74, "Sandbox transactions simulate payments and do not move funds."), E("/get-started/account/activate", 66, 66, "Testing in a sandbox is available right after creating an account before live activation.")], "No payment required for sandbox testing.")
            unknown_elig("testing", "admin_approval_required", "Individual developer accounts can use sandboxes directly; within an organisation, an Administrator can enable or disable MCP access for team members in sandbox and live modes (mcp L110-111).")
            elig("testing", "vendor_approval_required", False, [E("/get-started/account/activate", 66, 66, "Users can test Stripe services in a sandbox immediately after creating an account; business verification applies to live mode.")], "No vendor approval needed for sandbox testing.")
            elig("testing", "partner_approval_required", False, [E("/get-started/account/activate", 66, 66, "Standard account creation enables sandbox testing without partner approval.")], "No partner approval needed for sandbox testing.")
            elig("testing", "contact_sales_required", False, [E("/get-started/account/activate", 61, 66, "Developers create an account and test in a sandbox self-serve.")], "No sales contact needed for sandbox testing.")
            elig("testing", "self_serve", True, [E("/keys", 93, 97, "Developers create and manage sandbox keys directly in the Stripe Dashboard."), E("/get-started/account/activate", 61, 66, "Account creation and sandbox testing are self-serve.")], "Self-serve sandbox creation and API key generation.")
            # Production eligibility
            unknown_elig("production", "free_access", "Standard Stripe pricing has no setup or monthly fees, but live payment processing incurs per-transaction fees (stripe.com/pricing L257-260).")
            unknown_elig("production", "trial_access", "No live-mode free trial documented; testing occurs in sandboxes.")
            elig("production", "sandbox_access", False, [E("/keys", 112, 115, "Live mode uses live keys and processes real money, distinct from sandboxes.")], "Production live mode is strictly separated from sandboxes.")
            unknown_elig("production", "paid_required", "No upfront or monthly fee on Standard pay-as-you-go pricing, though live payment transactions incur per-transaction fees (stripe.com/pricing L257-260).")
            unknown_elig("production", "admin_approval_required", "In multi-user Stripe organisations, Administrators control team MCP access and session revocation (mcp L110-124); single-owner accounts act as their own admin.")
            elig("production", "vendor_approval_required", True, [E("/get-started/account/activate", 55, 68, "Using Stripe services in live mode requires verifying business information and completing KYC activation review by Stripe.")], "Stripe KYC/business verification review is required to activate live-mode services.")
            elig("production", "partner_approval_required", False, [E("/get-started/account/activate", 60, 66, "Standard live activation is a business KYC onboarding flow rather than a commercial partner program.")], "Commercial partner approval is not required for standard live accounts.")
            elig("production", "contact_sales_required", False, [E("/get-started/account/activate", 60, 66, "Standard live account activation is completed in the Dashboard."), E("/pricing", 257, 258, "Standard pricing is pay-as-you-go without custom enterprise sales gating.")], "Standard live accounts do not require contacting sales.")
            elig("production", "self_serve", True, [E("/get-started/account/activate", 60, 66, "Developers create an account and submit business verification in the Dashboard to activate live mode."), E("/keys", 208, 217, "Live keys are revealed and managed in the Dashboard.")], "Self-serve Dashboard onboarding and live key management, subject to KYC verification.")
            # API surface
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("/api", 155, 165, "Stripe API is organized around REST with JSON responses over HTTPS at https://api.stripe.com.")]),
                    claim("api.protocol.sdk", "SDK", [E("/api", 166, 174, "Official client libraries documented for Ruby, Python, PHP, Java, Node.js, Go, and .NET.")]),
                    claim("api.protocol.cli", "CLI", [E("/mcp", 72, 82, "Stripe CLI is documented for installation and agent setup."), E("/testing", 98, 98, "Stripe CLI is listed alongside cURL and SDKs for API testing.")]),
                ],
                "REST API, official multi-language SDKs, and Stripe CLI documented.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("/api", 1, 165, "Stripe API Reference is publicly readable without login.")])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("core_payments", "Core Payments & Customers (Charges, Customers, Payment Intents, Payment Methods, Payouts, Refunds, Disputes)", [E("/api", 17, 54, "API Reference lists Core Resources and Payment Methods including Charges, Customers, Payment Intents, Payouts, Refunds, and Disputes.")]),
                    group("billing_products", "Products, Checkout & Billing (Products, Prices, Checkout Sessions, Invoices, Subscriptions, Billing Meters, Quotes)", [E("/api", 56, 103, "API Reference lists Products, Checkout, Payment Links, and Billing resources including Invoices, Subscriptions, and Meters.")]),
                    group("connect_platforms", "Connect & Platforms (Connected Accounts, Account Links, Transfers, Application Fees, Payouts)", [E("/api", 107, 125, "API Reference lists Connect resources including Accounts, Account Links, Application Fees, and Transfers.")]),
                    group("financial_data_risk", "Financial Services, Risk & Data (Issuing, Terminal, Treasury, Financial Connections, Tax, Identity, Fraud, Sigma, Reporting, Webhooks)", [E("/api", 126, 145, "API Reference lists Fraud, Issuing, Terminal, Treasury, Sigma, Reporting, Financial Connections, Tax, Identity, and Webhooks.")]),
                ],
                "Four major domain groupings captured from the Stripe API Reference navigation.",
            )
            breadth("broad", ["core_payments", "billing_products", "connect_platforms", "financial_data_risk"], [E("/api", 17, 145, "Stripe API spans core payments, billing, Connect marketplaces, issuing, treasury, tax, identity, and analytics.")], "Broad multi-domain financial infrastructure API covering payments, subscriptions, marketplaces, cards/treasury, and reporting.")
            set_mcp_entries(
                [("official_stripe_mcp", "official", "Stripe MCP Server", [E("/mcp", 69, 106, "Official Stripe hosted MCP server at https://mcp.stripe.com supporting OAuth and agent API keys."), E("/mcp", 130, 155, "Exposes callable API search/read/write, account, analytics, treasury, and documentation tools.")], "/mcp", "Official hosted callable MCP server (Public preview) exposing Stripe API read/write, account, analytics, Treasury, and docs search tools via OAuth or agent API keys.", "https://mcp.stripe.com", None)],
                [E("/mcp", 63, 100, "Official Stripe MCP server documented at https://mcp.stripe.com.")],
            )
            set_build(
                "build_now",
                "Stripe REST API and official hosted MCP server for sandbox development and verified live-mode payment/billing workflows.",
                ["Live-mode activation requires KYC/business verification and supported country eligibility.", "Starting January 11, 2027, Stripe MCP drops non-agent restricted/secret keys in favor of OAuth or agent API keys; sensitive MCP actions can require Dashboard human confirmation."],
                ["Use free sandbox keys (rk_test_/sk_test_) for development and testing.", "Use restricted or agent-tagged API keys (or OAuth for interactive MCP / Connect platforms) with least-privilege permissions."],
                ["identity.resolution", "auth.api_keys", "auth.connect_oauth2", "testing.sandbox_access", "testing.self_serve", "api.protocol.rest", "api.breadth", "mcp.official_stripe_mcp"],
                [E("/api", 155, 165, "Public REST API with sandboxes."), E("/mcp", 69, 106, "Official hosted callable MCP server."), E("/get-started/account/activate", 61, 67, "Self-serve sandbox and KYC live activation.")],
                "Complete public REST API, official SDKs, official hosted MCP server, and free self-serve sandboxes support immediate integration; live payment processing requires KYC activation.",
            )

        # =====================================================================
        # 82: Plaid
        # =====================================================================
        elif app == 82:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                "Plaid financial data connectivity API (sandbox.plaid.com / production.plaid.com) with official Sandbox and Dashboard MCP servers.",
                [
                    E("/docs/api/", 69, 82, "Plaid API Reference documents the JSON-over-HTTP API at sandbox.plaid.com and production.plaid.com."),
                    E("/docs/resources/mcp/", 25, 37, "Plaid documents official Dashboard and Sandbox MCP servers."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Financial account connectivity API for bank auth, transactions, balances, identity, income, payments, and underwriting, plus Sandbox and Dashboard MCP servers.",
                [
                    E("/docs/api/", 20, 56, "Plaid API Reference covers Payments/Funding, Financial Insights, KYC/AML, Credit/Underwriting, and Link/Items."),
                    E("/docs/resources/mcp/", 25, 27, "Plaid offers a remote Dashboard MCP server and a local Sandbox MCP server."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "client_id_secret",
                        "API_key",
                        "Plaid client_id and secret credentials sent in JSON POST request body or PLAID-CLIENT-ID and PLAID-SECRET HTTP headers, paired with per-Item access_token obtained via Link token exchange.",
                        [E("/docs/api/", 74, 77, "Plaid API endpoints require client_id and secret in the JSON body or PLAID-CLIENT-ID/PLAID-SECRET headers."), E("/docs/launch-checklist/", 101, 105, "Item access_tokens map users to linked financial institutions and must stay server-side.")],
                        "Plaid Sandbox and Production REST/JSON API requests.",
                    ),
                    auth(
                        "oauth2_dashboard_mcp",
                        "OAuth2",
                        "OAuth 2.0 client_credentials and refresh_token grants at https://production.plaid.com/oauth/token with scope mcp:dashboard returning 15-minute Bearer access tokens.",
                        [E("/docs/resources/mcp/", 44, 57, "Dashboard MCP uses OAuth 2.0 client_credentials grant with mcp:dashboard scope at /oauth/token."), E("/docs/resources/mcp/", 170, 179, "MCP access tokens expire after 15 minutes and refresh via refresh_token grant.")],
                        "Remote Plaid Dashboard MCP server (Production only).",
                        scopes=["mcp:dashboard"],
                    ),
                ],
                "Checked official Plaid API overview, launch checklist, and MCP docs.",
            )
            # Testing eligibility
            elig("testing", "free_access", True, [E("/docs/sandbox/", 35, 35, "Plaid Sandbox is a free and fully-featured environment for development and testing."), E("/docs/account/billing/", 97, 97, "Usage of Sandbox is always free.")], "Sandbox is always free.")
            elig("testing", "trial_access", True, [E("/docs/sandbox/", 68, 71, "Free Trial plans (US and Canada only) let new teams test many Plaid products with real production data."), E("/16110110883479-", 56, 58, "Trial plans are auto-approved for most US/CA developers and support up to 10 Production Items.")], "US/CA Trial plans provide free real-data testing up to 10 Production Items.")
            elig("testing", "sandbox_access", True, [E("/docs/sandbox/", 35, 44, "Sandbox supports unlimited test Items, test credentials, and /sandbox/public_token/create.")], "Full-featured Sandbox environment available.")
            elig("testing", "paid_required", False, [E("/docs/sandbox/", 35, 35, "Sandbox is free."), E("/16110110883479-", 19, 22, "Sandbox and Trial plan cost is Free.")], "No payment required for Sandbox or US/CA Trial.")
            unknown_elig("testing", "admin_approval_required", "Sandbox keys are available in the Dashboard for team members; internal team role restrictions not detailed in captured docs.")
            elig("testing", "vendor_approval_required", False, [E("/16110110883479-", 34, 35, "Sandbox approval requirement is None.")], "No vendor approval required for Sandbox (certain products like EU/UK Payment Initiation may require enablement ticket, sandbox L41).")
            elig("testing", "partner_approval_required", False, [E("/16110110883479-", 34, 40, "Sandbox is available to all developers with no approval required.")], "No partner approval required for Sandbox.")
            elig("testing", "contact_sales_required", False, [E("/docs/sandbox/", 35, 35, "Sandbox API keys can be obtained in the Plaid Dashboard.")], "No sales contact required for Sandbox.")
            elig("testing", "self_serve", True, [E("/docs/api/", 74, 74, "Create a Dashboard account and acknowledge terms to obtain API credentials."), E("/docs/sandbox/", 35, 35, "Obtain Sandbox keys directly in the Dashboard.")], "Self-serve Dashboard signup and Sandbox keys.")
            # Production eligibility
            elig("production", "free_access", False, [E("/16110110883479-", 16, 21, "Full Production cost is Paid (Trial plan is capped at 10 Production Items)."), E("/docs/account/billing/", 38, 42, "Full Production plans are Pay-as-you-go, Growth, or Custom.")], "Full Production is paid; free Trial is capped at 10 Items and limited to US/CA.")
            elig("production", "trial_access", True, [E("/docs/account/billing/", 39, 39, "Trial plan offers free access with a limit of 10 Production Items."), E("/docs/account/billing/", 77, 81, "US/CA Trial plans allow real production data up to 10 Items before upgrading.")], "Limited 10-Item Production Trial available in US/Canada.")
            elig("production", "sandbox_access", False, [E("/docs/api/", 80, 82, "Sandbox and Production are separate environments; Items cannot be moved between them.")], "Production is separate from Sandbox.")
            elig("production", "paid_required", True, [E("/16110110883479-", 16, 21, "Full Production is Paid."), E("/docs/account/billing/", 38, 43, "Paid plans (Pay-as-you-go, Growth, Custom) are required beyond the 10-Item Trial.")], "Paid billing required for full Production.")
            unknown_elig("production", "admin_approval_required", "Dashboard team permissions for requesting Production access are not specified in captured docs.")
            elig("production", "vendor_approval_required", True, [E("/16110110883479-", 35, 36, "Full Production approval is Required (a few business days; company + use-case info)."), E("/docs/launch-checklist/", 42, 45, "Requires Production access request, company/app profile, security questionnaire for OAuth institutions, and separate EU/UK compliance.")], "Plaid Production access approval, security questionnaire, and regional compliance are required.")
            unknown_elig("production", "partner_approval_required", "Direct customers apply for Plaid Production approval; reseller/processor partner paths are separate (billing L201-202).")
            unknown_elig("production", "contact_sales_required", "Pay-as-you-go can be requested via Dashboard, whereas Growth, Custom, and all EU/UK customers require contacting sales / Custom plans (billing L43-46).")
            elig("production", "self_serve", False, [E("/16110110883479-", 35, 36, "Full Production requires Plaid approval taking a few business days."), E("/docs/launch-checklist/", 42, 45, "Production access and EU/UK compliance require review and approval.")], "Full Production is gated on Plaid vendor approval rather than immediate self-serve.")
            # API surface
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("/docs/api/", 76, 99, "JSON over HTTPS TLS 1.2 POST API described by an official OpenAPI specification.")]),
                    claim("api.protocol.sdk", "SDK", [E("/docs/api/", 102, 103, "Official client libraries are documented."), E("/docs/resources/mcp/", 66, 82, "Official Python Plaid SDK usage demonstrated.")]),
                ],
                "JSON-over-HTTPS REST/RPC-style POST API with OpenAPI definition and official SDKs.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("/docs/api/", 69, 103, "Plaid API documentation is publicly accessible.")])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("payments_funding", "Payments & Funding (Auth, Signal & Balance, Identity, Transfer, Investments Move, Payment Initiation, Virtual Accounts)", [E("/docs/api/", 20, 27, "API Reference lists Payments and Funding product groups.")]),
                    group("financial_insights", "Financial Insights (Transactions, Investments, Liabilities, Enrich)", [E("/docs/api/", 28, 32, "API Reference lists Financial Insights product groups.")]),
                    group("kyc_underwriting", "KYC/AML & Underwriting (Identity Verification, Monitor, Consumer Report, Assets, Statements, Income, Plaid Layer)", [E("/docs/api/", 33, 43, "API Reference lists KYC/AML, Anti-fraud, and Credit/Underwriting product groups.")]),
                    group("fundamentals_link", "Fundamentals & Link (Items, Accounts, Institutions, Sandbox, Link, Users, Consent, OAuth, Webhooks)", [E("/docs/api/", 19, 19, "Webhooks documented."), E("/docs/api/", 44, 56, "Fundamentals include Items, Accounts, Institutions, Sandbox, Link, Users, Consent, OAuth, and Partnerships.")]),
                ],
                "Four major product groupings captured from the Plaid API Reference.",
            )
            breadth("broad", ["payments_funding", "financial_insights", "kyc_underwriting", "fundamentals_link"], [E("/docs/api/", 19, 56, "Plaid API spans payments, banking insights, identity/KYC, underwriting, and Link/OAuth management.")], "Broad multi-domain financial data and payments API.")
            set_mcp_entries(
                [
                    ("official_dashboard_mcp", "official", "Plaid Dashboard MCP Server", [E("/docs/resources/mcp/", 25, 38, "Remote hosted Dashboard MCP server at https://api.dashboard.plaid.com/mcp/ using Streamable HTTP; Production-approved teams only."), E("/docs/resources/mcp/", 180, 188, "Callable tools: plaid_debug_item, plaid_get_link_analytics, plaid_get_tools_introduction, plaid_get_usages, plaid_list_teams.")], "/docs/resources/mcp/", "Official hosted callable MCP server (Streamable HTTP) for Production diagnostics, Link analytics, and usage metrics; requires Production approval and OAuth mcp:dashboard token.", "https://api.dashboard.plaid.com/mcp/", None),
                    ("official_sandbox_mcp", "official", "Plaid Sandbox MCP Server (mcp-server-plaid)", [E("/sandbox/README.md", 1, 25, "Official local stdio callable MCP server in plaid/ai-coding-toolkit providing search_documentation, get_mock_data_prompt, get_sandbox_access_token, and simulate_webhook for Sandbox.")], "/sandbox/README.md", "Official local stdio callable MCP server (mcp-server-plaid) for Sandbox testing, mock data, webhooks, and docs search.", None, None),
                ],
                [E("/docs/resources/mcp/", 25, 27, "Plaid documents two official MCP servers: hosted Dashboard MCP and local Sandbox MCP.")],
            )
            set_build(
                "conditional",
                "Plaid API and official MCP servers for financial data integration (Sandbox/Trial development vs full Production launch).",
                ["Full Production access requires Plaid approval (company/use-case review), security questionnaire for OAuth institutions, and paid billing.", "EU/UK Production requires Custom plans and separate compliance review.", "Official Dashboard MCP server requires approved Production access (does not run on Sandbox)."],
                ["Develop and test immediately in free Sandbox (and official Sandbox MCP server).", "For US/CA live testing, use the 10-Item Trial plan; submit Production request and OAuth security questionnaire before commercial launch."],
                ["identity.resolution", "auth.client_id_secret", "testing.sandbox_access", "production.vendor_approval_required", "production.paid_required", "api.protocol.rest", "api.breadth", "mcp.official_dashboard_mcp", "mcp.official_sandbox_mcp"],
                [E("/docs/sandbox/", 35, 37, "Free Sandbox for development."), E("/16110110883479-", 35, 36, "Full Production requires approval."), E("/docs/resources/mcp/", 31, 32, "Dashboard MCP requires Production approval.")],
                "Immediate development is possible in free Sandbox and limited US/CA Trial, but production deployment is conditional on Plaid vendor approval, institution OAuth compliance, and paid plans.",
            )

        # =====================================================================
        # 83: Binance
        # =====================================================================
        elif app == 83:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                "Binance global Spot exchange API (https://api.binance.com and Spot Testnet https://testnet.binance.vision), documented in official repository binance/binance-spot-api-docs.",
                [
                    E("/binance-spot-api-docs/master/README.md", 1, 18, "Official Documentation for the Binance APIs and Streams covering Spot REST, WebSocket, FIX, and Testnet."),
                    E("/binance-spot-api-docs/master/rest-api.md", 78, 86, "Public Rest API for Binance base endpoints at https://api.binance.com."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Cryptocurrency exchange Spot API for public market data, account queries, and order trading across REST, WebSocket, and FIX.",
                [
                    E("/binance-spot-api-docs/master/README.md", 10, 17, "Official Spot REST API, WebSocket API/streams, FIX API, and Spot Testnet."),
                    E("/binance-spot-api-docs/master/rest-api.md", 22, 74, "Covers general exchange info, market data, trading, and account endpoints."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "public_none",
                        "none",
                        "Public market-data endpoints have security type NONE and require no API key or signature (dedicated market-data host https://data-api.binance.vision).",
                        [E("/binance-spot-api-docs/master/rest-api.md", 103, 105, "Public market data only endpoint at https://data-api.binance.vision."), E("/binance-spot-api-docs/master/rest-api.md", 232, 247, "Unspecified security type is NONE for public market data.")],
                        "Public Spot market-data endpoints.",
                    ),
                    auth(
                        "signed_api_key",
                        "API_key",
                        "API key passed in X-MBX-APIKEY header with cryptographic request signing using HMAC-SHA-256, RSA (2048-4096 bit PKCS#1 v1.5), or Ed25519 keys for SIGNED endpoints (TRADE, USER_DATA, USER_STREAM); trading permission must be explicitly enabled in API Management.",
                        [
                            E("/binance-spot-api-docs/master/rest-api.md", 99, 100, "Supports HMAC, RSA, and Ed25519 API key types."),
                            E("/binance-spot-api-docs/master/rest-api.md", 229, 250, "Secure endpoints require API key plus signature with TRADE, USER_DATA, or USER_STREAM permissions."),
                            E("/binance-spot-api-docs/master/testnet/general-info.md", 94, 195, "Documents X-MBX-APIKEY header with HMAC-SHA-256, RSA, and Ed25519 signing."),
                        ],
                        "Signed Spot account, trading, and user data stream endpoints (Production and Spot Testnet).",
                        scopes=["TRADE", "USER_DATA", "USER_STREAM"],
                    ),
                ],
                "Checked official binance/binance-spot-api-docs REST API and Testnet guides; developers.binance.com HTML pages returned empty_readable_content.",
            )
            # Testing eligibility
            elig("testing", "free_access", True, [E("/binance-spot-api-docs/master/testnet/general-info.md", 66, 71, "All users registering on Spot Test Network automatically receive virtual asset balances.")], "Spot Testnet provides free virtual balances.")
            unknown_elig("testing", "trial_access", "Spot Testnet is a persistent test network with monthly resets rather than a time-limited trial.")
            elig("testing", "sandbox_access", True, [E("/binance-spot-api-docs/master/testnet/general-info.md", 3, 16, "Dedicated Spot Test Network at https://testnet.binance.vision/api (supports /api/* only, not /sapi/*)."), E("/binance-spot-api-docs/master/README.md", 80, 83, "Spot Testnet available via API for /api/* endpoints.")], "Dedicated Spot Testnet environment.")
            elig("testing", "paid_required", False, [E("/binance-spot-api-docs/master/testnet/general-info.md", 67, 71, "Virtual assets automatically granted on registration; no real funds involved.")], "No payment required for Spot Testnet.")
            unknown_elig("testing", "admin_approval_required", "Individual developer login on testnet.binance.vision; org admin controls not documented.")
            elig("testing", "vendor_approval_required", False, [E("/binance-spot-api-docs/master/testnet/general-info.md", 3, 4, "Users log in on testnet.binance.vision and generate an API key directly.")], "No vendor approval documented for Spot Testnet.")
            elig("testing", "partner_approval_required", False, [E("/binance-spot-api-docs/master/testnet/general-info.md", 3, 4, "Open self-serve login on testnet.binance.vision.")], "No partner approval required for Spot Testnet.")
            elig("testing", "contact_sales_required", False, [E("/binance-spot-api-docs/master/testnet/general-info.md", 3, 4, "Self-serve Spot Testnet key generation.")], "No sales contact required for Spot Testnet.")
            elig("testing", "self_serve", True, [E("/binance-spot-api-docs/master/testnet/general-info.md", 3, 4, "Log in on testnet.binance.vision and generate an API key.")], "Self-serve Spot Testnet key generation.")
            # Production eligibility
            unknown_elig("production", "free_access", "Public market data is unauthenticated, but live trading/account APIs require a Binance account and incur trading commissions; KYC and regional eligibility rules are not captured in the Spot API repo.")
            unknown_elig("production", "trial_access", "Not documented in captured Spot API repository.")
            elig("production", "sandbox_access", False, [E("/binance-spot-api-docs/master/testnet/general-info.md", 8, 16, "Production api.binance.com is separate from Spot Testnet testnet.binance.vision.")], "Production is separate from Spot Testnet.")
            unknown_elig("production", "paid_required", "API key creation fee is not stated, while live Spot trades carry commissions and require funded accounts.")
            unknown_elig("production", "admin_approval_required", "Account-level API Management controls exist (rest-api.md L236-244), but enterprise workspace admin rules are not documented in captured sources.")
            unknown_elig("production", "vendor_approval_required", "Regional availability and KYC/identity verification requirements for Binance global accounts are unresolved in captured docs.")
            unknown_elig("production", "partner_approval_required", "Not documented in captured Spot API repository.")
            unknown_elig("production", "contact_sales_required", "Not documented in captured Spot API repository.")
            unknown_elig("production", "self_serve", "API keys are created on the Binance account API Management page (rest-api.md L236-244), but regional/KYC prerequisites for opening a global Binance account are not captured.")
            # API surface
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("/binance-spot-api-docs/master/rest-api.md", 78, 89, "Spot REST API returning JSON (or SBE) over HTTPS.")]),
                    claim("api.protocol.other", "other", [E("/binance-spot-api-docs/master/README.md", 11, 16, "Official WebSocket API, WebSocket market/user streams, SBE streams, and FIX API.")]),
                    claim("api.protocol.sdk", "SDK", [E("/binance-spot-api-docs/master/README.md", 65, 77, "Official lightweight connector SDKs for Python, Node.js, Ruby, .NET, Java, Rust, PHP, Go, TypeScript, and Python FIX.")]),
                ],
                "REST, WebSocket API/streams, FIX, SBE, and official multi-language connectors documented.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("/binance-spot-api-docs/master/README.md", 1, 18, "Official Binance Spot API documentation is publicly hosted on GitHub.")])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("general_exchange", "General & Exchange Info (connectivity, server time, exchangeInfo, execution rules)", [E("/binance-spot-api-docs/master/rest-api.md", 23, 27, "Lists General endpoints: test connectivity, server time, exchange info, execution rules.")]),
                    group("market_data", "Market Data (order book, trades, klines/candlesticks, tickers, average/reference price)", [E("/binance-spot-api-docs/master/rest-api.md", 28, 43, "Lists Market Data endpoints for order books, trades, klines, and tickers.")]),
                    group("spot_trading", "Spot Trading (new/test/cancel/replace/amend orders, OCO/OTO/OTOCO/OPO order lists, SOR)", [E("/binance-spot-api-docs/master/rest-api.md", 44, 59, "Lists Trading endpoints for orders, order lists, and Smart Order Routing.")]),
                    group("account_user_data", "Account & User Data (account info, open/all orders, trade list, allocations, commission rates, rate limits)", [E("/binance-spot-api-docs/master/rest-api.md", 60, 74, "Lists Account endpoints for balances, orders, trades, and commission rates.")]),
                ],
                "Core Spot REST API groups captured from rest-api.md; README also links to Margin, Futures, Options, Wallet, Sub-Account, Convert, and Pay APIs on developers.binance.com (HTML pages returned empty_readable_content).",
            )
            breadth("broad", ["general_exchange", "market_data", "spot_trading", "account_user_data"], [E("/binance-spot-api-docs/master/rest-api.md", 23, 74, "Spot REST API spans exchange metadata, market data, complex order execution, and account reporting."), E("/binance-spot-api-docs/master/README.md", 20, 43, "Official README also indexes broader exchange domains (Margin, Futures, Options, Wallet, Convert, Pay).")], "Broad exchange API covering market data, Spot trading, account telemetry, and adjacent exchange domains.")
            set_mcp_entries(
                [("community_binance_mcp", "community", "Binance MCP (mujeeb8/Binance-MCP)", [E("/mujeeb8/Binance-MCP/main/README.md", 1, 38, "Community TypeScript MCP server exposing spot prices, book tickers, spot/funding balances, and Binance Convert tools."), E("/mujeeb8/Binance-MCP/main/README.md", 56, 87, "Runs locally over stdio; public market tools require no auth, account/Convert tools require BINANCE_API_KEY and BINANCE_API_SECRET.")], "/mujeeb8/Binance-MCP/main/README.md", "Community local stdio callable MCP server for Binance Spot market data, account balances, and Convert workflows; not vendor-endorsed.", None, None)],
                [E("/mujeeb8/Binance-MCP/main/README.md", 1, 17, "Community callable MCP server documented in mujeeb8/Binance-MCP; no official Binance MCP server found in checked official Spot API repo.")],
            )
            set_build(
                "conditional",
                "Binance global Spot REST/WebSocket API and community MCP server; public market data is open while signed production trading depends on regional/KYC eligibility.",
                ["Regional/jurisdictional eligibility and KYC requirements for global Binance production accounts are unresolved in captured docs.", "No official vendor-endorsed MCP server was found in checked official Spot API sources.", "Spot Testnet supports /api/* only (not /sapi/*) and resets roughly monthly; developers.binance.com HTML returned empty readable content."],
                ["Build against public market-data endpoints and Spot Testnet using official connectors.", "Verify jurisdictional eligibility and Binance account KYC/API Management permissions before enabling live TRADE keys."],
                ["identity.resolution", "auth.public_none", "auth.signed_api_key", "testing.sandbox_access", "api.protocol.rest", "api.breadth", "mcp.community_binance_mcp"],
                [E("/binance-spot-api-docs/master/rest-api.md", 78, 105, "Public REST API endpoints and market-data host."), E("/binance-spot-api-docs/master/testnet/general-info.md", 3, 71, "Self-serve Spot Testnet with virtual assets.")],
                "Public Spot REST/WebSocket/FIX docs and free Spot Testnet support development, but production trading is conditional on unresolved jurisdictional/KYC eligibility and lacks an official vendor MCP.",
            )

        # =====================================================================
        # 84: Paygent Connect (UNRESOLVED IDENTITY)
        # =====================================================================
        elif app == 84:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                None,
                [],
                "unknown",
                (),
                "Unresolved identity: data/apps.json preserves original hint 'paygent (NMI-powered)' with identity_status='unresolved' and flags legacy lead paygentglobal.com as unmatched. Captured NMI pages (nmi.com, docs.nmi.com) describe NMI's general white-label gateway platform and do not establish a primary vendor or product match for 'Paygent Connect'. Per evidence rules, neither paygentglobal.com nor Japanese Paygent Co., Ltd. nor NMI is substituted.",
            )
            r["purpose"] = claim("purpose", None, [], "unknown", (), "Blocked by unresolved product identity for Paygent Connect ('paygent (NMI-powered)').")
            items(r["auth"], [], "No product-specific auth claims promoted while Paygent Connect identity remains unresolved.", cov="not_researched")
            for env in ("testing", "production"):
                for k in ("free_access", "trial_access", "sandbox_access", "paid_required", "admin_approval_required", "vendor_approval_required", "partner_approval_required", "contact_sales_required", "self_serve"):
                    unknown_elig(env, k, "Blocked by unresolved product identity for Paygent Connect.")
            items(r["api_surface"]["protocols"], [], "Blocked by unresolved product identity.", cov="not_researched")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", None, [], "unknown", (), "Blocked by unresolved product identity.")
            items(r["api_surface"]["resource_groups"], [], "Blocked by unresolved product identity.", cov="not_researched")
            r["api_surface"]["breadth"] = claim("api.breadth", None, [], "unknown", (), "Blocked by unresolved product identity.")
            r["mcp"]["discovery"] = claim("mcp.discovery", None, [], "unknown", (), "Blocked by unresolved product identity.")
            r["mcp"]["entries"] = []
            r["buildability"] = claim("buildability", None, [], "unknown", (), "Cannot assess buildability until primary evidence resolves which vendor/product 'Paygent Connect (paygent (NMI-powered))' refers to.")

        # =====================================================================
        # 85: iPayX
        # =====================================================================
        elif app == 85:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                "iPayX Protocol — FINTRAC-registered FX forensic audit layer at https://www.ipayx.ai/ (static HTTP capture returned single-line SPA title only).",
                [E("https://www.ipayx.ai/", 1, 1, "Homepage title on original domain hint identifies 'iPayX Protocol — FINTRAC-registered FX forensic audit layer'.")],
            )
            r["purpose"] = claim(
                "purpose",
                "FINTRAC-registered FX forensic audit layer (iPayX Protocol).",
                [E("https://www.ipayx.ai/", 1, 1, "Homepage title states 'iPayX Protocol — FINTRAC-registered FX forensic audit layer'.")],
            )
            items(
                r["auth"],
                [],
                "Primary vendor-domain docs (ipayx.ai/docs, /docs/api, /docs/mcp, /api-terms) rendered as 1-line JS SPA shells under static HTTP capture and /pricing timed out. The iPAYX-Technologies/mcp-fx-audit GitHub README (conservatively tagged community_repository because the SPA did not render a GitHub ownership link) documents unauthenticated free MCP tools plus Bearer API key auth for full_forensic_fx_report, which is recorded under MCP rather than primary product auth.",
                cov="partial",
            )
            for env in ("testing", "production"):
                for k in ("free_access", "trial_access", "sandbox_access", "paid_required", "admin_approval_required", "vendor_approval_required", "partner_approval_required", "contact_sales_required", "self_serve"):
                    unknown_elig(env, k, "Primary vendor-domain docs/pricing on ipayx.ai could not be read via static HTTP (1-line JS SPA shells and pricing timeout); community-tagged GitHub MCP README cannot establish primary vendor credential eligibility.")
            items(r["api_surface"]["protocols"], [], "Primary vendor-domain API docs on ipayx.ai/docs/api returned a 1-line JS SPA shell; REST/API protocols unverified from primary HTML.", cov="partial")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", None, [], "unknown", (), "ipayx.ai/docs and /docs/api returned 1-line JS SPA shells under static HTTP; public API doc readability requires JS rendering.")
            items(r["api_surface"]["resource_groups"], [], "Primary vendor-domain API docs returned 1-line JS SPA shells.", cov="partial")
            r["api_surface"]["breadth"] = claim("api.breadth", None, [], "unknown", (), "Insufficient primary API resource-group documentation captured due to JS SPA rendering.")
            set_mcp_entries(
                [("community_ipayx_fx_audit_mcp", "community", "iPayX FX Audit MCP (iPAYX-Technologies/mcp-fx-audit)", [E("/iPAYX-Technologies/mcp-fx-audit/main/README.md", 1, 65, "Documents remote streamable-HTTP MCP server v1.4.0 at https://mcp.ipayx.ai/mcp with 4 tools: check_fx_mid_market_rate, audit_fx_transaction (3 free/IP/month), compare_fx_sources, and full_forensic_fx_report (Bearer API key)."), E("/iPAYX-Technologies/mcp-fx-audit/main/README.md", 96, 105, "States operator 11850091 Canada Inc. operating as iPayX Protocol, FINTRAC MSB C10001283, read-only audit server.")], "/iPAYX-Technologies/mcp-fx-audit/main/README.md", "Remote streamable-HTTP callable MCP server (v1.4.0) for read-only FX mid-market rate checks and forensic fee audits; conservatively tagged community because vendor-domain SPA did not render a link verifying GitHub org ownership.", "https://mcp.ipayx.ai/mcp", None)],
                [E("/iPAYX-Technologies/mcp-fx-audit/main/README.md", 1, 8, "Callable remote MCP server documented at https://mcp.ipayx.ai/mcp.")],
            )
            set_build(
                "conditional",
                "iPayX FX Audit remote MCP server (https://mcp.ipayx.ai/mcp); primary REST API and pricing remain uncaptured.",
                ["ipayx.ai/docs, /docs/api, /docs/mcp, and /api-terms returned 1-line JS SPA shells under static HTTP capture, and ipayx.ai/pricing timed out.", "Vendor-domain confirmation linking ipayx.ai to GitHub org iPAYX-Technologies could not be verified from static HTML.", "Full forensic report tool requires a Bearer API key from ipayx.ai/ai-access whose pricing/terms were not captured."],
                ["Capture JS-rendered ipayx.ai/docs, /pricing, and /ai-access pages to confirm official MCP ownership, REST API surface, and paid-tier terms.", "Evaluate read-only free MCP tools against operational requirements once ownership is verified."],
                ["identity.resolution", "mcp.discovery", "mcp.community_ipayx_fx_audit_mcp"],
                [E("https://www.ipayx.ai/", 1, 1, "Domain identifies iPayX Protocol — FINTRAC-registered FX forensic audit layer; JS SPA prevented static capture of primary API docs.")],
                "A callable remote MCP server is documented in the repository, but primary vendor-domain API docs, pricing, terms, and official ownership confirmation remain uncaptured.",
            )

        # =====================================================================
        # 86: QuickBooks
        # =====================================================================
        elif app == 86:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                "QuickBooks Online Accounting API on Intuit Developer (distinct from QuickBooks Desktop).",
                [
                    E("/oauth-2.0.html", 6, 14, "Intuit Developer OAuth 2.0 guide for QuickBooks Online Accounting API."),
                    E("/publish-app.html", 1, 4, "Intuit Developer guide for publishing QuickBooks Online apps."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Cloud accounting API for QuickBooks Online companies with OAuth 2.0, official multi-language SDKs, and an official local MCP server.",
                [
                    E("/oauth-2.0.html", 7, 26, "QuickBooks Online Accounting API uses OAuth 2.0 and official SDKs to interact with company accounting data."),
                    E("/quickbooks-online-mcp-server/main/README.md", 1, 22, "Official Intuit local stdio MCP server covers 29 QuickBooks Online entity types and 11 financial reports."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_auth_code",
                        "OAuth2",
                        "OAuth 2.0 Authorization Code and Refresh Token flow via Intuit OAuth 2.0 Server (TLS 1.2+), scoped per QuickBooks Online company (realmId); browser-based user consent required, 100-day refresh token window.",
                        [
                            E("/oauth-2.0.html", 3, 14, "Requires TLS 1.2+ and OAuth 2.0 authorization tied to user's QuickBooks Online company (realmId)."),
                            E("/oauth-2.0.html", 58, 120, "Documents authorization code flow, user consent, token exchange, refresh tokens, and browser modal requirement."),
                            E("/oauth-2.0.html", 184, 184, "Lists accounting and payment scopes (com.intuit.quickbooks.accounting, com.intuit.quickbooks.payment)."),
                            E("/quickbooks-online-mcp-server/main/README.md", 23, 23, "Notes one-time browser OAuth handshake, localhost redirect in sandbox, public HTTPS callback in production, and 100-day refresh window."),
                        ],
                        "QuickBooks Online Accounting API (sandbox and production companies).",
                        scopes=["com.intuit.quickbooks.accounting", "com.intuit.quickbooks.payment", "openid"],
                    ),
                ],
                "Checked official Intuit OAuth 2.0 guide and official QuickBooks Online MCP server README.",
            )
            # Testing eligibility
            unknown_elig("testing", "free_access", "Sandbox companies are attached to an Intuit Developer account, but explicit pricing/free-tier terms (tos.html) timed out during capture.")
            unknown_elig("testing", "trial_access", "Sandbox companies with sample data are provided; time-limited trial terms not stated in captured docs.")
            elig("testing", "sandbox_access", True, [E("/sandboxes.html", 2, 5, "Developers can start with a sandbox company connected to their Intuit Developer account with sample data."), E("/oauth-2.0.html", 71, 71, "Development section provides sandbox Client ID and Client secret.")], "Dedicated sandbox companies with sample data.")
            unknown_elig("testing", "paid_required", "Intuit Developer Terms of Service page timed out; no fee is mentioned for sandbox creation in sandboxes.html.")
            unknown_elig("testing", "admin_approval_required", "Individual Intuit Developer account creates sandbox apps; customer company admin approval applies when connecting real companies.")
            elig("testing", "vendor_approval_required", False, [E("/oauth-2.0.html", 11, 14, "Developers create an app on the Intuit Developer Portal and obtain Development credentials directly."), E("/publish-app.html", 26, 48, "App Assessment Questionnaire approval is required for Production credentials, not Development sandbox keys.")], "Development sandbox keys do not require App Assessment Questionnaire approval.")
            elig("testing", "partner_approval_required", False, [E("/oauth-2.0.html", 11, 14, "App creation on Intuit Developer Portal is open without commercial partner approval.")], "No partner approval needed for sandbox.")
            elig("testing", "contact_sales_required", False, [E("/oauth-2.0.html", 11, 14, "Self-serve developer portal app creation.")], "No sales contact needed for sandbox.")
            elig("testing", "self_serve", True, [E("/oauth-2.0.html", 11, 14, "Sign in to Intuit Developer account and create an app."), E("/oauth-2.0.html", 71, 71, "Get Development Client ID and Client secret in portal."), E("/sandboxes.html", 3, 5, "Use connected sandbox company.")], "Self-serve developer portal app and sandbox setup.")
            # Production eligibility
            unknown_elig("production", "free_access", "Intuit Developer Terms/API pricing page (tos.html) timed out; production API billing terms uncaptured.")
            unknown_elig("production", "trial_access", "Not documented in captured Intuit pages.")
            elig("production", "sandbox_access", False, [E("/oauth-2.0.html", 70, 71, "Production and Development keys are separate."), E("/mcp-connector.html", 20, 21, "Explicitly separates sandbox data from production credentials and company data.")], "Production credentials and companies are separate from sandbox.")
            unknown_elig("production", "paid_required", "Intuit Developer ToS/pricing page timed out; QuickBooks Online company subscription requirements and API tier fees remain uncaptured.")
            unknown_elig("production", "admin_approval_required", "QuickBooks Online user must grant OAuth consent to connect their company (oauth-2.0.html L58-60), but specific company admin role requirements are not stated in captured pages.")
            elig("production", "vendor_approval_required", True, [E("/publish-app.html", 26, 34, "Must complete App Assessment Questionnaire and compliance URLs before getting production credentials."), E("/publish-app.html", 48, 48, "Show Credentials switch for Production appears only after the App Assessment Questionnaire is approved.")], "Intuit App Assessment Questionnaire approval is required before Production credentials are unlocked.")
            unknown_elig("production", "partner_approval_required", "Semi-private production apps are allowed after App Assessment approval; public listing on QuickBooks App Store is optional (publish-app.html L51-54).")
            unknown_elig("production", "contact_sales_required", "Not stated in publish-app.html; ToS/pricing page timed out.")
            elig("production", "self_serve", False, [E("/publish-app.html", 48, 48, "Production credentials are gated behind Intuit approval of the App Assessment Questionnaire.")], "Production credentials require Intuit compliance questionnaire approval.")
            # API surface
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("/oauth-2.0.html", 7, 10, "HTTP/TLS 1.2+ OAuth 2.0 QuickBooks Online v3 API."), E("/QuickBooks-V3-PHP-SDK/master/README.md", 1, 10, "Official QuickBooks Online V3 API SDK.")]),
                    claim("api.protocol.sdk", "SDK", [E("/oauth-2.0.html", 18, 49, "Official OAuth 2.0 and QuickBooks Online SDKs for .NET, Java, PHP, Node.js, Python, and Ruby.")]),
                ],
                "REST API (v3) and official multi-language SDKs documented; all-entities HTML page failed capture (timeout/403).",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("/oauth-2.0.html", 6, 75, "Intuit Developer OAuth, sandbox, and publish guides are publicly readable.")])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("sales_ar", "Sales & Accounts Receivable (Customer, Invoice, Estimate, Payment, Sales Receipt, Credit Memo, Refund Receipt)", [E("/quickbooks-online-mcp-server/main/README.md", 80, 97, "Official Intuit QBO MCP README documents full CRUD for Customer, Invoice, Estimate, Payment, Sales Receipt, Credit Memo, Refund Receipt.")]),
                    group("purchases_ap", "Purchases & Accounts Payable (Vendor, Bill, Bill Payment, Purchase, Purchase Order, Vendor Credit)", [E("/quickbooks-online-mcp-server/main/README.md", 86, 99, "Documents CRUD for Bill, Vendor, Bill Payment, Purchase, Purchase Order, Vendor Credit.")]),
                    group("ledger_banking_tax", "General Ledger, Banking & Tax (Account, Item, Journal Entry, Deposit, Transfer, Tax Code/Rate/Agency)", [E("/quickbooks-online-mcp-server/main/README.md", 89, 109, "Documents Account, Item, Journal Entry, Deposit, Transfer, Tax Code, Tax Rate, Tax Agency.")]),
                    group("org_time_reports", "Organization, Time & Financial Reports (Employee, Time Activity, Class, Department, Company Info, Attachable, 11 Financial Reports)", [E("/quickbooks-online-mcp-server/main/README.md", 88, 125, "Documents Employee, Time Activity, Class, Department, Company Info, Attachable, and 11 financial reports including Balance Sheet, P&L, Cash Flow, Trial Balance, General Ledger.")]),
                ],
                "Resource groups captured from official intuit/quickbooks-online-mcp-server README (static all-entities HTML returned 403/timeout).",
            )
            breadth("broad", ["sales_ar", "purchases_ap", "ledger_banking_tax", "org_time_reports"], [E("/quickbooks-online-mcp-server/main/README.md", 14, 125, "Covers 29 accounting entity types and 11 financial reports across AR, AP, GL, banking, tax, and time tracking.")], "Broad accounting API spanning AR, AP, general ledger, banking, tax, time tracking, and financial reporting.")
            set_mcp_entries(
                [("official_qbo_mcp_server", "official", "QuickBooks Online MCP Server (intuit/quickbooks-online-mcp-server)", [E("/quickbooks-online-mcp-server/main/README.md", 1, 23, "Official Intuit local stdio callable MCP server providing 145 tools across 29 entity types and 11 financial reports via OAuth 2.0."), E("/quickbooks-online-mcp-server/main/README.md", 78, 126, "Lists all 29 CRUD entity groups and 11 financial report tools.")], "/quickbooks-online-mcp-server/main/README.md", "Official local stdio callable MCP server exposing 145 QuickBooks Online CRUD and reporting tools over OAuth 2.0 (separate from Intuit Developer Plugin onboarding helper).", None, None)],
                [E("/quickbooks-online-mcp-server/main/README.md", 1, 22, "Official QuickBooks Online local stdio MCP server documented in intuit/quickbooks-online-mcp-server.")],
            )
            set_build(
                "conditional",
                "QuickBooks Online Accounting API and official local MCP server for sandbox development and approved production apps.",
                ["Production Client ID and Client Secret require Intuit approval of the App Assessment Questionnaire and compliance URLs.", "Production OAuth requires a public HTTPS callback URL and user consent per company realm (100-day refresh window).", "Intuit ToS/API pricing page and all-entities reference HTML failed static HTTP capture."],
                ["Build and test immediately against a self-serve Intuit Developer sandbox company and official SDK/MCP server.", "Complete App Details, EULA/Privacy Policy URLs, and App Assessment Questionnaire to unlock Production credentials."],
                ["identity.resolution", "auth.oauth2_auth_code", "testing.sandbox_access", "production.vendor_approval_required", "api.protocol.rest", "api.breadth", "mcp.official_qbo_mcp_server"],
                [E("/sandboxes.html", 2, 5, "Self-serve sandbox companies."), E("/publish-app.html", 48, 48, "Production credentials gated on App Assessment Questionnaire approval."), E("/quickbooks-online-mcp-server/main/README.md", 14, 23, "Official local MCP server with 145 tools.")],
                "Sandbox development and official local MCP integration can start immediately, but production deployment is conditional on Intuit App Assessment Questionnaire approval.",
            )

        # =====================================================================
        # 87: Xero
        # =====================================================================
        elif app == 87:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                "Xero Accounting API and Xero Developer Platform (developer.xero.com, XeroAPI GitHub org).",
                [
                    E("/pricing", 10, 17, "Xero Developer Pricing and Policies for Xero apps (Starter, Core, Plus, Advanced, Enterprise)."),
                    E("/Xero-OpenAPI/master/README.md", 1, 15, "Official Xero OpenAPI 3.0 specifications covering Accounting, Identity, Bank Feeds, Assets, Projects, Payroll, and Files."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Cloud accounting and business API suite with OAuth 2.0, OpenAPI 3.0 specs, SDKs, and official hosted Remote MCP and local MCP servers.",
                [
                    E("/Xero-OpenAPI/master/README.md", 1, 15, "Official OpenAPI 3.0 specs for Accounting, Identity, Bank Feeds, Fixed Assets, Projects, Payroll, and Files."),
                    E("/faq/remote-mcp", 64, 73, "Official hosted Remote MCP server at https://api.xero.com/mcp/v1."),
                    E("/xero-mcp-server/main/README.md", 1, 8, "Official open-source local MCP server for Xero."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_auth_code_pkce",
                        "OAuth2",
                        "OAuth 2.0 Authorization Code (web apps) and PKCE (public/MCP clients) flows with 30-minute access tokens, refresh tokens, and granular scopes; basic API keys are not supported and OAuth 1.0a is deprecated.",
                        [
                            E("/faq/getting-started", 29, 30, "Xero API does not support basic API Key authentication; uses OAuth 2.0."),
                            E("/faq/getting-started", 44, 45, "OAuth 2.0 is required for all new integrations (OAuth 1.0a deprecated)."),
                            E("/faq/remote-mcp", 35, 46, "Remote MCP authorizes via OAuth 2.0 with PKCE (web app also possible)."),
                            E("/faq/custom-integration", 76, 77, "All Xero access tokens expire after 30 minutes; refresh tokens renew access."),
                            E("/xero-mcp-server/main/README.md", 76, 100, "Lists granular OAuth 2.0 accounting and payroll scopes."),
                        ],
                        "Multi-org commercial apps and Xero Remote MCP (per-organisation OAuth consent).",
                        scopes=["accounting.invoices", "accounting.invoices.read", "accounting.payments", "accounting.banktransactions", "accounting.contacts", "accounting.settings", "payroll.employees", "payroll.timesheets"],
                    ),
                    auth(
                        "oauth2_client_credentials_custom",
                        "OAuth2",
                        "OAuth 2.0 Client Credentials grant for single-organisation machine-to-machine Custom Connections (paid subscription in AU/NZ/UK/US, free on Demo Company; new Custom Connection creation closes 1 December 2026 while client credentials remains part of the platform).",
                        [
                            E("/faq/custom-integration", 29, 38, "New Custom Connection creation stops 1 Dec 2026, while client credentials remains supported."),
                            E("/faq/custom-integration", 49, 80, "Single-org client_id/client_secret client_credentials grant with 30-min access tokens, no refresh tokens, no xero-tenant-id header; eligible for AU/NZ/UK/US orgs or Demo Company; ineligible for Remote MCP."),
                            E("/faq/remote-mcp", 39, 40, "Custom Connections apps are not eligible to access the Remote MCP Server."),
                        ],
                        "Single-organisation machine-to-machine Custom Connections (AU/NZ/UK/US) and local xero-mcp-server.",
                    ),
                ],
                "Checked Xero Developer pricing, Remote MCP FAQ, Custom Integration FAQ, Getting Started FAQ, and official XeroAPI GitHub repos.",
            )
            # Testing eligibility
            elig("testing", "free_access", True, [E("/faq/getting-started", 35, 39, "Sign up for a free Xero account and develop without cost using the Demo Company."), E("/pricing", 85, 86, "Starter plan has No charge.")], "Free Xero account, Demo Company, and Starter plan.")
            elig("testing", "trial_access", True, [E("/faq/getting-started", 38, 38, "Can start a trial Xero organisation subscription for development."), E("/xero-mcp-server/main/README.md", 21, 21, "Notes signing up using the free trial.")], "Free trial Xero organisation option available.")
            elig("testing", "sandbox_access", True, [E("/faq/getting-started", 31, 37, "Demo Company comes with pre-loaded sample data and supports most API functionality."), E("/xero-mcp-server/main/README.md", 22, 22, "Demo Company data can be reset or country changed at any time.")], "Resettable Demo Company sandbox.")
            elig("testing", "paid_required", False, [E("/faq/getting-started", 36, 37, "Develop without incurring any cost using the Demo Company."), E("/faq/custom-integration", 70, 70, "No charge when testing Custom Connections with a demo company.")], "No payment required for Demo Company testing.")
            unknown_elig("testing", "admin_approval_required", "Single developer can spin up a free account and Demo Company; organisation role rules for shared tenants not detailed in captured FAQs.")
            elig("testing", "vendor_approval_required", False, [E("/pricing", 13, 27, "Starter and Core plans do not require App Certification.")], "No vendor certification needed for Starter/Demo testing.")
            elig("testing", "partner_approval_required", False, [E("/faq/getting-started", 35, 39, "Open free developer signup and Demo Company.")], "No partner approval needed for testing.")
            elig("testing", "contact_sales_required", False, [E("/pricing", 13, 36, "Starter plan requires no payment method or sales contact.")], "No sales contact needed for testing.")
            elig("testing", "self_serve", True, [E("/faq/getting-started", 35, 39, "Self-serve free Xero account and Demo Company setup.")], "Self-serve signup and Demo Company.")
            # Production eligibility
            elig("production", "free_access", True, [E("/pricing", 13, 19, "Starter plan supports up to 5 connections at No charge (1,000 calls/day/org)."), E("/pricing", 84, 86, "Starter monthly tier fee is No charge; Remote MCP on Starter is Demo org only.")], "Free Starter tier allows up to 5 real connections (Remote MCP requires Core+ for real orgs).")
            unknown_elig("production", "trial_access", "Free trial applies to Xero organisation accounts, while developer API app tiers are Starter/Core/Plus/Advanced/Enterprise.")
            elig("production", "sandbox_access", False, [E("/faq/remote-mcp", 34, 34, "Distinguishes Demo organisation from real customer organisations.")], "Real customer organisations are separate from Demo Company.")
            unknown_elig("production", "paid_required", "Depends on scope: Starter is free up to 5 connections for standard API, whereas >5 connections or real-org Remote MCP requires paid Core ($35 AUD/mo), Plus ($245 AUD/mo), Advanced ($1445 AUD/mo), or Enterprise (accountants/bookkeepers may request fee exemption; pricing L84-89, faq/remote-mcp L34-38).")
            unknown_elig("production", "admin_approval_required", "Each customer organisation goes through OAuth consent (faq/remote-mcp L30), but specific Xero org role requirements are not detailed in captured pages.")
            unknown_elig("production", "vendor_approval_required", "Starter and Core require no App Certification; Plus, Advanced, and Enterprise require App Certification, and Advanced/Enterprise also require initial and annual Security Assessment (pricing L24-30, faq/remote-mcp L44).")
            unknown_elig("production", "partner_approval_required", "Xero App Store listing is optional on Plus/Advanced and required on Enterprise, not required on Starter/Core (pricing L37-42, L67).")
            unknown_elig("production", "contact_sales_required", "Starter through Advanced have published self-serve credit-card pricing; Enterprise is Price on Application (pricing L84-97).")
            unknown_elig("production", "self_serve", "Starter (<=5 connections) and Core (<=50 connections, card on file) are self-serve, while Plus/Advanced/Enterprise require certification/security assessment or sales (pricing L18-42, L84-97).")
            # API surface
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("/Xero-OpenAPI/master/README.md", 1, 15, "Official OpenAPI 3.0 specifications for Xero REST APIs.")]),
                    claim("api.protocol.sdk", "SDK", [E("/faq/getting-started", 34, 34, "Official SDKs plus OpenAPI spec for code generation."), E("/xero-node/master/README.md", 1, 30, "Official XeroAPI/xero-node SDK.")]),
                ],
                "REST APIs defined via official OpenAPI 3.0 YAML specs plus official SDKs.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("/Xero-OpenAPI/master/README.md", 1, 15, "Public OpenAPI specs on GitHub."), E("/pricing", 10, 89, "Public pricing and FAQ docs on developer.xero.com (some guide pages are JS SPAs).")])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("accounting_identity", "Accounting & Identity (contacts, accounts, invoices, payments, bank transactions, journals, reports, tenants)", [E("/Xero-OpenAPI/master/README.md", 7, 8, "OpenAPI specs for Accounting and Identity."), E("/xero-mcp-server/main/README.md", 101, 146, "Covers accounts, contacts, invoices, quotes, credit notes, payments, bank transactions, manual journals, and financial reports.")]),
                    group("bank_feeds_assets_projects", "Bank Feeds, Fixed Assets & Projects", [E("/Xero-OpenAPI/master/README.md", 9, 11, "OpenAPI specs for Bank Feeds, Fixed Assets, and Projects.")]),
                    group("payroll_files", "Regional Payroll (AU, UK, NZ) & Files", [E("/Xero-OpenAPI/master/README.md", 12, 15, "OpenAPI specs for Payroll AU, Payroll UK, Payroll NZ, and Files.")]),
                ],
                "Resource groups captured from official XeroAPI/Xero-OpenAPI and xero-mcp-server repositories.",
            )
            breadth("broad", ["accounting_identity", "bank_feeds_assets_projects", "payroll_files"], [E("/Xero-OpenAPI/master/README.md", 6, 15, "Spans Accounting, Identity, Bank Feeds, Fixed Assets, Projects, multi-region Payroll, and Files.")], "Broad accounting and business platform API across multiple distinct domains.")
            set_mcp_entries(
                [
                    ("official_xero_remote_mcp", "official", "Xero Remote MCP Server", [E("/faq/remote-mcp", 29, 73, "Official hosted Remote MCP server at https://api.xero.com/mcp/v1 using OAuth 2.0 + PKCE; Starter=Demo org only, Core+=real orgs; excludes Custom Connections."), E("/pricing", 49, 49, "Remote MCP server on Starter is Demo org only.")], "/faq/remote-mcp", "Official hosted callable Remote MCP server (https://api.xero.com/mcp/v1) supporting read/write Xero accounting tools via OAuth 2.0 + PKCE (Core+ required for real orgs).", "https://api.xero.com/mcp/v1", None),
                    ("official_xero_local_mcp", "official", "Xero MCP Server (XeroAPI/xero-mcp-server)", [E("/xero-mcp-server/main/README.md", 1, 75, "Official open-source local stdio callable MCP server (@xeroapi/xero-mcp-server, MIT) supporting Custom Connections or Bearer Token auth."), E("/xero-mcp-server/main/README.md", 101, 152, "Exposes accounting, contacts, invoices, payments, bank transactions, reports, and payroll tools.")], "/xero-mcp-server/main/README.md", "Official open-source local stdio callable MCP server (@xeroapi/xero-mcp-server) supporting Custom Connections or OAuth Bearer token.", None, None),
                ],
                [E("/faq/remote-mcp", 64, 73, "Official Remote MCP server at https://api.xero.com/mcp/v1."), E("/xero-mcp-server/main/README.md", 1, 8, "Official open-source Xero MCP server repo.")],
            )
            set_build(
                "build_now",
                "Xero Accounting API (Starter/Core OAuth 2.0) and official Remote/Local MCP servers.",
                ["Starter tier caps connections at 5 (1,000 calls/day/org) and limits Remote MCP to the Demo organisation.", "Real-org Remote MCP or >5 connections requires paid Core ($35 AUD/mo) or higher; >50 connections (Plus+) requires App Certification and Advanced+ requires Security Assessment.", "New Custom Connection creation closes 1 December 2026; several developer.xero.com guide pages render as JS SPAs."],
                ["Start immediately with a free Xero account, Demo Company, OpenAPI specs, and Starter plan.", "Upgrade to Core for real-org Remote MCP or >5 connections; plan App Certification before scaling past 50 connections."],
                ["identity.resolution", "auth.oauth2_auth_code_pkce", "testing.sandbox_access", "testing.self_serve", "production.free_access", "api.protocol.rest", "api.breadth", "mcp.official_xero_remote_mcp", "mcp.official_xero_local_mcp"],
                [E("/faq/getting-started", 35, 39, "Free account and Demo Company."), E("/pricing", 13, 86, "Free Starter tier up to 5 connections; paid tiers above."), E("/faq/remote-mcp", 34, 69, "Official Remote MCP server.")],
                "Free Demo Company, free Starter tier (up to 5 connections), OpenAPI 3.0 specs, official SDKs, and both official Remote and local MCP servers enable immediate building; scaling and real-org Remote MCP require paid/certified tiers.",
            )

        # =====================================================================
        # 88: Brex
        # =====================================================================
        elif app == 88:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                "Brex unified spend platform Developer API (https://api.brex.com) and official hosted Brex MCP server (https://api.brex.com/mcp).",
                [
                    E("https://developer.brex.com/", 37, 49, "Brex Developer Overview describing the unified spend platform REST APIs."),
                    E("/docs/mcp.md", 1, 10, "Official Brex MCP documentation for https://api.brex.com/mcp."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Corporate card, expense, travel, bill pay, and banking spend-management REST API with an official hosted MCP server.",
                [
                    E("https://developer.brex.com/", 37, 49, "Covers global corporate cards, expenses, reimbursements, travel, bill pay, budgets, and banking via REST APIs."),
                    E("/docs/mcp.md", 1, 10, "Official hosted Brex MCP server lets AI assistants interact with Brex accounts."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "own_account_user_token",
                        "Bearer_token",
                        "Admin-provisioned user token (bxt_*) generated in Brex Dashboard (Developer > Settings) by an Account Admin or Card Admin after accepting the Developer API agreement; passed as Authorization: Bearer; expires after 90 days of inactivity.",
                        [E("/guides/authentication", 40, 62, "Account or Card Admin accepts Developer API agreement, creates scoped user token bxt_*, passes as Bearer header to https://api.brex.com; expires after 90 days idle.")],
                        "Own-account Brex customer REST API access (production only).",
                    ),
                    auth(
                        "partner_oauth2_auth_code",
                        "OAuth2",
                        "Partner OAuth 2.0 Authorization Code Grant (optional PKCE) and OpenID Connect via https://accounts-api.brex.com/oauth2/default; 1-hour Bearer access tokens and 90-day rotating refresh tokens; client may decline individual scopes.",
                        [E("/guides/partner_authentication", 40, 122, "Documents partner OAuth 2.0 Authorization Code Grant, OIDC discovery, scopes (openid, offline_access), 1-hour access tokens, and 90-day rotating refresh tokens.")],
                        "Approved Brex developer partners accessing customer Brex accounts.",
                        scopes=["openid", "offline_access"],
                    ),
                    auth(
                        "partner_oauth2_client_credentials",
                        "OAuth2",
                        "Partner OAuth 2.0 Client Credentials Grant for the Onboarding API (1-hour Bearer access tokens, no existing Brex client involved).",
                        [E("/guides/partner_authentication", 62, 63, "Client Credentials Grant is used for the Onboarding API."), E("/guides/partner_authentication", 123, 145, "Documents grant_type=client_credentials token request returning 1-hour Bearer tokens.")],
                        "Approved Brex developer partners using the Onboarding API.",
                    ),
                    auth(
                        "mcp_oauth2_dcr",
                        "OAuth2",
                        "Brex MCP OAuth 2.0 with Dynamic Client Registration (RFC 7591) at https://accounts-api.brex.com/oauth2/default (any employee can authorize once admin accepts API agreement and enables beta; admin API token Bearer fallback also supported).",
                        [E("/docs/mcp.md", 5, 10, "Admin accepts Developer API agreement and enables beta; then any employee can connect via OAuth."), E("/docs/mcp.md", 49, 62, "MCP supports OAuth with RFC 7591 Dynamic Client Registration or admin Bearer API token.")],
                        "Hosted Brex MCP server (https://api.brex.com/mcp).",
                    ),
                ],
                "Checked official Brex developer authentication, partner authentication, partner onboarding, and MCP docs.",
            )
            # Testing eligibility
            unknown_elig("testing", "free_access", "No fee is stated for partner staging, while own-account customers have no separate sandbox environment (guides/authentication L61-62).")
            unknown_elig("testing", "trial_access", "No developer free trial documented in captured Brex docs.")
            unknown_elig("testing", "sandbox_access", "Path-dependent: own-account customers only have production https://api.brex.com with no sandbox (guides/authentication L61-62), whereas approved developer partners receive ephemeral staging https://api-staging.brex.com (guides/partner_authentication L44-47, docs/partner_onboarding L21-27).")
            unknown_elig("testing", "paid_required", "Own-account API requires a Brex business account; partner staging cost is not stated.")
            unknown_elig("testing", "admin_approval_required", "Own-account testing runs on production and requires Account/Card Admin; partner staging is provisioned by Brex.")
            elig("testing", "vendor_approval_required", True, [E("/docs/partner_onboarding", 21, 23, "Partner staging credentials and staging accounts are provisioned by Brex only after application approval and Unilateral API Access Agreement.")], "Staging environment access requires Brex approval and manual provisioning.")
            elig("testing", "partner_approval_required", True, [E("/guides/partner_authentication", 40, 45, "Staging server api-staging.brex.com is in the partner-only section."), E("/docs/partner_onboarding", 21, 23, "Requires partner application approval and signing Unilateral API Access Agreement.")], "Staging environment is restricted to approved Brex developer partners.")
            unknown_elig("testing", "contact_sales_required", "Partner onboarding requires contacting developer support and signing a Unilateral API Access Agreement (guides/partner_authentication L67, docs/partner_onboarding L21-22).")
            elig("testing", "self_serve", False, [E("/guides/authentication", 61, 62, "Brex currently only offers a production API server for own-account customers."), E("/docs/partner_onboarding", 21, 23, "Staging credentials are issued manually via SendSafely after partner approval.")], "No self-serve sandbox/staging environment.")
            # Production eligibility
            unknown_elig("production", "free_access", "Requires an active Brex business account (own-account) or approved Brex partner status; pricing not captured.")
            unknown_elig("production", "trial_access", "Not documented in captured Brex docs.")
            elig("production", "sandbox_access", False, [E("/guides/authentication", 61, 62, "https://api.brex.com is the production API server.")], "Production is live account data.")
            unknown_elig("production", "paid_required", "Brex account plan pricing/eligibility not captured in developer docs.")
            elig("production", "admin_approval_required", True, [E("/guides/authentication", 42, 44, "Must sign in as Account Admin or Card Admin and accept Developer API agreement to create user tokens."), E("/docs/mcp.md", 6, 8, "Account or Card Admin must accept Developer API agreement and enable beta before users can connect to Brex MCP."), E("/guides/partner_authentication", 64, 64, "Only Brex clients with proper roles may grant partner OAuth permission.")], "Workspace/account admin approval and agreement acceptance are required across customer tokens, MCP beta, and partner OAuth.")
            unknown_elig("production", "vendor_approval_required", "Own-account customer tokens require no Brex review after accepting terms, whereas partner production credentials require Brex demo video review (docs/partner_onboarding L24).")
            unknown_elig("production", "partner_approval_required", "Own-account customer tokens do not require partner approval, whereas multi-tenant third-party partner OAuth requires Brex partner approval, Unilateral API Access Agreement, and demo video review (guides/partner_authentication L67, docs/partner_onboarding L21-24).")
            unknown_elig("production", "contact_sales_required", "Not required for existing Brex customer admins; partner path contacts developer support.")
            unknown_elig("production", "self_serve", "Self-serve for existing Brex customer Account/Card Admins; partner-approved and manually issued via SendSafely for third-party multi-tenant apps.")
            # API surface
            items(
                r["api_surface"]["protocols"],
                [claim("api.protocol.rest", "REST", [E("https://developer.brex.com/", 38, 38, "Brex APIs use REST architecture, OpenAPI specification, and JSON over HTTPS.")])],
                "REST API defined via OpenAPI; docs note Community Supported Libraries.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("https://developer.brex.com/", 37, 53, "Brex developer documentation is publicly readable.")])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("expenses_budgets_cards", "Expenses, Budgets & Limits, Fields (card expenses, receipts, budgets, custom fields)", [E("https://developer.brex.com/", 41, 43, "Budgets, Expenses, and Fields APIs.")]),
                    group("payments_transactions", "Payments & Transactions (vendors, ACH, domestic wires, checks, transactions, accounts, statements)", [E("https://developer.brex.com/", 45, 47, "Payments and Transactions APIs.")]),
                    group("accounting_team_travel", "Accounting, Team, Travel, Onboarding & Webhooks", [E("https://developer.brex.com/", 40, 49, "Accounting, Onboarding, Team, Travel, and Webhooks APIs.")]),
                ],
                "All 10 documented Brex REST API domains captured from developer.brex.com overview.",
            )
            breadth("broad", ["expenses_budgets_cards", "payments_transactions", "accounting_team_travel"], [E("https://developer.brex.com/", 40, 49, "Covers 10 distinct spend-management domains: Accounting, Budgets, Expenses, Fields, Onboarding, Payments, Team, Transactions, Travel, Webhooks.")], "Broad spend-management API covering cards/expenses, payments/banking, accounting, team, travel, and webhooks.")
            set_mcp_entries(
                [("official_brex_mcp", "official", "Brex MCP Server", [E("/docs/mcp.md", 1, 10, "Official Beta hosted HTTP callable MCP server at https://api.brex.com/mcp."), E("/docs/mcp.md", 49, 137, "Supports OAuth 2.0 DCR or admin Bearer token; exposes 40+ tools for users, expenses, cards metadata, banking, bills/vendors, accounting, and travel (no raw PAN/CVV).")], "/docs/mcp.md", "Official hosted HTTP callable MCP server (Beta) at https://api.brex.com/mcp with OAuth DCR or admin Bearer token; requires admin API agreement and beta toggle.", "https://api.brex.com/mcp", None)],
                [E("/docs/mcp.md", 1, 10, "Official Brex MCP server documented at https://api.brex.com/mcp.")],
            )
            set_build(
                "conditional",
                "Brex REST API and official hosted MCP server (own-account customer integration vs multi-tenant partner integration).",
                ["Own-account customers have no sandbox environment (production https://api.brex.com only) and require an Account/Card Admin to accept the Developer API agreement and create tokens or enable MCP beta.", "Multi-tenant third-party partner OAuth and staging require Brex partner approval, signing a Unilateral API Access Agreement, and submitting a demo video for production credentials."],
                ["For own-account automation, have an Account/Card Admin accept the API agreement and issue scoped user tokens or enable Brex MCP beta.", "For multi-tenant partner integrations, apply to Brex partner onboarding to obtain staging credentials and OAuth client credentials."],
                ["identity.resolution", "auth.own_account_user_token", "auth.partner_oauth2_auth_code", "testing.partner_approval_required", "production.admin_approval_required", "api.protocol.rest", "api.breadth", "mcp.official_brex_mcp"],
                [E("/guides/authentication", 40, 62, "Own-account admin token on production only."), E("/docs/partner_onboarding", 21, 24, "Partner staging and demo-video gated production."), E("/docs/mcp.md", 5, 10, "Official hosted MCP server.")],
                "Public REST API and official hosted MCP exist, but building is conditional on having an active Brex account with Admin approval (no customer sandbox) or completing Brex partner onboarding and demo review.",
            )

        # =====================================================================
        # 89: Ramp
        # =====================================================================
        elif app == 89:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                "Ramp Developer API (https://api.ramp.com / https://demo-api.ramp.com), Ramp CLI, and official Ramp MCP server (https://mcp.ramp.com/mcp).",
                [
                    E("/llms.txt", 1, 14, "Official Ramp Developer API machine-readable index covering Developer API, Ramp MCP, and Ramp CLI."),
                    E("/llms-guides/getting-started.txt", 24, 27, "Documents Production (api.ramp.com) and Sandbox (demo-api.ramp.com) API base URLs."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Corporate spend-management, card, bill pay, procurement, treasury, and accounting REST API with official hosted MCP servers and CLI.",
                [
                    E("/llms.txt", 10, 30, "Ramp provides Developer API, Webhooks, Custom Records, Ramp CLI, and Ramp MCP for spend automation."),
                    E("/llms-guides/ramp-mcp.txt", 1, 19, "Official hosted Ramp MCP server connects AI assistants to a Ramp account."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_client_credentials",
                        "OAuth2",
                        "OAuth 2.0 Client Credentials grant authenticated via HTTP Basic Auth (client_id:client_secret) at /developer/v1/token for own-business server-to-server apps; returns 10-day Bearer token (ramp_business_tok_*) with no refresh token.",
                        [
                            E("/llms-guides/authorization.txt", 8, 15, "Client Credentials grant for internal server-to-server integrations with resource:permission scopes."),
                            E("/llms-guides/authorization.txt", 96, 106, "10-day Bearer token lifetime, Basic Auth client credentials, no refresh token."),
                            E("/llms-guides/getting-started.txt", 10, 45, "Admin creates app under Company -> Developer and exchanges Basic Auth for scoped Bearer token."),
                        ],
                        "Own-business server-to-server Ramp Developer API apps.",
                        scopes=["transactions:read", "transactions:write", "bills:read", "bills:write", "cards:read", "cards:write", "users:read", "accounting:read"],
                    ),
                    auth(
                        "oauth2_auth_code",
                        "OAuth2",
                        "OAuth 2.0 Authorization Code and Refresh Token grants at app.ramp.com/v1/authorize (demo.ramp.com in sandbox) and /developer/v1/token for third-party/partner apps; 1-hour access tokens; requires Admin/Business Owner approval for business-wide apps.",
                        [E("/llms-guides/authorization.txt", 107, 147, "Documents Authorization Code flow, Admin/Business Owner approval requirement, 5-minute code expiry, 1-hour access token, and Refresh Token grant.")],
                        "Third-party and multi-tenant partner Ramp integrations.",
                        scopes=["transactions:read", "business:read", "openid", "offline_access"],
                    ),
                    auth(
                        "mcp_cli_oauth2",
                        "OAuth2",
                        "User-scoped OAuth sign-in for Ramp MCP and Ramp CLI selecting Full access or Read-only (inherits connecting user's Ramp role permissions, 30-day connection expiry, subject to Admin AI-tool role permissions and redirect URI allowlisting for custom MCP clients).",
                        [
                            E("/llms-guides/authorization.txt", 87, 94, "Ramp MCP and CLI use OAuth with Full access or Read-only, role-bounded permissions, and 30-day expiry."),
                            E("/llms-guides/ramp-mcp.txt", 18, 22, "Notes 30-day expiry, redirect URI allowlisting for custom clients, and Admin AI-tool role gating."),
                        ],
                        "Official Ramp MCP server (https://mcp.ramp.com/mcp) and Ramp CLI.",
                    ),
                ],
                "Checked official Ramp llms-guides authorization, getting-started, and ramp-mcp text exports.",
            )
            # Testing eligibility
            unknown_elig("testing", "free_access", "Sandbox access is requested via /developer-api/v1/sandbox-access, whose text export contained no body; pricing/free status not stated.")
            unknown_elig("testing", "trial_access", "Not documented in captured Ramp guides.")
            elig("testing", "sandbox_access", True, [E("/llms.txt", 66, 67, "Ramp sandbox is a testing environment for developers and partners."), E("/llms-guides/getting-started.txt", 6, 27, "Documents sandbox host https://demo-api.ramp.com and https://demo.ramp.com.")], "Dedicated Ramp sandbox environment exists.")
            unknown_elig("testing", "paid_required", "Not stated in captured Ramp sandbox docs.")
            unknown_elig("testing", "admin_approval_required", "Sandbox access form body was empty in capture; own-account app creation requires admin access (getting-started.txt L6, L10).")
            unknown_elig("testing", "vendor_approval_required", "Sandbox requires submitting a 'Request sandbox access' flow (/developer-api/v1/sandbox-access), but whether Ramp manually reviews requests is not stated in the captured 4-line stub.")
            unknown_elig("testing", "partner_approval_required", "Sandbox is documented for both developers and partners (llms.txt L66); partner-specific console gating is separate.")
            unknown_elig("testing", "contact_sales_required", "Not stated in captured Ramp guides.")
            unknown_elig("testing", "self_serve", "Sandbox requires a 'Request sandbox access' form whose approval policy was not present in the captured 4-line stub.")
            # Production eligibility
            unknown_elig("production", "free_access", "Requires a Ramp business account; some endpoints require specific Ramp plan features and return 403 without them (authorization.txt L86).")
            unknown_elig("production", "trial_access", "Not documented in captured Ramp guides.")
            elig("production", "sandbox_access", False, [E("/llms-guides/authorization.txt", 99, 99, "Tokens work only in the environment that issued them; sandbox and production need separate apps."), E("/llms-guides/getting-started.txt", 24, 27, "Separates Production api.ramp.com from Sandbox demo-api.ramp.com.")], "Production is separate from sandbox.")
            unknown_elig("production", "paid_required", "Some API endpoints require specific Ramp plan features and return 403 without them (authorization.txt L86); full plan pricing not captured.")
            elig("production", "admin_approval_required", True, [E("/llms-guides/getting-started.txt", 6, 10, "Admin access is required to create developer apps under Company -> Developer."), E("/llms-guides/authorization.txt", 122, 123, "Admin or Business Owner must approve business-wide OAuth apps or enable user-level apps in Manage Access."), E("/llms-guides/ramp-mcp.txt", 22, 22, "Admin controls which Ramp roles can access connected AI tools.")], "Admin/Business Owner approval is required for own-business apps, third-party OAuth installs, and AI/MCP role access.")
            unknown_elig("production", "vendor_approval_required", "Standard own-business API apps do not state vendor review, whereas cards:read_vault requires approved integrator status and custom MCP client redirect URIs require Ramp allowlisting (authorization.txt L86, ramp-mcp.txt L21, llms.txt L56).")
            unknown_elig("production", "partner_approval_required", "Own-business apps do not require partner approval, whereas partner-only scopes (applications, incorporation, bank_accounts:write) and public listing require the partner Developer Console / Technology Partnerships Application (authorization.txt L86, llms.txt L40, L70).")
            unknown_elig("production", "contact_sales_required", "Not stated for standard own-business Developer API; partner/enterprise terms not captured.")
            unknown_elig("production", "self_serve", "Own-business apps are self-serve for Ramp business Admins (getting-started.txt L10-15), whereas partner apps, vault scopes, and custom MCP redirect URIs require Ramp approval.")
            # API surface
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("/llms.txt", 27, 77, "Full REST Developer API with canonical OpenAPI spec and plain-text API reference."), E("/llms-api.txt", 1, 80, "Documents /developer/v1/* REST JSON endpoints.")]),
                    claim("api.protocol.cli", "CLI", [E("/llms.txt", 12, 43, "Official Ramp CLI with JSON agent mode for terminal/scripted workflows.")]),
                ],
                "REST API (OpenAPI + /llms-api.txt) and official Ramp CLI documented.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("/llms.txt", 1, 80, "Ramp developer documentation is publicly readable via llms.txt, llms-guides/*.txt, and llms-api.txt.")])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("accounting_erp", "Accounting & ERP Sync (GL accounts, accounting sync settings, statements)", [E("/llms-api.txt", 1, 79, "Documents /developer/v1/accounting/accounts endpoints."), E("/llms-guides/authorization.txt", 18, 19, "accounting:read and accounting:write scopes.")]),
                    group("cards_spend_controls", "Cards, Virtual Cards, Funds & Spend Programs", [E("/llms.txt", 41, 73, "Guides for Cards, Spend Controls, Spend Programs, and Virtual Cards."), E("/llms-guides/authorization.txt", 36, 48, "cards:*, funds:*, spend_programs:* scopes.")]),
                    group("transactions_reimbursements", "Transactions, Reimbursements, Receipts & Memos", [E("/llms-guides/authorization.txt", 56, 76, "memos:*, receipts:*, reimbursements:*, transactions:* scopes.")]),
                    group("bills_vendors_procurement", "Bill Pay, Vendors, Payments & Procurement (Bills, POs, Approvals, Blank Canvas)", [E("/llms.txt", 38, 60, "Guides for Bill Pay, Bill Payments, Procurement, and Blank Canvas."), E("/llms-guides/authorization.txt", 25, 85, "approvals:*, bills:*, payments:*, purchase_orders:*, unified_requests:*, vendors:* scopes.")]),
                    group("banking_users_custom", "Banking/Treasury, Users, Entities, Custom Records & Webhooks", [E("/llms.txt", 37, 74, "Guides for Banking, Custom Records, Users, and Webhooks."), E("/llms-guides/authorization.txt", 28, 83, "bank_accounts:*, treasury:*, transfers:*, users:*, departments:*, entities:*, custom_records:* scopes.")]),
                ],
                "Five major domain groupings captured from Ramp llms.txt, authorization scopes, and llms-api.txt.",
            )
            breadth("broad", ["accounting_erp", "cards_spend_controls", "transactions_reimbursements", "bills_vendors_procurement", "banking_users_custom"], [E("/llms.txt", 32, 74, "Spans accounting, cards, spend controls, transactions, reimbursements, bill pay, procurement, banking/treasury, users, custom records, and webhooks.")], "Broad corporate finance and spend-management API.")
            set_mcp_entries(
                [("official_ramp_mcp", "official", "Ramp MCP Server", [E("/llms-guides/ramp-mcp.txt", 1, 23, "Official hosted HTTP callable MCP server at https://mcp.ramp.com/mcp for Claude, ChatGPT, Cursor, Claude Code, Codex, and custom clients (with redirect URI allowlisting)."), E("/llms-guides/authorization.txt", 87, 94, "Uses user-scoped OAuth with Full access or Read-only and 30-day connection expiry.")], "/llms-guides/ramp-mcp.txt", "Official hosted HTTP callable MCP server (https://mcp.ramp.com/mcp) acting with the signed-in user's Ramp role permissions (Full access or Read-only); Ramp also lists a separate Ramp Data MCP server for benchmarks.", "https://mcp.ramp.com/mcp", None)],
                [E("/llms-guides/ramp-mcp.txt", 1, 17, "Official Ramp MCP server documented at https://mcp.ramp.com/mcp.")],
            )
            set_build(
                "conditional",
                "Ramp Developer REST API, Ramp CLI, and official hosted Ramp MCP server.",
                ["Own-business API apps and third-party OAuth installations require a Ramp business account and Admin/Business Owner approval.", "Sandbox access requires submitting a request form whose approval terms were not present in the captured stub.", "Custom MCP client redirect URIs require Ramp allowlisting; partner-only scopes and cards:read_vault require Ramp approval; some endpoints require specific Ramp plan features."],
                ["For own-business workflows, create an OAuth Client Credentials app as a Ramp Admin or connect via Ramp MCP/CLI.", "Request sandbox access via /developer-api/v1/sandbox-access and submit redirect URI allowlist or Technology Partnerships applications for custom/multi-tenant integrations."],
                ["identity.resolution", "auth.oauth2_client_credentials", "auth.oauth2_auth_code", "testing.sandbox_access", "production.admin_approval_required", "api.protocol.rest", "api.breadth", "mcp.official_ramp_mcp"],
                [E("/llms-guides/getting-started.txt", 6, 27, "Admin required for own-business apps; sandbox access request link."), E("/llms-guides/authorization.txt", 86, 123, "Admin approval, plan-feature gating, and partner/vault restrictions."), E("/llms-guides/ramp-mcp.txt", 12, 22, "Official hosted MCP server with redirect URI allowlisting and Admin role gating.")],
                "Strong public REST API, CLI, and official hosted MCP exist, but production use is conditional on Ramp business Admin approval, plan features, and (for custom MCP/partner/vault paths) Ramp vendor/partner approval.",
            )

        # =====================================================================
        # 90: PitchBook (ALL OFFICIAL FETCH ATTEMPTS BLOCKED HTTP 403)
        # =====================================================================
        elif app == 90:
            r["identity"]["resolution"] = claim(
                "identity.resolution",
                None,
                [],
                "unknown",
                (),
                "All 7 official pitchbook.com / www.pitchbook.com HTTP capture attempts in task15-capture-001 through task15-capture-003 returned HTTP 403 (blocked; see fetches[0..6]). Per evidence rules, inaccessible pages do not prove absence of an API or MCP, and third-party/search snippets cannot substitute for captured primary vendor evidence.",
            )
            r["purpose"] = claim("purpose", None, [], "unknown", (), "All 7 official pitchbook.com fetch attempts returned HTTP 403 (fetches[0..6]); no primary snapshot captured.")
            items(r["auth"], [], "All 7 official pitchbook.com fetch attempts returned HTTP 403; auth mechanisms remain unknown pending primary capture.", cov="not_researched")
            for env in ("testing", "production"):
                for k in ("free_access", "trial_access", "sandbox_access", "paid_required", "admin_approval_required", "vendor_approval_required", "partner_approval_required", "contact_sales_required", "self_serve"):
                    unknown_elig(env, k, "All 7 official pitchbook.com fetch attempts returned HTTP 403 (fetches[0..6]); eligibility remains unknown.")
            items(r["api_surface"]["protocols"], [], "All 7 official pitchbook.com fetch attempts returned HTTP 403.", cov="not_researched")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", None, [], "unknown", (), "All 7 official pitchbook.com fetch attempts returned HTTP 403 (fetches[0..6]); public doc availability unverified via static HTTP.")
            items(r["api_surface"]["resource_groups"], [], "All 7 official pitchbook.com fetch attempts returned HTTP 403.", cov="not_researched")
            r["api_surface"]["breadth"] = claim("api.breadth", None, [], "unknown", (), "All 7 official pitchbook.com fetch attempts returned HTTP 403.")
            r["mcp"]["discovery"] = claim("mcp.discovery", None, [], "unknown", (), "All 7 official pitchbook.com fetch attempts returned HTTP 403; MCP status remains unknown pending primary capture.")
            r["mcp"]["entries"] = []
            r["buildability"] = claim("buildability", None, [], "unknown", (), "Cannot infer buildability from HTTP 403 capture blocks on pitchbook.com (fetches[0..6]); requires future approved browser/receipt capture of primary PitchBook docs.")

        # Preserve review pending
        r["review"] = {"status": "pending", "reviewer": None, "reviewed_on": None, "adjudications": []}

    destination.write_text(json.dumps({"records": records}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} records to {destination}")


if __name__ == "__main__":
    build("task15-capture-005", ROOT / "work/task-15-agent/extracted-001.json")
