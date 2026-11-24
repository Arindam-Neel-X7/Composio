"""Task 07 researcher-authored extraction (CRM and Sales, IDs 1-10, contract v1.1).

Every claim and paraphrase was authored after directly reading the captured primary
snapshots in task07-capture-004. No model API, synthetic fixture, authenticated
account operation, independent review, or accuracy measurement occurs here.
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

        def auth(key, method, details, ev, subcontext, scopes=(), status="observed", refs=()):
            return claim(
                "auth." + key,
                {"method": method, "context": subcontext, "scopes": list(scopes), "details": details},
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

        def set_mcp_not_found(ev, rationale):
            r["mcp"]["entries"] = []
            r["mcp"]["discovery"] = claim("mcp", None, ev, status="not_found_in_checked_sources", rationale=rationale)

        def buildability(verdict, workflow, blockers, steps, refs, ev):
            r["buildability"] = claim(
                "buildability",
                {"verdict": verdict, "scope": workflow, "blockers": blockers, "next_steps": steps},
                ev,
                "inferred",
                ["identity"] + refs,
                "Feasibility inference for the stated workflow from cited documentation; neither implementation nor successful execution established.",
            )

        # Initialize all scalar claims as unknown so unestablished items never stay not_researched by accident
        for _, c in p.claims(r):
            c.update(
                context=scope,
                status="unknown",
                rationale="Checked selected sources; this scoped question is not established. Silence does not establish false.",
            )
        for env in ("testing", "production"):
            r["credential_eligibility"][env]["context"] = (
                scope + f"; {env} path; narrower prerequisites are stated in each claim rationale"
            )

        # =====================================================================
        # 1. Salesforce
        # =====================================================================
        if app == 1:
            sf_price_id = E("salesforce.com/crm/pricing", 5, 7, "Salesforce markets its agentic CRM with tiered CRM pricing plans.")
            sf_th_rest = E("api_basics_rest", 128, 130, "Trailhead documents making REST API calls to a Trailhead Playground org via standard HTTP requests.")
            sf_pm = E("postman-salesforce-apis", 159, 171, "Official forcedotcom Postman collection lists Salesforce Platform APIs: Auth, Bulk (v1 & v2), Composite, Metadata, REST, Subscription Management, and Tooling.")
            sf_mcp_eol = E("salesforcecli/mcp", 174, 177, "Official salesforcecli/mcp repository states that the Salesforce DX local MCP server (@salesforce/mcp) reaches end of life on November 2, 2026.")
            sf_mcp_tools = E("salesforcecli/mcp", 190, 202, "Salesforce DX MCP Server (@salesforce/mcp) exposes callable toolsets including orgs, metadata, data, and users and tools such as run_apex_test via npx.")

            sf_mcp_arch = E("salesforcecli/mcp", 92, 93, "GitHub repository salesforcecli/mcp is marked Public archive.")
            r["identity"]["resolution"] = claim("identity", "Salesforce CRM platform and Salesforce Platform APIs; original Salesforce identity matched.", [sf_price_id, sf_pm])
            r["purpose"] = claim("purpose", "CRM platform providing Salesforce Platform APIs including Auth, Bulk (v1 & v2), Composite, Metadata, REST, Subscription Management, and Tooling.", [sf_price_id, sf_pm])

            sf_soap_note = E("api_basics_rest", 200, 207, "Trailhead Node.js JSforce sample notes basic SOAP login and references documentation for other authentication options.")
            items(
                r["auth"],
                [
                    auth("soap_login", "other", "JSforce sample demonstrates basic SOAP login while pointing to docs for other auth options; OAuth 2.0 reference pages on developer.salesforce.com returned HTTP 403 and remain uncaptured.", [sf_soap_note], "Trailhead JSforce sample auth note"),
                ],
                "Partial coverage: developer.salesforce.com OAuth and edition-gating reference pages returned HTTP 403 (blocked). OAuth 2.0 flows and Connected App details require unblocked primary doc capture.",
            )

            sf_trial = E("salesforce.com/crm/pricing", 141, 143, "Salesforce CRM pricing page offers a 30-day free trial with no credit card required.")
            sf_pg = E("api_basics_rest", 129, 130, "Trailhead REST API guide uses a Trailhead Playground org for making REST API calls.")
            sf_paid = E("salesforce.com/crm/pricing", 15, 84, "Salesforce CRM pricing page lists paid Starter Suite and Pro Suite plans (contract/annual billing notes) without a permanent free CRM tier.")
            sf_sales = E("salesforce.com/crm/pricing", 124, 138, "Pricing page notes contacting an account executive or sales representative for detailed pricing and Signature Success plans.")
            elig("testing", "trial_access", True, [sf_trial], "30-day free CRM trial without credit card documented on pricing page.")
            elig("testing", "sandbox_access", True, [sf_pg], "Trailhead Playground documented as a testing org for REST API requests; enterprise sandbox edition rules remain unknown due to 403 on developer.salesforce.com.")
            elig("production", "paid_required", True, [sf_paid], "Paid CRM plans (Starter Suite, Pro Suite, and enterprise tiers) listed; API-enabled edition thresholds remain unknown due to 403 on developer.salesforce.com.")

            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.rest", "REST", [E("api_basics_rest", 141, 152, "REST API uses /services/data/v{version}/sobjects endpoints returning JSON or XML.")]),
                    claim("api.bulk", "other", [sf_pm], rationale="Official Postman collection documents Bulk (v1 & v2), Composite, Metadata, and Tooling Platform APIs."),
                ],
                "REST and Platform APIs (Bulk v1/v2, Composite, Metadata, Tooling) documented; GraphQL/PubSub not captured due to developer.salesforce.com 403.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [sf_th_rest, sf_pm])
            g_sobj = group("sobjects", "CRM sObjects (e.g., Account describe/create via REST)", [E("api_basics_rest", 131, 162, "REST API exposes sObject endpoints such as Account describe and create.")])
            g_meta = group("metadata_tooling", "Org Metadata and Tooling APIs", [sf_pm])
            g_bulk = group("bulk_sub", "Bulk (v1 & v2) and Subscription Management APIs", [sf_pm])
            items(r["api_surface"]["resource_groups"], [g_sobj, g_meta, g_bulk], "Confirmed from Trailhead and official forcedotcom Postman collection; full REST reference blocked by HTTP 403.")
            breadth("broad", ["sobjects", "metadata_tooling", "bulk_sub"], [g_sobj["evidence"][0], sf_pm], "Spans CRM sObjects, Bulk data processing, Metadata/Tooling, and Subscription Management domains.")

            set_mcp_entries(
                [
                    (
                        "dx_official",
                        "official",
                        "Salesforce DX MCP Server (@salesforce/mcp)",
                        [sf_mcp_arch, sf_mcp_eol, sf_mcp_tools],
                        "salesforcecli/mcp",
                        "Callable local MCP server for Salesforce orgs (orgs, metadata, data, users toolsets); archived repository notes End of Life on November 2, 2026.",
                        None,
                        "https://github.com/salesforcecli/mcp",
                    )
                ],
                [sf_mcp_arch, sf_mcp_eol, sf_mcp_tools],
            )

            buildability(
                "conditional",
                "CRM record and org-metadata agent toolkit via Salesforce REST API or successor hosted MCP",
                [
                    "Production requires paid Salesforce CRM licensing, and edition-level API gating docs on developer.salesforce.com returned HTTP 403 (blocked).",
                    "Official local Salesforce DX MCP server (@salesforce/mcp) reached End of Life on November 2, 2026.",
                ],
                [
                    "Verify OAuth 2.0 Connected App / External Client App setup and edition API enablement in unblocked Salesforce developer docs.",
                    "Evaluate Salesforce hosted MCP server replacement if adopting native MCP instead of REST API.",
                ],
                ["api.rest", "api.breadth", "production.paid_required", "mcp.dx_official"],
                [sf_th_rest, sf_paid, sf_mcp_eol],
            )

        # =====================================================================
        # 2. HubSpot (continuing verified Task 04 baseline + v1.1 current OAuth production fix)
        # =====================================================================
        elif app == 2:
            intro = E("developer-platform-basics", 251, 259, "Developers can use a free account, sample-data test accounts, and public APIs for development.")
            ident = E("developer-platform-basics", 244, 245, "HubSpot developer tooling supports private integrations, Marketplace apps, and APIs.")
            purpose = E("remote-hubspot-mcp-server", 77, 80, "HubSpot CRM integration surface lets applications and AI agents access account CRM data.")
            r["identity"]["resolution"] = claim("identity", "HubSpot CRM and developer platform; original HubSpot identity matched (consistent with Task 04/05 pilot).", [ident, purpose])
            r["purpose"] = claim("purpose", "CRM platform whose APIs and remote MCP server let integrations and agents work with customer records and business workflows.", [purpose])

            oa = E("authentication/overview", 81, 91, "Multi-account apps require OAuth; API requests send the installed account access token as Bearer.")
            oa_work = E("working-with-oauth", 80, 99, "Multi-account or Marketplace apps must use OAuth 2.0 authorization code flow exchanging code at /oauth/v3/token for access and refresh tokens; installing users need Super Admin or Marketplace Access permissions.")
            static = E("authentication/overview", 93, 98, "Single-account private distribution uses a static access token in a Bearer header.")
            legacy = E("private-apps/overview", 55, 59, "Existing legacy private apps remain supported; new creation ended October 26, 2026, and access requires Super Admin.")
            items(
                r["auth"],
                [
                    auth("oauth", "OAuth2", "OAuth 2.0 authorization code flow (/oauth/v3/token) for installed accounts; required for multi-account or Marketplace apps.", [oa, oa_work], "Installed account API access (current developer platform)"),
                    auth("static", "Bearer_token", "Static access token in Bearer header for single-account private distribution on current developer platform.", [static], "Current developer-platform single-account app"),
                    auth("legacy", "Bearer_token", "Existing legacy private app Bearer token; new legacy private app creation ended October 26, 2026.", [legacy, E("private-apps/overview", 63, 69, "Legacy private app API calls send the access token in a Bearer header.")], "Existing legacy private apps (sunset for new creation)"),
                    auth("developer_key", "API_key", "Developer API key via hapikey query parameter for selected app-management endpoints, not general CRM data.", [E("authentication/overview", 100, 104, "Selected developer endpoints use a developer API key in the hapikey query parameter.")], "Selected developer app-management endpoints"),
                    auth("client_credentials", "OAuth2", "Expiring OAuth 2.0 client-credentials tokens for app-global webhooks journal operations.", [E("authentication/overview", 105, 114, "App-global webhooks journal operations use expiring OAuth 2.0 client-credentials tokens.")], "App-global webhooks journal"),
                ],
                "Multiple auth methods and dated legacy sunset (2026-10-26) preserved; continuity with Task 04/05 pilot maintained with added current OAuth installation doc.",
            )

            for key, val in [("free_access", True), ("paid_required", False), ("sandbox_access", True)]:
                elig("testing", key, val, [intro], "Free developer testing path with sample-data developer test accounts (distinct from paid enterprise sandboxes).")
            elig("testing", "self_serve", True, [intro, E("developer-platform-basics", 76, 87, "Free signup, guided CLI authentication, and project creation form the developer onboarding path.")], "Inference for an eligible developer creating a free developer account.", "inferred", ["testing.free_access", "auth.static"])

            elig("production", "admin_approval_required", True, [oa_work, legacy], "Current OAuth app installation requires Super Admin or HubSpot Marketplace Access permissions; legacy private apps also require Super Admin.")
            elig("production", "free_access", True, [E("private-apps/overview", 130, 134, "Legacy private-app rate limits explicitly include Free and Starter accounts.")], "Documented specifically for existing legacy private apps in Free/Starter accounts; current pricing page returned 1-line JS shell.")
            elig("production", "paid_required", False, [E("private-apps/overview", 130, 134, "Legacy private-app rate limits explicitly include the Free tier.")], "Documented specifically for Free-tier legacy private app features; premium CRM features remain plan-dependent.")

            items(r["api_surface"]["protocols"], [claim("api.rest", "REST", [E("developer-platform-basics", 265, 267, "Backend integrations can call RESTful HubSpot APIs.")])], "REST documented; GraphQL not checked in this capture.")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("latest/overview", 118, 124, "Public API reference documents date-versioned paths and a contacts GET request.")])
            gs = [
                group("crm", "CRM objects, associations, owners, pipelines, and properties", [E("latest/overview", 64, 81, "Reference lists CRM objects, associations, owners, pipelines, and properties.")]),
                group("marketing", "Marketing campaigns, forms, and marketing emails", [E("latest/overview", 93, 100, "Reference lists campaigns, forms, and marketing-email APIs.")]),
                group("content", "CMS blogs, pages, HubDB, and source code", [E("latest/overview", 38, 52, "Reference lists CMS blogs, pages, HubDB, and source code.")]),
            ]
            items(r["api_surface"]["resource_groups"], gs, "Documented domain families from date-versioned reference; plan entitlements vary.")
            breadth("broad", ["crm", "marketing", "content"], [g["evidence"][0] for g in gs], "CRM, marketing, and CMS content are distinct business domains in the captured reference.")

            hs_mcp_ev = [
                E("remote-hubspot-mcp-server", 77, 87, "HubSpot documents its official remote CRM MCP server at https://mcp.hubspot.com using OAuth with PKCE."),
                E("remote-hubspot-mcp-server", 119, 127, "Remote MCP server exposes callable CRM tools respecting user permissions and account plan configuration."),
            ]
            set_mcp_entries(
                [("remote_official", "official", "HubSpot Remote CRM MCP Server", hs_mcp_ev, "remote-hubspot-mcp-server", "Official hosted callable MCP server exposing HubSpot CRM data/actions via OAuth + PKCE.", "https://mcp.hubspot.com", None)],
                hs_mcp_ev,
            )

            buildability(
                "build_now",
                "CRM contact/deal read-write and agent workflows via HubSpot REST API or official remote MCP",
                [
                    "Production tenant installation requires Super Admin or Marketplace Access permissions.",
                    "Legacy private app creation ended October 26, 2026; new integrations must use current OAuth or static-token developer platform apps.",
                ],
                [
                    "Create a free HubSpot developer account and test account via developer platform onboarding.",
                    "Implement OAuth 2.0 (/oauth/v3/token) for multi-tenant CRM toolkit or connect to https://mcp.hubspot.com with PKCE.",
                ],
                ["auth.oauth", "testing.free_access", "api.rest", "api.breadth", "mcp.remote_official"],
                [intro, oa_work, hs_mcp_ev[0]],
            )

        # =====================================================================
        # 3. Pipedrive
        # =====================================================================
        elif app == 3:
            pd_id = E("pipedrive.readme.io/llms.txt", 1, 2, "Pipedrive Developer Documentation covers creating public or private apps, core API concepts, OAuth guides, and Marketplace programs.")
            pd_v2 = E("pipedrive-api-v2.md", 15, 32, "Pipedrive API v2 provides REST endpoints for Deals, Persons, Organizations, Activities, Products, Pipelines/Stages, Fields, and Search alongside v1.")
            r["identity"]["resolution"] = claim("identity", "Pipedrive CRM and Developer Platform (v1/v2 REST APIs and Marketplace); original Pipedrive identity matched.", [pd_id, pd_v2])
            r["purpose"] = claim("purpose", "Sales CRM platform with REST v1/v2 APIs for managing deals, persons, organizations, activities, pipelines, and products.", [pd_id, pd_v2])

            pd_tok = E("core-api-concepts-authentication", 117, 123, "API token integrations pass the user's personal API token in the x-api-token header (e.g., GET /api/v2/deals).")
            pd_oa = E("marketplace-oauth-api.md", 7, 17, "Public Marketplace apps use OAuth 2.0 user authorization with granular permission scopes and expiring access tokens.")
            items(
                r["auth"],
                [
                    auth("api_token", "API_key", "Personal user API token sent in the x-api-token HTTP header for single-user or internal integrations.", [pd_tok], "Direct REST API integration (v1/v2)"),
                    auth("oauth2", "OAuth2", "OAuth 2.0 authorization code flow with granular scopes for public or private Marketplace apps.", [pd_oa], "Pipedrive Marketplace public/private apps"),
                ],
                "Both personal API token and OAuth 2.0 documented; OAuth is required for Marketplace distribution.",
            )

            pd_sb = E("developer-sandbox-account.md", 6, 15, "Pipedrive offers a developer sandbox account via form submission giving access to Developer Hub for risk-free app testing and building.")
            pd_admin = E("enabling-api-for-company-users.md", 6, 22, "Company admins control API token visibility and usage via permission sets ('use API' toggle).")
            pd_review = E("marketplace-app-approval-process.md", 7, 38, "Each new public app submitted to the Pipedrive Marketplace must pass Pipedrive's app approval process (up to 21 business days); internal private apps do not require submission.")
            elig("testing", "sandbox_access", True, [pd_sb], "Dedicated developer sandbox account available for testing and building apps in Developer Hub; inactive sandboxes deleted after 45 days.")
            elig("production", "admin_approval_required", True, [pd_admin], "Company admin permission sets control whether company users can access and use the API token.")
            elig("production", "vendor_approval_required", True, [pd_review], "Public Marketplace OAuth apps require Pipedrive vendor app review and approval; internal private apps can skip Marketplace submission.")

            items(r["api_surface"]["protocols"], [claim("api.rest", "REST", [pd_tok, pd_v2])], "REST v1 and v2 documented (v1 endpoints gradually deprecated with >=1 year grace period as v2 expands); Node.js and PHP clients noted.")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [pd_id, pd_v2])
            g_deals = group("deals_pipelines", "Deals, Deal Followers/Products, Pipelines, and Stages", [pd_v2])
            g_contacts = group("contacts", "Persons, Organizations, and Followers", [pd_v2])
            g_act = group("activities_products", "Activities, Products, Fields, and Search", [pd_v2])
            items(r["api_surface"]["resource_groups"], [g_deals, g_contacts, g_act], "Confirmed from Pipedrive API v2 availability list; additional v1 resources exist.")
            breadth("broad", ["deals_pipelines", "contacts", "activities_products"], [pd_v2], "Covers deals/pipelines, persons/organizations, activities, products, custom fields, and search.")

            pd_mcp_ev = [
                E("Wirasm/pipedrive-mcp", 168, 176, "Community repository Wirasm/pipedrive-mcp implements an MCP server for Pipedrive CRM covering Persons, Organizations, Deals, Leads, and Activities."),
                E("Wirasm/pipedrive-mcp", 187, 208, "Setup uses Python's uv package manager and configures PIPEDRIVE_API_TOKEN and PIPEDRIVE_COMPANY_DOMAIN in .env."),
                E("Wirasm/pipedrive-mcp", 228, 241, "Lists callable MCP tools including create_person_in_pipedrive, get_person_from_pipedrive, update_person_in_pipedrive, delete_person_from_pipedrive, and search_persons_in_pipedrive."),
            ]
            set_mcp_entries(
                [("community_wirasm", "community", "Wirasm/pipedrive-mcp", pd_mcp_ev, "Wirasm/pipedrive-mcp", "Community local Python callable MCP server calling Pipedrive API with PIPEDRIVE_API_TOKEN for CRM CRUD/search.", None, "https://github.com/Wirasm/pipedrive-mcp")],
                pd_mcp_ev,
            )

            buildability(
                "conditional",
                "Sales CRM agent toolkit for deals, contacts, and activities via Pipedrive REST API",
                [
                    "Public multi-tenant Marketplace OAuth distribution requires Pipedrive vendor app review (up to 21 business days).",
                    "Company admins must enable 'use API' in permission sets for end-user API token access; pipedrive.com/en/pricing returned HTTP 403 so production plan cost thresholds remain unverified.",
                ],
                [
                    "Request a Pipedrive Developer Sandbox account via Developer Hub for OAuth and REST v2 testing.",
                    "Use private app / API token for internal testing, or submit public OAuth app through Pipedrive Marketplace review for multi-tenant production.",
                ],
                ["auth.api_token", "auth.oauth2", "testing.sandbox_access", "production.admin_approval_required", "production.vendor_approval_required", "api.rest", "api.breadth"],
                [pd_sb, pd_oa, pd_admin, pd_review, pd_v2],
            )

        # =====================================================================
        # 4. Attio
        # =====================================================================
        elif app == 4:
            at_ov = E("rest-api/overview", 81, 89, "Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination.")
            at_nav = E("rest-api/overview", 57, 75, "REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members.")
            at_pr = E("attio.com/pricing", 71, 81, "Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans.")
            at_tiers = E("attio.com/pricing", 94, 118, "Pro plan adds Custom objects; Ultra plan ($1,000/mo/workspace) includes querying in SQL with API or MCP.")
            at_mcp_intro = E("mcp/overview.md", 7, 15, "Attio MCP is Attio's hosted MCP server connecting AI assistants to Attio CRM workspaces for people, companies, deals, tasks, and notes.")
            r["identity"]["resolution"] = claim("identity", "Attio CRM and Developer Platform (REST API, SQL, and hosted MCP); original Attio identity matched.", [at_ov, at_pr, at_tiers, at_mcp_intro])
            r["purpose"] = claim("purpose", "Flexible CRM platform offering a JSON REST API and hosted MCP server for managing objects, records, lists, activities, notes, and tasks.", [at_ov, at_nav, at_mcp_intro])

            at_auth = E("guides/authentication", 91, 105, "Attio REST API supports two ways to generate access tokens: OAuth 2.0 Authorization Code Grant Flow (RFC 6749) for multi-workspace apps, or manually generated workspace API keys for single-workspace integrations.")
            items(
                r["auth"],
                [
                    auth("oauth2", "OAuth2", "Standard OAuth 2.0 Authorization Code Grant Flow (RFC 6749) for multi-workspace apps and Attio MCP.", [at_auth], "Multi-workspace REST API and Attio MCP"),
                    auth("api_key", "API_key", "Manually generated workspace access token (API key) for single-workspace integrations.", [at_auth], "Single-workspace REST API"),
                ],
                "Both OAuth 2.0 and single-workspace API keys documented in primary authentication guide.",
            )

            elig("testing", "free_access", True, [at_pr], "Attio Free plan ($0, up to 3 users) provides a free workspace for testing.")
            elig("testing", "paid_required", False, [at_pr], "Free plan ($0) available without paid subscription.")
            elig("production", "free_access", True, [at_pr], "Free plan ($0, up to 3 users, 50,000 records, 3 objects); advanced features like custom objects (Pro) and SQL via API/MCP (Ultra) require paid plans.")
            elig("production", "paid_required", False, [at_pr], "Free plan exists for up to 3 users; paid Plus/Pro/Ultra tiers required for higher limits, custom objects, or SQL API/MCP queries.")

            at_sql = E("attio.com/pricing", 116, 118, "Ultra plan includes querying workspace data in SQL with API or MCP.")
            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.rest", "REST", [at_ov]),
                    claim("api.sql", "other", [at_sql], rationale="Read-only SQL querying via API or MCP documented on Ultra plan."),
                ],
                "Public REST API (JSON over HTTPS) documented across plans; SQL querying via API/MCP documented on Ultra plan.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [at_ov])
            g_rec = group("objects_records", "Standard/custom objects and records", [at_nav])
            g_lists = group("lists_notes_tasks", "Lists, notes, comments, and tasks", [at_nav])
            g_wh = group("webhooks_scim", "Webhooks, activities, call recordings, and SCIM 2.0", [at_nav])
            items(r["api_surface"]["resource_groups"], [g_rec, g_lists, g_wh], "Confirmed from REST API overview and MCP tool reference.")
            breadth("broad", ["objects_records", "lists_notes_tasks", "webhooks_scim"], [at_nav], "Spans CRM objects/records, lists/notes/tasks, activities/call recordings, webhooks, and SCIM provisioning.")

            at_mcp_ev = [
                E("mcp/overview.md", 8, 15, "Attio MCP is Attio's official hosted MCP server giving AI tools OAuth-authenticated access to search, read, create, and update workspace records."),
                E("mcp/overview.md", 28, 33, "Hosted remote MCP server endpoint is https://mcp.attio.com/mcp using OAuth authentication (no API keys required)."),
                E("mcp/overview.md", 49, 78, "Documents callable MCP tools across Records & Objects (list-objects, search-records, create-record, upsert-record), Activities, and Lists."),
            ]
            set_mcp_entries(
                [("hosted_official", "official", "Attio MCP", at_mcp_ev, "mcp/overview.md", "Official hosted remote callable MCP server (https://mcp.attio.com/mcp) with OAuth user-scoped read/write tools for records, objects, activities, and lists.", "https://mcp.attio.com/mcp", None)],
                at_mcp_ev,
            )

            buildability(
                "build_now",
                "CRM record, list, activity, and task automation via Attio REST API or official hosted MCP",
                ["SQL querying via API/MCP requires the Ultra plan ($1,000/mo/workspace); custom objects require Pro or higher."],
                [
                    "Create a free Attio workspace to generate a workspace API key or register an OAuth 2.0 app.",
                    "Build against Attio REST API or connect MCP clients to https://mcp.attio.com/mcp via OAuth.",
                ],
                ["auth.oauth2", "auth.api_key", "testing.free_access", "api.rest", "api.breadth", "mcp.hosted_official"],
                [at_ov, at_auth, at_pr, at_tiers, at_mcp_ev[1]],
            )

        # =====================================================================
        # 5. Twenty
        # =====================================================================
        elif app == 5:
            tw_repo = E("twentyhq/twenty", 195, 196, "Twenty is an open-source custom CRM designed for technical teams to build, ship, and version like software.")
            tw_api = E("docs.twenty.com/developers/extend/api", 51, 61, "Twenty generates schema-per-tenant REST and GraphQL APIs (Core API and Metadata API) from each workspace's data model.")
            r["identity"]["resolution"] = claim("identity", "Twenty open-source CRM (twentyhq/twenty; cloud and self-hosted); original Twenty identity matched.", [tw_repo, tw_api])
            r["purpose"] = claim("purpose", "Open-source CRM providing schema-per-tenant REST and GraphQL APIs for CRM records and dynamic data-model metadata.", [tw_repo, tw_api])

            tw_auth = E("docs.twenty.com/developers/extend/api", 66, 69, "Authentication uses Bearer API keys created in Settings -> Developers -> API (role-scoped) or OAuth for external apps acting on behalf of users.")
            items(
                r["auth"],
                [
                    auth("api_key", "API_key", "Role-scoped API key sent as Authorization: Bearer YOUR_API_KEY, generated under Settings -> Developers -> API.", [tw_auth], "Workspace REST and GraphQL APIs"),
                    auth("oauth2", "OAuth2", "OAuth-based access documented for external applications acting on behalf of users.", [tw_auth], "External multi-user apps"),
                ],
                "Both Bearer API keys and OAuth documented on Twenty API overview page.",
            )

            tw_sh = E("twentyhq/twenty", 227, 228, "Twenty can be self-hosted on your own infrastructure with Docker Compose or run locally.")
            tw_pr = E("twenty.com/pricing", 10, 48, "Twenty Cloud offers a free trial without credit card, plus Pro ($9/user/mo), Organization ($39/user/mo), and Enterprise (from $50k/yr) plans alongside self-hosting.")
            elig("testing", "free_access", True, [tw_sh], "Open-source self-hosting via Docker Compose enables free local/self-hosted testing.")
            elig("testing", "trial_access", True, [tw_pr], "Twenty Cloud offers a free trial without credit card.")
            elig("testing", "paid_required", False, [tw_sh, tw_pr], "Free self-hosting and no-card Cloud trial allow testing without payment.")
            elig("production", "free_access", True, [tw_sh], "Self-hosted open-source edition can be run on user infrastructure without Twenty Cloud subscription fees; Twenty Cloud production plans are paid (Pro $9/user/mo+).")
            elig("production", "paid_required", False, [tw_sh], "Self-hosted deployment is free; Twenty Cloud requires a paid Pro/Organization/Enterprise plan after trial.")

            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.rest", "REST", [tw_api]),
                    claim("api.graphql", "GraphQL", [tw_api]),
                ],
                "Both REST (/rest/, /rest/metadata/) and GraphQL (/graphql/, /metadata/) dynamically generated per workspace schema; batch up to 60 records.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [tw_api])
            g_core = group("core_records", "Core CRM records (People, Companies, Opportunities, custom objects)", [E("docs.twenty.com/developers/extend/api", 57, 58, "Core API (/rest/ and /graphql/) provides CRUD, filtering, and relation traversal for People, Companies, Opportunities, and custom objects.")])
            g_meta = group("metadata", "Workspace schema Metadata API (objects, fields, relations)", [E("docs.twenty.com/developers/extend/api", 59, 60, "Metadata API (/rest/metadata/ and /metadata/) creates, modifies, and deletes objects, fields, and relations.")])
            items(r["api_surface"]["resource_groups"], [g_core, g_meta], "Schema-per-tenant model exposes Core and Metadata APIs; exact custom objects vary by workspace.")
            breadth("moderate", ["core_records", "metadata"], [g_core["evidence"][0], g_meta["evidence"][0]], "Covers core CRM record operations and full programmatic schema metadata management across REST and GraphQL.")

            tw_mcp_ev = [
                E("jezweb/twenty-mcp", 211, 212, "Community repo jezweb/twenty-mcp implements a Model Context Protocol server for the Twenty CRM API."),
                E("jezweb/twenty-mcp", 226, 230, "Provides callable MCP tools for contacts, companies, opportunities, tasks, and notes."),
            ]
            set_mcp_entries(
                [("community_jezweb", "community", "jezweb/twenty-mcp", tw_mcp_ev, "jezweb/twenty-mcp", "Community TypeScript callable MCP server wrapping Twenty CRM API for contacts, companies, opportunities, tasks, and notes.", None, "https://github.com/jezweb/twenty-mcp")],
                tw_mcp_ev,
            )

            buildability(
                "build_now",
                "CRM record and schema-metadata agent toolkit via Twenty REST/GraphQL APIs",
                ["Schema-per-tenant endpoints require workspace-specific discovery for custom objects; Twenty Cloud production plans are paid (Pro $9/user/mo+) unless self-hosted."],
                [
                    "Spin up a local Docker Compose instance or start a Twenty Cloud free trial and create a role-scoped API key.",
                    "Build against /rest/ or /graphql/ and /rest/metadata/ endpoints, or evaluate community MCP servers.",
                ],
                ["auth.api_key", "testing.free_access", "api.rest", "api.graphql", "api.breadth"],
                [tw_api, tw_auth, tw_sh, tw_pr],
            )

        # =====================================================================
        # 6. Podio
        # =====================================================================
        elif app == 6:
            po_id = E("developers.podio.com/", 23, 37, "Podio API provides a complete programmable interface to all Podio functionality, including webhooks and official client libraries.")
            po_pr = E("podio.com/site/pricing", 92, 125, "Progress Podio offers Free ($0, up to 5 users), Plus ($11.20/$14), and Premium ($19.20/$24, 30-day free trial) plans for workspaces, apps, and task management.")
            po_oa = E("developers.podio.com/authentication", 25, 46, "Podio API uses OAuth 2.0 requiring registered Client ID and Client Secret, supporting Server-side, Client-side, Username & password, and App authentication flows with 'Authorization: OAuth2 ACCESS_TOKEN' header (8h access / 28d refresh).")
            r["identity"]["resolution"] = claim("identity", "Progress Podio work-management/CRM platform and REST API; original Podio identity matched.", [po_id, po_pr])
            r["purpose"] = claim("purpose", "Customizable workspace and CRM app platform exposing its full functionality via an OAuth 2.0 REST API and webhooks.", [po_id, po_oa])

            items(
                r["auth"],
                [
                    auth("oauth2_server", "OAuth2", "OAuth 2.0 Server-side and Client-side flows using registered Client ID/Secret; requests send Authorization: OAuth2 ACCESS_TOKEN (8h expiry, 28d refresh).", [po_oa], "User-delegated web/client integrations"),
                    auth("oauth2_app", "OAuth2", "OAuth 2.0 App authentication flow for single-app automated scripts without user context (preferred over username/password flow).", [po_oa], "Single-app automated scripts"),
                    auth("oauth2_password", "OAuth2", "OAuth 2.0 Username & password flow documented as a fallback only when other flows are unsuitable.", [po_oa], "Fallback user-credential flow"),
                ],
                "All four OAuth 2.0 flows documented on developers.podio.com/authentication.",
            )

            po_key = E("developers.podio.com/", 25, 39, "Developers need a Podio account and can generate an API key (Client ID/Secret) directly from their account settings page.")
            elig("testing", "free_access", True, [po_pr, po_key], "Free plan ($0, up to 5 users) and account-settings API key generation support free testing.")
            elig("testing", "trial_access", True, [po_pr], "30-day free trial available for all Premium features.")
            elig("testing", "paid_required", False, [po_pr], "Free plan ($0) available.")
            elig("testing", "self_serve", True, [po_key, po_pr], "Inference from self-serve Free signup and account-settings API key generation.", "inferred", ["testing.free_access", "auth.oauth2_server"])
            elig("production", "free_access", True, [po_pr], "Free plan ($0, up to 5 users); larger teams and workflow automation require paid Plus/Premium plans.")
            elig("production", "paid_required", False, [po_pr], "Free tier exists up to 5 users; paid Plus/Premium plans required beyond free limits.")

            items(r["api_surface"]["protocols"], [claim("api.rest", "REST", [po_id, po_oa])], "RESTful HTTP API with OAuth2 header and official wrappers for PHP, .NET, Ruby, Java, Python, Android, and Objective-C.")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [E("developers.podio.com/doc", 62, 75, "Public API reference documents Core Areas and Other Areas.")])
            po_doc = E("developers.podio.com/doc", 39, 81, "API Reference lists Organizations plus Core and Other Areas including Applications, Items, Contacts, Comments, Hooks, Status, Tasks, Actions, Alerts, Batch, Calendar, and Conversations.")
            g_apps = group("apps_items", "Applications and Items (custom app entries)", [po_doc])
            g_contacts = group("contacts_orgs", "Contacts and Organizations", [po_doc])
            g_collab = group("tasks_hooks_cal", "Tasks, Comments, Hooks (webhooks), Calendar, and Conversations", [po_doc])
            items(r["api_surface"]["resource_groups"], [g_apps, g_contacts, g_collab], "Documented API areas from developers.podio.com/doc.")
            breadth("broad", ["apps_items", "contacts_orgs", "tasks_hooks_cal"], [po_doc], "Covers custom applications/items, contacts/organizations, tasks, webhooks, calendar, and messaging.")

            set_mcp_not_found(
                [po_id, po_doc],
                "Checked official Podio developer docs (developers.podio.com/, /authentication, /doc) and pricing page; no official or community MCP server was documented in checked sources. This does not prove no MCP exists.",
            )

            buildability(
                "build_now",
                "CRM app-item, contact, and task automation via Podio REST API",
                ["No official MCP server found in checked Podio docs; requires custom REST wrapper using OAuth 2.0 (or App auth for single-app scripts)."],
                [
                    "Create a free Podio account and generate Client ID/Secret from account settings.",
                    "Implement OAuth 2.0 Server-side flow (multi-user) or App authentication flow (single-app) against Podio REST API.",
                ],
                ["auth.oauth2_server", "testing.free_access", "api.rest", "api.breadth"],
                [po_id, po_oa, po_pr],
            )

        # =====================================================================
        # 7. Zoho CRM
        # =====================================================================
        elif app == 7:
            zo_v8 = E("api/v8/", 2, 8, "Zoho CRM V8 APIs provide Metadata APIs, Core RESTful APIs for CRM module CRUD, and a Composite API combining up to five calls.")
            zo_pr = E("crm/pricing.html", 143, 168, "Zoho CRM Free Edition is forever free for 3 users including workflows and APIs (5,000 API calls/day), alongside Standard, Professional, Enterprise, and Ultimate paid editions with free trials.")
            zo_res = E("oauth-overview.html", 16, 17, "Protected Zoho CRM resources include Leads, Contacts, and Deals.")
            zo_mcp_ev = [
                E("zoho.com/mcp/", 7, 10, "Zoho MCP is Zoho's official Model Context Protocol connecting LLMs (GPT, Claude) to Zoho's APIs, data models, and actions."),
                E("zoho.com/mcp/", 79, 82, "Lists Zoho CRM among the supported Zoho MCP integrations for agent-driven actions."),
            ]
            r["identity"]["resolution"] = claim("identity", "Zoho CRM (v8 REST API and Zoho MCP); original Zoho CRM identity matched.", [zo_v8, zo_pr, zo_mcp_ev[0]])
            r["purpose"] = claim("purpose", "CRM platform offering v8 RESTful Core, Metadata, and Composite APIs plus Zoho MCP for managing leads, contacts, deals, and workflows.", [zo_v8, zo_res, zo_pr, zo_mcp_ev[0]])

            zo_oa = E("oauth-overview.html", 2, 36, "Zoho CRM v8 APIs use OAuth 2.0 with expiring access tokens and permanent (until revoked) refresh tokens.")
            zo_reg = E("register-client.html", 2, 20, "Developers register Client-based, Server-based, Mobile-based, or Self Client applications in Zoho Developer Console to obtain Client ID/Secret.")
            zo_sc = E("scopes.html", 3, 39, "OAuth 2.0 scopes follow service_name.scope_name.operation_type (e.g., ZohoCRM.modules.ALL, ZohoCRM.modules.leads.ALL, ZohoCRM.settings.ALL).")
            items(
                r["auth"],
                [
                    auth("oauth2", "OAuth2", "OAuth 2.0 (Client-based, Server-based, Mobile, Self-Client) registered in Zoho Developer Console with granular module/operation scopes and refresh tokens.", [zo_oa, zo_reg, zo_sc], "Zoho CRM v8 REST API", scopes=["ZohoCRM.modules.ALL", "ZohoCRM.modules.leads.ALL", "ZohoCRM.modules.deals.ALL", "ZohoCRM.settings.ALL"]),
                ],
                "OAuth 2.0 is the documented authentication protocol for Zoho CRM v8 APIs.",
            )

            zo_lim = E("api-limits.html", 13, 29, "Free Edition includes 5,000 API credits/24h; Standard/Professional/Enterprise/Ultimate scale from 50,000+ credits; trial editions inherit their corresponding paid edition's API credit limits.")
            elig("testing", "free_access", True, [zo_pr, zo_lim], "Zoho CRM Free Edition (up to 3 users) includes 5,000 API credits/day.")
            elig("testing", "trial_access", True, [zo_pr, zo_lim], "Free trials of paid editions (Standard, Professional, Enterprise) include the corresponding paid edition's API credit limits.")
            elig("testing", "paid_required", False, [zo_pr, zo_lim], "Free Edition and free trials allow API testing without payment.")
            elig("production", "free_access", True, [zo_pr, zo_lim], "Forever-free edition supports up to 3 users and 5,000 API credits/day; higher scale and advanced features require paid editions.")
            elig("production", "paid_required", False, [zo_pr, zo_lim], "Free Edition includes API access (5,000 credits/day); paid editions required for >3 users or higher credit limits.")

            items(r["api_surface"]["protocols"], [claim("api.rest", "REST", [zo_v8])], "RESTful v8 APIs (Core, Metadata, Composite, COQL, Bulk) documented.")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [zo_v8, zo_oa])
            g_core = group("core_modules", "Core CRM modules (Leads, Contacts, Deals, COQL queries)", [zo_v8, zo_res, E("api-limits.html", 37, 49, "Documents COQL queries, insert/update/upsert, merge records, and mail operations.")])
            g_meta = group("metadata_fields", "Metadata APIs (modules, fields, layouts, custom views, related lists)", [zo_v8, E("api-limits.html", 64, 66, "Documents custom field create/update/delete operations.")])
            g_bulk = group("bulk_territories", "Bulk Write, Mass Convert/Delete, Composite API, and Territories", [zo_v8, E("api-limits.html", 56, 63, "Documents Bulk Write, Mass Convert Leads, Mass Delete, and Territory management.")])
            items(r["api_surface"]["resource_groups"], [g_core, g_meta, g_bulk], "Confirmed from Zoho CRM v8 API overview and API limits reference.")
            breadth("broad", ["core_modules", "metadata_fields", "bulk_territories"], [zo_v8, zo_lim], "Spans CRM modules/COQL, metadata/schema customization, composite/bulk jobs, and territories.")

            set_mcp_entries(
                [("zoho_mcp_official", "official", "Zoho MCP (Zoho CRM)", zo_mcp_ev, "zoho.com/mcp/", "Official callable MCP server platform exposing Zoho CRM APIs, data models, and agent actions to LLMs (endpoint URL not published on product overview page).", None, None)],
                zo_mcp_ev,
            )

            buildability(
                "build_now",
                "CRM lead/contact/deal automation via Zoho CRM v8 REST API or official Zoho MCP",
                ["API credit budgets vary by edition (5,000/day on Free); Sandbox KB page returned empty_readable_content so sandbox tier gating remains unverified."],
                [
                    "Register a client in Zoho Developer Console and test against a Free Edition or paid-edition trial org.",
                    "Implement OAuth 2.0 with scoped v8 REST endpoints or connect via Zoho MCP.",
                ],
                ["auth.oauth2", "testing.free_access", "api.rest", "api.breadth", "mcp.zoho_mcp_official"],
                [zo_v8, zo_oa, zo_pr, zo_mcp_ev[0]],
            )

        # =====================================================================
        # 8. Close
        # =====================================================================
        elif app == 8:
            cl_dev = E("developer.close.com/", 16, 38, "Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.")
            cl_pr = E("close.com/pricing", 52, 113, "Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed.")
            r["identity"]["resolution"] = claim("identity", "Close CRM and Developer Platform (REST API and Close MCP Server); original Close identity matched.", [cl_dev, cl_pr])
            r["purpose"] = claim("purpose", "Sales CRM with built-in calling, email, and SMS, offering a REST API, webhooks, and hosted MCP server for leads, contacts, and outreach.", [cl_dev, cl_pr])

            cl_ak = E("topics/authentication/", 15, 31, "API keys (created in Settings -> Developer -> API Keys, user/org-scoped) authenticate via HTTP Basic Auth with the API key as username and an empty password.")
            cl_ak_mcp = E("developer.close.com/mcp/", 88, 88, "Close MCP server also supports API key authentication via the Close-API-Key header.")
            cl_oa = E("oauth-authentication.md", 31, 45, "OAuth 2.0 authorization code flow exchanges code for Bearer access_token (expires_in 3600s) and refresh_token with scopes all.full_access and offline_access.")
            cl_oa_app = E("create-an-oauth-app.md", 3, 21, "OAuth apps are created in Settings -> Developer -> OAuth Apps with all.full_access offline_access scopes; apps are Private by default and require requesting publication to become public.")
            items(
                r["auth"],
                [
                    auth("api_key", "Basic", "Per-user/org API key sent via HTTP Basic Auth (API key as username, blank password); also usable via Close-API-Key header for MCP.", [cl_ak, cl_ak_mcp], "Internal scripts and single-org integrations"),
                    auth("oauth2", "OAuth2", "OAuth 2.0 authorization code flow issuing Bearer access tokens (1h) and refresh tokens; Private by default, public multi-org requires publication request.", [cl_oa, cl_oa_app], "User-facing and multi-tenant integrations", scopes=["all.full_access", "offline_access"]),
                ],
                "Both API key (HTTP Basic) and OAuth 2.0 documented in primary developer docs.",
            )

            elig("testing", "trial_access", True, [cl_pr], "14-day free trial with no credit card required documented on Close pricing page.")
            elig("testing", "paid_required", False, [cl_pr], "14-day no-card free trial allows initial testing without payment.")
            elig("production", "free_access", False, [cl_pr], "Pricing page lists only paid plans (Solo, Essentials, Growth, Scale) after the 14-day free trial; no free production tier is offered.")
            elig("production", "paid_required", True, [cl_pr], "Production use requires a paid Close CRM subscription (Solo $19/$9 through Scale $149/$139/user/mo); Essentials+ notes no daily API request quota or per-request fees.")
            elig("production", "vendor_approval_required", True, [cl_oa_app], "OAuth apps are Private (own organization only) by default; making an OAuth app public for other Close customers requires requesting Close publication approval.")

            items(r["api_surface"]["protocols"], [claim("api.rest", "REST", [cl_dev])], "REST API with webhooks and 30-day event log documented.")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [cl_dev])
            g_crm = group("leads_contacts", "Leads, contacts, and custom data", [cl_dev])
            g_out = group("activities_outreach", "Activities, email/SMS outreach, sequences, and bulk actions", [cl_dev])
            g_evt = group("webhooks_reporting", "Webhooks, 30-day event log, and pipeline reporting", [cl_dev])
            items(r["api_surface"]["resource_groups"], [g_crm, g_out, g_evt], "Confirmed from Close Developer Platform overview and MCP tool reference.")
            breadth("broad", ["leads_contacts", "activities_outreach", "webhooks_reporting"], [cl_dev], "Covers CRM leads/contacts, multi-channel outreach/sequences, webhooks/events, and reporting.")

            cl_mcp_ev = [
                E("developer.close.com/mcp/", 78, 88, "Official Close MCP server hosted at https://mcp.close.com/mcp using HTTP Streamable transport with MCP OAuth2 (recommended) or Close-API-Key header."),
                E("mcp/tools.md", 3, 19, "Documents scoped callable Close MCP read-only tools (mcp.read including activity_search and search/fetch tools)."),
            ]
            set_mcp_entries(
                [("hosted_official", "official", "Close MCP Server", cl_mcp_ev, "developer.close.com/mcp/", "Official hosted HTTP Streamable callable MCP server (https://mcp.close.com/mcp) supporting OAuth2 or Close-API-Key with scoped CRM read/search tools (e.g., mcp.read).", "https://mcp.close.com/mcp", None)],
                cl_mcp_ev,
            )

            buildability(
                "conditional",
                "Sales CRM and outreach agent toolkit via Close REST API or official hosted MCP",
                [
                    "Production requires a paid Close subscription (only a 14-day free trial is offered; no free tier).",
                    "Multi-tenant public OAuth distribution requires requesting publication approval from Close (OAuth apps are Private by default).",
                ],
                [
                    "Start a 14-day no-card free trial to test API key (Basic Auth), private OAuth app, or https://mcp.close.com/mcp.",
                    "Submit OAuth app for Close public listing if distributing across external Close customer orgs.",
                ],
                ["auth.api_key", "auth.oauth2", "testing.trial_access", "production.paid_required", "production.vendor_approval_required", "api.rest", "api.breadth", "mcp.hosted_official"],
                [cl_dev, cl_pr, cl_oa_app, cl_mcp_ev[0]],
            )

        # =====================================================================
        # 9. Copper
        # =====================================================================
        elif app == 9:
            co_dev = E("developer.copper.com/", 189, 196, "Copper Developer API ('Dev API') provides a RESTful JSON interface at https://api.copper.com/developer_api/ to build custom applications.")
            co_pr = E("copper.com/pricing", 95, 182, "Copper CRM offers a free trial (no credit card required) and paid Basic ($29/$23), Professional ($69/$59), and Business ($134/$99) plans per seat/month; no free tier is listed.")
            co_ent = E("developer.copper.com/", 40, 83, "Documents Users, Leads, People, and Companies endpoints including CRUD, bulk operations, upsert, convert, and search.")
            co_act = E("developer.copper.com/", 125, 163, "Documents Activities, Custom Fields, Custom Activity Types, Connect fields, Field Layouts, and Related Items.")
            co_wh = E("developer.copper.com/", 164, 181, "Documents File Upload (S3) and Webhook subscriptions.")
            r["identity"]["resolution"] = claim("identity", "Copper CRM (formerly ProsperWorks) and Developer API; original Copper identity matched.", [co_dev, co_pr])
            r["purpose"] = claim("purpose", "Google Workspace-oriented CRM platform exposing a RESTful JSON Developer API for leads, people, companies, activities, custom fields, and webhooks.", [co_dev, E("copper.com/pricing", 62, 62, "Copper positions itself as a Google Workspace CRM."), co_ent, co_act, co_wh])

            co_auth = E("introduction/authentication.html", 181, 192, "Copper Developer API supports API keys (token header plus user email address, generated under System settings > API Keys; admins can view/generate all tokens) and OAuth 2.0 (preferred for partner integrations).")
            items(
                r["auth"],
                [
                    auth("api_key", "API_key", "Token-based authentication sending API key and generating user's email address in request headers; generated in System settings > API Keys.", [co_auth], "Individual user / single-tenant Dev API"),
                    auth("oauth2", "OAuth2", "OAuth 2.0 documented as the preferred method for partner integrations (detailed OAuth subpage returned HTTP 404).", [co_auth], "Partner integrations"),
                ],
                "Both API keys and OAuth 2.0 confirmed on primary authentication overview; detailed OAuth grant subpage returned HTTP 404.",
            )

            elig("testing", "trial_access", True, [co_pr], "Free trial with no credit card required documented on Copper pricing page.")
            elig("testing", "paid_required", False, [co_pr], "Free trial allows initial testing without payment.")
            elig("production", "free_access", False, [co_pr], "Pricing page lists only paid Basic, Professional, and Business plans with a free trial; no free production tier is offered.")
            elig("production", "paid_required", True, [co_pr], "Production use requires a paid Copper plan (Basic $29/$23 through Business $134/$99 per seat/month); exact plan-level API gating is not explicitly stated on the pricing page.")

            items(r["api_surface"]["protocols"], [claim("api.rest", "REST", [co_dev])], "RESTful JSON API at https://api.copper.com/developer_api/ with downloadable Postman collection.")
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [co_dev])
            g_crm = group("crm_entities", "Leads, People, Companies, and Users (CRUD, bulk, upsert, search)", [E("developer.copper.com/", 40, 83, "Documents Users, Leads, People, and Companies endpoints including CRUD, bulk operations, upsert, convert, and search.")])
            g_act = group("activities_custom", "Activities, Custom Fields, Custom Activity Types, and Related Items", [E("developer.copper.com/", 125, 163, "Documents Activities, Custom Fields, Custom Activity Types, Connect fields, Field Layouts, and Related Items.")])
            g_wh = group("files_webhooks", "File Uploads (signed S3) and Webhooks", [E("developer.copper.com/", 164, 181, "Documents File Upload (S3) and Webhook subscriptions.")])
            items(r["api_surface"]["resource_groups"], [g_crm, g_act, g_wh], "Confirmed from Copper Developer API navigation and getting-started reference.")
            breadth("broad", ["crm_entities", "activities_custom", "files_webhooks"], [g_crm["evidence"][0], g_act["evidence"][0], g_wh["evidence"][0]], "Covers core CRM entities, activities/custom schema, file uploads, and webhooks.")

            set_mcp_not_found(
                [co_dev, co_auth],
                "Checked captured official Copper docs (developer.copper.com/, /introduction/authentication.html, copper.com/pricing); no MCP server was documented in checked sources (candidate blog URL returned HTTP 404). This does not prove no MCP exists.",
            )

            buildability(
                "conditional",
                "CRM lead, contact, company, and activity agent toolkit via Copper REST API",
                [
                    "Production requires a paid Copper subscription (no free tier after trial).",
                    "Detailed OAuth 2.0 partner onboarding documentation returned HTTP 404; no official MCP confirmed in checked sources.",
                ],
                [
                    "Start a no-card free trial and generate a Dev API key under System settings > API Keys for testing.",
                    "Confirm partner OAuth 2.0 registration requirements and plan-level API entitlements before multi-tenant production rollout.",
                ],
                ["auth.api_key", "auth.oauth2", "testing.trial_access", "production.paid_required", "api.rest", "api.breadth"],
                [co_dev, co_auth, co_pr],
            )

        # =====================================================================
        # 10. DealCloud
        # =====================================================================
        elif app == 10:
            dc_doc = E("api.docs.dealcloud.com/", 1, 10, "DealCloud Developer Documentation covers API Reference (API Keys, Authorization Token, Pagination, Rate Limits).")
            dc_sdks = E("api.docs.dealcloud.com/", 226, 233, "Documents API References, Intapp REST Client, Python SDK v1.X, and C# SDK.")
            dc_prod = E("intapp.com/dealcloud/", 13, 24, "Intapp DealCloud is an enterprise AI-powered deal and relationship management (CRM) platform accessed via 'Schedule a demo'.")
            dc_mcp_oa = E("mcp/authentication", 455, 461, "DealCloud MCP uses OAuth 2.0 with standard .well-known discovery endpoints so AI assistants authenticate on behalf of individual users under their DealCloud permissions.")
            dc_mcp_gs = E("mcp/getting-started", 459, 466, "DealCloud provides a default MCP Server exposing site schema under a DealCloud with Celeste license.")
            r["identity"]["resolution"] = claim("identity", "Intapp DealCloud CRM and Developer Platform (REST API, SDKs, and DealCloud MCP); original DealCloud identity matched.", [dc_doc, dc_sdks, dc_mcp_gs, dc_prod])
            r["purpose"] = claim("purpose", "Enterprise deal and relationship intelligence CRM offering REST APIs, Python/C# SDKs, and a Celeste-licensed OAuth MCP server.", [dc_prod, dc_doc, dc_sdks, dc_mcp_gs, dc_mcp_oa])

            items(
                r["auth"],
                [
                    auth("mcp_oauth2", "OAuth2", "OAuth 2.0 with .well-known discovery for user-scoped DealCloud MCP connections enforcing DealCloud user data permissions.", [dc_mcp_oa], "DealCloud MCP Server"),
                ],
                "MCP OAuth 2.0 documented in captured primary docs; REST API 'API Keys' and 'Authorization Token' subpages returned HTTP 404 so REST OAuth grant details remain uncaptured.",
            )

            dc_req = E("mcp/getting-started", 460, 463, "DealCloud MCP prerequisites require a DealCloud with Celeste license, admin 'Manage MCP Servers' capability to configure, and Celeste Member user group with MCP Access enabled.")
            elig("production", "paid_required", True, [dc_req, dc_prod], "Enterprise product requiring a DealCloud license (and Celeste license for MCP); no self-serve free tier documented.")
            elig("production", "admin_approval_required", True, [dc_req], "Tenant admin with 'Manage MCP Servers' capability must configure MCP servers and assign end users to Celeste Member group with MCP Access.")
            elig("production", "contact_sales_required", True, [dc_prod], "Intapp DealCloud product page offers 'Schedule a demo' with no public self-serve signup or published pricing.")

            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.rest", "REST", [dc_sdks]),
                ],
                "REST API plus official Python v1.X, Intapp REST Client, and C# SDKs documented.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_documentation", True, [dc_doc])
            g_schema = group("schema_metadata", "Schema, EntryTypes, Fields, Site Metadata, and Schema Contracts", [E("api.docs.dealcloud.com/", 12, 32, "Documents Schema APIs for EntryTypes, Fields, Choice Field Values, Site Metadata, Currencies, Mappings, and Users."), E("api.docs.dealcloud.com/", 89, 89, "Documents Schema Contracts.")])
            g_data = group("data_files", "Data (Cells, Rows, Views, History, Files, Merge, Template Reports)", [E("api.docs.dealcloud.com/", 33, 55, "Documents Data APIs for Cells, Rows, Views, History, Files, Delete, Merge, and Template Reports.")])
            g_admin = group("users_pub_ri", "User Management, Publications (events), Site Backups, and Relationship Intelligence", [E("api.docs.dealcloud.com/", 56, 89, "Documents User Management, Publications/Event Types, Site Backups, and Relationship Intelligence APIs.")])
            items(r["api_surface"]["resource_groups"], [g_schema, g_data, g_admin], "Confirmed from api.docs.dealcloud.com API Reference structure.")
            breadth("broad", ["schema_metadata", "data_files", "users_pub_ri"], [g_schema["evidence"][0], g_data["evidence"][0], g_admin["evidence"][0]], "Covers full enterprise schema, data/files/reports, user administration, event publications, backups, and relationship intelligence.")

            dc_mcp_ev = [
                E("mcp/getting-started", 464, 470, "DealCloud provides an official default MCP Server at https://[tenant].my.intapp.com/mcp/celeste/DealCloud plus Custom MCP Servers paired with Schema Contracts and toggleable Write Tools."),
                dc_mcp_oa,
            ]
            set_mcp_entries(
                [("celeste_official", "official", "DealCloud MCP Server", dc_mcp_ev, "mcp/getting-started", "Official hosted tenant callable MCP server (template https://[tenant].my.intapp.com/mcp/celeste/DealCloud) with OAuth 2.0 user permissions, optional write tools, and custom Schema Contract servers.", None, None)],
                dc_mcp_ev,
            )

            buildability(
                "outreach_required",
                "Enterprise deal/relationship CRM agent toolkit via DealCloud REST API or DealCloud MCP",
                [
                    "Enterprise-only licensing (DealCloud + Celeste license for MCP) with demo/sales-led onboarding and no public self-serve developer sandbox.",
                    "Tenant admin configuration ('Manage MCP Servers' and Celeste Member group assignment) required; REST API Keys / Authorization Token subpages returned HTTP 404.",
                ],
                [
                    "Engage Intapp sales or a licensed DealCloud enterprise customer to obtain tenant/sandbox credentials and confirm REST token endpoint details.",
                    "Enable DealCloud MCP under Tools > MCP Servers with OAuth 2.0 or build against Intapp REST Client / Python SDK v1.X.",
                ],
                ["auth.mcp_oauth2", "production.paid_required", "production.admin_approval_required", "production.contact_sales_required", "api.rest", "api.breadth", "mcp.celeste_official"],
                [dc_prod, dc_req, dc_mcp_ev[0]],
            )

    destination.write_text(json.dumps({"records": records}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} extracted records to {destination}")


if __name__ == "__main__":
    build("task07-capture-004", Path(__file__).parent / "task07-extraction.json")
