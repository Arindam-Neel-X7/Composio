"""Task 12 researcher-authored extraction (Data, SEO and Scraping, IDs 51-60, contract v1.1).

Remediates both the 15 internal audit findings and all 18 external Codex review checkpoint
items (outputs/task-12-review.md) in immutable child run task12-first-pass-005.
Every claim and paraphrase was authored after directly reading the captured primary
snapshots in task12-capture-003. No model API, synthetic fixture, authenticated account
operation, independent review, or accuracy measurement occurs here.
"""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import research_pipeline as p
from make_sources import SCOPES


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

        AUTH_MAP = {
            "oauth2": "OAuth2",
            "api_key": "API_key",
            "basic": "Basic",
            "bearer_token": "Bearer_token",
            "jwt": "JWT",
            "session_cookie": "session_cookie",
            "none": "none",
            "other": "other",
        }

        def auth(key, method, details, ev, subcontext, scopes=(), status="observed", refs=()):
            return claim(
                "auth." + key,
                {"method": AUTH_MAP.get(method, method), "context": subcontext, "scopes": list(scopes), "details": details},
                ev,
                status,
                refs,
                "Scoped mechanism from primary documentation; no credentials obtained or authenticated call executed.",
            )

        def items(target, entries, notes, cov="checked_sources"):
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
                    "MCP entry documented in captured source; operational execution remains not_researched.",
                ))
            r["mcp"]["discovery"] = claim(
                "mcp.discovery",
                "found",
                discovery_ev,
                "observed",
                (),
                "At least one callable MCP server entry matching the product scope was observed in captured sources.",
            )
            r["mcp"]["entries"] = out

        def set_mcp_not_found(ev, rationale):
            r["mcp"]["discovery"] = claim("mcp.discovery", None, ev, "not_found_in_checked_sources", (), rationale)
            r["mcp"]["entries"] = []

        def buildability(verdict, bscope, blockers, next_steps, ev, refs, reason):
            r["buildability"] = claim(
                "buildability",
                {"verdict": verdict, "scope": bscope, "blockers": blockers, "next_steps": next_steps},
                ev,
                "inferred",
                refs,
                reason,
            )

        r["credential_eligibility"]["testing"]["context"] = scope
        r["credential_eligibility"]["production"]["context"] = scope

        # =====================================================================
        # 51. DataForSEO
        # =====================================================================
        if app == 51:
            e_intro = E("docs.dataforseo.com/v3/", 791, 817, "DataForSEO API v3 provides REST HTTP endpoints and official PHP, C#, Java, Python, and TypeScript client libraries for SEO software and data analysis pipelines.")
            e_auth = E("docs.dataforseo.com/v3/auth/", 810, 822, "DataForSEO API v3 at https://api.dataforseo.com/ uses HTTP Basic Authentication (Authorization: Basic base64(login:password)) with an API login and auto-generated API password from the dashboard API Access tab.")
            e_sbox = E("docs.dataforseo.com/v3/appendix/sandbox/", 791, 805, "DataForSEO Sandbox (https://sandbox.dataforseo.com/v3/$path) is a free testing environment for any registered user where requests are not charged.")
            e_price = E("dataforseo.com/pricing", 216, 300, "DataForSEO uses a pay-as-you-go pricing model across SERP, AI Optimization, Backlinks, Content Analysis, DataForSEO Labs, Keywords Data, OnPage, Merchant, App Data, Business Data, and Domain Analytics APIs with no monthly subscriptions or recurring fees and a $50 minimum account top-up that does not expire.")
            e_mcp_doc = E("dataforseo.com/model-context-protocol", 147, 202, "DataForSEO product MCP page documents a hosted remote HTTP MCP server at https://mcp.dataforseo.com/v3/mcp (authenticated via Authorization: Basic header) and a local npx dataforseo-mcp-server using DATAFORSEO_USERNAME and DATAFORSEO_PASSWORD.")
            e_mcp_repo = E("github.com/dataforseo/mcp-server-typescript", 165, 185, "Official dataforseo/mcp-server-typescript repository provides the v3 MCP server and CLI (npx dataforseo-mcp-server@latest) supporting stdio and HTTP transport, with OAuth 2.0 Bearer tokens as default for HTTP MCP (via Protected Resource metadata discovery) and HTTP Basic fallback via DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD (accepting DATAFORSEO_USERNAME as an alias).")

            e_serp = E("docs.dataforseo.com/v3/serp/overview/", 791, 795, "SERP API covers Google, Bing, YouTube, Yahoo, Baidu, Naver, and Seznam search engine results.")
            e_kw = E("docs.dataforseo.com/v3/keywords_data/overview/", 791, 795, "Keywords Data API provides keyword analysis across Google and Bing data sources.")
            e_bl = E("docs.dataforseo.com/v3/backlinks/overview/", 791, 795, "Backlinks API provides inbound links, referring domains, and referring pages data.")
            e_op = E("docs.dataforseo.com/v3/on_page/overview/", 791, 795, "OnPage API crawls websites and webpages according to customizable parameters to evaluate on-page SEO performance.")
            e_labs = E("docs.dataforseo.com/v3/dataforseo_labs/overview/", 791, 795, "DataForSEO Labs API provides keywords, SERPs, and domain analytics from in-house databases.")
            e_biz = E("docs.dataforseo.com/v3/business_data/overview/", 791, 795, "Business Data API provides business reviews and publicly shared business entity information.")
            e_dom = E("docs.dataforseo.com/v3/domain_analytics/overview/", 791, 795, "Domain Analytics API provides website traffic, technologies, and Whois details.")
            e_app = E("docs.dataforseo.com/v3/app_data/overview/", 791, 795, "App Data API provides mobile application rankings, ratings, reviews, and collections.")
            e_mer = E("docs.dataforseo.com/v3/merchant/overview/", 791, 795, "Merchant API provides ecommerce data on prices, products, and retailers.")
            e_cnt = E("docs.dataforseo.com/v3/content_analysis/overview/", 791, 795, "Content Analysis API provides brand monitoring, sentiment analysis, and citation management.")
            e_aio = E("docs.dataforseo.com/v3/ai_optimization/overview/", 791, 795, "AI Optimization API provides keyword discovery, conversational optimization, and real-time LLM benchmarking.")

            r["identity"]["resolution"] = claim(
                "identity",
                "DataForSEO (dataforseo.com / docs.dataforseo.com) — SEO, SERP, keyword, backlink, ecommerce, and AI search data platform offering REST API v3 and official MCP server.",
                [e_intro, e_auth, e_mcp_doc, e_serp, e_kw, e_bl, e_mer, e_aio],
            )
            r["purpose"] = claim(
                "purpose",
                "Pay-as-you-go SEO and digital marketing data platform offering v3 REST APIs (SERP, Keywords, Backlinks, OnPage, Labs, Business, Domain, App, Merchant, Content, AI Optimization), free developer Sandbox, and official MCP server.",
                [e_intro, e_sbox, e_price, e_mcp_doc, e_serp, e_kw, e_bl, e_op, e_labs, e_biz, e_dom, e_app, e_mer, e_cnt, e_aio],
            )
            items(r["auth"], [
                auth("basic_api_credentials", "basic",
                     "HTTP Basic Authentication passing Base64-encoded API login and auto-generated API password in the Authorization: Basic header across DataForSEO v3 REST APIs and remote MCP server; local stdio/CLI MCP uses environment variables (dataforseo/mcp-server-typescript v3 uses DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD and accepts DATAFORSEO_USERNAME as an alias, whereas dataforseo.com/model-context-protocol examples show DATAFORSEO_USERNAME and DATAFORSEO_PASSWORD).",
                     [e_auth, e_mcp_doc, e_mcp_repo], "DataForSEO v3 REST APIs, Sandbox, and MCP server HTTP Basic / stdio env-var fallback"),
                auth("mcp_http_oauth2", "oauth2",
                     "OAuth 2.0 (default for HTTP MCP in dataforseo/mcp-server-typescript v3): MCP clients discover the DataForSEO authorization server via Protected Resource metadata and send Authorization: Bearer tokens (falling back to HTTP Basic when no Authorization header is present).",
                     [e_mcp_repo], "DataForSEO v3 HTTP MCP server default OAuth 2.0 Bearer flow"),
            ], "REST v3 and Sandbox use HTTP Basic Auth (API login + API password); v3 HTTP MCP defaults to OAuth 2.0 Bearer with HTTP Basic fallback, while stdio/CLI MCP uses DATAFORSEO_LOGIN (or alias DATAFORSEO_USERNAME) and DATAFORSEO_PASSWORD.")

            elig("testing", "free_access", True, [e_auth, e_sbox], "Creating a DataForSEO account is free and registered users can call Sandbox endpoints without charges.")
            elig("testing", "sandbox_access", True, [e_sbox], "Dedicated Sandbox host https://sandbox.dataforseo.com/v3/$path is free for registered users and does not charge account balance.")
            elig("testing", "paid_required", False, [e_auth, e_sbox], "Sandbox testing is free for any registered user without account balance charges.")
            elig("testing", "self_serve", True, [e_auth, e_sbox], "Developers can create a free account and retrieve API login/password from https://app.dataforseo.com/api-access self-serve.")
            elig("production", "free_access", False, [e_price], "Production API requests consume account balance under a pay-as-you-go model requiring a $50 minimum top-up.")
            elig("production", "paid_required", True, [e_price], "Production usage requires adding funds under the pay-as-you-go pricing model ($50 minimum account top-up).")
            elig("production", "self_serve", True, [e_auth, e_price], "Developers self-serve create an account, retrieve API credentials in the dashboard, and top up balance ($50 minimum) with no recurring subscription.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_intro, e_auth]),
                claim("api.protocol.sdk", "SDK", [e_intro]),
                claim("api.protocol.cli", "CLI", [e_mcp_repo]),
            ], "REST HTTP v3 API, official PHP/C#/Java/Python/TypeScript client libraries, and CLI commands via dataforseo-mcp-server.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_intro, e_auth, e_sbox])

            items(r["api_surface"]["resource_groups"], [
                group("serp_keywords_labs", "SERP API, Keywords Data API, and DataForSEO Labs API", [e_serp, e_kw, e_labs]),
                group("backlinks_onpage_domain", "Backlinks API, OnPage crawling API, and Domain Analytics API (traffic, tech stack, Whois)", [e_bl, e_op, e_dom]),
                group("business_app_merchant", "Business Data API, App Data API (mobile app rankings/reviews), and Merchant ecommerce API", [e_biz, e_app, e_mer]),
                group("content_ai_optimization", "Content Analysis API (citations/sentiment) and AI Optimization API (LLM benchmarking)", [e_cnt, e_aio]),
            ], "All 11 DataForSEO v3 API product families captured from primary overview pages.")
            breadth("broad", ["serp_keywords_labs", "backlinks_onpage_domain", "business_app_merchant", "content_ai_optimization"],
                    [e_serp, e_bl, e_biz, e_app, e_mer, e_cnt, e_aio],
                    "Spans multiple distinct business domains across 11 API suites: search engine/keyword/backlink SEO, technical website crawling & domain/Whois intelligence, local business reviews, mobile app store rankings, ecommerce merchant/product pricing, brand sentiment/citations, and AI/LLM search optimization.")

            set_mcp_entries([
                ("official_remote_http", "official", "DataForSEO Remote HTTP MCP Server", [e_mcp_doc, e_mcp_repo], "dataforseo.com/model-context-protocol",
                 "Official hosted callable Streamable HTTP MCP server at https://mcp.dataforseo.com/v3/mcp supporting OAuth 2.0 Bearer tokens (default in v3 MCP) or HTTP Basic Authorization header.",
                 "https://mcp.dataforseo.com/v3/mcp", None),
                ("official_local_npx", "official", "DataForSEO TypeScript MCP Server (dataforseo-mcp-server)", [e_mcp_doc, e_mcp_repo], "github.com/dataforseo/mcp-server-typescript",
                 "Official open-source callable stdio/HTTP MCP server and CLI (npx dataforseo-mcp-server@latest) for browsing DataForSEO docs and executing authenticated v3 API calls.",
                 None, "https://github.com/dataforseo/mcp-server-typescript"),
            ], [e_mcp_doc, e_mcp_repo])

            buildability(
                "build_now",
                "Build a DataForSEO SEO/SERP/keyword/backlink/AI-search agent integration via REST API v3 or official MCP server.",
                ["Live production API calls require pay-as-you-go account balance ($50 minimum account top-up); Sandbox returns free test responses at https://sandbox.dataforseo.com/v3/."],
                ["Register a free DataForSEO account and copy API login and API password from https://app.dataforseo.com/api-access.",
                 "Test against https://sandbox.dataforseo.com/v3/ or connect via https://mcp.dataforseo.com/v3/mcp or npx dataforseo-mcp-server@latest."],
                [e_auth, e_sbox, e_price, e_mcp_doc, e_mcp_repo],
                ["identity", "auth.basic_api_credentials", "auth.mcp_http_oauth2", "testing.free_access", "testing.sandbox_access", "testing.self_serve", "production.paid_required", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp.discovery"],
                "Public v3 REST documentation, self-serve free account and Sandbox environment, pay-as-you-go production access, and official remote + local MCP servers support immediate buildability.",
            )

        # =====================================================================
        # 52. SE Ranking
        # =====================================================================
        elif app == 52:
            e_api = E("seranking.com/api/", 435, 516, "SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit.")
            e_faq = E("seranking.com/api/", 611, 621, "API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account.")
            e_oas = E("seranking/openapi/main/README.md", 12, 74, "Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.")
            e_mcp = E("seranking.com/api/integrations/mcp/", 444, 464, "SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).")
            e_price = E("seranking.com/pricing.html", 100, 147, "SE Ranking plans start at $129/mo (25K API credits & MCP access, with a 14-day free trial, no credit card required), higher plans include 100K API credits & MCP access, and Enterprise requires 'Talk to sales'.")
            e_apiprice = E("seranking.com/pricing.html", 331, 336, "SE Ranking also offers a standalone SE Ranking API plan starting from $179/mo (annual billing only).")
            e_skills = E("seranking/seo-skills/main/README.md", 1, 54, "Official seranking/seo-skills repository distributes 32 open-source Claude/Cursor SEO skills configured for the hosted SE Ranking remote MCP server at https://api.seranking.com/mcp with OAuth sign-in.")

            r["identity"]["resolution"] = claim(
                "identity",
                "SE Ranking (seranking.com) — SEO and AI-search visibility platform offering Data API, Project API, Local Marketing API, SE Visible API, and hosted MCP server.",
                [e_api, e_oas, e_mcp],
            )
            r["purpose"] = claim(
                "purpose",
                "SEO and AI-visibility platform with REST APIs (Data API, Project API, Local Marketing API, SE Visible API at https://api.seranking.com), OpenAPI 3.0 specs, and a hosted remote MCP server.",
                [e_api, e_oas, e_mcp],
            )
            items(r["auth"], [
                auth("api_key_token", "api_key",
                     "SE Ranking API key generated in the master account API Dashboard (Settings > API) and passed in the Authorization: Token YOUR_API_KEY HTTP header (recommended) or as the apikey query parameter, or entered manually in MCP connection dialogs.",
                     [e_faq, e_oas, e_mcp], "SE Ranking REST APIs (Data, Project, Local Marketing, SE Visible) and manual MCP key auth"),
                auth("mcp_oauth2", "oauth2",
                     "OAuth 2.1 with Dynamic Client Registration (DCR) for authenticating AI clients against the hosted Streamable HTTP MCP server at https://api.seranking.com/mcp using a master SE Ranking account.",
                     [e_mcp, e_skills], "SE Ranking hosted remote MCP server (https://api.seranking.com/mcp)"),
            ], "REST endpoints use Authorization: Token <API_KEY> or ?apikey=<API_KEY>; hosted MCP uses OAuth 2.1 with DCR or manual master-account API key.")

            elig("testing", "trial_access", True, [e_api, e_price], "SE Ranking offers a 14-day free trial with no credit card required on its core subscription plan ($129/mo tier with 25K API credits & MCP access).")
            elig("testing", "self_serve", True, [e_api, e_faq, e_price], "Master-account owners can start a 14-day trial without a credit card and retrieve an API key from Settings > API in the dashboard.")
            elig("production", "paid_required", True, [e_faq, e_price, e_apiprice], "Production API and MCP access is bundled with paid SE Ranking subscriptions (from $129/mo) or the standalone SE Ranking API plan (from $179/mo billed annually).")
            elig("production", "admin_approval_required", None, [e_faq, e_mcp],
                 "Actor-dependent across master accounts vs. shared-workspace sub-accounts: master account holders self-serve copy their API key in Settings > API or sign in via OAuth, whereas shared-workspace sub-accounts cannot connect via 'Sign in with SE Ranking' and must obtain the master-account API key from their account administrator (until sub-account API keys are released). Left unknown rather than asserting a universal app-wide boolean.",
                 status="unknown")
            elig("production", "self_serve", True, [e_faq, e_price], "For master account owners, standard paid plans ($129/mo+) and API key generation in Settings > API are self-serve (shared-workspace sub-accounts require an administrator's master API key, and custom Enterprise setups use Talk to sales).")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_api, e_oas]),
            ], "HTTP REST APIs returning JSON with official OpenAPI 3.0 YAML/JSON specifications in github.com/seranking/openapi.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_api, e_oas, e_mcp])

            e_data = E("seranking.com/api/data/", 435, 463, "Data API covers keyword database, domain profiles, backlinks, Google AI Overviews, AI models, SERP features, and monthly technical audits.")
            e_proj = E("seranking.com/api/project/", 435, 446, "Project API covers creating/managing projects, keyword groups, tracking competitors, running website audits, monitoring backlinks, and account/seat management.")

            items(r["api_surface"]["resource_groups"], [
                group("data_api", "Data API (Backlinks, Domain Analysis, Keyword Research, AI Search, SERP, Website Audit, Account subscription/credit balance)", [e_oas, e_data]),
                group("project_api", "Project API (projects, project groups, keywords/rankings, search engines, competitors, URL tags, GSC data, website audits, Backlink Checker, AI Results Tracker)", [e_oas, e_proj]),
                group("local_marketing_api", "Local Marketing API (locations, local rankings, Google Business Profile reports, business listings, reviews, local audits)", [e_oas, e_mcp]),
                group("se_visible_api", "SE Visible API (AI visibility projects, brands, topics, prompts, prompt results, sources, engines, locations)", [e_oas, e_mcp]),
            ], "Four REST API suites documented in seranking/openapi and seranking.com/api/mcp/.")
            breadth("moderate", ["data_api", "project_api", "local_marketing_api", "se_visible_api"],
                    [e_oas, e_data, e_proj],
                    "Multiple related SEO and search-visibility resource groups across global SEO research (Data API), campaign/project management (Project API), local business listings/GBP (Local Marketing API), and AI search engine visibility (SE Visible API).")

            set_mcp_entries([
                ("official_remote_mcp", "official", "SE Ranking Remote MCP Server", [e_mcp, e_skills], "seranking.com/api/integrations/mcp/",
                 "Official hosted Streamable HTTP MCP server at https://api.seranking.com/mcp exposing Data API, Project API, Local Marketing API, and SE Visible API tools via OAuth 2.1 DCR or API key.",
                 "https://api.seranking.com/mcp", None),
            ], [e_mcp, e_skills])

            buildability(
                "build_now",
                "Integrate SE Ranking Data, Project, Local Marketing, and SE Visible APIs via REST/OpenAPI 3.0 or the hosted MCP server at https://api.seranking.com/mcp.",
                ["Production usage requires a paid SE Ranking subscription (from $129/mo with 25K API credits) or standalone API plan ($179/mo annual) and consumes API credits.",
                 "In shared workspaces, sub-accounts cannot use OAuth button sign-in directly and must use a master-account API key from an administrator."],
                ["Generate an API key in the SE Ranking API Dashboard (Settings > API) or connect an MCP client to https://api.seranking.com/mcp via OAuth 2.1.",
                 "Use official OpenAPI 3.0 specs from github.com/seranking/openapi to generate typed REST clients."],
                [e_faq, e_oas, e_mcp, e_price, e_apiprice],
                ["identity", "auth.api_key_token", "auth.mcp_oauth2", "testing.trial_access", "testing.self_serve", "production.paid_required", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp.discovery"],
                "Public OpenAPI 3.0 specifications, self-serve API keys and 14-day trial for master accounts, and an official hosted MCP server make SE Ranking immediately buildable.",
            )

        # =====================================================================
        # 53. Ahrefs
        # =====================================================================
        elif app == 53:
            e_intro = E("docs.ahrefs.com/api/docs/introduction.md", 1, 41, "Ahrefs API v3 pulls workspace data across Site Explorer, Keywords Explorer, Site Audit, SERP Overview, Rank Tracker, Batch Analysis, Brand Radar, Social Media Management, Content Helper, Management, Subscription information, and Public endpoints with an OpenAPI spec at https://docs.ahrefs.com/openapi.json.")
            e_keys = E("docs.ahrefs.com/api/docs/api-keys-creation-and-management.md", 1, 12, "Ahrefs API v3 requests authenticate with Authorization: Bearer YOUR_API_KEY; only workspace owners and admins can create and manage API keys in Account settings / API keys.")
            e_free = E("docs.ahrefs.com/api/docs/free-test-queries.md", 1, 24, "Users on any paid plan can run a limited set of free test queries (using targets ahrefs.com, yep.com, or firehose.com, capped at limit=100) without consuming API units, using an API key.")
            e_pub = E("docs.ahrefs.com/reference/public.json", 1, 90, "Ahrefs Public API v3 endpoints (https://api.ahrefs.com/v3/public, including crawler IPs/ranges and domain-rating-free) are free endpoints that don't require an Ahrefs subscription or use a free/public APIv3 key generated after signing up for a free Ahrefs account.")
            e_lim = E("docs.ahrefs.com/api/docs/limits-consumption.md", 1, 15, "Ahrefs API v3 is available on eligible paid plans (with limited free test queries on other plans); billable requests consume at least 50 API units while Rank Tracker, Management, and Public endpoints are free of unit cost.")
            e_oauth = E("docs.ahrefs.com/ahrefs-connect/docs/oauth-guide.md", 1, 50, "Ahrefs Connect uses OAuth 2.0 Authorization Code Flow with PKCE (authorize at https://app.ahrefs.com/web/oauth/authorize with scope apiv3-integration-apps, token exchange at https://ahrefs.com/oauth/token returning a 1-year Bearer access_token) and requires an Approval process.")
            e_mcp = E("docs.ahrefs.com/mcp/docs/introduction.md", 1, 45, "Ahrefs provides an official hosted Streamable HTTP MCP server at https://api.ahrefs.com/mcp/mcp for paid plans starting from Lite, supporting OAuth consent (creating an MCP-scoped key with 200,000 monthly unit default limit), manual MCP keys, or Enterprise API keys; custom scripts/bridges calling the external MCP endpoint are prohibited.")
            e_mcpt = E("docs.ahrefs.com/mcp/docs/tool-categories.md", 1, 51, "Ahrefs MCP server supports ?tools= group filtering across site-explorer, keywords-explorer, serp-overview, rank-tracker, site-audit, brand-radar, web-analytics, gsc, social-media, content-helper, batch-analysis, management, public, subscription-info, essentials, and search-exec.")
            e_price = E("ahrefs.com/pricing", 119, 234, "Ahrefs pricing includes Ahrefs Free, Starter ($29/mo), Lite ($129/mo, with API and MCP access), Standard ($249/mo, API and MCP access), Advanced ($449/mo, API and MCP access), and Enterprise ('Talk to sales', uncapped API access and custom API endpoints).")
            e_oas_ver = E("docs.ahrefs.com/openapi.json", 1, 17, "Ahrefs complete OpenAPI specification uses OpenAPI 3.2.0 with base server https://api.ahrefs.com/v3.")
            e_ent_addon = E("docs.ahrefs.com/openapi.json", 8210, 8216, "Certain Ahrefs API v3 endpoints in openapi.json require the Traffic Analytics Enterprise add-on.")
            e_llms = E("docs.ahrefs.com/llms.txt", 1, 33, "Ahrefs API v3 base URL is https://api.ahrefs.com/v3/{tool}/{endpoint} and tools cover Site Explorer, Competitive Analysis, Keywords Explorer, Site Audit, Rank Tracker, SERP Overview, Batch Analysis, Subscription Information, Management, Brand Radar, Content Helper, Web Analytics, GSC Insights, Social Media, and Public.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Ahrefs (ahrefs.com / docs.ahrefs.com) — SEO, backlink, keyword, site audit, and AI brand visibility platform offering REST API v3, Ahrefs Connect OAuth 2.0, and hosted MCP server (distinct from consumer-only web views).",
                [e_intro, e_mcp, e_price, e_llms],
            )
            r["purpose"] = claim(
                "purpose",
                "SEO and marketing intelligence platform exposing REST API v3 (https://api.ahrefs.com/v3/{tool}/{endpoint} with OpenAPI 3.2.0 spec), Ahrefs Connect OAuth 2.0 PKCE, and an official hosted MCP server (https://api.ahrefs.com/mcp/mcp).",
                [e_intro, e_oauth, e_mcp, e_oas_ver, e_llms],
            )
            items(r["auth"], [
                auth("bearer_api_key", "bearer_token",
                     "API key (or manually generated MCP key) created by workspace owners/admins in Account settings / API keys and sent in the Authorization: Bearer <API_KEY> HTTP header.",
                     [e_keys, e_mcp, e_llms], "Ahrefs REST API v3 and MCP server manual/Enterprise key authentication"),
                auth("oauth2_pkce", "oauth2",
                     "OAuth 2.0 Authorization Code Flow with PKCE (S256) via https://app.ahrefs.com/web/oauth/authorize and https://ahrefs.com/oauth/token (scope apiv3-integration-apps for Ahrefs Connect; MCP OAuth consent screen issues an MCP-scoped key with a 200,000 unit/month default limit).",
                     [e_oauth, e_mcp], "Ahrefs Connect third-party integration apps and hosted MCP server OAuth sign-in",
                     scopes=["apiv3-integration-apps", "MCP"]),
            ], "Direct API v3 calls use Authorization: Bearer <API_KEY> (free public crawler IP endpoints require no key); multi-user integrations and MCP clients support OAuth 2.0.")

            # Separate Ahrefs' distinct credential paths explicitly:
            # (1) /v3/public endpoints (crawler IPs require no key; domain-rating-free uses a free Ahrefs account APIv3 key, public.json lines 81-85),
            # (2) Free test queries on Site/Keywords/SERP (targets ahrefs.com, yep.com, firehose.com) which explicitly state "Users on any paid plan can test Ahrefs API..." (free-test-queries.md line 2),
            # (3) Full API v3 & hosted MCP on eligible paid plans starting from Lite ($129/mo), where only workspace owners/admins can create API keys (api-keys-creation-and-management.md line 4),
            # (4) Ahrefs Connect third-party OAuth apps requiring Ahrefs' Approval process (oauth-guide.md line 50).
            elig("testing", "free_access", None, [e_intro, e_free, e_pub, e_lim],
                 "Path-dependent across Ahrefs API v3 surfaces: `/v3/public` endpoints (`crawler-ips`, `crawler-ip-ranges`, and `domain-rating-free`) work without a paid subscription (or with a free Ahrefs account APIv3 key per public.json lines 81-85), whereas complimentary test queries on Site Explorer/Keywords Explorer/SERP Overview (targets `ahrefs.com`, `yep.com`, `firehose.com`) state 'Users on any paid plan can test Ahrefs API by running a limited set of free test queries' (free-test-queries.md line 2) and non-test queries require an eligible paid plan (Lite $129/mo+). Left unknown rather than collapsing paid-plan test queries and free public endpoints into one boolean.",
                 status="unknown")
            elig("testing", "paid_required", None, [e_intro, e_free, e_pub, e_lim],
                 "Path-dependent: `/v3/public` endpoints require no paid subscription (public.json lines 5, 81-85), whereas running complimentary free test queries on Site/Keywords/SERP requires a paid plan (free-test-queries.md line 2) and full API/MCP testing requires an eligible paid plan starting from Lite ($129/mo). Preserved as unknown with explicit path breakdown.",
                 status="unknown")
            elig("testing", "admin_approval_required", True, [e_intro, e_keys], "For authenticated API v3 requests (including complimentary test queries and full API keys), only workspace owners and admins have access to Account settings / API keys to create or manage API keys (unauthenticated `/v3/public` crawler-IP endpoints require no key).")
            elig("testing", "self_serve", True, [e_keys, e_free, e_pub], "Workspace owners/admins can self-serve generate APIv3 keys in Account settings without vendor intervention (and free account holders can self-serve generate a key for `/v3/public/domain-rating-free`).")
            elig("production", "free_access", False, [e_intro, e_lim, e_mcp, e_price], "Full production Ahrefs API v3 (Site Explorer, Keywords Explorer, Site Audit, SERP Overview, Brand Radar, etc.) and hosted MCP server access require an eligible paid plan starting from Lite ($129/mo) and consume monthly API units (only narrow `/v3/public` endpoints are free without a subscription).")
            elig("production", "paid_required", True, [e_intro, e_lim, e_mcp, e_price], "Full production API v3 and hosted MCP access require a paid plan starting from Lite ($129/mo; Standard $249/mo; Advanced $449/mo; Enterprise custom).")
            elig("production", "admin_approval_required", True, [e_keys, e_mcp], "Only workspace owners and admins can create/manage API keys and adjust per-key API unit limits in Account settings / API keys.")
            elig("production", "vendor_approval_required", None, [e_keys, e_oauth, e_mcp],
                 "Path-dependent: direct workspace APIv3 keys and user MCP OAuth connections on Lite+ plans are self-serve without vendor approval, whereas third-party multi-user OAuth 2.0 integration apps using Ahrefs Connect (`scope=apiv3-integration-apps`) must pass Ahrefs' vendor Approval process demonstrating secure token handling (oauth-guide.md line 50). Preserved as unknown rather than collapsing direct keys and Ahrefs Connect apps.",
                 status="unknown")
            elig("production", "self_serve", True, [e_keys, e_mcp, e_price], "For workspace owners/admins on Lite ($129/mo), Standard ($249/mo), and Advanced ($449/mo) plans, subscription signup and API/MCP key creation are self-serve (whereas Ahrefs Connect OAuth apps require vendor approval, and Enterprise custom endpoints/uncapped API and Traffic Analytics add-on require sales contact).")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_intro, e_pub, e_oas_ver, e_llms]),
            ], "REST HTTP endpoints under https://api.ahrefs.com/v3/{tool}/{endpoint} documented with full and per-tool OpenAPI 3.2.0 JSON specifications.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_intro, e_pub, e_mcpt, e_oas_ver, e_llms])

            items(r["api_surface"]["resource_groups"], [
                group("site_keywords_serp_batch", "Site Explorer, Competitive Analysis, Keywords Explorer, SERP Overview, and Batch Analysis (up to 100 targets)", [e_intro, e_llms]),
                group("audit_rank_gsc_webanalytics", "Site Audit, Rank Tracker, Google Search Console (GSC) Insights, and Web Analytics", [e_intro, e_llms, e_mcpt]),
                group("brand_radar_content_social", "Brand Radar (AI prompt/visibility tracking), Content Helper, and Social Media Management", [e_intro, e_llms, e_mcpt]),
                group("management_subscription_public", "Management (Rank Tracker projects & keyword lists), Subscription Information (limits/usage), and Public endpoints (crawler IPs & free domain rating)", [e_intro, e_llms, e_pub]),
            ], "15 tool categories documented in docs.ahrefs.com/llms.txt and openapi.json.")
            breadth("broad", ["site_keywords_serp_batch", "audit_rank_gsc_webanalytics", "brand_radar_content_social", "management_subscription_public"],
                    [e_intro, e_llms, e_mcpt],
                    "Covers 15 distinct tool families spanning backlink/domain competitive intelligence, keyword research, technical site auditing, rank tracking, first-party web analytics & GSC, social media channel/post management, AI brand visibility (Brand Radar), and workspace management.")

            set_mcp_entries([
                ("official_remote_mcp", "official", "Ahrefs Hosted MCP Server", [e_mcp, e_mcpt], "docs.ahrefs.com/mcp/docs/introduction.md",
                 "Official hosted Streamable HTTP MCP server at https://api.ahrefs.com/mcp/mcp (with ?tools= category filtering and tools=search-exec / tools=essentials modes) for supported AI agents on Lite+ plans.",
                 "https://api.ahrefs.com/mcp/mcp", None),
            ], [e_mcp, e_mcpt])

            buildability(
                "build_now",
                "Build an Ahrefs SEO, backlink, keyword, site audit, and Brand Radar integration via REST API v3 (https://api.ahrefs.com/v3/) or connect supported AI clients to https://api.ahrefs.com/mcp/mcp.",
                ["Full production API v3 and MCP usage requires a paid Ahrefs plan (Lite $129/mo or higher; complimentary test queries on ahrefs.com/yep.com/firehose.com also require a paid plan, while only `/v3/public` works on a free account) and workspace owner/admin role to generate API keys; billable requests cost a minimum of 50 API units.",
                 "Traffic Analytics endpoints require the Enterprise add-on, Ahrefs Connect third-party OAuth apps require vendor approval, and Ahrefs prohibits calling the external MCP endpoint from custom scripts/bridges or standalone HTTP/JSON-RPC clients (use REST API v3 for custom code)."],
                ["Use REST API v3 (https://docs.ahrefs.com/openapi.json) with Authorization: Bearer <API_KEY> for custom programmatic integrations and test with free test queries (ahrefs.com, yep.com, firehose.com) or `/v3/public` endpoints.",
                 "Use https://api.ahrefs.com/mcp/mcp only from supported MCP AI clients via OAuth or an MCP key."],
                [e_intro, e_keys, e_free, e_pub, e_oauth, e_mcp, e_price, e_oas_ver, e_ent_addon, e_llms],
                ["identity", "auth.bearer_api_key", "auth.oauth2_pkce", "testing.admin_approval_required", "testing.self_serve", "production.paid_required", "production.admin_approval_required", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp.discovery"],
                "Public OpenAPI 3.2.0 specs, free public endpoints and paid-plan complimentary test queries, self-serve Lite+ workspace API keys, and an official hosted MCP server support immediate development (using REST API v3 for custom programmatic code per Ahrefs MCP policy).",
            )

        # =====================================================================
        # 54. MrScraper
        # =====================================================================
        elif app == 54:
            e_over = E("docs.mrscraper.com/docs/api/overview", 26, 48, "MrScraper API is a REST API for programmatically scraping web pages (HTML, Markdown, screenshots, brand data, and JSON) and managing scrapers, authenticated with an API token in the x-api-token header.")
            e_auth = E("docs.mrscraper.com/docs/api/authentication", 26, 55, "MrScraper API authenticates requests via x-api-token: <MRSCRAPER_API_TOKEN> (generated in the dashboard at app.mrscraper.com/api-tokens) or Authorization: Bearer <MRSCRAPER_API_TOKEN> for Marketplace endpoints, with token verification at GET https://api.app.mrscraper.com/api/v1/subscription-accounts.")
            e_tok = E("docs.mrscraper.com/docs/getting-started/api-token", 28, 43, "MrScraper uses Plan Tokens to measure compute/bandwidth/AI usage and API Tokens to authenticate API requests.")
            e_bill = E("docs.mrscraper.com/docs/getting-started/billing", 28, 39, "docs.mrscraper.com/docs/getting-started/billing lists Scraper Free (table shows 1,000 API tokens and 10 concurrent requests; text states 100 tokens/month with no credit card required), Scraper Pro (200,000 tokens, 100 concurrent), and Scraper Enterprise (Custom).")
            e_price = E("mrscraper.com/pricing", 1, 63, "mrscraper.com/pricing header states 'Start Free, Plans From $99/Month' and displays Essential ($99/month, 200,000 tokens, 20 concurrent requests, 'Get Started') and Enterprise ('Contact Us', 500k+ tokens, 200 concurrent requests, 'Book a Call').")
            e_mcp = E("docs.mrscraper.com/docs/getting-started/mcp-server", 28, 122, "Official MrScraper MCP server (@mrscraper/mcp v0.5.0) is available as a hosted Streamable HTTP endpoint at https://mcp.mrscraper.com/mcp (using OAuth 2.1 browser sign-in with scopes scrape:read and account:read, or an API key fallback) and locally via stdio/HTTP, exposing 7 tools (status, scrapeHtml, scrapeMarkdown, getScreenshot, scrapeBrand, scrapeJson, webSearch).")
            e_mcp_auth = E("docs.mrscraper.com/docs/getting-started/mcp-server", 190, 210, "MrScraper MCP authentication table distinguishes Hosted Streamable HTTP (OAuth 2.1 browser sign-in via protected-resource metadata, or API key fallback), Self-hosted Streamable HTTP (OAuth 2.1 access token or Authorization: Bearer <MrScraper API key>), and Local stdio (MRSCRAPER_API_KEY, then MRSCRAPER_API_TOKEN environment variables), advertising scopes scrape:read and account:read (plus offline_access).")
            e_cli = E("docs.mrscraper.com/docs/getting-started/cli", 28, 92, "MrScraper CLI (v0.7.1, Node.js 20+) provides terminal access to the 7 MrScraper services (status, scrape-html, scrape-markdown, get-screenshot, scrape-brand, scrape-json, web-search) using browser sign-in (`mrscraper login`, which approves in the browser and saves a dedicated API key in ~/.mrscraper/auth.json) or an API key.")
            e_html = E("docs.mrscraper.com/docs/api/v3/scraper/web-fetching-scraping", 24, 115, "Scraper API v3 at https://api.mrscraper.com provides Scrape HTML, Scrape Markdown, Get Screenshot, and Web Search endpoints.")
            e_json = E("docs.mrscraper.com/docs/api/scraper-api/scrape-json", 24, 52, "Scrape JSON endpoint at https://api.mrscraper.com extracts structured JSON from a single page using a natural-language prompt and optional JSON Schema with agent=general.")
            e_llms = E("docs.mrscraper.com/llms.txt", 1, 123, "docs.mrscraper.com/llms.txt indexes Scraper API, Web Search, Platform/Workflow APIs, Residential Proxy API, SDKs, CLI, MCP Server, and x402 agentic market OpenAPI specs.")
            e_sdks = E("docs.mrscraper.com/llms.txt", 84, 88, "docs.mrscraper.com/llms.txt lists official Node.js (@mrscraper/sdk) and Python (mrscraper-sdk) SDKs as well as LangChain and Vercel AI SDK packages.")

            r["identity"]["resolution"] = claim(
                "identity",
                "MrScraper (mrscraper.com / docs.mrscraper.com) — AI-powered web scraping, web search, and residential proxy platform offering REST APIs, official MCP server, and CLI.",
                [e_over, e_mcp, e_cli],
            )
            r["purpose"] = claim(
                "purpose",
                "AI web scraping and search platform providing REST Scraper/Platform APIs (HTML, Markdown, screenshot, brand, JSON extraction, web search, workflows), an official hosted and local MCP server (@mrscraper/mcp), and a CLI.",
                [e_over, e_mcp, e_cli, e_html, e_json],
            )
            items(r["auth"], [
                auth("x_api_token", "api_key",
                     "API token created in the MrScraper dashboard (app.mrscraper.com/api-tokens, or provisioned via `mrscraper login` browser approval into ~/.mrscraper/auth.json for CLI use) and passed in the x-api-token HTTP header on Scraper API (https://api.mrscraper.com) and Platform/Analytics endpoints (https://api.app.mrscraper.com), or via MRSCRAPER_API_KEY / MRSCRAPER_API_TOKEN environment variables for local stdio MCP.",
                     [e_over, e_auth, e_mcp_auth, e_cli, e_html], "MrScraper Scraper API, Platform/Analytics REST endpoints, CLI, and local stdio MCP environment credentials"),
                auth("bearer_token", "bearer_token",
                     "MrScraper API token passed in the standard RFC 6750 Authorization: Bearer <MRSCRAPER_API_TOKEN> HTTP header for Marketplace endpoints and HTTP MCP server connections (hosted API key fallback or self-hosted Streamable HTTP).",
                     [e_auth, e_mcp, e_mcp_auth], "MrScraper Marketplace endpoints and Streamable HTTP MCP Bearer API-key authentication"),
                auth("mcp_oauth2", "oauth2",
                     "OAuth 2.1 browser sign-in (via OAuth 2.1 protected-resource metadata challenge) for the hosted Streamable HTTP MCP server at https://mcp.mrscraper.com/mcp, advertising application scopes scrape:read and account:read (plus offline_access).",
                     [e_mcp, e_mcp_auth], "Hosted MrScraper MCP server (https://mcp.mrscraper.com/mcp)",
                     scopes=["scrape:read", "account:read", "offline_access"]),
            ], "REST endpoints use x-api-token (or Authorization: Bearer for Marketplace); hosted HTTP MCP uses OAuth 2.1 browser sign-in or Bearer API key fallback; local stdio MCP uses MRSCRAPER_API_KEY / MRSCRAPER_API_TOKEN env vars; CLI browser login saves a dedicated API key.")

            elig("testing", "free_access", True, [e_bill, e_price], "Billing docs document a Scraper Free plan requiring no credit card (noting an internal discrepancy on the same page between '1,000 token' in the comparison table at line 32 and '100 tokens per month with no credit card required' at line 38; mrscraper.com/pricing also advertises 'Start Free').")
            elig("testing", "paid_required", False, [e_bill], "The Free plan includes monthly tokens with no credit card required.")
            elig("testing", "self_serve", True, [e_auth, e_bill, e_price], "Developers can sign up for a free account without a credit card and create API tokens self-serve in the dashboard (app.mrscraper.com/api-tokens).")
            elig("production", "free_access", True, [e_bill], "A recurring monthly Free tier exists (100 or 1,000 tokens/month, 10 concurrent requests, no residential proxies), while higher production volumes and residential proxies require paid plans from $99/month.")
            elig("production", "paid_required", False, [e_bill, e_price], "Low-volume scraping can use the monthly Free tier, while production residential proxies and 200,000+ monthly tokens require paid plans (Essential/Pro at $99/month or custom Enterprise).")
            elig("production", "self_serve", True, [e_auth, e_bill, e_price], "Free and Essential/Scraper Pro ($99/month, 200,000 tokens) plans and dashboard API token creation are self-serve; Enterprise requires contacting sales ('Contact Us' / 'Book a Call').")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_over, e_auth, e_html]),
                claim("api.protocol.cli", "CLI", [e_cli]),
                claim("api.protocol.sdk", "SDK", [e_mcp, e_sdks]),
            ], "REST HTTP endpoints (https://api.mrscraper.com and https://api.app.mrscraper.com), official CLI v0.7.1, and official Node.js/Python SDKs.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_over, e_auth, e_mcp, e_llms])

            items(r["api_surface"]["resource_groups"], [
                group("scraper_api", "Scraper API (Scrape HTML, Scrape Markdown, Get Screenshot, Scrape Brand, Scrape JSON, Scrape Sitemap)", [e_over, e_html, e_json, e_llms]),
                group("web_search", "Web Search API (ranked web search results by country)", [e_mcp, e_html, e_llms]),
                group("platform_workflows_analytics", "Platform API (Workflow scraper execution, cancel bulk scraping, results, subscription-accounts status, and analytics)", [e_auth, e_llms]),
                group("proxies_marketplace", "Residential Proxy configuration/generator and Marketplace / x402 agentic market endpoints", [e_auth, e_llms]),
            ], "Resource groups verified from docs.mrscraper.com API Reference and llms.txt.")
            breadth("moderate", ["scraper_api", "web_search", "platform_workflows_analytics", "proxies_marketplace"],
                    [e_over, e_auth, e_html, e_llms],
                    "Multiple related web-scraping and data-retrieval resource groups covering single-page/brand/JSON scraping, web search, scraper workflow management & usage analytics, and residential proxy/marketplace endpoints.")

            set_mcp_entries([
                ("official_mcp", "official", "MrScraper MCP Server (@mrscraper/mcp)", [e_mcp, e_mcp_auth], "docs.mrscraper.com/docs/getting-started/mcp-server",
                 "Official callable MCP server hosted via Streamable HTTP at https://mcp.mrscraper.com/mcp (OAuth 2.1 or Bearer API key) and publishable locally via @mrscraper/mcp npm package, exposing status, scrapeHtml, scrapeMarkdown, getScreenshot, scrapeBrand, scrapeJson, and webSearch.",
                 "https://mcp.mrscraper.com/mcp", None),
            ], [e_mcp, e_mcp_auth])

            buildability(
                "build_now",
                "Build a MrScraper web scraping, structured JSON extraction, and web search integration via REST API, CLI, or official MCP server.",
                ["Free plan excludes residential proxies and caps monthly tokens (docs show a minor discrepancy between 100 and 1,000 free tokens/month, and between 'Scraper Pro' in docs vs 'Essential $99/month' on the pricing page)."],
                ["Create a free MrScraper account and generate an API token at app.mrscraper.com/api-tokens, or connect via OAuth 2.1 to https://mcp.mrscraper.com/mcp.",
                 "Call https://api.mrscraper.com endpoints with x-api-token or use the 7 MCP tools."],
                [e_over, e_auth, e_bill, e_price, e_mcp, e_mcp_auth, e_cli],
                ["identity", "auth.x_api_token", "auth.bearer_token", "auth.mcp_oauth2", "testing.free_access", "testing.self_serve", "production.free_access", "production.self_serve", "api.protocol.rest", "api.protocol.cli", "api.breadth", "mcp.discovery"],
                "Self-serve free tier, public REST and CLI docs, API token + OAuth 2.1 authentication, and an official hosted MCP server support immediate integration.",
            )

        # =====================================================================
        # 55. Apify
        # =====================================================================
        elif app == 55:
            e_v2 = E("docs.apify.com/api/v2.md", 8, 135, "Apify API v2 provides RESTful HTTP access to the Apify platform (with complete OpenAPI YAML/JSON schemas) authenticated preferably via Authorization: Bearer <token> (or payment credentials / temporary spend-capped API tokens from Apify AGI via x402 / MPP), supporting running Actors, fetching Datasets, Key-Value Stores, Request Queues, Webhooks, and Schedules.")
            e_v2_toc = E("docs.apify.com/api/v2.md", 8, 25, "Apify API v2 table of contents lists Actors, Actor runs, Actor tasks, Datasets, Key-value stores, Request queues, Webhooks, Webhook dispatches, Schedules, and Store.")
            e_int_api = E("docs.apify.com/platform/integrations/api.md", 18, 30, "Users create and manage Personal API tokens (with optional permission limits and expiration dates) on the API & Integrations page in Apify Console; Apify CLI authenticates via apify login in the browser.")
            e_mcp = E("docs.apify.com/platform/integrations/mcp.md", 13, 38, "Apify's official MCP server at https://mcp.apify.com exposes Apify Actors, storage, and documentation tools over Streamable HTTP with OAuth or Bearer API token (plus unauthenticated access when the tools parameter selects only tools enabled for unauthenticated discovery/doc search, or local stdio via npx @apify/actors-mcp-server).")
            e_mcp_pay = E("docs.apify.com/platform/integrations/mcp.md", 91, 106, "For agentic payments without an Apify account, agents buy a prepaid, spend-capped API token from Apify AGI (https://agi.apify.com) and pass it in the Authorization: Bearer <PREPAID_TOKEN> header to https://mcp.apify.com.")
            e_mcp_repo = E("raw.githubusercontent.com/apify/apify-mcp-server/master/README.md", 1, 142, "Official github.com/apify/apify-mcp-server (@apify/actors-mcp-server) supports remote HTTP at https://mcp.apify.com (OAuth or Bearer token) and local stdio (APIFY_TOKEN env var or Apify CLI login).")
            e_price = E("apify.com/pricing", 90, 145, "Apify offers a Free plan ($0/month, no credit card required, $5 monthly credit to spend in Apify Store or on Actors at $0.20/CU) and paid self-serve Starter ($19/mo), Scale ($199/mo), and Business ($999/mo) plans plus pay-as-you-go and x402 agentic payments.")
            e_actors = E("docs.apify.com/platform/actors", 32, 58, "Actors are serverless cloud programs taking JSON input for web scraping, browser automation, and data processing, backed by storage (Datasets, Key-Value Stores, Request Queues) and Apify Store.")
            e_js = E("docs.apify.com/api/client/js/", 8, 60, "Official apify-client JavaScript/TypeScript library and SDKs for JavaScript/Python plus Apify CLI.")
            e_py = E("docs.apify.com/api/client/python/", 40, 56, "Official apify-client Python library (synchronous and asynchronous) for the Apify REST API.")
            e_acc = E("docs.apify.com/platform/collaboration/access-rights", 39, 53, "Apify provides a granular permissions system to share Actors, tasks, key-value stores, datasets, and request queues across users and organization accounts.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Apify (apify.com / docs.apify.com) — cloud web scraping and browser automation platform featuring serverless Actors, REST API v2, official SDKs/CLI, and hosted MCP server (mcp.apify.com).",
                [e_v2, e_mcp, e_actors],
            )
            r["purpose"] = claim(
                "purpose",
                "Serverless web scraping and browser automation platform (Apify Actors & Store) with REST API v2, multi-language API clients/SDKs, Apify CLI, and an official hosted/local MCP server (mcp.apify.com / @apify/actors-mcp-server).",
                [e_v2, e_mcp, e_mcp_repo, e_actors, e_js],
            )
            items(r["auth"], [
                auth("bearer_api_token", "bearer_token",
                     "Personal API token created in Apify Console (Settings > API & Integrations, with optional scoped permissions and expiration) or prepaid spend-capped token purchased via Apify AGI (x402 / MPP), passed in the Authorization: Bearer <token> HTTP header (recommended over URL query parameter) or as APIFY_TOKEN for local MCP/CLI/SDKs.",
                     [e_v2, e_int_api, e_mcp_pay, e_mcp_repo], "Apify REST API v2, SDKs, CLI, and MCP server (including prepaid Apify AGI tokens)"),
                auth("mcp_oauth2", "oauth2",
                     "OAuth sign-in for the hosted Apify MCP server at https://mcp.apify.com (and browser login via apify login for the Apify CLI).",
                     [e_int_api, e_mcp, e_mcp_repo], "Hosted Apify MCP server (https://mcp.apify.com) and Apify CLI"),
                auth("keyless_public_mcp", "none",
                     "Unauthenticated (tokenless) requests accepted by https://mcp.apify.com strictly when the tools query parameter selects only public tools enabled for unauthenticated Actor discovery and documentation search (excluding Actor execution and paid calls).",
                     [e_mcp], "Apify MCP server public Actor discovery and documentation search tools only"),
            ], "Supports Bearer API tokens (personal Console tokens or prepaid Apify AGI tokens), OAuth on hosted MCP, and keyless MCP access strictly for public Actor discovery/docs tools.")

            elig("testing", "free_access", True, [e_mcp, e_price], "Free plan ($0/month, no credit card required) includes $5 monthly platform credit for running Actors, plus keyless MCP discovery/docs tools.")
            elig("testing", "paid_required", False, [e_price], "Free tier ($0/mo with $5 spending credit) requires no credit card or payment.")
            elig("testing", "self_serve", True, [e_v2, e_int_api, e_price], "Developers sign up for free with no credit card and create Personal API tokens in Apify Console self-serve.")
            elig("production", "free_access", True, [e_price], "Free plan ($0/month) provides $5 recurring credit for Apify Store or custom Actors; higher production workloads use Starter ($19/mo), Scale ($199/mo), or Business ($999/mo) plans.")
            elig("production", "paid_required", False, [e_price], "Workloads within the $5/month Free credit allowance do not require a paid plan; larger workloads use paid plans ($19–$999/mo + pay-as-you-go).")
            elig("production", "admin_approval_required", None, [e_int_api, e_acc],
                 "Individual developers create Personal API tokens self-serve without admin approval (integrations/api.md lines 18-30), whereas accessing another user's or organization's shared Actors/storages requires the resource owner/admin to grant permissions (access-rights lines 39-53). Left unknown rather than asserting a mandatory administrator gate.",
                 status="unknown")
            elig("production", "self_serve", True, [e_int_api, e_price], "Free, Starter ($19/mo), Scale ($199/mo), and Business ($999/mo) plans and Personal API token creation are self-serve.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_v2]),
                claim("api.protocol.sdk", "SDK", [e_js, e_py]),
                claim("api.protocol.cli", "CLI", [e_int_api, e_js]),
            ], "RESTful HTTP API v2 (with OpenAPI YAML/JSON schemas), official API clients (JS, Python, Go, PHP, Java, .NET, Rust) & Actor SDKs (JS, Python), and Apify CLI.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_v2, e_mcp, e_js])

            e_v2_queues = E("docs.apify.com/api/v2.md", 227, 243, "Apify API v2 includes Key-Value Store record operations and Request Queue batch/locking endpoints.")

            items(r["api_surface"]["resource_groups"], [
                group("actors_runs_tasks", "Actors, Actor Runs, Saved Tasks, and Apify Store catalog", [e_v2, e_v2_toc, e_actors]),
                group("datasets", "Datasets (structured scraping results storage and retrieval)", [e_v2, e_v2_toc, e_js]),
                group("kv_stores_request_queues", "Key-Value Stores and Request Queues (crawl frontier and state management)", [e_v2_toc, e_v2_queues, e_js]),
                group("webhooks_schedules_access", "Integrations, Webhooks, Webhook Dispatches, Schedules, and granular resource permissions", [e_v2, e_v2_toc, e_actors, e_acc]),
            ], "Core Apify platform resource groups documented in API v2 and platform guides.")
            breadth("moderate", ["actors_runs_tasks", "datasets", "kv_stores_request_queues", "webhooks_schedules_access"],
                    [e_v2, e_v2_toc, e_v2_queues, e_actors, e_acc],
                    "Multiple related cloud scraping and actor-orchestration resource groups covering serverless Actor build/run lifecycle & Store catalog, Datasets, Key-Value Stores & Request Queues, and Webhooks/Schedules/permissions.")

            set_mcp_entries([
                ("official_hosted_mcp", "official", "Apify Hosted MCP Server (mcp.apify.com)", [e_mcp, e_mcp_pay, e_mcp_repo], "docs.apify.com/platform/integrations/mcp.md",
                 "Official hosted Streamable HTTP MCP server at https://mcp.apify.com exposing Apify Store Actors, Actor execution, storage retrieval, and documentation search via OAuth, Bearer API token, or keyless discovery mode.",
                 "https://mcp.apify.com", "https://github.com/apify/apify-mcp-server"),
                ("official_local_mcp", "official", "Apify Actors MCP Server (@apify/actors-mcp-server)", [e_mcp, e_mcp_repo], "raw.githubusercontent.com/apify/apify-mcp-server/master/README.md",
                 "Official open-source local stdio MCP server (npx @apify/actors-mcp-server) authenticated via APIFY_TOKEN or Apify CLI login.",
                 None, "https://github.com/apify/apify-mcp-server"),
            ], [e_mcp, e_mcp_repo])

            buildability(
                "build_now",
                "Build an Apify Actor execution, dataset retrieval, and web scraping integration via REST API v2, apify-client SDKs, or official MCP server.",
                ["Free tier is capped at $5/month of platform usage credit ($0.20 per compute unit); high-volume scraping requires paid plans ($19–$999/month) or pay-as-you-go."],
                ["Sign up for a free Apify account and generate a Personal API token in Apify Console (Settings > API & Integrations), or connect via OAuth to https://mcp.apify.com.",
                 "Use REST API v2 (https://docs.apify.com/api/openapi.json), apify-client (JS/Python), or @apify/actors-mcp-server."],
                [e_v2, e_int_api, e_mcp, e_mcp_repo, e_price],
                ["identity", "auth.bearer_api_token", "auth.mcp_oauth2", "testing.free_access", "testing.self_serve", "production.free_access", "production.self_serve", "api.protocol.rest", "api.protocol.sdk", "api.breadth", "mcp.discovery"],
                "Public OpenAPI schema, self-serve Free tier ($5/month credit, no card required), multi-language SDKs/CLI, and official hosted + local MCP servers enable immediate building.",
            )

        # =====================================================================
        # 56. Firecrawl
        # =====================================================================
        elif app == 56:
            e_intro = E("docs.firecrawl.dev/introduction.md", 4, 27, "Firecrawl is the context API for AI agents to search the web, scrape any page into clean Markdown or structured data, and interact with live pages, with a hosted Streamable HTTP MCP server at https://mcp.firecrawl.dev/v2/mcp, REST API, and official Python/Node SDKs.")
            e_api = E("docs.firecrawl.dev/api-reference/introduction.md", 24, 69, "Firecrawl REST API at base URL https://api.firecrawl.dev authenticates via Authorization: Bearer fc-... header, while /v1/scrape and /v1/search also support rate-limited keyless calls when the Authorization header is omitted.")
            e_mcp = E("docs.firecrawl.dev/mcp-server.md", 4, 49, "Firecrawl's official hosted MCP server supports keyless access or Bearer API key auth at https://mcp.firecrawl.dev/v2/mcp and browser OAuth team sign-in at https://mcp.firecrawl.dev/v2/mcp-oauth.")
            e_mcp_repo = E("raw.githubusercontent.com/firecrawl/firecrawl-mcp-server/main/README.md", 20, 72, "Official firecrawl/firecrawl-mcp-server repository provides 34 MCP tools (scrape, map, crawl, search, interact, monitor, credit_usage, etc.) supporting Firecrawl Cloud, self-hosted instances, a keyless free tier for scrape/search/parse, and FIRECRAWL_API_KEY configuration.")
            e_mcp_env = E("raw.githubusercontent.com/firecrawl/firecrawl-mcp-server/main/README.md", 218, 255, "firecrawl-mcp-server configuration documents FIRECRAWL_API_KEY (required for cloud API, optional for self-hosted with FIRECRAWL_API_URL) and MCP OAuth Bearer access tokens (fco_... via Authorization: Bearer or FIRECRAWL_OAUTH_TOKEN on stdio).")
            e_price = E("www.firecrawl.dev/pricing", 23, 114, "Firecrawl pricing includes a Free Plan ($0/month, no credit card required, 1,000 credits/month refreshed monthly), self-serve paid plans (Hobby $19/mo monthly or $16/mo annual for 5,000 credits; Standard $99/$83 for 100k; Growth $399/$333 for 500k; Scale $749/$599 for 1M with instant checkout and no sales call needed), and custom Enterprise ('Contact sales').")
            e_self = E("docs.firecrawl.dev/contributing/self-host", 88, 128, "Firecrawl open-source edition can be self-hosted via Docker Compose (quickstart disables API auth on a trusted network and starts without durable storage, TLS, HA, or every Firecrawl Cloud capability).")
            e_self_lim = E("docs.firecrawl.dev/contributing/self-host", 210, 220, "Self-hosted feature support table notes that core scrape/crawl/map/search routes are included, LLM extraction requires configuring an OpenAI-compatible/Ollama provider, and Fire-engine anti-bot, screenshots/page actions, Agent, Browser, and interact require Firecrawl Cloud or separate services.")
            e_lic = E("raw.githubusercontent.com/firecrawl/firecrawl/main/LICENSE", 1, 10, "The open-source Firecrawl repository (github.com/firecrawl/firecrawl) is licensed under the GNU Affero General Public License v3 (AGPL-3.0).")
            e_llms = E("docs.firecrawl.dev/llms.txt", 1, 30, "docs.firecrawl.dev/llms.txt publishes v2, v1, and webhooks OpenAPI JSON specifications (/api-reference/v2-openapi.json, /api-reference/webhooks-openapi.json).")
            e_doc_idx = E("docs.firecrawl.dev/_llms/en/v2/documentation.txt", 1, 149, "Firecrawl v2 documentation index covers CLI (lines 11-12), Scrape, Search, Interact (Browser Sandbox), Crawl, Map, Batch Scrape, Agent, SDKs (Node, Python, Go, Rust, CLI at lines 63-98), MCP Server, and Webhooks (lines 144-148).")

            r["identity"]["resolution"] = claim(
                "identity",
                "Firecrawl (firecrawl.dev / docs.firecrawl.dev / github.com/firecrawl/firecrawl) — web scraping, crawling, search, and browser interaction API and MCP server (distinguishing hosted Firecrawl Cloud from the AGPL-3.0 open-source self-hosted edition).",
                [e_intro, e_api, e_self, e_lic],
            )
            r["purpose"] = claim(
                "purpose",
                "AI web context API and AGPL-3.0 self-hostable engine for scraping pages to Markdown/JSON, site mapping/crawling, web search, and live browser interaction, with REST API v2, SDKs/CLI, and official MCP servers.",
                [e_intro, e_api, e_mcp_repo, e_self, e_self_lim, e_lic, e_doc_idx],
            )
            items(r["auth"], [
                auth("bearer_api_key", "bearer_token",
                     "Firecrawl API key (prefixed fc-...) passed in the Authorization: Bearer fc-... HTTP header for https://api.firecrawl.dev and https://mcp.firecrawl.dev/v2/mcp (or via FIRECRAWL_API_KEY env var for local firecrawl-mcp-server and SDKs; optional on self-hosted instances configured via FIRECRAWL_API_URL).",
                     [e_api, e_mcp, e_mcp_repo, e_mcp_env, e_doc_idx], "Firecrawl Cloud and self-hosted REST API v2, SDKs, CLI, and MCP server"),
                auth("mcp_oauth2", "oauth2",
                     "Browser OAuth sign-in and team approval via the hosted OAuth MCP endpoint https://mcp.firecrawl.dev/v2/mcp-oauth (issuing fco_... OAuth Bearer access tokens, or FIRECRAWL_OAUTH_TOKEN for stdio).",
                     [e_mcp, e_mcp_env], "Firecrawl hosted OAuth MCP server (https://mcp.firecrawl.dev/v2/mcp-oauth) and MCP OAuth access tokens"),
                auth("keyless_trial", "none",
                     "Rate-limited keyless access (omitting the Authorization header) on /v1/scrape, /v1/search, and https://mcp.firecrawl.dev/v2/mcp (scrape, search, parse tools).",
                     [e_intro, e_api, e_mcp, e_mcp_repo], "Firecrawl rate-limited keyless scrape/search/parse endpoints and MCP tools"),
            ], "Supports Bearer API keys (fc-... / FIRECRAWL_API_KEY), browser OAuth at /v2/mcp-oauth (fco_... tokens), and rate-limited keyless scrape/search access.")

            elig("testing", "free_access", True, [e_api, e_mcp, e_price], "Free tier provides 1,000 credits every month (refreshed monthly, no credit card required), plus rate-limited keyless scrape/search access and AGPL-3.0 self-hosting.")
            elig("testing", "paid_required", False, [e_price], "Free Plan ($0/month, 1,000 credits/month) requires no credit card or payment.")
            elig("testing", "self_serve", True, [e_mcp, e_price], "Developers can start keyless immediately or sign up self-serve for the Free Plan (no credit card required).")
            elig("production", "free_access", True, [e_price, e_self], "Hosted Free Plan provides 1,000 recurring monthly credits ($0/mo), and the open-source core can be self-hosted via Docker Compose under AGPL-3.0.")
            elig("production", "paid_required", False, [e_price, e_self], "Low-volume cloud workloads fit within the 1,000 monthly free credits (or self-hosted Docker Compose), while higher cloud volumes use paid plans ($19–$749/mo).")
            elig("production", "contact_sales_required", False, [e_price], "For standard self-serve Cloud plans — Free (1k credits/mo), Hobby (5k), Standard (100k), Growth (500k), and Scale (1,000,000 credits/month at $599/mo annual / $749/mo monthly, which 'checks out instantly, no sales call needed' at line 74) — no sales contact is required; only custom Enterprise plans (lines 88-94) use 'Contact sales'.")
            elig("production", "self_serve", True, [e_price], "All cloud tiers up to Scale ($599/mo annual / $749/mo monthly for 1M credits) check out self-serve without a sales call (custom Enterprise uses Contact sales).")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_api, e_llms]),
                claim("api.protocol.sdk", "SDK", [e_intro, e_llms, e_doc_idx]),
                claim("api.protocol.cli", "CLI", [e_doc_idx]),
            ], "REST HTTP API (v2/v1 with OpenAPI specs), official Python/Node/Go/Rust SDKs, and Firecrawl CLI.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_intro, e_api, e_llms, e_doc_idx])

            items(r["api_surface"]["resource_groups"], [
                group("scrape_batch_extract", "Scrape, Batch Scrape, and structured JSON/Markdown extraction", [e_intro, e_price, e_doc_idx]),
                group("crawl_map_webhooks", "Crawl, Map (site URL discovery), and Webhooks", [e_mcp_repo, e_llms, e_doc_idx]),
                group("search_interact_monitor", "Web Search, Interact (live browser actions/sessions), and page change Monitoring", [e_intro, e_mcp_repo, e_doc_idx]),
                group("usage_billing_account", "Credit usage and billing inspection (firecrawl_credit_usage)", [e_mcp_repo]),
            ], "Core Firecrawl v2 capabilities documented across docs.firecrawl.dev and firecrawl-mcp-server.")
            breadth("moderate", ["scrape_batch_extract", "crawl_map_webhooks", "search_interact_monitor", "usage_billing_account"],
                    [e_intro, e_mcp_repo, e_llms, e_doc_idx],
                    "Multiple related web-context and scraping resource groups covering single/batch page scraping & extraction, site crawling/mapping & webhooks, web search & browser interaction/monitoring, and credit usage inspection.")

            e_fc_repo_link = E("raw.githubusercontent.com/firecrawl/firecrawl/main/README.md", 342, 346, "Official firecrawl/firecrawl README links to https://github.com/firecrawl/firecrawl-mcp-server for MCP.")
            set_mcp_entries([
                ("official_hosted_mcp", "official", "Firecrawl Hosted MCP Server", [e_intro, e_mcp, e_fc_repo_link], "docs.firecrawl.dev/mcp-server.md",
                 "Official hosted Streamable HTTP MCP server at https://mcp.firecrawl.dev/v2/mcp (keyless or Bearer API key) and https://mcp.firecrawl.dev/v2/mcp-oauth (browser OAuth sign-in).",
                 "https://mcp.firecrawl.dev/v2/mcp", "https://github.com/firecrawl/firecrawl-mcp-server"),
                ("official_local_mcp", "official", "Firecrawl Open-Source MCP Server (firecrawl-mcp)", [e_mcp_repo, e_mcp_env, e_fc_repo_link], "raw.githubusercontent.com/firecrawl/firecrawl-mcp-server/main/README.md",
                 "Official open-source MCP server repository (github.com/firecrawl/firecrawl-mcp-server, 34 tools) supporting Firecrawl Cloud and self-hosted Firecrawl deployments.",
                 None, "https://github.com/firecrawl/firecrawl-mcp-server"),
            ], [e_intro, e_mcp, e_mcp_repo, e_fc_repo_link])

            buildability(
                "build_now",
                "Build a Firecrawl web scraping, site crawling/mapping, search, and browser interaction integration via REST API v2, SDKs, or official MCP server.",
                ["Free Cloud tier is capped at 1,000 credits/month and 2 concurrent requests (keyless mode is rate-limited and restricted to scrape/search/parse).",
                 "Self-hosted open-source edition is licensed under AGPL-3.0 and its default Docker Compose stack omits Fire-engine anti-bot, screenshots/page actions, Agent, Browser, and interact unless configured with external services or Firecrawl Cloud."],
                ["Connect immediately to https://mcp.firecrawl.dev/v2/mcp (keyless or with Bearer fc-... API key) or https://mcp.firecrawl.dev/v2/mcp-oauth.",
                 "For custom backend services, call https://api.firecrawl.dev using v2 OpenAPI specs or official Python/Node SDKs."],
                [e_intro, e_api, e_mcp, e_mcp_repo, e_mcp_env, e_price, e_self, e_self_lim, e_lic, e_llms, e_doc_idx],
                ["identity", "auth.bearer_api_key", "auth.mcp_oauth2", "auth.keyless_trial", "testing.free_access", "testing.self_serve", "production.free_access", "production.self_serve", "api.protocol.rest", "api.protocol.sdk", "api.breadth", "mcp.discovery"],
                "Public OpenAPI specs, 1,000 free monthly credits (no credit card required), keyless trial endpoints, and official hosted + local MCP servers support immediate building.",
            )

        # =====================================================================
        # 57. Bright Data
        # =====================================================================
        elif app == 57:
            e_auth = E("docs.brightdata.com/api-reference/authentication.md", 4, 41, "Bright Data supports API Access via an API key passed as Authorization: Bearer <token> (a default key is created automatically upon account creation, and additional keys with scoped permissions can be created in Account settings) and Native Access via proxy protocol username and password.")
            e_auth_proxy = E("docs.brightdata.com/api-reference/authentication.md", 96, 117, "Bright Data Native proxy protocol authentication is supported across all proxy networks (Datacenter, ISP, Residential, Mobile), Web Unlocker, and Scraping Browser using --proxy brd.superproxy.io:44445 and --proxy-user brd-customer-[ACCOUNT_ID]-zone-[PROXY_NAME]:[PROXY_PASSWORD].")
            e_free = E("docs.brightdata.com/general/account/billing-and-pricing/free-tier.md", 4, 30, "Every new Bright Data account automatically gets 5,000 free credits per month (~$7.50 value, no credit card, no promo code, no commitment, renewing monthly on a prepaid wallet with a hard stop) across Web Unlocker API, SERP API, Web Scraper API, Scraper Studio, Browser API, and Bright Data MCP server (proxies are excluded and get a separate one-time $2 7-day trial credit).")
            e_mcp = E("docs.brightdata.com/products/mcp-server/overview.md", 4, 42, "Official Bright Data MCP server gives AI agents real-time web data access (drawing from the 5,000 free monthly credits pool) with both Remote (hosted) and Local (self-hosted) deployment options.")
            e_mcp_repo = E("raw.githubusercontent.com/brightdata/brightdata-mcp/main/README.md", 25, 65, "Official github.com/brightdata/brightdata-mcp (@brightdata/mcp) exposes 31 tools (Web search, Page scraping Fetch API, 1,200+ pre-built Web Scraper APIs, Business Search, Browser automation, LLM response collection) via a remote hosted server at https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN or local stdio via npx @brightdata/mcp with API_TOKEN.")
            e_price = E("brightdata.com/pricing", 60, 116, "Bright Data pricing includes FREE TIER on Web Access APIs (Unlocker, SERP, Browser) and Scraper APIs/Scraper Studio, plus pay-as-you-go rates for Datasets ($250/100K rec), Data Firehose, Retail Insights ($2000/mo), Managed Data ($1500/mo), and Proxy Infrastructure, with self-serve 'Start free trial' and enterprise 'Contact sales'.")
            e_unlocker = E("docs.brightdata.com/products/web-unlocker/introduction.md", 4, 7, "Web Unlocker API handles proxy rotation, anti-bot challenges, and CAPTCHA solving in a single API call returning clean HTML or JSON.")
            e_serp = E("docs.brightdata.com/products/serp-api/introduction.md", 4, 7, "SERP API extracts structured search results from Google, Bing, and other search engines.")
            e_scrapers = E("docs.brightdata.com/products/scrapers/overview.md", 4, 6, "Web Scraper API provides pre-built scrapers returning structured JSON for Amazon, LinkedIn, Instagram, TikTok, and thousands of websites.")
            e_datasets = E("docs.brightdata.com/api-reference/marketplace-dataset-api/overview.md", 4, 7, "Marketplace Dataset API queries 900+ pre-collected Marketplace datasets via real-time Search and bulk async Filter endpoints at $2.5 CPM.")
            e_zone = E("docs.brightdata.com/api-reference/account-management-api/Add_a_Zone.md", 4, 6, "Account Management API adds a Zone via POST /zone returning zone or account configuration data as JSON.")
            e_browser = E("docs.brightdata.com/products/scraping-browser/introduction.md", 4, 25, "Browser API runs Puppeteer, Playwright, or Selenium scripts on remote cloud browsers with built-in unblocking.")
            e_cli = E("docs.brightdata.com/products/cli/overview.md", 4, 7, "Bright Data CLI scrapes sites, searches the web, queries pre-built scrapers, and manages accounts from a terminal.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Bright Data (brightdata.com / docs.brightdata.com) — web data, unlocker, SERP, scraper, dataset, remote browser, and proxy platform offering REST APIs, CLI/SDKs, and official MCP server.",
                [e_auth, e_free, e_mcp, e_datasets, e_zone],
            )
            r["purpose"] = claim(
                "purpose",
                "Web data and proxy platform offering Web Unlocker, SERP API, Web Scraper API, Marketplace Datasets, Browser API, Account Management API, CLI/SDKs, and an official hosted/local MCP server (@brightdata/mcp) with 5,000 free monthly credits on eligible scraping/browser APIs.",
                [e_auth, e_free, e_mcp, e_mcp_repo, e_datasets, e_zone, e_cli],
            )
            items(r["auth"], [
                auth("bearer_api_key", "bearer_token",
                     "Bright Data API key (created automatically upon account signup or in Account settings with scoped user permissions) passed in the Authorization: Bearer <token> HTTP header for REST APIs, as API_TOKEN for local npx @brightdata/mcp, or in the token query parameter for https://mcp.brightdata.com/mcp.",
                     [e_auth, e_mcp_repo], "Bright Data REST APIs, CLI, SDKs, and official MCP server"),
                auth("native_proxy_credentials", "basic",
                     "Native proxy protocol authentication across proxy networks (Datacenter, ISP, Residential, Mobile), Web Unlocker, and Scraping Browser using host brd.superproxy.io:44445 and compound username/password brd-customer-[ACCOUNT_ID]-zone-[PROXY_NAME]:[PROXY_PASSWORD].",
                     [e_auth, e_auth_proxy], "Bright Data Native proxy protocol access (Proxy Networks, Web Unlocker, and Scraping Browser)"),
            ], "REST APIs and MCP use API key tokens (Authorization: Bearer <token>); proxy protocol connections use Native zone username/password (brd-customer-[ACCOUNT_ID]-zone-[PROXY_NAME]:[PROXY_PASSWORD]).")

            elig("testing", "free_access", True, [e_free, e_mcp, e_datasets], "Every new account automatically receives 5,000 free credits per month (~$7.50 value, no credit card required) usable across the eligible free-pool products: Web Unlocker API, SERP API, Web Scraper API, Scraper Studio, Browser API, and Bright Data MCP server (whereas Proxy networks and Marketplace Datasets at $2.5 CPM / $250 per 100K records are not in the 5,000-credit free pool).")
            elig("testing", "trial_access", True, [e_free, e_price], "In addition to the 5,000 monthly free API credits on scraping/unlocker/browser APIs, new accounts receive a separate one-time $2 7-day trial credit to test proxy products.")
            elig("testing", "paid_required", False, [e_free], "Testing the eligible free-pool APIs (Web Unlocker, SERP, Web Scraper, Scraper Studio, Browser API, and MCP) within 5,000 monthly credits (or proxies within the $2 7-day trial credit) requires no credit card or payment.")
            elig("testing", "self_serve", True, [e_auth, e_free], "A default API key and the 5,000 monthly free credit allowance are provisioned automatically upon self-serve account creation.")
            elig("production", "free_access", True, [e_free, e_datasets, e_price], "Scoped to the 5,000-credit/month free-tier product pool (Web Unlocker API, SERP API, Web Scraper API, Scraper Studio, Browser API, and MCP server), credits renew on the first of every month with a prepaid wallet hard stop; Marketplace Datasets ($2.5 CPM / $250 per 100K records) and Proxy Infrastructure (Datacenter, ISP, Residential) are excluded from the monthly free credits.")
            elig("production", "paid_required", False, [e_free, e_datasets, e_price], "Scoped to the eligible 5,000-credit/month free-pool products (Web Unlocker, SERP, Web Scraper, Scraper Studio, Browser API, and MCP), usage up to 5,000 credits/month requires no payment; exceeding 5,000 credits/month or using Marketplace Datasets ($2.5 CPM) or Proxy Infrastructure requires prepaid wallet deposits or paid plans.")
            elig("production", "self_serve", True, [e_auth, e_free, e_price], "Account signup, default API key provisioning, 5,000/month free tier, and pay-as-you-go wallet deposits are self-serve.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_auth, e_unlocker, e_datasets, e_zone]),
                claim("api.protocol.cli", "CLI", [e_auth, e_cli]),
                claim("api.protocol.sdk", "SDK", [e_auth]),
            ], "REST HTTP APIs (https://api.brightdata.com), Bright Data CLI, Python/JavaScript SDKs, and remote Browser/Proxy protocols.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_auth, e_free, e_mcp])

            items(r["api_surface"]["resource_groups"], [
                group("unlocker_serp_browser", "Web Unlocker API, SERP API, and Browser API (remote Puppeteer/Playwright/Selenium)", [e_unlocker, e_serp, e_browser]),
                group("scrapers_studio", "Web Scraper API (1,200+ pre-built domain scrapers) and Scraper Studio", [e_free, e_mcp_repo, e_scrapers]),
                group("marketplace_datasets", "Marketplace Dataset API (real-time Search and async Filter across 900+ datasets)", [e_datasets]),
                group("account_zone_management", "Account Management API (adding a Zone via POST /zone and returning zone/account configuration JSON)", [e_zone]),
            ], "Core Bright Data API product suites verified from primary docs.")
            breadth("broad", ["unlocker_serp_browser", "scrapers_studio", "marketplace_datasets", "account_zone_management"],
                    [e_mcp_repo, e_unlocker, e_serp, e_scrapers, e_datasets, e_zone, e_browser],
                    "Spans web unblocking, multi-engine SERP extraction, 1,200+ pre-built structured scrapers, 900+ pre-collected Marketplace datasets, remote cloud browser automation (Puppeteer/Playwright/Selenium), and account/zone creation (`POST /zone`).")

            set_mcp_entries([
                ("official_remote_mcp", "official", "Bright Data Remote MCP Server", [e_mcp, e_mcp_repo], "raw.githubusercontent.com/brightdata/brightdata-mcp/main/README.md",
                 "Official hosted remote MCP server at https://mcp.brightdata.com/mcp (authenticated via ?token=YOUR_API_TOKEN) providing web search, page scraping, structured scrapers, and remote browser automation.",
                 "https://mcp.brightdata.com/mcp", "https://github.com/brightdata/brightdata-mcp"),
                ("official_local_mcp", "official", "Bright Data Local MCP Server (@brightdata/mcp)", [e_mcp, e_mcp_repo], "docs.brightdata.com/products/mcp-server/overview.md",
                 "Official open-source local stdio MCP server (npx @brightdata/mcp with API_TOKEN) from github.com/brightdata/brightdata-mcp.",
                 None, "https://github.com/brightdata/brightdata-mcp"),
            ], [e_mcp, e_mcp_repo])

            buildability(
                "build_now",
                "Build a Bright Data web unblocking, SERP, structured scraping, dataset lookup, or browser automation integration via REST APIs or official MCP server.",
                ["Proxy infrastructure products (Residential, ISP, Datacenter) and Marketplace Datasets ($2.5 CPM / $250 per 100K records) are excluded from the 5,000 monthly free credits (proxies receive only a one-time $2 7-day trial credit), and usage beyond 5,000 monthly credits requires prepaid balance deposits."],
                ["Create a free Bright Data account (no credit card required) to receive an automatic default API key and 5,000 recurring monthly free credits across Web Unlocker, SERP, Web Scraper, Scraper Studio, Browser API, and MCP.",
                 "Connect via https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN, npx @brightdata/mcp, or REST endpoints at https://api.brightdata.com."],
                [e_auth, e_auth_proxy, e_free, e_mcp, e_mcp_repo, e_price, e_datasets],
                ["identity", "auth.bearer_api_key", "auth.native_proxy_credentials", "testing.free_access", "testing.paid_required", "testing.self_serve", "production.free_access", "production.paid_required", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp.discovery"],
                "Automatic API key creation, 5,000 free monthly credits on eligible scraping/browser/MCP products with no credit card required, public REST/CLI/SDK docs, and official remote + local MCP servers make Bright Data immediately buildable.",
            )

        # =====================================================================
        # 58. Sherlock (Pilot app — preserved pilot history + v1.1 clean capture)
        # =====================================================================
        elif app == 58:
            e_repo = E("github.com/sherlock-project/sherlock", 166, 226, "Sherlock Project (github.com/sherlock-project/sherlock, MIT license) is an open-source Python CLI tool to hunt down social media accounts by username across 400+ social networks; repository --help output (Version 0.16.0) lists options --folderoutput, --output, --csv, --xlsx, --site, --proxy, --dump-response, --json, --timeout, --print-all, --print-found, --no-color, --browse, --local, --nsfw, --txt, and --ignore-exclusions (omitting --tor / --unique-tor).")
            e_pyp = E("raw.githubusercontent.com/sherlock-project/sherlock/master/pyproject.toml", 7, 59, "pyproject.toml defines package sherlock-project v0.16.2 (MIT license, Python ^3.9, homepage https://sherlockproject.xyz/, repository https://github.com/sherlock-project/sherlock) with CLI entry point sherlock = 'sherlock_project.sherlock:main'.")
            e_lic = E("raw.githubusercontent.com/sherlock-project/sherlock/master/LICENSE", 1, 10, "MIT License granting free permission to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.")
            e_inst = E("sherlockproject.xyz/installation", 32, 90, "Sherlock is installed locally via pipx/pip (pipx install sherlock-project), Docker (docker run --rm -t sherlock/sherlock), dnf, or run as a Python module (python3 -m sherlock_project).")
            e_use = E("sherlockproject.xyz/usage", 25, 72, "sherlockproject.xyz/usage shows an older CLI --help excerpt labeled Version 0.14.3 accepting USERNAMES and options including --folderoutput, --output, --tor, --unique-tor, --csv, --xlsx, --site, --proxy, --json (load data from a JSON file or online JSON file), --timeout, --print-all, --print-found, --no-color, --browse, --local (force use of local data.json), and --nsfw.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Sherlock Project (github.com/sherlock-project/sherlock / sherlockproject.xyz, PyPI package sherlock-project) — open-source MIT-licensed Python CLI for searching usernames across 400+ social networks (local CLI software, not a hosted SaaS API).",
                [e_repo, e_pyp, e_inst],
            )
            r["purpose"] = claim(
                "purpose",
                "Open-source MIT-licensed Python command-line tool (sherlock-project) that searches for social media accounts by username across 400+ social networks.",
                [e_repo, e_pyp, e_use],
            )
            items(r["auth"], [
                auth("cli_no_auth", "none",
                     "Local open-source CLI execution (`sherlock USERNAMES`) requires no vendor account, API key, or authentication token; outbound probes support `--proxy PROXY_URL` (note: `sherlockproject.xyz/usage` Version 0.14.3 help lists `--tor`/`--unique-tor`, whereas `github.com/sherlock-project/sherlock` Version 0.16.0 help omits `--tor` while `pyproject.toml` is at v0.16.2).",
                     [e_repo, e_pyp, e_inst, e_use], "Local Sherlock CLI execution"),
            ], "Sherlock is local open-source CLI software under the MIT license and requires no vendor authentication credentials.")

            elig("testing", "free_access", True, [e_repo, e_lic, e_inst], "MIT-licensed open-source software freely installable via pipx, pip, Docker, or git clone at no cost.")
            elig("testing", "paid_required", False, [e_lic, e_inst], "MIT License permits free use without charge.")
            elig("testing", "admin_approval_required", False, [e_inst], "Userspace installation (pipx install sherlock-project or pip install --user sherlock-project) requires no vendor or organization admin approval.")
            elig("testing", "vendor_approval_required", False, [e_lic, e_inst], "Public MIT-licensed repository and PyPI/Docker packages require no vendor approval.")
            elig("testing", "partner_approval_required", False, [e_lic, e_inst], "No partner program or approval applies to the open-source CLI.")
            elig("testing", "contact_sales_required", False, [e_lic, e_inst], "Open-source download and installation require no sales contact.")
            elig("testing", "self_serve", True, [e_inst], "Developers self-serve install from PyPI, Docker Hub, or GitHub.")

            elig("production", "free_access", True, [e_lic, e_inst], "MIT License grants unrestricted royalty-free use, modification, and deployment.")
            elig("production", "paid_required", False, [e_lic], "MIT License permits use and distribution free of charge.")
            elig("production", "admin_approval_required", False, [e_lic, e_inst], "No vendor/tenant admin approval is required to deploy the local CLI or Docker container.")
            elig("production", "vendor_approval_required", False, [e_lic], "MIT License requires no vendor review or approval.")
            elig("production", "partner_approval_required", False, [e_lic], "No partner approval applies to the MIT-licensed CLI.")
            elig("production", "contact_sales_required", False, [e_lic], "No sales contact applies to the MIT-licensed CLI.")
            elig("production", "self_serve", True, [e_lic, e_inst], "Self-serve installation and execution via PyPI, Docker, or source repository.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.cli", "CLI", [e_repo, e_pyp, e_use]),
            ], "Local CLI entrypoint (`sherlock` / `python3 -m sherlock_project`); no official hosted REST or GraphQL API.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_repo, e_inst, e_use])

            items(r["api_surface"]["resource_groups"], [
                group("username_search_cli", "Username search across 400+ social networks with site selection (`--site`, `--nsfw`, `--ignore-exclusions`), site-data source selection (`--json`, `--local`), proxy routing (`--proxy`; `--tor`/`--unique-tor` in v0.14.3 usage docs but omitted in v0.16.0 repo README help), and file export (`--output`, `--folderoutput`, `--csv`, `--xlsx`, `--txt`)", [e_repo, e_pyp, e_use]),
            ], "Single focused CLI workflow for multi-site username reconnaissance and result export.")
            breadth("narrow", ["username_search_cli"],
                    [e_repo, e_use],
                    "Focused single-domain command-line utility for probing candidate social-network profiles by username and exporting results.")

            set_mcp_not_found(
                [e_repo, e_pyp, e_inst, e_use],
                "Checked official Sherlock repository (github.com/sherlock-project/sherlock), pyproject.toml, and official documentation (sherlockproject.xyz) contain no MCP server entry (bounded to checked official sources; consistent with Task 05 pilot verification).",
            )

            buildability(
                "build_now",
                "Wrap the local open-source Sherlock CLI (or Docker image sherlock/sherlock) as a bounded agent tool returning structured CSV/text username-search output.",
                ["Sherlock is a local CLI utility rather than a hosted REST API, and no MCP server was found in checked official sources; execution requires a Python/container runtime and outbound network access to target sites, which may rate-limit or block probes."],
                ["Install sherlock-project via pipx/pip or pull the official sherlock/sherlock Docker image.",
                 "Invoke `sherlock --csv --timeout <sec> --print-found <username>` in a subprocess with bounded timeouts and parse the generated output."],
                [e_repo, e_lic, e_inst, e_use],
                ["identity", "auth.cli_no_auth", "testing.free_access", "testing.self_serve", "production.free_access", "production.self_serve", "api.protocol.cli", "api.breadth"],
                "MIT-licensed open-source CLI requires no credentials or vendor approval and can be wrapped immediately in a local/containerized agent tool.",
            )

        # =====================================================================
        # 59. Waterfall.io
        # =====================================================================
        elif app == 59:
            e_over = E("docs.waterfall.io/v1/overview.md", 4, 34, "Waterfall.io (docs.waterfall.io) is a B2B contact and company GTM data API aggregating 30+ data vendors at https://api.waterfall.io with x-api-key header authentication.")
            e_about = E("docs.waterfall.io/v1/about-waterfall.md", 4, 25, "Waterfall combines 30+ B2B data providers through one API for finding prospects, enriching contacts and companies, finding emails and mobile numbers, verifying emails, and checking job changes.")
            e_auth = E("docs.waterfall.io/v1/authentication.md", 4, 18, "Waterfall API requests to https://api.waterfall.io (/v1/ data endpoints and /v2/account Account Reporter V2) authenticate with the x-api-key header; master API keys can create and manage labeled sub-keys.")
            e_keys = E("docs.waterfall.io/v1/api-keys-overview.md", 4, 19, "A Waterfall master API key manages sub-keys via GET/POST/PUT /v1/api-keys; enabling key management for an account requires contacting your account manager.")
            e_demo = E("docs.waterfall.io/v1/book-demo.md", 4, 15, "Waterfall API access is available by approval: developers request an API key via the email field on waterfall.io or book a call, and a member of the Waterfall team reviews every access request before enabling access.")
            e_faq = E("docs.waterfall.io/v1/faq.md", 90, 128, "Waterfall FAQ confirms API access is available by approval after team review, capabilities (such as include_phones) are enabled per key, agents call the HTTP API using an authorized API key and the published OpenAPI file, and responses report per-job cost in output.usage.")
            e_eval = E("docs.waterfall.io/v1/evaluate-waterfall.md", 45, 50, "To evaluate Waterfall on sample inputs, prospective customers can talk to the Waterfall team (mailto:support@waterfall.io) about a test plan.")
            e_price = E("waterfall.io/pricing", 15, 34, "Waterfall pricing is outcome-based (a credit is deducted only when a verified result is returned) and has no public rate card; per-credit rates are quoted by the team after benchmarking a sample of the customer's records.")
            e_skills = E("docs.waterfall.io/v1/skills-overview.md", 4, 21, "Waterfall publishes agent skills (waterfall-direct-api and waterfall-integration) that guide coding agents to call the Waterfall HTTP API using an API key and OpenAPI specification.")
            e_llms = E("docs.waterfall.io/llms.txt", 1, 56, "docs.waterfall.io/llms.txt indexes the complete Waterfall v1/v2 documentation and OpenAPI specifications, containing agent skills and REST endpoints but no MCP server.")
            e_comp = E("docs.waterfall.io/v1/company-enrichment-launcher.md", 4, 35, "Company Enrichment Launcher reference embeds OpenAPI `openapi: 3.1.0` specification.")
            e_emv = E("docs.waterfall.io/v1/email-verifier.md", 4, 34, "Email Verifier synchronous endpoint reference embeds OpenAPI `openapi: 3.1.0` specification.")
            e_rev = E("docs.waterfall.io/v1/company-reveal-launcher.md", 4, 29, "Company Reveal Launcher (IPv4 to company lookup) embeds OpenAPI `openapi: 3.1.0` specification.")
            e_job = E("docs.waterfall.io/v1/job-change-launcher.md", 4, 33, "Job Change Launcher reference embeds OpenAPI `openapi: 3.1.0` specification.")
            e_rep = E("docs.waterfall.io/v1/account-reporter-v2.md", 4, 27, "Account Reporter v2 (/v2/account) reports API usage by key and account, remaining balance, and master-key unit prices.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Waterfall.io (waterfall.io / docs.waterfall.io) — B2B contact and company enrichment REST API aggregating 30+ data vendors (matches the roster hint 'waterfall.io (contact/company intel)'; distinct from other products named Waterfall).",
                [e_over, e_about, e_price],
            )
            r["purpose"] = claim(
                "purpose",
                "B2B contact and company intelligence REST API (https://api.waterfall.io) aggregating 30+ data providers for prospecting, contact/phone/company enrichment, email verification, job-change tracking, and IP company reveal.",
                [e_over, e_about, e_llms],
            )
            items(r["auth"], [
                auth("x_api_key", "api_key",
                     "Waterfall API key (master key or sub-key) passed in the x-api-key HTTP header on requests to https://api.waterfall.io (/v1/ data endpoints and /v2/account Account Reporter V2); master keys also manage sub-keys at /v1/api-keys.",
                     [e_auth, e_keys, e_faq], "Waterfall.io v1 data/api-keys endpoints and v2 Account Reporter API"),
            ], "All Waterfall API requests authenticate with x-api-key: YOUR_API_KEY; webhook deliveries are verified via Waterfall public JWKS signing keys.")

            elig("testing", "vendor_approval_required", True, [e_demo, e_faq, e_eval], "API access is available by approval: the Waterfall team reviews every API key request before enabling access.")
            elig("testing", "contact_sales_required", None, [e_demo, e_faq, e_eval],
                 "docs.waterfall.io/v1/book-demo.md (lines 6-11) and faq.md (line 91) state that developers can either enter their work email on the Waterfall homepage to request an API key or optionally book a call ('Request an API key... or book a call'). Because a key request undergoes team approval without necessarily requiring a sales call for testing, testing.contact_sales_required is preserved as unknown.",
                 status="unknown")
            elig("testing", "self_serve", False, [e_demo, e_faq], "There is no self-serve instant key signup; every access request is reviewed by the Waterfall team before enabling access.")

            elig("production", "paid_required", True, [e_faq, e_price], "Production requests deduct paid credits/USD balance per verified result under custom quoted per-credit rates.")
            elig("production", "vendor_approval_required", True, [e_demo, e_faq], "Every API access request is reviewed by the Waterfall team, and specific capabilities (such as phone enrichment) must be enabled on the key.")
            elig("production", "contact_sales_required", True, [e_keys, e_demo, e_faq, e_price], "Waterfall has no public rate card or self-serve commercial checkout; production per-credit rates are quoted after benchmarking a sample of records with the Waterfall team, and enabling master-key sub-key management requires contacting an account manager.")
            elig("production", "self_serve", False, [e_demo, e_faq, e_price], "API access and commercial terms require Waterfall team review and custom quoting rather than self-serve provisioning.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_over, e_auth, e_faq, e_comp]),
            ], "REST HTTP API at https://api.waterfall.io with published OpenAPI 3.1.0 specification and signed webhook callbacks.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_over, e_auth, e_llms, e_comp])

            items(r["api_surface"]["resource_groups"], [
                group("contact_phone_enrichment_verify", "Contact Enrichment, Phone Enrichment, and Email Verifier", [e_over, e_faq, e_emv]),
                group("prospector_search_titles", "Prospector, Search Contact, Search Company, and Company Titles", [e_over, e_llms]),
                group("company_reveal_job_change", "Company Enrichment, Company Reveal (IPv4-to-company), and Job Change tracking", [e_comp, e_rev, e_job]),
                group("account_keys_webhooks", "Account Reporter v2 (/v2/account), API Keys Management (/v1/api-keys), and Webhook JWKS verification", [e_auth, e_keys, e_llms, e_rep]),
            ], "All Waterfall v1/v2 endpoint groups indexed in docs.waterfall.io/llms.txt.")
            breadth("moderate", ["contact_phone_enrichment_verify", "prospector_search_titles", "company_reveal_job_change", "account_keys_webhooks"],
                    [e_over, e_llms, e_rep],
                    "Multiple related B2B GTM data resource groups covering contact/phone/company enrichment, prospecting/search, email verification, job-change/IP reveal, and account/sub-key usage reporting.")

            set_mcp_not_found(
                [e_faq, e_skills, e_llms],
                "Checked docs.waterfall.io (including llms.txt, FAQ, and Agent Skills pages) document agent skills (waterfall-direct-api, waterfall-integration) that call the REST API via OpenAPI 3.1.0, and list no official or community MCP server.",
            )

            buildability(
                "outreach_required",
                "Build a Waterfall.io B2B contact/company enrichment, prospecting, email verification, and job-change agent toolkit via the REST API (https://api.waterfall.io).",
                ["API access is gated by Waterfall team approval and commercial onboarding ('Request an API key' or 'Book a call' on waterfall.io; no self-serve key signup or public rate card).",
                 "Individual capabilities such as phone enrichment (include_phones: true) and master-key sub-key management (via account manager) must be explicitly enabled on the account key."],
                ["Request API access and an evaluation test plan from the Waterfall team (waterfall.io or support@waterfall.io) and confirm required endpoint entitlements.",
                 "Use the public OpenAPI 3.1.0 specification and x-api-key authentication to implement async Launcher/Finder polling or signed webhook handlers."],
                [e_over, e_auth, e_keys, e_demo, e_faq, e_price, e_llms, e_comp],
                ["identity", "auth.x_api_key", "testing.vendor_approval_required", "testing.self_serve", "production.paid_required", "production.vendor_approval_required", "production.contact_sales_required", "production.self_serve", "api.protocol.rest", "api.public_docs", "api.breadth"],
                "The REST API and OpenAPI 3.1.0 spec are publicly documented in detail, but obtaining an API key for testing or production requires outreach and approval from the Waterfall team.",
            )

        # =====================================================================
        # 60. Clay
        # =====================================================================
        elif app == 60:
            e_dev = E("developers.clay.com/index.md", 4, 42, "Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.")
            e_qs = E("developers.clay.com/quickstart.md", 4, 29, "Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`).")
            e_auth = E("developers.clay.com/public-api/authentication.md", 4, 23, "Every request to the Clay Public API (e.g., https://api.clay.com/public/v0/me) requires a personal API key in the clay-api-key HTTP header, tied to a Clay user and workspace access.")
            e_rate = E("developers.clay.com/public-api/rate-limits.md", 4, 15, "Clay Public API enforces a default rate limit of 300 requests per minute per workspace, shared across all API keys and OAuth credentials in the workspace.")
            e_cli = E("developers.clay.com/concepts/cli-basics.md", 4, 37, "The JSON-first Clay CLI (`clay`) writes machine-readable JSON to stdout and authenticates per workspace via `clay login` (browser OAuth) or `clay login --device` for headless environments.")
            e_srch = E("developers.clay.com/searches.md", 17, 30, "Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).")
            e_tbl = E("developers.clay.com/tables.md", 4, 25, "Tables API (POST https://api.clay.com/public/v0/tables/query) lets customers query known Clay tables and is available on Enterprise plans only.")
            e_rout = E("developers.clay.com/routines/api.md", 4, 100, "Routines API runs Clay-managed functions and custom functions via POST https://api.clay.com/public/v0/routines/{routine_id}/run and polls GET .../routines/run/{id}/results; Workflows are also routines and are in Alpha.")
            e_cfunc = E("developers.clay.com/routines/custom-functions.md", 21, 47, "Calling a custom function via Clay's MCP connector (`list_subroutines`) requires enabling MCP access in the function's settings; workspace and role permissions still apply, and if a user cannot change access they can ask a workspace admin to check integration and role access settings.")
            e_wh = E("developers.clay.com/public-api/webhooks.md", 4, 58, "Clay webhooks notify a service when a routine run finishes by sending a signed POST (`X-Clay-Signature` HMAC-SHA256).")
            e_mcp_page = E("www.clay.com/mcp", 166, 268, "Clay MCP (©2026 Clay Labs Inc. at line 267) connects AI tools (Claude, ChatGPT, Codex) to Clay's 200+ data providers, Clay Functions, Audiences, and People Search with budget guardrails and admin controls.")
            e_price = E("www.clay.com/pricing", 212, 319, "Clay pricing includes a Free plan ('Start building in Clay for free. No strings attached.', 500 actions/mo), 14-day trials on self-serve paid Launch (starts at $54/mo annual / $60/mo monthly; adds 'Reuse functions across workflows') and Growth (starts at $185/mo annual / $205/mo monthly; adds 'Integrate with any HTTP API' and 'Automate any signal via webhook') plans, and custom Enterprise ('Get a demo' or 'buy now', RBAC, SSO, credit budgeting).")
            e_plug = E("raw.githubusercontent.com/clay-run/agent-plugins/main/README.md", 7, 38, "Official github.com/clay-run/agent-plugins repository provides Clay skills and the `clay` CLI for Claude Code, Codex, and Cursor.")
            e_llms60 = E("developers.clay.com/llms.txt", 1, 55, "developers.clay.com/llms.txt indexes Workflows (Alpha), Audiences privacy deletion, Get workspace credit balances (api-reference/credits/get-workspace-credit-balances.md), Get the authenticated user (api-reference/me/get-the-authenticated-user.md), Routines execution/batch runs, Search queries/iterators, Tables (Enterprise) structured queries, and Workflows runs search, plus /openapi.json.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Clay (Clay Labs Inc., clay.com / developers.clay.com) — go-to-market data enrichment and automation platform providing Public REST API (api.clay.com/public/v0), JSON-first `clay` CLI, and official Clay MCP connector.",
                [e_dev, e_auth, e_cli, e_mcp_page],
            )
            r["purpose"] = claim(
                "purpose",
                "Go-to-market data enrichment and automation platform with a Public REST API (Searches, Routines/Functions, Enterprise Tables, workspace credit balances, and signed Webhooks at https://api.clay.com/public/v0), JSON-first `clay` CLI, and an official Clay MCP connector.",
                [e_dev, e_auth, e_cli, e_rout, e_wh, e_mcp_page, e_llms60],
            )
            items(r["auth"], [
                auth("clay_api_key", "api_key",
                     "Personal Clay API key created under API and CLI -> API keys in the Clay workspace (or via `clay api-keys create`) and sent in the `clay-api-key` HTTP header on requests to https://api.clay.com/public/v0/.",
                     [e_qs, e_auth], "Clay Public REST API (https://api.clay.com/public/v0)"),
                auth("oauth2_cli_and_workspace", "oauth2",
                     "Per-workspace OAuth authentication used by `clay login` (browser flow) and `clay login --device` (headless device-code flow) for the Clay CLI and workspace OAuth integrations (sharing the 300 req/min per-workspace rate limit with API keys).",
                     [e_qs, e_rate, e_cli], "Clay CLI and workspace OAuth integrations"),
            ], "Public REST API uses the clay-api-key header; Clay CLI (`clay login` / `clay login --device`) and workspace connectors use OAuth.")

            elig("testing", "free_access", True, [e_srch, e_mcp_page, e_price], "Clay offers a Free plan (no credit card required, 500 actions/month) and explicitly documents a Free plan tier for Public API/CLI Searches (50 results per request/search, 100 results per 30 days).")
            elig("testing", "trial_access", True, [e_srch, e_price], "Clay offers a 14-day trial on Launch and Growth plans, and Searches documents a Trial quota of 10,000 results for the trial duration.")
            elig("testing", "paid_required", False, [e_srch, e_price], "Free plan (for Searches up to 100 results/30 days) and 14-day Launch/Growth trials allow testing without payment.")
            elig("testing", "self_serve", True, [e_qs, e_srch, e_price], "Developers can sign up for the Free plan or 14-day trial and create an API key self-serve via API and CLI -> API keys or `clay api-keys create`.")

            # Per Codex item 2 & item 17:
            # - Searches explicitly documents a Free plan quota (100 results/30 days), whereas Tables is Enterprise-only, reusable functions appear under Launch ($54-$60/mo+), and webhook signals appear under Growth ($185-$205/mo+).
            # - Custom functions MCP exposure says "If access cannot be changed, ask a workspace admin to check the integration and role access settings" (conditional on role, not a universal admin approval gate for workspace owners/editors).
            elig("production", "free_access", None, [e_srch, e_tbl, e_price],
                 "Feature-dependent across Clay primitives: Public API/CLI Searches explicitly include a Free plan quota (50 results/request, 100 results per 30 days in searches.md line 21, excluding phone number enrichment), whereas reusable functions appear under paid Launch plans ($54-$60/mo+, pricing line 248), webhook signal automation under Growth ($185-$205/mo+, pricing line 273), and the Tables API (/public/v0/tables/query) is restricted to Enterprise plans (tables.md line 9). Left unknown rather than asserting an unconditional app-wide boolean.",
                 status="unknown")
            elig("production", "paid_required", None, [e_srch, e_tbl, e_price],
                 "Feature-dependent: low-volume Public API/CLI Searches (up to 100 results/30 days) work on the Free plan, whereas higher Search quotas (1M–10M/30 days), reusable functions across workflows (Launch+), webhook signals (Growth+), and the Enterprise-only Tables API (/public/v0/tables/query) require Paid or Enterprise plans. Preserved as unknown with explicit primitive-level breakdown.",
                 status="unknown")
            elig("production", "admin_approval_required", None, [e_qs, e_cfunc, e_mcp_page, e_price],
                 "Role-dependent: users with appropriate workspace permissions can create personal `clay-api-key` keys and enable API/MCP access in Function Details directly, whereas users whose role cannot change function/integration settings must ask a workspace admin (`custom-functions.md` line 45) and Enterprise workspaces support admin-managed RBAC and credit budgets. Left unknown rather than asserting a mandatory universal admin gate.",
                 status="unknown")
            elig("production", "self_serve", True, [e_qs, e_srch, e_price], "Free, Launch ($54–$60/mo+), and Growth ($185–$205/mo+) plans and personal API key generation (`clay api-keys create` or API and CLI -> API keys) are self-serve (Enterprise plans offer 'Get a demo' or 'or buy now').")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_auth, e_tbl, e_rout]),
                claim("api.protocol.cli", "CLI", [e_qs, e_cli, e_plug]),
            ], "Public REST API (https://api.clay.com/public/v0 with OpenAPI spec at developers.clay.com/openapi.json), JSON-first `clay` CLI, and signed webhooks.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_dev, e_auth, e_srch])

            items(r["api_surface"]["resource_groups"], [
                group("searches_gtm_db", "Searches (people and companies search queries and paginated iterators in Clay's GTM database)", [e_dev, e_srch, e_llms60]),
                group("routines_functions_workflows", "Routines (running Clay-managed functions, custom functions, batch JSONL runs, and alpha Workflows)", [e_dev, e_rout, e_cfunc, e_llms60]),
                group("tables_enterprise", "Tables (Enterprise-only structured queries across known Clay tables at POST /public/v0/tables/query)", [e_dev, e_tbl, e_llms60]),
                group("audiences_signals_webhooks_credits", "Audiences (records, segments, activities, privacy deletion), Signals triggers, signed Webhooks, authenticated user (/public/v0/me), and workspace credit balances", [e_dev, e_auth, e_wh, e_llms60]),
            ], "Core primitives and Public API v0 endpoints documented at developers.clay.com.")
            breadth("moderate", ["searches_gtm_db", "routines_functions_workflows", "tables_enterprise", "audiences_signals_webhooks_credits"],
                    [e_dev, e_srch, e_tbl, e_rout, e_llms60],
                    "Multiple related B2B go-to-market data and workflow primitives covering people/company database Searches, enrichment/research Routines & batch runs, Enterprise table queries, and Audiences/Signals/Webhooks/credit balance endpoints.")

            set_mcp_entries([
                ("official_clay_mcp", "official", "Clay MCP Connector", [e_dev, e_cfunc, e_mcp_page], "developers.clay.com/routines/custom-functions.md",
                 "Official callable Clay MCP server/connector exposing workspace-governed Clay functions (`list_subroutines`), Audiences, and People/Company Search to MCP clients (Claude, ChatGPT, Codex, Cursor).",
                 None, None),
            ], [e_cfunc, e_mcp_page])

            buildability(
                "build_now",
                "Build a Clay GTM search, enrichment routine execution, and webhook/CLI integration via the Clay Public REST API (https://api.clay.com/public/v0), `clay` CLI, or Clay MCP connector.",
                ["The Tables API (POST /public/v0/tables/query) is restricted to Enterprise plans (and has no list-tables endpoint; table IDs must be known).",
                 "Free plan explicitly covers Searches up to 100 results per 30 days (excluding phone enrichment), whereas reusable functions across workflows require Launch+ ($54-$60/mo+) and webhook signal automation requires Growth+ ($185-$205/mo+); custom functions must have API or MCP access explicitly enabled in Function Details (and workspace role permissions must allow access).",
                 "Captured official Clay pages document the Clay MCP connector and `list_subroutines` workflow but do not print the raw hosted MCP endpoint URL in the captured text, so server_url is recorded as null."],
                ["Create a personal API key under API and CLI -> API keys (or via `clay api-keys create`) and authenticate against https://api.clay.com/public/v0 with `clay-api-key`.",
                 "Enable API and/or MCP access on target custom functions in https://app.clay.com/functions, or install the official `clay` CLI plugin from github.com/clay-run/agent-plugins."],
                [e_dev, e_qs, e_auth, e_cli, e_srch, e_tbl, e_rout, e_cfunc, e_wh, e_price, e_llms60],
                ["identity", "auth.clay_api_key", "auth.oauth2_cli_and_workspace", "testing.free_access", "testing.trial_access", "testing.self_serve", "production.self_serve", "api.protocol.rest", "api.protocol.cli", "api.breadth", "mcp.discovery"],
                "Public developer documentation at developers.clay.com, self-serve API keys and CLI OAuth, Free/Trial/Paid tiers for Searches and paid/trial tiers for Routines/Webhooks, and an official MCP connector make Clay immediately buildable (with Enterprise required only for direct Tables queries).",
            )

        # Convert remaining investigated-but-unestablished credential eligibility booleans to explicit unknown
        for env in ("testing", "production"):
            for k, cobj in r["credential_eligibility"][env].items():
                if k == "context":
                    continue
                if cobj["status"] == "not_researched":
                    cobj["status"] = "unknown"
                    cobj["context"] = scope
                    cobj["rationale"] = f"Checked primary sources for app {app} did not explicitly establish {env}.{k}; preserved as unknown per Contract v1.1."

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps({"records": records}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} records to {destination}")


if __name__ == "__main__":
    build("task12-capture-003", Path(__file__).parent / "extracted-records-003.json")
