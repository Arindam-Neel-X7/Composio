"""Task 10 researcher-authored extraction (Marketing, Ads, Email and Social, IDs 31-40, contract v1.1).

Every claim and paraphrase was authored after directly reading the captured primary
and community snapshots in task10-capture-005. Remediated in task10-first-pass-003
after independent AI audit of task10-first-pass-002 to tighten per-claim evidence
attachments and locator line ranges. No model API, synthetic fixture, authenticated
account operation, independent review, or accuracy measurement occurs here.
"""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import research_pipeline as p

SCOPES = {
    31: "Google Ads API (gRPC/REST) and official Google Ads MCP server; Cloud-project access tiers and OAuth 2.0; test accounts versus production access",
    32: "Meta Marketing API (Graph API) for Facebook/Instagram Ads; OAuth 2.0 access tokens and App Review tiers; test/development versus production access",
    33: "LinkedIn Marketing API / Advertising API; OAuth 2.0 and Development vs Standard access tiers; testing versus production ad accounts",
    34: "GoHighLevel (HighLevel) API v2 and official MCP server; OAuth 2.0 and Private Integration Tokens; paid subscription plans and agency/sub-account scopes",
    35: "Mailchimp Marketing API v3.0 (distinct from Transactional/Mandrill API); API key and OAuth 2.0 auth; Free vs paid Marketing plans",
    36: "Klaviyo REST API and official Klaviyo MCP server; Private API keys, Public site IDs, and OAuth 2.0; Free vs paid platform plans",
    37: "systeme.io Public API and official MCP server; API key and MCP key auth; Free vs paid subscription plans",
    38: "Pinterest API v5; OAuth 2.0 and Trial vs Standard access tiers; sandbox/trial testing versus production access",
    39: "Meta Threads API (graph.threads.net); OAuth 2.0 user access tokens and App Review; Development/tester mode versus Live production access",
    40: "Twilio SendGrid Web API v3; API key Bearer auth; Free/Trial vs paid Email API plans; community MCP ecosystem",
}


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
        assert len(matches) == 1, f"Expected 1 match for ({app_id}, {substr!r}), got {len(matches)}"
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

        AUTH_MAP = {
            "oauth2": "OAuth2",
            "api_key": "API_key",
            "basic": "Basic",
            "bearer_token": "Bearer_token",
        }

        def auth(key, method, details, ev, subcontext, scopes=(), status="observed", refs=()):
            return claim(
                "auth." + key,
                {
                    "method": AUTH_MAP.get(method, method),
                    "context": subcontext,
                    "scopes": list(scopes),
                    "details": details,
                },
                ev,
                status,
                refs,
                "Scoped mechanism from primary documentation; no credentials obtained or authenticated call executed.",
            )

        def items(target, entries, notes, cov="partial"):
            target.update(coverage_status=cov, items=entries, notes=notes)

        def elig(env, key, val, ev, rationale, status="observed", refs=()):
            r["credential_eligibility"][env][key] = claim(f"{env}.{key}", val, ev, status, refs, rationale)

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
                src_url = find_cap(app, substr)["spec"]["url"]
                out.append(
                    claim(
                        f"mcp.{key}",
                        {
                            "origin": origin,
                            "name": name,
                            "source_url": src_url,
                            "repository_url": repo,
                            "server_url": server,
                            "scope": tool_scope,
                            "operational_check": op,
                        },
                        ev,
                    )
                )
            r["mcp"]["entries"] = out
            r["mcp"]["discovery"] = claim("mcp", "found", discovery_ev)

        def buildability(verdict, workflow, blockers, steps, refs, ev, rationale):
            r["buildability"] = claim(
                "buildability",
                {
                    "verdict": verdict,
                    "scope": workflow,
                    "blockers": blockers,
                    "next_steps": steps,
                },
                ev,
                status="inferred",
                refs=refs,
                rationale=rationale,
            )

        # Initialize default unknown eligibility claims
        for env in ("testing", "production"):
            r["credential_eligibility"][env]["context"] = scope
            for k in (
                "free_access", "trial_access", "sandbox_access", "paid_required",
                "admin_approval_required", "vendor_approval_required",
                "partner_approval_required", "contact_sales_required", "self_serve",
            ):
                r["credential_eligibility"][env][k] = claim(
                    f"{env}.{k}",
                    None,
                    status="unknown",
                    rationale="Not explicitly established for this environment in checked public sources.",
                )

        # =====================================================================
        # APP 31: Google Ads
        # =====================================================================
        if app == 31:
            r["identity"]["resolution"] = claim(
                "identity",
                "Google Ads API by Google — programmatic interface for managing Google Ads accounts, campaigns, reporting, and conversions.",
                [E("/docs/start", 429, 455, "Introduction defines Google Ads API as Google's programmatic interface for managing Google Ads accounts, campaigns, reporting, and conversions.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Programmatic advertising platform API for managing Google Ads accounts, campaigns, GAQL reporting, conversions, and Smart Bidding, plus an official MCP server.",
                [
                    E("/docs/start", 429, 455, "Lists automated account management, GAQL custom reporting, Performance Max/Search/Demand Gen/Shopping/Video/App campaign management, conversion measurement, and Smart Bidding."),
                    E("mcp-server", 473, 496, "Documents the official Google Ads MCP server over local stdio or remote streamable-http."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_user_and_service",
                        "oauth2",
                        "OAuth 2.0 (single-user, multi-user, or service account workflow) configured in the same Google Cloud project where Google Ads API is enabled; ADC supported for local MCP.",
                        [
                            E("oauth/overview", 429, 480, "Google Ads API uses OAuth 2.0 across single-user, multi-user, and service account workflows configured in the API-enabled Google Cloud project."),
                            E("google-ads-mcp/main/README.md", 47, 63, "Official MCP server supports OAuth 2.0 ADC with https://www.googleapis.com/auth/adwords scope or FastMCP OAuth proxy."),
                        ],
                        "Google Ads API and official Google Ads MCP server",
                        scopes=("https://www.googleapis.com/auth/adwords",),
                    ),
                ],
                "Legacy developer tokens were sunset on September 9, 2026; API access levels are now managed on the Google Cloud project (access-levels L68-L73, mcp-server L486-L489). Note oauth/overview summary line 430 still contains a legacy reference to a developer token.",
                cov="checked_sources",
            )
            # Testing eligibility
            elig(
                "testing", "sandbox_access", True,
                [E("best-practices/testing", 442, 446, "Test accounts are available for development purposes to validate application code and configuration.")],
                "Dedicated Google Ads test accounts are documented for development and testing.",
            )
            elig(
                "testing", "free_access", True,
                [E("mcp-server", 480, 482, "Enabling the Google Ads API on a Google Cloud project grants Test access for test accounts.")],
                "Enabling the API on a Google Cloud project grants Test access automatically without a separate API fee documented.",
            )
            elig(
                "testing", "vendor_approval_required", False,
                [E("mcp-server", 480, 482, "Enabling the Google Ads API grants Test access for testing read and mutate workflows against test accounts.")],
                "Test access is granted automatically upon enabling the API.",
            )
            elig(
                "testing", "self_serve", True,
                [
                    E("mcp-server", 480, 482, "Developers create/select a Google Cloud project and enable the Google Ads API for Test access."),
                    E("best-practices/testing", 477, 494, "Developers create separate test credentials and OAuth refresh tokens or service accounts for test accounts."),
                ],
                "Test account access and OAuth test credentials are self-serve.",
            )
            # Production eligibility
            elig(
                "production", "vendor_approval_required", True,
                [E("access-levels", 68, 216, "Production account access requires applying for Explorer (automated review, feature-restricted), Basic (requires brand verification, 15,000 ops/day), or Standard (manual compliance audit, unlimited ops/day) access levels on the Google Cloud project.")],
                "Production API calls fail until the Google Cloud project is approved for Explorer, Basic, or Standard access.",
            )
            elig(
                "production", "self_serve", False,
                [E("access-levels", 161, 215, "Upgrading from Test to Explorer, Basic (brand verification), or Standard (manual compliance audit) requires Google access-level application and review.")],
                "Production access is gated by Google's Explorer/Basic/Standard review tiers rather than purely self-serve activation.",
            )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("/docs/start", 424, 535, "Public Google Ads API documentation covers quickstart, OAuth, REST, client libraries, GAQL reporting, and MCP server.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("best-practices/testing", 508, 512, "Documents the Google Ads REST API interface, curl examples, and REST explorer.")]),
                    claim("api.protocol.sdk", "SDK", [E("/docs/start", 512, 520, "Documents official client libraries for Java, .NET, PHP, Python, Ruby, and Perl.")]),
                ],
                "Official REST interface and multi-language client libraries (which use gRPC/protobuf under the hood) are documented.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("accounts_hierarchy", "Customers, account hierarchies, and user access management", [E("/docs/start", 437, 439, "Automated account management: create/link accounts, manage hierarchies, automate user access."), E("api-structure", 436, 441, "Top-level customer resource containing campaigns.")]),
                    group("campaigns_ads", "Campaigns (Search, Performance Max, Shopping, Video, App, Demand Gen), ad groups, ads, budgets, and assets", [E("/docs/start", 443, 451, "Create and update Performance Max, Search, Demand Gen, Shopping, Video, and App campaigns, budgets, and assets."), E("api-structure", 440, 445, "Customer -> campaigns -> ad groups -> ad group ads hierarchy.")]),
                    group("reporting_gaql", "Reporting and performance metrics via Google Ads Query Language (GAQL)", [E("/docs/start", 440, 442, "Query performance metrics, segments, and resource attributes using GAQL.")]),
                    group("conversions_bidding", "Conversion measurement and Smart Bidding strategies", [E("/docs/start", 452, 455, "Upload click, call, and enhanced conversions and configure automated bidding strategies.")]),
                    group("planning_audiences", "Keyword planning, audience insights, and reach planning (Basic/Standard tiers)", [E("access-levels", 133, 155, "Lists KeywordPlanService, KeywordPlanIdeaService, AudienceInsightsService, and ReachPlanService (restricted in Explorer, available in Basic/Standard).")]),
                ],
                "Core Google Ads API resource domains from official overview, structure, and access-levels docs.",
                cov="partial",
            )
            breadth(
                "broad",
                ["accounts_hierarchy", "campaigns_ads", "reporting_gaql", "conversions_bidding", "planning_audiences"],
                [E("/docs/start", 433, 455, "Covers accounts, multiple campaign types, GAQL reporting, conversions, and bidding."), E("access-levels", 133, 155, "Includes keyword planning and audience/reach planning services.")],
                "Inferred broad API surface spanning five distinct advertising domains (account hierarchy, multi-format campaigns/assets, GAQL reporting, conversions/bidding, and keyword/audience planning).",
            )
            set_mcp_entries(
                [
                    (
                        "official_google_ads",
                        "official",
                        "Google Ads MCP Server (googleads/google-ads-mcp)",
                        [
                            E("mcp-server", 473, 557, "Official Google Ads MCP server developer integration guide; supports local stdio (ADC) and remote streamable-http (FastMCP OAuth proxy) for reporting, asset creation, video upload, and label management."),
                            E("google-ads-mcp/main/README.md", 1, 145, "Official googleads/google-ads-mcp repository exposing callable MCP tools (GAQL queries, customer discovery, metadata, guarded mutations via Propose & Confirm) and MCP resources."),
                        ],
                        "google-ads-mcp/main/README.md",
                        "Callable MCP server (local stdio via ADC or self-hosted Streamable HTTP via FastMCP OAuth proxy) exposing read/reporting GAQL tools and guarded mutate tools for Google Ads accounts.",
                        None,
                        "https://github.com/googleads/google-ads-mcp",
                    ),
                ],
                [
                    E("mcp-server", 473, 496, "Official Google Ads MCP server guide."),
                    E("google-ads-mcp/main/README.md", 1, 30, "Official googleads/google-ads-mcp repository."),
                ],
            )
            buildability(
                "conditional",
                "Build Google Ads campaign reporting and management agent integration via REST/SDK or official Google Ads MCP server",
                [
                    "Production account calls require Google Cloud project approval for Explorer (feature-restricted), Basic (brand verification), or Standard (manual compliance audit) access.",
                    "Test accounts cannot test all production features such as live performance reports.",
                ],
                [
                    "Enable Google Ads API on a Google Cloud project for immediate Test account prototyping.",
                    "Complete brand verification and apply for Basic access (or Explorer for initial production read/mutate) before production rollout.",
                ],
                ["identity", "auth.oauth2_user_and_service", "testing.sandbox_access", "production.vendor_approval_required", "api.protocol.rest", "mcp.official_google_ads"],
                [
                    E("access-levels", 73, 215, "Production access requires Explorer, Basic, or Standard access level approval."),
                    E("mcp-server", 480, 489, "Test access is immediate; production requires Explorer/Basic/Standard approval."),
                    E("best-practices/testing", 430, 469, "Test accounts cannot test production-only features such as performance reports."),
                ],
                "Conditional: immediate self-serve Test account development and official MCP server exist, but production calls are gated by Google's Explorer/Basic/Standard access-level review.",
            )

        # =====================================================================
        # APP 32: Meta Ads
        # =====================================================================
        elif app == 32:
            r["identity"]["resolution"] = claim(
                "identity",
                "Meta Marketing API (Ads and Commerce) by Meta — Graph API interface for automating advertising across Facebook, Instagram, Messenger, and WhatsApp.",
                [
                    E("marketing-api/overview", 1, 17, "Marketing API automates advertising across Meta technologies (Facebook, Instagram, Messenger, WhatsApp)."),
                    E("ads-commerce/llms.txt", 1, 2, "Ads and Commerce Guides and Documentation for Meta's ads and commerce APIs."),
                    E("docs/marketing-apis/", 1198, 1198, "The Marketing API is a collection of Graph API endpoints used to advertise across Meta technologies."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Programmatic Meta advertising API for creating and managing campaigns, ad sets, creatives, audiences, catalogs, and insights, plus a Meta-hosted Ads MCP Server.",
                [
                    E("marketing-api/overview", 1, 27, "Covers ad campaigns, ad sets, ad creatives, ads, budgets, audiences, and performance insights."),
                    E("ads-mcp-server-overview.md", 1, 17, "Meta-hosted Ads MCP Server at https://mcp.facebook.com/ads for reporting, ad creation, catalogs, signals, A/B tests, and activity logs."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_user_token",
                        "oauth2",
                        "OAuth 2.0 Facebook Login / dialog/oauth returning User Access Tokens scoped with ads_read and ads_management (and ads_mcp_management for Ads MCP).",
                        [
                            E("overview/authorization", 27, 46, "OAuth dialog https://www.facebook.com/v27.0/dialog/oauth requesting ads_management and ads_read scopes."),
                            E("ads-mcp-server-get-started.md", 9, 27, "Ads MCP supports Facebook Login for Business OAuth and User Access Tokens with ads_mcp_management."),
                        ],
                        "Meta Marketing API and Meta Ads MCP Server (user-authorized access)",
                        scopes=("ads_read", "ads_management", "ads_mcp_management"),
                    ),
                    auth(
                        "system_user_token",
                        "bearer_token",
                        "Business Manager System User Access Tokens for server-to-server programmatic access (Limited access allows 1 system user + 1 admin system user; Full access allows 10; Ads MCP requires Employee-role system user tokens).",
                        [
                            E("overview/authorization", 16, 22, "System users: Limited access allows 1 system user and 1 admin system user; Full access allows 10 system users and 1 admin system user."),
                            E("ads-mcp-server-get-started.md", 14, 17, "System user access tokens supported for server-to-server Ads MCP access (Employee-role only; Admin-role cannot access Ads MCP)."),
                        ],
                        "Server-to-server Business Manager and Ads MCP integrations",
                        scopes=("ads_mcp_management",),
                    ),
                ],
                "Both user OAuth tokens and Business Manager system user tokens are documented across Marketing API and Ads MCP.",
                cov="checked_sources",
            )
            # Testing eligibility
            elig(
                "testing", "sandbox_access", False,
                [E("overview/authorization", 11, 11, "Explicit warning: Calls on ANY access level are against production data.")],
                "Meta explicitly warns that Marketing API calls on any access level operate against production data rather than an isolated sandbox.",
            )
            elig(
                "testing", "vendor_approval_required", False,
                [E("overview/authorization", 16, 34, "Limited access is automatically granted when adding Marketing API; Business apps are automatically approved for Standard access to manage own ad accounts.")],
                "Limited access and Standard permission access for own ad accounts are automatically granted without App Review.",
            )
            elig(
                "testing", "self_serve", True,
                [E("overview/authorization", 16, 34, "Adding the Marketing API product automatically grants Limited access and Standard access for development and own-account management.")],
                "Self-serve developer app setup grants Limited/Standard access for development and own ad accounts.",
            )
            # Production eligibility
            elig(
                "production", "vendor_approval_required", True,
                [E("overview/authorization", 15, 55, "Full access (production apps for live advertisers) and Advanced access (managing other people's ad accounts) require Meta App Review, 500 Marketing API calls in 15 days with <15% error rate, and Business Verification for sensitive data.")],
                "Multi-tenant/production Marketing API apps require Meta App Review (Full access / Advanced access) and Business Verification.",
            )
            elig(
                "production", "self_serve", False,
                [E("overview/authorization", 15, 39, "Limited access is for development only and not for production apps running for live advertisers; Full access and Advanced access require App Review.")],
                "Production multi-advertiser access requires Meta App Review rather than self-serve activation.",
            )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("marketing-api/overview", 1, 29, "Public Meta Marketing API overview and full documentation index at developers.facebook.com.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim(
                        "api.protocol.rest", "REST",
                        [
                            E("facebook-python-business-sdk/main/README.md", 376, 385, "Curl HTTP GET/POST requests to Graph API endpoints at https://graph.facebook.com/."),
                            E("docs/marketing-apis/", 1198, 1198, "Marketing API is a collection of Graph API HTTP endpoints."),
                        ],
                    ),
                    claim(
                        "api.protocol.sdk", "SDK",
                        [
                            E("facebook-python-business-sdk/main/README.md", 1, 10, "Official Facebook Business SDK for Python (facebook_business) wrapping Marketing API."),
                            E("facebook-python-business-sdk/main/README.md", 301, 302, "Business SDK includes a server-side client for the Conversions API."),
                        ],
                    ),
                    claim("api.protocol.cli", "CLI", [E("ads-commerce/llms.txt", 4, 12, "Documents official Meta Ads CLI under Ads AI Connectors.")]),
                ],
                "Graph API HTTP/REST interface, official Business SDKs, and Ads CLI are documented.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("campaigns_adsets_ads", "Ad campaigns, ad sets, ad creatives, and ads", [E("marketing-api/overview", 8, 27, "Documents Ad campaigns, Ad sets, Ad creatives, and Ads across Facebook, Instagram, Messenger, and WhatsApp.")]),
                    group("audiences_targeting", "Custom audiences, lookalike audiences, and targeting", [E("docs/marketing-apis/", 278, 310, "Lists Customer File, Lookalike, Engagement, Mobile App, Website, Offline, and Dynamic Custom Audiences plus Advantage+ Audience targeting.")]),
                    group("insights_reporting", "Insights API and delivery/performance reporting", [E("docs/marketing-apis/", 313, 343, "Lists Insights API, Ads Webhooks, Content Delivery Reports, and Publisher Delivery Reports.")]),
                    group("catalogs_conversions", "Product catalogs and Conversions API (web/app/offline events)", [E("facebook-python-business-sdk/main/README.md", 302, 302, "Documents Conversions API for server-side web, app, and offline events."), E("ads-commerce/llms.txt", 41, 60, "Documents Product Catalog API, Feed API, and Catalog Batch API.")]),
                ],
                "Core Meta Marketing API and Ads/Commerce domains from primary docs and official SDK.",
                cov="partial",
            )
            breadth(
                "broad",
                ["campaigns_adsets_ads", "audiences_targeting", "insights_reporting", "catalogs_conversions"],
                [E("marketing-api/overview", 1, 27, "Campaign/ad/creative management and insights."), E("docs/marketing-apis/", 278, 343, "Audiences, Insights, Webhooks, and Delivery Reports."), E("ads-commerce/llms.txt", 41, 60, "Product Catalog APIs.")],
                "Inferred broad API surface spanning campaign/ad management, audience targeting, performance insights/webhooks, product catalogs, and Conversions API.",
            )
            set_mcp_entries(
                [
                    (
                        "official_meta_ads",
                        "official",
                        "Meta Ads MCP Server",
                        [
                            E("ads-mcp-server-overview.md", 1, 17, "Official Meta-hosted remote MCP server at https://mcp.facebook.com/ads exposing callable tools across 7 categories (reporting, ad creation/management, catalogs, signals/datasets, help, A/B tests, activity logs)."),
                            E("ads-mcp-server-get-started.md", 2, 49, "Supports OAuth (Facebook Login for Business), User access token, and Employee-role System User access token via Authorization: Bearer against https://mcp.facebook.com/ads."),
                        ],
                        "ads-mcp-server-overview.md",
                        "Official Meta-hosted remote callable MCP server (HTTP/JSON-RPC) for managing Meta Ads campaigns, reporting, catalogs, signals, A/B tests, and activity logs.",
                        "https://mcp.facebook.com/ads",
                        None,
                    ),
                    (
                        "community_pipeboard",
                        "community",
                        "Pipeboard Meta Ads MCP (pipeboard-co/meta-ads-mcp)",
                        [E("pipeboard-co/meta-ads-mcp/main/README.md", 1, 76, "Independent open-source community Meta Ads MCP server (42 callable tools for campaigns, ad sets, ads, creatives, insights) hosted at https://meta-ads.mcp.pipeboard.co/ or self-hosted.")],
                        "pipeboard-co/meta-ads-mcp/main/README.md",
                        "Community callable MCP server (hosted remote or self-hosted) exposing 42 Meta Ads management and reporting tools; community repo establishes its own implementation only.",
                        "https://meta-ads.mcp.pipeboard.co/",
                        None,
                    ),
                ],
                [
                    E("ads-mcp-server-overview.md", 1, 17, "Official Meta-hosted Ads MCP Server."),
                    E("pipeboard-co/meta-ads-mcp/main/README.md", 1, 30, "Community Meta Ads MCP repository."),
                ],
            )
            buildability(
                "conditional",
                "Build Meta Ads campaign management and reporting agent integration via Marketing API or official Meta Ads MCP Server",
                [
                    "Production multi-advertiser apps require Meta App Review (Full access / Advanced access), 500 API calls in 15 days with <15% error rate, and Business Verification.",
                    "All Marketing API calls on any access level operate against production data (no isolated sandbox).",
                ],
                [
                    "Create a Meta Business app to get automatic Limited/Standard access for own-account prototyping, or connect to Meta's hosted Ads MCP server (https://mcp.facebook.com/ads).",
                    "Submit App Review and Business Verification before onboarding external advertiser accounts.",
                ],
                ["identity", "auth.oauth2_user_token", "testing.vendor_approval_required", "production.vendor_approval_required", "api.protocol.rest", "mcp.official_meta_ads"],
                [
                    E("overview/authorization", 11, 55, "Calls hit production data; Limited/Standard access is automatic for own accounts, while Full/Advanced access requires App Review and Business Verification."),
                    E("ads-mcp-server-overview.md", 1, 6, "Official Meta-hosted Ads MCP server available at https://mcp.facebook.com/ads."),
                ],
                "Conditional: own-account prototyping and Meta's hosted Ads MCP server are accessible, but multi-tenant production apps require Meta App Review and Business Verification.",
            )

        # =====================================================================
        # APP 33: LinkedIn Ads
        # =====================================================================
        elif app == 33:
            r["identity"]["resolution"] = claim(
                "identity",
                "LinkedIn Marketing API Program / Advertising API by LinkedIn (documented on Microsoft Learn) — APIs for LinkedIn ad campaign management, audience targeting, and analytics.",
                [E("en-us/linkedin/marketing/", 1, 26, "LinkedIn Marketing API Program on Microsoft Learn offers Advertising APIs for campaign management, audience targeting, reporting, and analytics.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Programmatic LinkedIn advertising and marketing APIs for managing ad accounts, campaigns, creatives, matched audiences, conversions, and reporting analytics.",
                [
                    E("en-us/linkedin/marketing/", 7, 87, "Covers Advertising APIs (Campaign Management, Reporting/Analytics), Matched Audiences, Audience Insights, Media Planning, and Conversions."),
                    E("create-and-manage-campaigns", 31, 43, "Covers Ad Accounts, Campaigns, and Creatives."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_3legged",
                        "oauth2",
                        "OAuth 2.0 3-legged Member Authorization flow requiring explicit LinkedIn member consent plus appropriate Ad Account role (ACCOUNT_BILLING_ADMIN, ACCOUNT_MANAGER, CAMPAIGN_MANAGER, etc.); 2-legged client credentials are not supported for Advertising API scopes.",
                        [
                            E("linkedin/marketing/getting-started", 94, 135, "Advertising API permissions (r_ads, rw_ads, r_ads_reporting, rw_organization_admin, r_organization_admin, r_basicprofile) are 3-legged member permissions requiring explicit consent and Ad Account / Company Page roles."),
                            E("authentication/authentication", 27, 41, "LinkedIn API uses OAuth 2.0 3-legged Member Authorization flow."),
                        ],
                        "LinkedIn Advertising API (all campaign, reporting, and ad account endpoints)",
                        scopes=("r_ads", "rw_ads", "r_ads_reporting", "rw_organization_admin", "r_organization_admin", "r_basicprofile"),
                    ),
                ],
                "2-legged OAuth Client Credentials exists on LinkedIn generally (authentication L42-L47), but getting-started L99 explicitly restricts Advertising API scopes to 3-legged member authorization.",
                cov="checked_sources",
            )
            # Testing eligibility
            elig(
                "testing", "vendor_approval_required", True,
                [
                    E("linkedin/marketing/getting-started", 80, 86, "Once accepted into the Development Tier, apps can manage up to 5 ad accounts and cannot create new accounts via API."),
                    E("linkedin/marketing/quick-start", 42, 65, "Requires creating a developer app, reviewing restricted use cases, and getting Development tier access; Token Generator tool available for testing."),
                ],
                "Even Development Tier testing requires application acceptance into the LinkedIn Marketing API Program.",
            )
            elig(
                "testing", "self_serve", False,
                [E("linkedin/marketing/getting-started", 80, 86, "Application must be accepted into the Development Tier before managing up to 5 ad accounts.")],
                "Development Tier access requires LinkedIn program acceptance rather than instant self-serve activation.",
            )
            # Production eligibility
            elig(
                "production", "vendor_approval_required", True,
                [E("linkedin/marketing/quick-start", 70, 85, "Upgrading from Development tier to Advertising API Standard tier requires submitting a tier upgrade request with a video demonstrating platform functionality (and screen recording/test credentials for Community Management Standard tier).")],
                "Production Standard Tier access requires LinkedIn review and video demo approval.",
            )
            elig(
                "production", "admin_approval_required", True,
                [E("linkedin/marketing/getting-started", 65, 135, "API calls require an authenticated LinkedIn member who holds an appropriate Ad Account role (e.g., ACCOUNT_BILLING_ADMIN, CAMPAIGN_MANAGER) or Company Page ADMINISTRATOR role.")],
                "Member tokens only work on ad accounts/pages where the member has sufficient admin/manager roles.",
            )
            elig(
                "production", "self_serve", False,
                [E("linkedin/marketing/quick-start", 70, 70, "Advertising API Standard tier requires formal upgrade application and video demo review.")],
                "Production Standard Tier requires vendor review.",
            )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("en-us/linkedin/marketing/", 1, 100, "Public LinkedIn Marketing API documentation hosted on Microsoft Learn.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim(
                        "api.protocol.rest", "REST",
                        [
                            E("authentication/authentication", 49, 49, "Documents RESTful OAuth calls to the LinkedIn Authentication server."),
                            E("linkedin/marketing/quick-start", 55, 77, "Documents REST endpoints /adAccountUsers and /organizationAcls."),
                        ],
                    ),
                ],
                "REST API with versioned endpoints and webhooks (quick-start L119) is documented.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("campaigns_accounts", "Ad Accounts, Campaign Groups, Campaigns, and Creatives", [E("en-us/linkedin/marketing/", 23, 24, "Advertising APIs for campaign management."), E("create-and-manage-campaigns", 31, 288, "Campaign schema, campaign groups, ad formats, budgets, bidding, targeting criteria, and serving statuses.")]),
                    group("reporting_analytics", "Reporting, Analytics, and Company Engagement Insights", [E("en-us/linkedin/marketing/", 26, 27, "Reporting and Analytics APIs."), E("en-us/linkedin/marketing/", 87, 87, "Company-level paid/organic impressions, clicks, leads, and engagement insights.")]),
                    group("audiences_targeting", "Matched Audiences, Predictive Audiences, and Audience Insights", [E("en-us/linkedin/marketing/", 49, 66, "Matched Audiences (contact lists, website retargeting, account targeting), Predictive Audiences, and Audience Insights APIs.")]),
                    group("media_planning_conversions", "Media Planning and Conversions API", [E("en-us/linkedin/marketing/", 68, 76, "Media Planning API and conversion event tracking for LinkedIn ad campaigns.")]),
                ],
                "Core LinkedIn Marketing API domains from Microsoft Learn overview and campaign management reference.",
                cov="partial",
            )
            breadth(
                "broad",
                ["campaigns_accounts", "reporting_analytics", "audiences_targeting", "media_planning_conversions"],
                [E("en-us/linkedin/marketing/", 23, 87, "Spans Campaign Management, Reporting/Analytics, Matched Audiences, Audience Insights, Media Planning, and Conversions.")],
                "Inferred broad API surface across four distinct LinkedIn advertising domains.",
            )
            set_mcp_entries(
                [
                    (
                        "community_adspirer",
                        "community",
                        "Adspirer Ads MCP (amekala/ads-mcp)",
                        [E("amekala/ads-mcp/main/README.md", 1, 160, "Community cross-platform remote MCP server at https://mcp.adspirer.com/mcp (Streamable HTTP, OAuth 2.1 + PKCE) exposing 54 callable LinkedIn Ads tools (sponsored content, lead-gen forms, campaign groups, targeting facets, audience insights, conversion tracking).")],
                        "amekala/ads-mcp/main/README.md",
                        "Third-party/community remote callable MCP server exposing 54 LinkedIn Ads tools alongside other ad networks; community repo establishes its own implementation only (no official LinkedIn Ads MCP found in checked Microsoft Learn docs).",
                        "https://mcp.adspirer.com/mcp",
                        "https://github.com/amekala/ads-mcp",
                    ),
                ],
                [E("amekala/ads-mcp/main/README.md", 1, 55, "Community cross-platform Ads MCP repository covering LinkedIn Ads.")],
            )
            buildability(
                "conditional",
                "Build LinkedIn Ads campaign management and reporting integration via REST API",
                [
                    "Requires LinkedIn Marketing API Program acceptance for Development Tier (max 5 ad accounts, no account creation) and video-demo review for Standard Tier production access.",
                    "Requires 3-legged OAuth member consent with sufficient Ad Account/Company Page roles; no official LinkedIn Ads MCP server found in checked vendor docs.",
                ],
                [
                    "Create a LinkedIn Developer app and apply for Advertising API Development Tier access.",
                    "Build and record the OAuth + campaign workflow demo to apply for Standard Tier before multi-account production use.",
                ],
                ["identity", "auth.oauth2_3legged", "testing.vendor_approval_required", "production.vendor_approval_required", "api.protocol.rest", "mcp.community_adspirer"],
                [
                    E("linkedin/marketing/getting-started", 80, 99, "Development tier limits and 3-legged OAuth requirements."),
                    E("linkedin/marketing/quick-start", 70, 70, "Standard tier requires upgrade request with video demo."),
                ],
                "Conditional: well-documented REST API, but both Development and Standard production tiers require LinkedIn application/review approval.",
            )

        # =====================================================================
        # APP 34: GoHighLevel
        # =====================================================================
        elif app == 34:
            r["identity"]["resolution"] = claim(
                "identity",
                "GoHighLevel (HighLevel) CRM & Marketing Platform — all-in-one agency/business CRM, funnel builder, email/SMS marketing, and automation platform with API v2 (LeadConnector).",
                [
                    E("marketplace.gohighlevel.com/docs/", 1, 49, "HighLevel API Documentation: Complete REST API documentation for the HighLevel CRM platform at services.leadconnectorhq.com."),
                    E("gohighlevel.com/pricing", 49, 172, "All-in-one agency platform replacing CRM, funnel builder, email marketing software, appointment tools, and automations."),
                    E("Authorization/OAuth2.0/", 74, 76, "HighLevel v2 APIs with OAuth 2.0 Authorization Code Grant flow."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "All-in-one agency CRM, funnel, email/SMS marketing, and workflow automation platform exposing LeadConnector REST API v2 and an official 717-action MCP Server.",
                [
                    E("marketplace.gohighlevel.com/docs/", 1, 49, "REST API covering CRM/Contacts, SMS/email/call conversations, webhooks, SDKs, and CLI at services.leadconnectorhq.com."),
                    E("gohighlevel.com/pricing", 49, 172, "Agency CRM, funnel builder, email/SMS marketing, and automations."),
                    E("Authorization/OAuth2.0/", 74, 76, "HighLevel v2 APIs."),
                    E("docs/other/mcp/", 70, 116, "Official HighLevel MCP Server exposing 717 supported actions across 38 feature areas."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_marketplace",
                        "oauth2",
                        "OAuth 2.0 Authorization Code Grant flow via HighLevel Marketplace (POST https://services.leadconnectorhq.com/oauth/token); access tokens expire after ~24h (86,399s) and refresh tokens are valid up to 1 year (single-use rotating); PKCE/S256 not supported for Marketplace install flow.",
                        [E("Authorization/OAuth2.0/", 74, 219, "OAuth 2.0 Authorization Code Grant for v2 APIs; 24h access tokens, 1-year rotating refresh tokens; granular scopes like calendars.readonly, calendars.write, businesses.readonly, companies.readonly.")],
                        "GoHighLevel Marketplace public/private apps (agency or sub-account installations)",
                        scopes=("calendars.readonly", "calendars.write", "businesses.readonly", "businesses.write"),
                    ),
                    auth(
                        "private_integration_token",
                        "bearer_token",
                        "Private Integration Tokens (PIT) — static scoped Bearer tokens generated from account settings (Authorization: Bearer <TOKEN>), replacing EOL API v1.0 global API keys.",
                        [E("PrivateIntegrationsToken/", 76, 128, "Private Integration Tokens are static/fixed scoped OAuth2-style Bearer tokens for API v2.0 replacing end-of-life API v1.0 API keys.")],
                        "Single-account / internal API v2 integrations (agency or sub-account)",
                    ),
                ],
                "Legacy API v1.0 API keys have reached end-of-life (PrivateIntegrationsToken L86); v2 uses OAuth 2.0 or Private Integration Tokens.",
                cov="checked_sources",
            )
            # Testing eligibility
            elig(
                "testing", "trial_access", True,
                [E("gohighlevel.com/pricing", 36, 168, "14-day FREE trial on any plan with full access to chosen tier features.")],
                "GoHighLevel offers a self-serve 14-day free trial across plans.",
            )
            elig(
                "testing", "self_serve", True,
                [
                    E("gohighlevel.com/pricing", 36, 168, "Self-serve 14-day free trial signup."),
                    E("PrivateIntegrationsToken/", 80, 102, "Generate Private Integration Tokens directly from account settings."),
                ],
                "Trial signup and Private Integration Token generation are self-serve.",
            )
            # Production eligibility
            elig(
                "production", "paid_required", True,
                [E("gohighlevel.com/pricing", 41, 184, "Paid plans: Agency Starter $97/mo (3 sub-accounts), Unlimited $297/mo (includes Basic API access line 74), Pro $497/mo; billing begins automatically after 14-day trial unless canceled.")],
                "Ongoing production use requires a paid subscription plan after the 14-day trial (plus usage-based telecom/AI fees).",
            )
            elig(
                "production", "admin_approval_required", True,
                [
                    E("PrivateIntegrationsToken/", 115, 120, "By default, agency admins create and manage Private Integrations and control user-level permissions."),
                    E("Authorization/OAuth2.0/", 108, 108, "Location/agency admin must visit the Installation URL to install an OAuth app."),
                ],
                "Agency or location admin role is required to create Private Integration Tokens or install OAuth apps.",
            )
            r["credential_eligibility"]["production"]["vendor_approval_required"] = claim(
                "production.vendor_approval_required",
                None,
                [
                    E("Authorization/OAuth2.0/", 84, 84, "Public Marketplace apps are visible and installable by all users only once approved."),
                    E("PrivateIntegrationsToken/", 80, 91, "Private Integration Tokens are generated directly in the UI without marketplace review."),
                ],
                status="unknown",
                rationale="Path-dependent: Public Marketplace OAuth apps require HighLevel approval (OAuth2.0 L84), whereas Private Integration Tokens are self-generated by agency admins without vendor review; not collapsed to a single boolean per Contract v1.1.",
            )
            elig(
                "production", "self_serve", True,
                [
                    E("gohighlevel.com/pricing", 164, 174, "Month-to-month self-serve plans ($97/$297/$497); Enterprise is custom."),
                    E("PrivateIntegrationsToken/", 80, 105, "Self-serve Private Integration Token generation from account settings."),
                ],
                "Paid plans and Private Integration Token / private OAuth setup are self-serve (Public Marketplace distribution requires review).",
            )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("marketplace.gohighlevel.com/docs/", 1, 49, "Public HighLevel API Documentation at marketplace.gohighlevel.com/docs/.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("marketplace.gohighlevel.com/docs/", 11, 41, "Complete REST API at https://services.leadconnectorhq.com/.")]),
                    claim("api.protocol.sdk", "SDK", [E("marketplace.gohighlevel.com/docs/", 3, 37, "Documents official SDKs and code examples.")]),
                    claim("api.protocol.cli", "CLI", [E("marketplace.gohighlevel.com/docs/", 3, 3, "Navigation includes official HighLevel CLI.")]),
                ],
                "REST API, SDKs, CLI, and 50+ webhook events are documented.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("crm_contacts_opportunities", "Contacts, Companies, Opportunities/Pipelines, and Calendars", [E("marketplace.gohighlevel.com/docs/", 15, 26, "CRM & Contacts, Calendar & Events, and Opportunities/Pipelines."), E("docs/other/mcp/", 120, 128, "Calendars/bookings, Contacts, Companies, and Sales Pipeline deals.")]),
                    group("conversations_messaging", "SMS, Email, and Call Conversations", [E("marketplace.gohighlevel.com/docs/", 19, 19, "Handle SMS, email, and call communications; send messages and manage threads.")]),
                    group("marketing_funnels_social", "Campaigns, Email Marketing, Funnels/Websites, Social Planner, and Brand Boards", [E("Authorization/OAuth2.0/", 28, 62, "Lists Brand Boards, Campaigns, Email, Funnels, and Social Planner APIs."), E("docs/other/mcp/", 144, 165, "Social Planner, Email marketing, Ad results, Affiliates, Campaigns, Funnels and websites.")]),
                    group("payments_webhooks_courses", "Invoices/Payments, Webhooks (50+ events), Courses, and Projects", [E("marketplace.gohighlevel.com/docs/", 30, 32, "Webhooks for 50+ real-time events."), E("docs/other/mcp/", 129, 198, "Invoices, offers/prices, shipping, courses, projects, and client portals.")]),
                ],
                "Core GoHighLevel API v2 and MCP domains from primary documentation.",
                cov="partial",
            )
            breadth(
                "broad",
                ["crm_contacts_opportunities", "conversations_messaging", "marketing_funnels_social", "payments_webhooks_courses"],
                [E("marketplace.gohighlevel.com/docs/", 14, 32, "CRM, communications, and 50+ webhooks."), E("docs/other/mcp/", 116, 198, "717 actions across 38 feature areas.")],
                "Inferred broad API surface covering 38 feature areas across CRM, omnichannel messaging, marketing/funnels/social, payments, courses, and webhooks.",
            )
            set_mcp_entries(
                [
                    (
                        "official_highlevel_mcp",
                        "official",
                        "HighLevel MCP Server (LeadConnector)",
                        [E("docs/other/mcp/", 70, 239, "Official HighLevel hosted MCP server exposing 717 callable actions across 38 feature areas via OAuth sign-in, with hosted endpoints https://services.leadconnectorhq.com/mcp/anthropic/v2 (Claude) and https://services.leadconnectorhq.com/mcp/openai/v2/ (ChatGPT/Codex).")],
                        "docs/other/mcp/",
                        "Official HighLevel hosted remote callable MCP server exposing 717 actions across 38 CRM/marketing/payments feature areas via OAuth sub-account authorization.",
                        "https://services.leadconnectorhq.com/mcp/anthropic/v2",
                        None,
                    ),
                ],
                [E("docs/other/mcp/", 70, 116, "Official HighLevel MCP Server documentation.")],
            )
            buildability(
                "build_now",
                "Build GoHighLevel CRM/marketing agent integration via REST API v2 (OAuth 2.0 or PIT) or official HighLevel MCP Server",
                [
                    "Production use requires a paid GoHighLevel subscription ($97-$497/mo after 14-day free trial) and agency/location admin authorization.",
                    "Public Marketplace distribution requires HighLevel app approval (private integrations and PITs do not).",
                ],
                [
                    "Use a 14-day free trial with a scoped Private Integration Token or OAuth app for immediate development.",
                    "Connect directly to HighLevel's official hosted MCP server or LeadConnector REST API v2.",
                ],
                ["identity", "auth.oauth2_marketplace", "auth.private_integration_token", "testing.trial_access", "production.paid_required", "production.admin_approval_required", "api.protocol.rest", "mcp.official_highlevel_mcp"],
                [
                    E("marketplace.gohighlevel.com/docs/", 11, 41, "Public REST API with OAuth 2.0 and PIT."),
                    E("Authorization/OAuth2.0/", 74, 108, "Public Marketplace OAuth apps require approval and location/agency admin installation."),
                    E("PrivateIntegrationsToken/", 80, 120, "Scoped Private Integration Tokens are generated by agency admins without Marketplace review."),
                    E("docs/other/mcp/", 70, 116, "Official 717-action hosted MCP server."),
                    E("gohighlevel.com/pricing", 36, 184, "Self-serve 14-day free trial and paid monthly tiers."),
                ],
                "Build now: self-serve 14-day trial, well-documented REST API v2 with OAuth 2.0 and PIT, and an official 717-action hosted MCP server (paid subscription required post-trial).",
            )

        # =====================================================================
        # APP 35: Mailchimp
        # =====================================================================
        elif app == 35:
            r["identity"]["resolution"] = claim(
                "identity",
                "Mailchimp Marketing API v3.0 — REST API for email marketing campaigns, audiences, contacts, templates, automations, and reporting (distinct from Mailchimp Transactional).",
                [
                    E("marketing/api/", 3, 172, "Mailchimp Marketing API for campaigns, audiences, contacts, automations, templates, and reporting."),
                    E("quick-start/", 21, 79, "Marketing API v3.0 endpoint at https://api.mailchimp.com/3.0/, distinct from Mailchimp Transactional."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Email marketing and audience management platform exposing Marketing API v3.0 for audiences, contacts, campaigns, templates, automations, webhooks, and reporting.",
                [E("marketing/api/", 3, 235, "Marketing API v3.0 covers Audiences, Contacts, Campaigns, SMS Campaigns, Automations, Templates, Batch Webhooks, and Reports.")],
            )
            items(
                r["auth"],
                [
                    auth(
                        "api_key",
                        "api_key",
                        "Mailchimp API key passed via HTTP Basic auth (--user 'anystring:<API_KEY>') or Authorization: Bearer <token> header.",
                        [
                            E("marketing/api/", 21, 70, "Authorization: Bearer <token> using a Mailchimp API key."),
                            E("quick-start/", 31, 34, "HTTP Basic auth example: --user 'anystring:${apikey}' against https://api.mailchimp.com/3.0/ping."),
                        ],
                        "Single-account / server-side Mailchimp Marketing API v3.0 requests",
                    ),
                    auth(
                        "oauth2",
                        "oauth2",
                        "OAuth 2.0 Authorization Code flow via https://login.mailchimp.com/oauth2/authorize and token exchange at https://login.mailchimp.com/oauth2/token.",
                        [
                            E("access-user-data-oauth-2/", 22, 139, "Documents full OAuth 2.0 authorization_code flow (authorize URL, callback code, POST to login.mailchimp.com/oauth2/token, access_token usage)."),
                            E("marketing/api/", 71, 72, "Lists Authorization: Bearer using OAuth."),
                        ],
                        "Multi-tenant / third-party applications accessing other users' Mailchimp accounts",
                    ),
                ],
                "Both API Key (Basic/Bearer) and OAuth 2.0 are documented in primary Mailchimp Marketing API docs.",
                cov="checked_sources",
            )
            # Testing & Production eligibility
            for env in ("testing", "production"):
                elig(
                    env, "free_access", True,
                    [
                        E("pricing/marketing/", 281, 282, "Basic Free plan available; users can cancel or downgrade to the Free plan at any time."),
                        E("marketing/api/", 113, 115, "API account schema pricing_plan_type explicitly includes forever_free."),
                    ],
                    "Mailchimp offers a Free (forever_free) Marketing plan usable for API development and small-scale production.",
                )
                elig(
                    env, "paid_required", False,
                    [E("pricing/marketing/", 280, 685, "Free plan ($0, capped at 250 contacts and 500 email sends/month or 250/day) exists alongside Essentials, Standard, and Premium paid plans.")],
                    "Paid plan is not required to start on the Free tier, though higher contact/send limits and Premium features require paid tiers.",
                )
                elig(
                    env, "self_serve", True,
                    [
                        E("quick-start/", 28, 60, "Self-serve API key generation and quick-start ping request."),
                        E("access-user-data-oauth-2/", 18, 139, "Self-serve OAuth app setup guide."),
                    ],
                    "Account signup, API key creation, and OAuth app setup are self-serve.",
                )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("marketing/api/", 1, 15, "Public Mailchimp Marketing API v3.0 reference and guides at mailchimp.com/developer.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("quick-start/", 31, 35, "HTTP REST API at https://api.mailchimp.com/3.0/.")]),
                    claim("api.protocol.sdk", "SDK", [E("quick-start/", 12, 46, "Documents official client libraries and SDKs handling authentication and response parsing.")]),
                ],
                "REST v3.0 API, official client libraries/SDKs, and webhooks are documented.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("audiences_contacts", "Audiences and Contacts (CRUD, archive, forget, tags)", [E("marketing/api/", 135, 172, "Audiences and Contacts CRUD, archive, forget."), E("quick-start/", 61, 62, "Import/export contacts and organize contacts with tags.")]),
                    group("campaigns_sms", "Email Campaigns, Campaign Folders, Content, Scheduling, and SMS Campaigns", [E("marketing/api/", 140, 235, "Campaign folders, Campaigns CRUD/send/schedule/test/content/feedback, and SMS Campaigns.")]),
                    group("automations_templates", "Automations / Workflow Emails and Templates", [E("marketing/api/", 156, 198, "Template folders, Templates, and Automation workflow emails/subscribers.")]),
                    group("reporting_webhooks", "Reports, Reporting, and Batch Webhooks", [E("marketing/api/", 138, 206, "Batch Webhooks CRUD and Reports/Reporting endpoints.")]),
                ],
                "Core Mailchimp Marketing API v3.0 resource groups from official API reference.",
                cov="partial",
            )
            breadth(
                "broad",
                ["audiences_contacts", "campaigns_sms", "automations_templates", "reporting_webhooks"],
                [E("marketing/api/", 135, 235, "Spans Audiences/Contacts, Campaigns/SMS, Automations, Templates, Batch Webhooks, and Reporting.")],
                "Inferred broad API surface across four distinct email/marketing domains.",
            )
            set_mcp_entries(
                [
                    (
                        "community_mcp_mailchimp",
                        "community",
                        "mcp-mailchimp (AlexlaGuardia/mcp-mailchimp)",
                        [E("AlexlaGuardia/mcp-mailchimp/main/README.md", 1, 172, "Community open-source local MCP server (pip install mcp-mailchimp, MAILCHIMP_API_KEY) exposing 71 callable tools for Mailchimp Marketing API (campaigns, reports, audiences, members, tags, segments, templates, automations, webhooks, e-commerce stores/orders).")],
                        "AlexlaGuardia/mcp-mailchimp/main/README.md",
                        "Community local CLI callable MCP server exposing 71 Mailchimp Marketing API v3 tools; community repo establishes its own implementation only.",
                        None,
                        "https://github.com/AlexlaGuardia/mcp-mailchimp",
                    ),
                ],
                [E("AlexlaGuardia/mcp-mailchimp/main/README.md", 1, 35, "Community Mailchimp Marketing API MCP server repository.")],
            )
            buildability(
                "build_now",
                "Build Mailchimp Marketing API v3.0 agent integration for audiences, contacts, campaigns, and reporting",
                [
                    "Free plan is capped at 250 contacts and 500 email sends/month (250/day), with sending paused when exceeded; higher volumes require Essentials, Standard, or Premium paid plans.",
                ],
                [
                    "Create a Free Mailchimp account and generate an API key (for single-tenant) or register an OAuth 2.0 app (for multi-tenant).",
                    "Call Mailchimp Marketing API v3.0 REST endpoints or official SDKs directly.",
                ],
                ["identity", "auth.api_key", "auth.oauth2", "testing.free_access", "production.self_serve", "api.protocol.rest", "mcp.community_mcp_mailchimp"],
                [
                    E("quick-start/", 28, 60, "Self-serve API key and REST v3.0 quickstart."),
                    E("access-user-data-oauth-2/", 22, 139, "OAuth 2.0 setup for multi-tenant apps."),
                    E("marketing/api/", 135, 235, "Marketing API v3.0 covers Audiences, Contacts, Campaigns, Automations, Templates, and Reporting."),
                    E("pricing/marketing/", 280, 685, "Free plan available (capped at 250 contacts and 500 sends/month) alongside paid plans."),
                ],
                "Build now: free self-serve tier, dual API key + OAuth 2.0 auth, mature REST v3.0 API and SDKs, with no vendor approval gate for standard API integration.",
            )

        # =====================================================================
        # APP 36: Klaviyo
        # =====================================================================
        elif app == 36:
            r["identity"]["resolution"] = claim(
                "identity",
                "Klaviyo — B2C CRM and Email/SMS Marketing Automation Platform with JSON:API REST API (revision 2026-10-15) and official Klaviyo MCP Server.",
                [
                    E("reference/api_overview", 1, 96, "Klaviyo Developers API Reference for the Klaviyo JSON:API REST API (revision 2026-10-15)."),
                    E("klaviyo.com/pricing", 3, 18, "Klaviyo: The Autonomous B2C CRM for Email, SMS, WhatsApp, Campaigns, and Reviews."),
                    E("klaviyo_mcp_server", 23, 40, "Official Klaviyo MCP server connecting AI clients to Klaviyo APIs."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "B2C CRM and email/SMS marketing automation platform exposing a JSON:API REST API (400+ endpoints across profiles, campaigns, flows, catalogs, events) and an official MCP Server.",
                [
                    E("reference/api_overview", 28, 159, "REST API (JSON:API) covering Profiles, Lists, Segments, Campaigns, Flows, Events, Metrics, Catalogs, Coupons, Templates, Reporting, and Webhooks."),
                    E("klaviyo_mcp_server", 30, 40, "Official Klaviyo MCP server (remote-hosted or local) connecting AI clients to Klaviyo APIs."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "private_api_key",
                        "api_key",
                        "Private API keys for server-side /api endpoints passed via 'Authorization: Klaviyo-API-Key <key>' header with read-only or full/custom endpoint scopes.",
                        [E("reference/api_overview", 43, 70, "Private API keys authenticate /api endpoints via Authorization: Klaviyo-API-Key header with granular scopes.")],
                        "Server-side single-account Klaviyo /api endpoints",
                    ),
                    auth(
                        "oauth2_pkce",
                        "oauth2",
                        "OAuth 2.0 Authorization Code flow with mandatory PKCE (S256) via https://www.klaviyo.com/oauth/authorize and https://a.klaviyo.com/oauth/token (Basic client_id:client_secret), returning Bearer access + refresh tokens; required for Klaviyo App Marketplace.",
                        [E("set_up_oauth", 33, 208, "OAuth 2.0 Authorization Code + PKCE (S256) flow with granular scopes (e.g., accounts:read, profiles:read, lists:write, campaigns:write, metrics:read); Bearer access tokens + revision header.")],
                        "Multi-tenant / tech-partner Klaviyo apps and App Marketplace integrations",
                        scopes=("accounts:read", "profiles:read", "lists:write", "campaigns:write", "metrics:read"),
                    ),
                    auth(
                        "public_api_key",
                        "api_key",
                        "Public API key (6-character Site ID) passed as query parameter for client-side /client tracking/object-creation endpoints only.",
                        [E("reference/api_overview", 51, 59, "Public API key (6-character site ID) passed via query parameter for publicly browseable client-side /client endpoints.")],
                        "Client-side browser/mobile tracking via /client endpoints",
                    ),
                ],
                "All three documented Klaviyo authentication methods (Private API key, OAuth 2.0 + PKCE, Public Site ID) are captured from primary docs.",
                cov="checked_sources",
            )
            # Testing & Production eligibility
            for env in ("testing", "production"):
                elig(
                    env, "free_access", True,
                    [E("klaviyo.com/pricing", 166, 173, "Klaviyo free plan ($0) includes up to 250 active profiles and 500 emails per month.")],
                    "Klaviyo provides a $0 Free plan usable for testing and small-scale production.",
                )
                elig(
                    env, "paid_required", False,
                    [E("klaviyo.com/pricing", 166, 224, "Free plan ($0, 250 profiles / 500 emails/mo) exists alongside paid Email ($20/mo), Marketing ($25/mo), and Custom plans.")],
                    "Paid plan is not required for accounts within Free plan limits (250 active profiles / 500 emails/mo).",
                )
                elig(
                    env, "self_serve", True,
                    [
                        E("klaviyo.com/pricing", 166, 168, "Self-serve 'Start for free' plan."),
                        E("set_up_oauth", 90, 90, "OAuth apps do not have to be listed in the Marketplace to share and use the installation URL with customers."),
                    ],
                    "Free account signup, Private API keys, and unlisted OAuth app installations are self-serve.",
                )
            elig(
                "production", "admin_approval_required", True,
                [E("set_up_oauth", 36, 36, "Only owner, admin, and manager roles can create OAuth apps in Klaviyo.")],
                "Owner, admin, or manager account role is required to create OAuth apps.",
            )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("reference/api_overview", 1, 28, "Public Klaviyo Developers REST API reference at developers.klaviyo.com.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("reference/api_overview", 28, 96, "Versioned JSON:API REST API (revision 2026-10-15) with relationships, filtering, and sparse fieldsets.")]),
                    claim("api.protocol.sdk", "SDK", [E("reference/api_overview", 33, 34, "Documents official Klaviyo SDKs."), E("klaviyo_mcp_server", 64, 65, "Lists Web and Mobile SDKs and developer tools.")]),
                ],
                "JSON:API REST API, official SDKs, and Flow/System webhooks (klaviyo_mcp_server L158-L163) are documented.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("profiles_lists_segments", "Profiles, Lists, Segments, Tags, and Custom Objects", [E("reference/api_overview", 123, 152, "Profiles (38 endpoints), Lists (13), Segments (11), Tags (26), Custom Objects (39).")]),
                    group("campaigns_flows_templates", "Campaigns, Flows, Templates, Forms, and Text Messaging", [E("reference/api_overview", 136, 154, "Campaigns (59 endpoints), Flows (22), Templates (17), Forms (12), Text Messaging (9).")]),
                    group("events_metrics_reporting", "Events, Metrics, and Reporting", [E("reference/api_overview", 142, 149, "Events (8 endpoints), Metrics (24), Reporting (7).")]),
                    group("catalogs_coupons_webhooks", "Catalogs, Coupons, Reviews, Webhooks, and Accounts/Billing", [E("reference/api_overview", 133, 158, "Accounts (2), Billing (2), Catalogs (55), Coupons (17), Reviews (3), Webhooks (7).")]),
                ],
                "Endpoint group counts directly from Klaviyo API Reference revision 2026-10-15.",
                cov="partial",
            )
            breadth(
                "broad",
                ["profiles_lists_segments", "campaigns_flows_templates", "events_metrics_reporting", "catalogs_coupons_webhooks"],
                [E("reference/api_overview", 120, 159, "28+ resource categories totaling 400+ REST endpoints across CRM profiles, campaigns/flows, analytics, catalogs, and webhooks.")],
                "Inferred broad API surface across four major B2C CRM and marketing automation domains (400+ endpoints).",
            )
            set_mcp_entries(
                [
                    (
                        "official_klaviyo_mcp",
                        "official",
                        "Klaviyo MCP Server",
                        [E("klaviyo_mcp_server", 30, 40, "Official Klaviyo MCP server connecting AI clients to Klaviyo APIs (e.g., querying campaign performance and creating email campaigns) via remote-hosted (recommended) or local server.")],
                        "klaviyo_mcp_server",
                        "Official Klaviyo callable MCP server (remote-hosted or local) for querying campaign/flow data and creating campaigns via Klaviyo APIs.",
                        None,
                        None,
                    ),
                ],
                [E("klaviyo_mcp_server", 30, 40, "Official Klaviyo MCP server documentation.")],
            )
            buildability(
                "build_now",
                "Build Klaviyo email/SMS marketing and profile automation integration via REST API or official Klaviyo MCP Server",
                [
                    "Public listing in the Klaviyo App Marketplace requires OAuth 2.0 + PKCE and passing app review (unlisted OAuth install URLs and Private API keys do not).",
                    "Free plan is capped at 250 active profiles and 500 emails/month.",
                ],
                [
                    "Create a free Klaviyo account and generate a scoped Private API key or OAuth 2.0 + PKCE app.",
                    "Integrate against Klaviyo REST API (revision 2026-10-15) or connect via the official Klaviyo MCP server.",
                ],
                ["identity", "auth.private_api_key", "auth.oauth2_pkce", "testing.free_access", "production.self_serve", "api.protocol.rest", "mcp.official_klaviyo_mcp"],
                [
                    E("reference/api_overview", 28, 70, "Public JSON:API REST reference and Private API key auth."),
                    E("set_up_oauth", 64, 399, "Self-serve OAuth 2.0 + PKCE usable without Marketplace listing; Marketplace listing requires passing app review."),
                    E("klaviyo_mcp_server", 30, 40, "Official remote-hosted and local MCP server."),
                    E("klaviyo.com/pricing", 166, 178, "Klaviyo free plan includes up to 250 active profiles and 500 emails per month."),
                ],
                "Build now: free self-serve tier, Private API keys and self-serve OAuth 2.0 + PKCE, broad 400+ endpoint REST API, and an official MCP server.",
            )

        # =====================================================================
        # APP 37: systeme.io
        # =====================================================================
        elif app == 37:
            r["identity"]["resolution"] = claim(
                "identity",
                "systeme.io — all-in-one online business platform combining sales funnels, email marketing, courses, communities, and automation with a Public API and official MCP Server.",
                [
                    E("systeme.io/", 1, 81, "Systeme.io combines email marketing, sales funnels, course creation, marketing automation, community builder, and Public API in one online business platform."),
                    E("developer.systeme.io/reference", 8, 12, "Systeme.io Public API reference."),
                    E("docs/mcp-server.md", 6, 12, "Official Systeme.io MCP Server overview."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "All-in-one funnel builder, email marketing, course, and automation platform exposing a Public REST API and an official MCP Server for contacts, tags, and newsletters.",
                [
                    E("systeme.io/", 28, 81, "Combines sales funnels, email marketing, online courses, marketing automation, and Public API."),
                    E("developer.systeme.io/reference", 11, 212, "Public API covering Automation, Booking Calendar, Community, Contacts, Funnels, Mailing/Newsletters/Campaigns, PricePlans, and Webhooks."),
                    E("docs/mcp-server.md", 6, 30, "Official Systeme.io MCP Server supporting contact, tag, contact field, and newsletter management."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "api_key",
                        "api_key",
                        "API key generated from profile settings and sent in the X-API-Key HTTP header (currently the only Public API authentication method).",
                        [E("developer.systeme.io/reference", 212, 264, "To authenticate with Systeme.io Public API, the only option is attaching the API key to the X-API-Key header; server-side use recommended.")],
                        "systeme.io Public REST API",
                    ),
                    auth(
                        "mcp_key",
                        "api_key",
                        "MCP key generated in Settings > MCP & API keys, sent either via X-MCP-Key HTTP header or mcpKey query parameter.",
                        [E("docs/mcp-server.md", 14, 22, "Systeme.io MCP server authenticates using an MCP key via X-MCP-Key HTTP header or mcpKey URL query parameter.")],
                        "systeme.io official MCP Server",
                    ),
                ],
                "Public API uses X-API-Key only (no OAuth documented); official MCP server uses dedicated MCP keys (X-MCP-Key header or mcpKey query param).",
                cov="checked_sources",
            )
            # Testing & Production eligibility
            for env in ("testing", "production"):
                elig(
                    env, "free_access", True,
                    [E("systeme.io/pricing", 396, 398, "Free plan supports up to 2,000 contacts, 3 sales funnels, 1 blog, 1 course, unlimited emails; never expires and requires no credit card.")],
                    "systeme.io offers a permanent Free plan with no credit card required.",
                )
                elig(
                    env, "paid_required", False,
                    [E("systeme.io/pricing", 396, 400, "Free plan ($0, up to 2,000 contacts) alongside Startup ($17/mo), Webinar ($47/mo), and Unlimited ($97/mo).")],
                    "Paid plan is not required for accounts under 2,000 contacts and Free plan limits.",
                )
                elig(
                    env, "self_serve", True,
                    [
                        E("systeme.io/pricing", 35, 38, "Self-serve 'Start for free' with no credit card required."),
                        E("developer.systeme.io/reference", 212, 218, "Self-serve API key creation in profile settings."),
                        E("docs/mcp-server.md", 14, 14, "Self-serve MCP key generation in dashboard MCP & API keys settings."),
                    ],
                    "Free account signup, API key generation, and MCP key generation are self-serve.",
                )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("developer.systeme.io/reference", 1, 226, "Public API reference and guides at developer.systeme.io.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("developer.systeme.io/reference", 43, 264, "HTTP REST endpoints (GET, POST, PATCH, DELETE) with JSON payloads and curl examples.")]),
                ],
                "HTTP REST API with webhooks (developer.systeme.io/llms.txt L6-L13) is documented.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("contacts_tags", "Contacts, ContactFields, and Tags", [E("developer.systeme.io/reference", 43, 55, "Contact CRUD, Tag assignment/removal, and ContactField CRUD.")]),
                    group("funnels_pages", "Funnels, FunnelSteps, Domains, Files, and Page Editor", [E("developer.systeme.io/reference", 56, 71, "Domains, Files, Funnels, and FunnelSteps CRUD."), E("developer.systeme.io/reference", 118, 122, "Page Editor and page templates.")]),
                    group("mailing_automation", "Mailing (Newsletters, Campaigns, Automation Emails/Stats), Automation Rules, and SMS Templates", [E("developer.systeme.io/reference", 11, 16, "AutomationRule CRUD."), E("developer.systeme.io/reference", 72, 116, "Newsletters, Campaigns, CampaignSteps, AutomationEmails, and email statistics."), E("developer.systeme.io/reference", 152, 158, "SmsTemplate CRUD.")]),
                    group("community_booking_commerce", "Communities, Booking Calendar, PricePlans, and Webhooks", [E("developer.systeme.io/reference", 17, 42, "Booking Calendar and Community/Memberships/Topics."), E("developer.systeme.io/reference", 130, 198, "PricePlan and Webhook CRUD.")]),
                ],
                "Core systeme.io Public API resource groups from developer.systeme.io/reference.",
                cov="partial",
            )
            breadth(
                "broad",
                ["contacts_tags", "funnels_pages", "mailing_automation", "community_booking_commerce"],
                [E("developer.systeme.io/reference", 11, 198, "Spans Automation, Booking Calendar, Community, Contacts, Funnels, Mailing, Page Editor, PricePlans, SMS Templates, and Webhooks.")],
                "Inferred broad API surface across four distinct online-business domains (contacts/CRM, funnels/pages, email/automation, and community/booking/pricing/webhooks).",
            )
            set_mcp_entries(
                [
                    (
                        "official_systeme_mcp",
                        "official",
                        "Systeme.io MCP Server",
                        [E("docs/mcp-server.md", 6, 36, "Official Systeme.io MCP Server (initial release) exposing callable tools for contacts, tags, tag assignment, contact fields, and newsletters; authenticates via MCP key (X-MCP-Key header or mcpKey query param).")],
                        "docs/mcp-server.md",
                        "Official Systeme.io callable MCP server (initial release) scoped to contact, tag, contact field, and newsletter management; other features not yet supported.",
                        None,
                        None,
                    ),
                ],
                [E("docs/mcp-server.md", 6, 30, "Official Systeme.io MCP Server documentation.")],
            )
            buildability(
                "build_now",
                "Build systeme.io contacts, funnels, email, and automation integration via Public REST API or official MCP Server",
                [
                    "Public API supports API key auth only (no OAuth 2.0 flow for multi-tenant delegated consent); users must supply their own X-API-Key or MCP key.",
                    "Official MCP server is in initial release and currently limited to contacts, tags, contact fields, and newsletters.",
                ],
                [
                    "Create a free systeme.io account (no credit card required) and generate an API key and/or MCP key in Settings > MCP & API keys.",
                    "Use Public REST API for full funnel/automation/webhook coverage or the official MCP server for contact/newsletter workflows.",
                ],
                ["identity", "auth.api_key", "auth.mcp_key", "testing.free_access", "production.self_serve", "api.protocol.rest", "mcp.official_systeme_mcp"],
                [
                    E("developer.systeme.io/reference", 11, 264, "Public REST API covering Funnels, Automation, Contacts, Mailing, and Webhooks with self-serve X-API-Key auth."),
                    E("docs/mcp-server.md", 6, 30, "Official MCP server (initial release) with self-serve MCP key for contacts, tags, and newsletters."),
                    E("systeme.io/pricing", 396, 398, "Free forever plan with no credit card required."),
                ],
                "Build now: permanent free self-serve tier, simple API key / MCP key auth, broad REST API, and an official MCP server.",
            )

        # =====================================================================
        # APP 38: Pinterest
        # =====================================================================
        elif app == 38:
            r["identity"]["resolution"] = claim(
                "identity",
                "Pinterest API v5 by Pinterest — REST API for managing Pinterest Pins, Boards, Audiences, Ads/Campaigns, and Analytics.",
                [
                    E("access-tiers/", 13, 26, "Pinterest API v5 for Pin Analytics, Audiences, Boards, and Pins."),
                    E("getting-access/", 42, 42, "Official Python SDK supports campaign management and authentication."),
                    E("set-up-authentication-and-authorization/", 35, 90, "Supports ads:read and ads:write scopes for creating ads."),
                    E("api-description/main/README.md", 1, 3, "Official Pinterest REST API OpenAPI 3.0.3 description repository."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Social visual-discovery and advertising platform exposing Pinterest REST API v5 for Pins, Boards, Audiences, Ads/Campaigns, and Analytics via OAuth 2.0.",
                [
                    E("access-tiers/", 13, 26, "Covers Pin Analytics, reading/creating Audiences, Boards, and Pins."),
                    E("getting-access/", 42, 42, "Official Python SDK supports campaign management and authentication."),
                    E("set-up-authentication-and-authorization/", 34, 189, "Covers boards, pins, and ads scopes (ads:read, ads:write, boards:read, pins:read) over https://api.pinterest.com/v5/."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_auth_code_and_cc",
                        "oauth2",
                        "OAuth 2.0 Authorization Code grant (https://www.pinterest.com/oauth/ -> POST https://api.pinterest.com/v5/oauth/token with HTTP Basic client_id:client_secret; continuous 60-day refresh tokens) and Client Credentials grant; Sandbox token endpoint at api-sandbox.pinterest.com/v5/oauth/token.",
                        [E("set-up-authentication-and-authorization/", 13, 207, "Documents OAuth 2.0 Authorization Code and Client Credentials grants, Basic client_id:client_secret token exchange, scopes (ads:read, ads:write, boards:read, pins:read), continuous refresh tokens, and Sandbox token endpoint.")],
                        "Pinterest API v5 (production and sandbox)",
                        scopes=("ads:read", "ads:write", "boards:read", "pins:read"),
                    ),
                    auth(
                        "trial_limited_token",
                        "bearer_token",
                        "Product-limited 24-hour test tokens generated after Trial access approval for testing endpoints without implementing the full OAuth flow.",
                        [E("getting-access/", 43, 43, "Once approved for Trial access, developers can generate 24-hour test tokens without setting up the OAuth flow.")],
                        "Trial-tier testing only",
                    ),
                ],
                "OAuth 2.0 is mandatory for production (Standard access review rejects login-credential or cookie scraping; access-tiers L76-L77).",
                cov="checked_sources",
            )
            # Testing eligibility
            elig(
                "testing", "trial_access", True,
                [E("access-tiers/", 13, 52, "Approved apps initially receive Trial access for exploring Pinterest API v5 (daily rate limits; created Pins/Boards visible only to creator).")],
                "Pinterest API v5 provides a Trial access tier for testing.",
            )
            elig(
                "testing", "sandbox_access", True,
                [
                    E("getting-access/", 44, 44, "Sandbox environment allows test calls without impacting Pinterest production."),
                    E("set-up-authentication-and-authorization/", 196, 205, "Sandbox OAuth token endpoint at https://api-sandbox.pinterest.com/v5/oauth/token."),
                    E("access-tiers/", 50, 52, "Pins and Boards created with Trial access are visible only to their creator as Sandbox content."),
                ],
                "Dedicated API Sandbox environment and creator-only Trial sandbox behavior are documented.",
            )
            elig(
                "testing", "vendor_approval_required", True,
                [E("getting-access/", 20, 23, "Developers must submit a request form for Trial access; application requests are reviewed by Pinterest for approval or denial.")],
                "Even Trial access requires Pinterest application review and approval.",
            )
            elig(
                "testing", "self_serve", False,
                [E("getting-access/", 20, 23, "Trial access requires submitting an app request form reviewed by Pinterest.")],
                "Trial access is gated by Pinterest review rather than instant self-serve credentials.",
            )
            # Production eligibility
            elig(
                "production", "vendor_approval_required", True,
                [E("access-tiers/", 53, 81, "Upgrading from Trial to Standard access requires a formal review with a video recording demonstrating the OAuth user authorization flow and a live Pinterest integration (even for single-user apps).")],
                "Production Standard access requires formal Pinterest review with an OAuth + live integration video demo.",
            )
            elig(
                "production", "self_serve", False,
                [E("access-tiers/", 53, 65, "Standard upgrade requests are submitted and reviewed by Pinterest.")],
                "Production Standard access requires vendor approval.",
            )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [
                    E("set-up-authentication-and-authorization/", 1, 207, "Public Pinterest Developers OAuth and getting-started docs."),
                    E("api-description/main/README.md", 1, 17, "Public official OpenAPI 3.0.3 schema repository at github.com/pinterest/api-description."),
                ],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("api-description/main/README.md", 1, 3, "Pinterest REST API described via OpenAPI 3.0.3."), E("set-up-authentication-and-authorization/", 189, 189, "REST base URL https://api.pinterest.com/v5/.")]),
                    claim("api.protocol.sdk", "SDK", [E("getting-access/", 42, 42, "Documents official Pinterest Python SDK supporting campaign management and authentication.")]),
                ],
                "Note: https://developers.pinterest.com/docs/api/v5/ rendered as a 9-line JS SPA shell in static HTTP capture; REST/OpenAPI and SDK facts are grounded in static getting-started docs and pinterest/api-description.",
                cov="partial",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("pins_boards", "Pins and Boards (read and create)", [E("access-tiers/", 20, 26, "Reading and creating Boards and Pins.")]),
                    group("audiences_ads", "Audiences and Ads/Campaign Management", [E("access-tiers/", 19, 24, "Reading and creating Audiences."), E("getting-access/", 42, 42, "Python SDK supports campaign management."), E("set-up-authentication-and-authorization/", 35, 90, "Documents ads:read and ads:write scopes for creating ads.")]),
                    group("analytics", "Pin Analytics", [E("access-tiers/", 17, 17, "Pin Analytics supported in Trial and Standard access.")]),
                ],
                "Resource groups grounded in captured access-tiers, auth, and getting-access docs (full endpoint reference at /docs/api/v5/ is JS-rendered).",
                cov="partial",
            )
            breadth(
                "moderate",
                ["pins_boards", "audiences_ads", "analytics"],
                [E("access-tiers/", 17, 26, "Covers Pins, Boards, Audiences, and Pin Analytics."), E("set-up-authentication-and-authorization/", 90, 90, "Covers ads:read and ads:write.")],
                "Inferred moderate API surface from captured docs spanning Pins/Boards, Audiences/Ads, and Pin Analytics (full OpenAPI endpoint catalog not expanded in static capture).",
            )
            r["mcp"]["entries"] = []
            r["mcp"]["discovery"] = claim(
                "mcp",
                None,
                [
                    E("getting-access/", 37, 44, "Checked Pinterest Developers getting-started developer tools list (API Quickstart, Python SDK, Product limited tokens, Sandbox); no official MCP server listed."),
                    E("api-description/main/README.md", 1, 25, "Checked official pinterest/api-description repository README; no MCP server listed (candidate community repo terryso/mcp-pinterest returned HTTP 404)."),
                ],
                status="not_found_in_checked_sources",
                rationale="Bounded search of checked Pinterest developer docs and official OpenAPI repo found no MCP server; candidate community repo URL returned HTTP 404. Does not prove no MCP exists.",
            )
            buildability(
                "conditional",
                "Build Pinterest API v5 agent integration for Pins, Boards, Audiences, and Ads via OAuth 2.0",
                [
                    "Both Trial access (for testing) and Standard access (for production public Pins/Boards and higher rate limits) require Pinterest application review.",
                    "Standard access requires a video demo of the OAuth flow and live Pinterest integration; no MCP server verified in checked sources.",
                ],
                [
                    "Create a Pinterest business account and submit an app request for Trial access.",
                    "Build the OAuth 2.0 integration against Sandbox/Trial endpoints, record the required demo video, and apply for Standard access.",
                ],
                ["identity", "auth.oauth2_auth_code_and_cc", "testing.vendor_approval_required", "production.vendor_approval_required", "api.protocol.rest"],
                [
                    E("getting-access/", 14, 44, "Business account, Pinterest review for Trial access, OAuth 2.0 flow, and Sandbox environment."),
                    E("access-tiers/", 13, 79, "Trial vs Standard access rate limits/visibility and Standard upgrade video demo review."),
                ],
                "Conditional: documented REST API v5 with OpenAPI schema and Sandbox, but both Trial and Standard production tiers require Pinterest vendor approval.",
            )

        # =====================================================================
        # APP 39: Threads (Meta)
        # =====================================================================
        elif app == 39:
            r["identity"]["resolution"] = claim(
                "identity",
                "Meta Threads API (graph.threads.com) by Meta — official REST API for publishing Threads posts, moderating replies, retrieving profiles/media, and reading insights.",
                [
                    E("docs/threads/", 1, 28, "Threads API by Meta for creating/publishing posts, retrieving media and profiles, moderating replies, and accessing insights."),
                    E("threads/posts", 38, 39, "REST API host https://graph.threads.com/v1.0/."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Meta social microblogging API for two-step media/text/carousel post publishing, reply moderation, profile/media retrieval, keyword search, webhooks, and insights.",
                [
                    E("docs/threads/", 1, 25, "Covers single/carousel posts, media, profiles, reply moderation, mentions, insights, webhooks, keyword search, and oEmbed."),
                    E("threads/posts", 1, 17, "Two-step container creation and publishing workflow for text, image, video, and carousel posts."),
                ],
            )
            items(
                r["auth"],
                [
                    auth(
                        "oauth2_user_token",
                        "oauth2",
                        "OAuth 2.0 Authorization Code flow via https://threads.com/oauth/authorize and POST https://graph.threads.com/oauth/access_token (using Threads App ID and Threads App Secret); short-lived tokens valid 1 hour, exchangeable for 60-day long-lived tokens; HTTPS redirect URI required (localhost not supported).",
                        [
                            E("threads/get-started", 8, 31, "App-scoped OAuth 2.0 Threads user access tokens (1h short-lived, 60-day long-lived) with threads_basic, threads_content_publish, threads_manage_replies, threads_read_replies, and threads_manage_insights permissions."),
                            E("get-access-tokens-and-permissions", 4, 91, "Authorization Window at https://threads.com/oauth/authorize and token exchange at POST https://graph.threads.com/oauth/access_token."),
                            E("fbsamples/threads_api/main/README.md", 34, 44, "Threads apps do not support localhost redirect URLs and require OAuth redirects over HTTPS."),
                        ],
                        "Meta Threads API (all authenticated endpoints)",
                        scopes=("threads_basic", "threads_content_publish", "threads_manage_replies", "threads_read_replies", "threads_manage_insights"),
                    ),
                ],
                "Only OAuth 2.0 Threads user access tokens are supported for authenticated endpoints (oEmbed can be called without a token per fbsamples README L19).",
                cov="checked_sources",
            )
            # Testing eligibility
            elig(
                "testing", "vendor_approval_required", False,
                [E("threads/get-started", 18, 34, "Designated Threads testers invited via the Meta App Dashboard can grant permissions at any time without App Review.")],
                "Testing with invited Threads testers requires no Meta App Review.",
            )
            elig(
                "testing", "self_serve", True,
                [E("threads/get-started", 6, 34, "Developers create a Meta app with the Threads use case and invite Threads testers via App Dashboard.")],
                "Creating a Meta app with the Threads use case and adding Threads testers is self-serve.",
            )
            # Production eligibility
            elig(
                "production", "vendor_approval_required", True,
                [
                    E("threads/get-started", 18, 18, "For app users without a role on your app, each permission must first be approved via Meta App Review."),
                    E("threads/posts", 13, 13, "Without advanced access approval for threads_content_publish, apps can only post on behalf of Threads testers."),
                ],
                "Production access for external users requires Meta App Review approval (advanced access) for each permission.",
            )
            elig(
                "production", "self_serve", False,
                [E("threads/posts", 13, 13, "External user publishing requires advanced access approval via Meta App Review.")],
                "Production multi-user rollout requires Meta App Review rather than self-serve activation.",
            )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("docs/threads/", 1, 28, "Public Meta Threads API guides, reference, and Postman collection at developers.facebook.com/docs/threads.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("threads/posts", 38, 60, "HTTP REST API at https://graph.threads.com/v1.0/ using POST/GET endpoints.")]),
                ],
                "REST API with webhooks and official Meta sample app (github.com/fbsamples/threads_api) and Postman collection.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("posts_publishing", "Single and Carousel Post Publishing (two-step media container workflow, AI disclosure, links, GIFs)", [E("threads/posts", 1, 286, "Two-step POST /{threads-user-id}/threads + POST /{threads-user-id}/threads_publish for text, image, video, carousel, links, and GIFs.")]),
                    group("profiles_media_search", "Profiles, Media retrieval, Keyword Search, and oEmbed", [E("docs/threads/", 16, 24, "Threads Media, Profiles, Keyword Search, and oEmbed."), E("fbsamples/threads_api/main/README.md", 11, 20, "Post browsing, keyword/topic search, oEmbed, and deletion.")]),
                    group("replies_mentions_webhooks", "Reply Moderation, Mentions, and Webhooks", [E("docs/threads/", 19, 22, "Reply Moderation, Mentions, and Webhooks.")]),
                    group("insights", "Media and User Insights Analytics", [E("threads/insights", 1, 86, "GET /{threads-media-id}/insights and GET /{threads-user-id}/threads_insights for views, likes, replies, reposts, quotes, shares, clicks, and follower demographics.")]),
                ],
                "Core Threads API resource domains from primary Meta docs and official sample app.",
                cov="partial",
            )
            breadth(
                "broad",
                ["posts_publishing", "profiles_media_search", "replies_mentions_webhooks", "insights"],
                [E("docs/threads/", 1, 25, "Spans publishing, media/profiles, reply moderation, mentions, insights, webhooks, and keyword search.")],
                "Inferred broad social API surface covering publishing, content discovery/search, conversation moderation/webhooks, and post/account analytics.",
            )
            set_mcp_entries(
                [
                    (
                        "community_threads_mcp",
                        "community",
                        "Threads MCP Server (quinnjr/threads-mcp)",
                        [E("quinnjr/threads-mcp/main/README.md", 1, 130, "Community TypeScript local CLI/npx MCP server (@pegasusheavy/threads-mcp) for Threads API v1.0 exposing callable tools (threads_get_profile, threads_get_threads, threads_create_thread, threads_reply_to_thread, threads_get_insights, threads_get_replies, threads_get_conversation).")],
                        "quinnjr/threads-mcp/main/README.md",
                        "Community local CLI/npx callable MCP server wrapping Threads API v1.0 via OAuth 2.0 or access token; community repo establishes its own implementation only (no official Meta Threads MCP found in checked docs).",
                        None,
                        "https://github.com/PegasusHeavyIndustries/threads-mcp",
                    ),
                ],
                [E("quinnjr/threads-mcp/main/README.md", 1, 35, "Community Threads MCP server repository.")],
            )
            buildability(
                "conditional",
                "Build Meta Threads publishing, reply moderation, and insights agent integration via Threads REST API",
                [
                    "Production access for external users requires Meta App Review approval (advanced access) for each permission (e.g., threads_content_publish).",
                    "Media publishing requires hosting media on a publicly accessible server and HTTPS OAuth redirect URIs (localhost not supported); no official Meta Threads MCP server found.",
                ],
                [
                    "Create a Meta app with the Threads use case and invite Threads testers for immediate end-to-end testing.",
                    "Submit requested permissions through Meta App Review before launching to external users.",
                ],
                ["identity", "auth.oauth2_user_token", "testing.self_serve", "production.vendor_approval_required", "api.protocol.rest", "mcp.community_threads_mcp"],
                [
                    E("threads/get-started", 6, 34, "Self-serve Meta app + Threads testers for development; App Review required for external users; media must be hosted on a public server."),
                    E("threads/posts", 13, 17, "Advanced access approval required for external posting; two-step container flow."),
                    E("fbsamples/threads_api/main/README.md", 34, 44, "Threads apps do not support localhost redirect URLs and require OAuth redirects over HTTPS."),
                ],
                "Conditional: immediate self-serve testing with Threads testers and clean REST API, but external production use is gated by Meta App Review.",
            )

        # =====================================================================
        # APP 40: SendGrid
        # =====================================================================
        elif app == 40:
            r["identity"]["resolution"] = claim(
                "identity",
                "Twilio SendGrid (SendGrid Web API v3) by Twilio — cloud email delivery and marketing campaigns platform.",
                [
                    E("sendgrid/api-reference", 4, 187, "Twilio SendGrid v3 Web API providing a REST interface for transactional email, marketing campaigns, contacts, and email statistics."),
                ],
            )
            r["purpose"] = claim(
                "purpose",
                "Transactional email API and marketing campaigns platform exposing SendGrid Web API v3 for mail send, transactional templates, contacts/lists, validation, webhooks, and deliverability analytics.",
                [E("sendgrid/api-reference", 9, 187, "Covers Mail Send, Domain Authentication, Email Address Validation, Email Activity/Stats, Event/Parse Webhooks, Marketing Campaigns/Contacts/Lists/Segments, Suppressions, and Transactional Templates.")],
            )
            items(
                r["auth"],
                [
                    auth(
                        "api_key_bearer",
                        "api_key",
                        "SendGrid API Key passed as 'Authorization: Bearer <API_KEY>' header, created in Settings > API Keys with Full Access, Custom Access (per-endpoint scopes), Billing Access, or Email Address Validation Access (limit 100 keys/account).",
                        [
                            E("sending-email/authentication", 81, 99, "Twilio SendGrid requires API keys passed via Authorization: Bearer <API_KEY> against https://api.sendgrid.com/v3/."),
                            E("account-and-settings/api-keys", 94, 123, "Up to 100 API keys per account with Full, Custom, Billing, or Email Address Validation permission scopes."),
                        ],
                        "Twilio SendGrid Web API v3 (recommended and required for 2FA-enabled accounts)",
                    ),
                    auth(
                        "basic_apikey",
                        "basic",
                        "HTTP Basic Authentication using literal username 'apikey' and the API key as password (legacy/selected endpoints; Basic auth with account password is not supported when 2FA is enabled, and 2FA is required for all users).",
                        [E("sending-email/authentication", 100, 114, "Basic authentication uses username 'apikey' and API key as password; Basic auth is not possible for users/subusers/teammates with 2FA enabled (2FA required for all users).")],
                        "Legacy/selected endpoints without 2FA user-password auth (upgrading to Bearer API keys recommended)",
                    ),
                ],
                "SendGrid uses scoped API keys via Bearer header (preferred); no OAuth 2.0 flow is documented in checked authentication pages.",
                cov="checked_sources",
            )
            # Testing eligibility
            elig(
                "testing", "trial_access", True,
                [E("pricing/email-api", 658, 665, "Free SendGrid Email API trial lets you send 100 emails/day for 60 days with no credit card required.")],
                "SendGrid offers a 60-day free trial (100 emails/day, no credit card required).",
            )
            elig(
                "testing", "paid_required", False,
                [E("pricing/email-api", 659, 665, "Free 60-day trial requires no credit card.")],
                "No payment required during the 60-day free trial.",
            )
            elig(
                "testing", "self_serve", True,
                [
                    E("pricing/email-api", 659, 663, "Self-serve free trial signup."),
                    E("account-and-settings/api-keys", 111, 188, "Self-serve API key creation in Settings > API Keys."),
                ],
                "Free trial signup and API key generation are self-serve.",
            )
            # Production eligibility
            elig(
                "production", "paid_required", True,
                [E("pricing/email-api", 665, 671, "Free trial is time-limited to 60 days (100 emails/day); ongoing plans start at Essentials ($19.95/month), with Pro and Premier volume plans.")],
                "Ongoing production use beyond the 60-day trial requires a paid plan starting at $19.95/month.",
            )
            elig(
                "production", "self_serve", True,
                [
                    E("pricing/email-api", 707, 726, "Users can upgrade any time after setting up their free account."),
                    E("account-and-settings/api-keys", 111, 188, "Self-serve API key creation in console."),
                ],
                "Upgrading to Essentials/Pro and creating API keys are self-serve.",
            )
            # API Surface
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("sendgrid/api-reference", 1, 187, "Public Twilio SendGrid Web API v3 reference at twilio.com/docs/sendgrid.")],
            )
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [E("sendgrid/api-reference", 185, 185, "SendGrid v3 Web API provides a REST interface to send email at scale.")]),
                    claim("api.protocol.sdk", "SDK", [E("sendgrid/api-reference", 206, 209, "Documents open-source SDKs and tools to integrate with SendGrid.")]),
                ],
                "REST v3 Web API, open-source SDKs, SMTP API (authentication L22), and Event/Inbound Parse webhooks are documented.",
                cov="checked_sources",
            )
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("mail_send_templates", "Mail Send, Scheduled Sends, and Transactional Templates", [E("sendgrid/api-reference", 9, 12, "Mail Send and Cancel Scheduled Sends APIs."), E("sendgrid/api-reference", 145, 149, "Transactional Templates and Template Versions APIs.")]),
                    group("marketing_contacts_campaigns", "Marketing Campaigns, Contacts, Lists, Segments, and Single Sends", [E("sendgrid/api-reference", 61, 96, "Legacy and New Marketing Campaigns, Contacts, Lists, Segmenting Contacts V2, and Campaign Stats.")]),
                    group("deliverability_validation_suppressions", "Domain Authentication, Email Address Validation, Suppressions, and Spam/Bounce Management", [E("sendgrid/api-reference", 24, 27, "Domain Authentication and Email Address Validation APIs."), E("sendgrid/api-reference", 130, 144, "Suppression Management, Blocks, Bounces, Invalid Emails, Spam Reports, and Suppressions APIs.")]),
                    group("stats_activity_webhooks_admin", "Email Activity/Logs, Statistics, Event/Parse Webhooks, API Keys, and Subusers", [E("sendgrid/api-reference", 46, 59, "Email Activity, Email Logs, Statistics, and Event/Parse Webhooks."), E("sendgrid/api-reference", 98, 122, "API Keys, API Key Permissions, Mail Settings, Subuser Statistics, and Users.")]),
                ],
                "Core SendGrid Web API v3 resource groups from official Twilio SendGrid API reference.",
                cov="partial",
            )
            breadth(
                "broad",
                ["mail_send_templates", "marketing_contacts_campaigns", "deliverability_validation_suppressions", "stats_activity_webhooks_admin"],
                [E("sendgrid/api-reference", 9, 149, "Spans Mail Send, Templates, Marketing Campaigns/Contacts, Domain Auth/Validation/Suppressions, Activity/Stats, Webhooks, and Account/API Key admin.")],
                "Inferred broad API surface across four distinct email delivery, marketing, deliverability, and observability domains.",
            )
            set_mcp_entries(
                [
                    (
                        "community_sendgrid_mcp",
                        "community",
                        "SendGrid MCP Server (Garoth/sendgrid-mcp)",
                        [E("Garoth/sendgrid-mcp/main/README.md", 1, 225, "Community open-source local Node.js MCP server (SENDGRID_API_KEY) exposing callable tools for SendGrid v3 contact management (list/add/delete contacts and lists), email sending (send_email, Single Sends), dynamic templates, email statistics, and email validation.")],
                        "Garoth/sendgrid-mcp/main/README.md",
                        "Community local Node.js callable MCP server wrapping SendGrid Marketing/Email API v3 via SENDGRID_API_KEY; community repo establishes its own implementation only (no official SendGrid execution MCP server found in checked Twilio SendGrid docs).",
                        None,
                        "https://github.com/Garoth/sendgrid-mcp",
                    ),
                ],
                [E("Garoth/sendgrid-mcp/main/README.md", 1, 30, "Community SendGrid MCP server repository.")],
            )
            buildability(
                "build_now",
                "Build Twilio SendGrid transactional/marketing email and contact management integration via Web API v3",
                [
                    "Free trial is limited to 60 days (100 emails/day); ongoing production use requires a paid plan (Essentials from $19.95/mo).",
                    "API key authentication only (no OAuth 2.0 flow documented); sender identity/domain must be verified before sending; no official Twilio SendGrid execution MCP server found.",
                ],
                [
                    "Sign up for the 60-day free trial (no credit card required) and create a scoped API key in Settings > API Keys.",
                    "Authenticate with Authorization: Bearer <API_KEY> against SendGrid Web API v3 or use official SDKs.",
                ],
                ["identity", "auth.api_key_bearer", "testing.trial_access", "production.paid_required", "production.self_serve", "api.protocol.rest", "mcp.community_sendgrid_mcp"],
                [
                    E("sending-email/authentication", 81, 99, "Bearer API key auth for SendGrid v3 REST API."),
                    E("account-and-settings/api-keys", 111, 123, "Create API keys in Settings > API Keys with Full, Custom, Billing, or Email Address Validation permissions."),
                    E("pricing/email-api", 658, 671, "Self-serve 60-day free trial and paid Essentials/Pro plans."),
                    E("sendgrid/api-reference", 24, 41, "Domain Authentication and Sender Verification APIs."),
                    E("sendgrid/api-reference", 185, 209, "Public REST API v3 and open-source SDKs."),
                ],
                "Build now: self-serve 60-day free trial, simple scoped Bearer API keys, broad well-documented REST v3 API and SDKs, and no vendor approval gate.",
            )

    destination.write_text(json.dumps({"records": records}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} researched records to {destination}")


if __name__ == "__main__":
    build("task10-capture-005", ROOT / "work/task-10-agent/extracted-002.json")
