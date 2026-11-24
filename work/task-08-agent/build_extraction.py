"""Task 08 researcher-authored extraction (Support and Helpdesk, IDs 11-20, contract v1.1).

Every claim and paraphrase was authored after directly reading the captured primary
and community snapshots in task08-capture-004. Remediated in task08-first-pass-003
after independent AI audit of task08-first-pass-002 to tighten per-claim evidence
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

        AUTH_MAP = {"oauth2": "OAuth2", "api_key": "API_key", "basic": "Basic", "bearer_token": "Bearer_token"}

        def auth(key, method, details, ev, subcontext, scopes=(), status="observed", refs=()):
            return claim(
                "auth." + key,
                {"method": AUTH_MAP.get(method, method), "context": subcontext, "scopes": list(scopes), "details": details},
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
        # 11. Zendesk
        # =====================================================================
        if app == 11:
            zd_id = E("ticketing/introduction/", 140, 141, "Zendesk Support (Ticketing) API manages tickets, users, organizations, custom objects, and ticket workflows.")
            zd_price_id = E("zendesk.com/pricing/", 280, 283, "Zendesk offers Support (email-based) and Suite (all-in-one ticketing, messaging, live chat, help centre, voice, AI agents) customer service plans.")
            zd_oauth = E("security-and-auth/", 37, 59, "Zendesk API requires verified users and supports OAuth access tokens (Authorization: Bearer) for single instances and client-side CORS requests; existing basic/API token users must migrate to OAuth.")
            zd_global_oauth = E("security-and-auth/", 60, 62, "Global OAuth access tokens are required for apps, integrations, or bots distributed to multiple Zendesk customers (not required for internal-only use).")
            zd_api_tok = E("security-and-auth/", 63, 74, "Zendesk API tokens (marked deprecated) are managed in Admin Center and sent via HTTP Basic auth ({email_address}/token:{api_token}).")
            zd_qs = E("zendesk-api-quick-start/", 101, 103, "Ticketing API quick start requires a Zendesk Support account with agent or admin access and references getting a free trial or sponsored account for development.")
            zd_trial = E("zendesk.com/pricing/", 313, 318, "Zendesk offers a 14-day free trial defaulting to Customer Service Suite Professional features.")
            zd_sandbox = E("zendesk.com/pricing/", 182, 194, "Suite Enterprise + Copilot includes a sandbox environment and requires Talk to Sales.")
            zd_paid = E("zendesk.com/pricing/", 167, 185, "Zendesk Suite Professional is listed at US$ 115/agent/month paid yearly with Buy now self-serve purchase; Suite Enterprise + Copilot requires Talk to Sales.")
            zd_buy = E("zendesk.com/pricing/", 297, 306, "Zendesk supports self-serve online card purchase for standard plans and requires sales-assisted purchasing for enterprise plans.")
            zd_rest = E("ticketing/introduction/", 140, 167, "Zendesk Support/Ticketing API is a JSON HTTP API under https://{subdomain}.zendesk.com/api/v2/ with OpenAPI download and Idempotency-Key support.")
            zd_grp_core = E("ticketing/introduction/", 35, 48, "Ticketing API documents Users/User Fields, Organizations, Lookup Relationships, Groups, and Ticket Management endpoints.")
            zd_grp_rules = E("ticketing/introduction/", 65, 95, "Ticketing API documents Business Rules (Views, Triggers, Macros, Automations, SLA Policies), Account Configuration, Audit Logs, OAuth Clients, and Apps.")
            zd_grp_collab = E("ticketing/introduction/", 102, 115, "Ticketing API documents Side Conversations, Jira Integration/Links, Approvals, and Tasks.")
            zd_mcp = E("reminia/zendesk-mcp-server", 154, 197, "Community GitHub repository reminia/zendesk-mcp-server implements a local uv-based Zendesk MCP server using OAuth (PKCE) with tools for tickets, comments, attachments, and Help Center knowledge base.")
            zd_mcp_tools = E("reminia/zendesk-mcp-server", 244, 258, "reminia/zendesk-mcp-server lists callable tools including get_ticket, get_tickets, get_ticket_comments, create_ticket, update_ticket, create_ticket_comment, and get_ticket_attachment.")

            r["identity"]["resolution"] = claim("identity", "Zendesk customer service and Support/Suite platform; original Zendesk identity matched.", [zd_id, zd_price_id])
            r["purpose"] = claim("purpose", "Omnichannel customer service and ticketing platform providing Support/Ticketing HTTP JSON APIs for tickets, users, organizations, custom objects, and workflows.", [zd_id, zd_price_id, zd_rest])

            items(
                r["auth"],
                [
                    auth("oauth2", "oauth2", "OAuth 2.0 Bearer access tokens for single-instance integrations; required migration path from deprecated API tokens.", [zd_oauth], "Zendesk API v2 single-instance integrations"),
                    auth("global_oauth2", "oauth2", "Global OAuth access tokens required for multi-customer public apps, integrations, or bots.", [zd_global_oauth], "Multi-tenant public Zendesk apps/integrations"),
                    auth("api_token_basic_deprecated", "basic", "Deprecated Admin Center API tokens authenticated via HTTP Basic ({email_address}/token:{api_token}).", [zd_api_tok], "Legacy/internal Zendesk API v2 calls (deprecated)"),
                ],
                "Checked official security-and-auth reference; OAuth 2.0, Global OAuth, and deprecated API token Basic auth captured.",
            )

            elig("testing", "trial_access", True, [zd_trial, zd_qs], "14-day free trial of Zendesk Suite Professional is available, and quick start notes trial/sponsored development accounts.")
            elig("testing", "sandbox_access", True, [zd_sandbox], "Sandbox environment is included on Suite Enterprise + Copilot tier (sales-assisted).")
            elig("testing", "self_serve", True, [zd_trial, zd_qs], "14-day free trial for testing is self-serve; Enterprise sandbox requires sales engagement.")
            elig("production", "paid_required", True, [zd_paid, zd_buy], "Production Zendesk Support/Suite plans are paid per-agent subscriptions (self-serve online for standard tiers; sales-assisted for Enterprise).")
            elig("production", "self_serve", True, [zd_buy], "Standard Zendesk plans can be purchased online self-serve; Enterprise plans require contacting Sales.")
            elig("production", "contact_sales_required", False, [zd_buy], "Standard production plans support online purchase without contacting Sales; Enterprise plans require sales engagement.")

            items(r["api_surface"]["protocols"], [claim("api.protocol.rest", "REST", [zd_rest])], "Zendesk Support/Ticketing REST API v2 with OpenAPI specification captured.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [zd_rest, zd_oauth])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("tickets_users_orgs", "Tickets, users, organizations, groups, custom objects, and lookup relationships", [zd_id, zd_grp_core]),
                    group("rules_sla_config", "Business rules (views, triggers, macros, automations, SLA policies), account configuration, audit logs, and OAuth/Apps", [zd_grp_rules]),
                    group("collab_tasks_approvals", "Side conversations, Jira links, approvals, and tasks", [zd_grp_collab]),
                ],
                "Resource groups captured from Zendesk Support/Ticketing API v2 reference index.",
            )
            breadth("broad", ["tickets_users_orgs", "rules_sla_config", "collab_tasks_approvals"], [zd_grp_core, zd_grp_rules, zd_grp_collab], "Covers ticketing, CRM entities, workflow/SLA automation, admin/audit configuration, and collaboration/tasks.")

            set_mcp_entries(
                [("community_reminia", "community", "reminia/zendesk-mcp-server", [zd_mcp, zd_mcp_tools], "reminia/zendesk-mcp-server",
                  "Third-party community local uv MCP server (callable server direction) exposing Zendesk ticket, comment, attachment, and Help Center tools via OAuth PKCE; not vendor-endorsed",
                  None, "https://github.com/reminia/zendesk-mcp-server")],
                [zd_mcp, zd_mcp_tools],
            )
            buildability(
                "build_now",
                "Zendesk Support ticketing, triage, and customer-context agent toolkit via REST API v2 (OAuth 2.0)",
                ["API tokens are deprecated in favor of OAuth 2.0", "Multi-tenant public distribution requires Global OAuth client approval", "Sandbox environment is gated to Enterprise tier"],
                ["Use 14-day Suite Professional trial for single-tenant OAuth prototyping", "Apply for Global OAuth client if distributing to multiple Zendesk customers"],
                ["auth.oauth2", "auth.global_oauth2", "testing.trial_access", "testing.sandbox_access", "production.paid_required", "api.protocol.rest", "api.breadth"],
                [zd_oauth, zd_global_oauth, zd_trial, zd_sandbox, zd_rest],
            )

        # =====================================================================
        # 12. Intercom
        # =====================================================================
        elif app == 12:
            ic_id = E("developers.intercom.com/docs", 43, 45, "Intercom Developer Platform is a suite of SDKs and APIs for building apps that extend or integrate with Intercom.")
            ic_price_id = E("intercom.com/pricing", 50, 69, "Intercom provides a human and Fin AI Agent customer support helpdesk with Messenger live chat, shared inbox, ticketing, reports, and public help center.")
            ic_tok = E("learn-more/authentication", 43, 75, "Intercom Access Tokens authenticate private apps and workspace scripts via Authorization:Bearer; issued to the installing teammate with their conversation permissions.")
            ic_oauth = E("learn-more/authentication", 45, 75, "Intercom OAuth 2.0 (Authorization:Bearer) is required for public apps accessing other customers' Intercom workspaces.")
            ic_devws = E("developers.intercom.com/docs", 54, 58, "Public app developers can sign up for a free US-only development workspace (with limitations vs paid workspaces) to access Developer Hub, webhooks, OAuth, and app review.")
            ic_review = E("developers.intercom.com/docs", 64, 68, "Public apps must be submitted for Intercom review in Developer Hub before customer installation; private apps using Access Tokens do not require review.")
            ic_trial = E("intercom.com/pricing", 52, 95, "Intercom offers a 14-day cardless free trial on paid helpdesk plans (Essential from $19/seat/mo annual, Advanced $85, Expert $132, plus $0.99/Fin outcome).")
            ic_rest = E("developers.intercom.com/docs", 18, 34, "Intercom exposes REST APIs, Canvas Kit, Webhooks, and Fin Agent API covering Messenger, Inbox, Contacts, Tickets, Help Center, and Reporting.")
            ic_mcp = E("guides/mcp", 43, 58, "Intercom hosts an official remote MCP server (Streamable HTTP) at https://mcp.intercom.com/mcp (US) and https://mcp.eu.intercom.com/mcp (EU); AU not yet supported.")
            ic_mcp_tools = E("guides/mcp", 69, 100, "Intercom MCP Server provides 16 callable tools including universal search and fetch for conversations, contacts, and companies, plus Fin Operator tools for OAuth connections.")

            r["identity"]["resolution"] = claim("identity", "Intercom customer support helpdesk and Fin Developer Platform; original Intercom identity matched.", [ic_id, ic_price_id])
            r["purpose"] = claim("purpose", "Customer support helpdesk and AI agent platform offering REST APIs, webhooks, Canvas Kit, and a hosted MCP server for inbox, contacts, tickets, and help center.", [ic_id, ic_price_id, ic_rest, ic_mcp])

            items(
                r["auth"],
                [
                    auth("access_token", "api_key", "Workspace Access Token sent as Authorization: Bearer for private apps and internal scripts; inherits installing teammate's conversation access.", [ic_tok], "Private workspace apps and internal scripts"),
                    auth("oauth2", "oauth2", "OAuth 2.0 Bearer tokens required for public/multi-tenant integrations accessing other customers' Intercom workspaces.", [ic_oauth], "Multi-tenant public Intercom apps"),
                ],
                "Checked official Intercom authentication guide; Access Tokens and OAuth 2.0 captured.",
            )

            elig("testing", "free_access", True, [ic_devws], "Free US-only development workspace is available for building and testing Intercom apps in Developer Hub.")
            elig("testing", "trial_access", True, [ic_trial], "14-day cardless free trial is available on Intercom helpdesk plans.")
            elig("testing", "sandbox_access", True, [ic_devws], "Free development workspace functions as a limited testing environment separate from paid workspaces.")
            elig("testing", "self_serve", True, [ic_devws, ic_trial], "Developers can self-serve sign up for a free development workspace or 14-day free trial.")
            elig("production", "paid_required", True, [ic_trial, ic_devws], "Full production Intercom helpdesk functionality requires a paid workspace plan (Essential, Advanced, or Expert).")
            elig("production", "vendor_approval_required", True, [ic_review], "Public multi-tenant OAuth apps require Intercom App Store review; private workspace apps using Access Tokens do not require review.")
            elig("production", "self_serve", True, [ic_review, ic_tok], "Private workspace apps with Access Tokens are self-serve without review; public App Store apps require Intercom review.")

            items(r["api_surface"]["protocols"], [claim("api.protocol.rest", "REST", [ic_rest])], "Intercom REST API, Canvas Kit, and Webhooks captured.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [ic_id, ic_rest])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("messaging_inbox_tickets", "Messenger, Inbox conversations, and Tickets", [ic_rest]),
                    group("contacts_helpcenter_reporting", "Contacts, Help Center, Reporting, Webhooks, and Fin Agent API", [ic_rest]),
                ],
                "Resource domains captured from official Intercom Developer Platform documentation index.",
            )
            breadth("broad", ["messaging_inbox_tickets", "contacts_helpcenter_reporting"], [ic_rest], "Spans live messaging, inbox/ticketing, customer contacts, knowledge base, reporting, webhooks, and AI agent APIs.")

            set_mcp_entries(
                [("hosted_official", "official", "Intercom Hosted Remote MCP Server", [ic_mcp, ic_mcp_tools], "guides/mcp",
                  "Official vendor-hosted Streamable HTTP MCP server (callable server direction) providing 16 tools (search, fetch, conversations, contacts, companies, plus Fin Operator tools via OAuth) for US (https://mcp.intercom.com/mcp) and EU (https://mcp.eu.intercom.com/mcp) workspaces",
                  "https://mcp.intercom.com/mcp", None)],
                [ic_mcp, ic_mcp_tools],
            )
            buildability(
                "build_now",
                "Intercom customer support triage, conversation/contact lookup, and helpdesk automation via REST API or official hosted MCP server",
                ["Public multi-tenant OAuth apps require Intercom App Store review", "Free development workspaces are US-region only with feature limitations", "MCP server does not yet support AU-hosted workspaces"],
                ["Provision free development workspace for OAuth/REST testing or connect to hosted MCP endpoint", "Submit public OAuth app for Intercom review before multi-tenant distribution"],
                ["auth.access_token", "auth.oauth2", "testing.free_access", "production.vendor_approval_required", "api.protocol.rest", "api.breadth", "mcp.hosted_official"],
                [ic_oauth, ic_devws, ic_review, ic_rest, ic_mcp],
            )

        # =====================================================================
        # 13. Freshdesk (Pilot app refreshed with newly captured 31,897-line API ref + pricing)
        # =====================================================================
        elif app == 13:
            fd_id = E("50000011778", 84, 90, "Freshdesk offers email-first Freshdesk and omnichannel Freshdesk Omni customer support platforms across Growth, Pro, and Enterprise plans.")
            fd_api_id = E("developers.freshdesk.com/api/", 794, 804, "Freshdesk REST API v2 (https://domain.freshdesk.com/api/v2/) exposes helpdesk resources scoped to the authenticated Freshdesk user profile permissions.")
            fd_basic = E("developers.freshdesk.com/api/", 779, 793, "Freshdesk API v2 authenticates requests using personal API keys via HTTP Basic Authentication (Base64-encoded APIkey:X in Authorization header).")
            fd_oauth = E("oauth-implementation-in-apps/", 35, 47, "Freshworks apps and Custom apps built with FDK support OAuth authorization and access token authentication against Freshdesk REST APIs.")
            fd_price = E("freshworks.com/freshdesk/pricing/", 19, 65, "Freshdesk offers paid Growth ($19/agent/mo), Pro ($55), and Enterprise ($89, including Sandbox) plans billed annually with Try it free trials and MCP action add-ons ($15/1000 actions).")
            fd_mcp_ov = E("50000012670", 67, 108, "Freshworks MCP server (GA Sept 10, 2026) connects AI tools to Freshdesk using API key authentication only; included annual MCP actions are 1,200 (Growth), 6,000 (Pro), and 12,000 (Enterprise).")
            fd_mcp_url = E("50000012670", 127, 149, "Freshdesk MCP server uses HTTP transport at tenant-specific endpoint https://<subdomain>.freshdesk.com/mcp with Authorization: <api-key> header.")
            fd_grp_tkt = E("developers.freshdesk.com/api/", 32, 120, "Freshdesk API v2 reference documents Tickets, Ticket Fields, Sections, Ticket Forms, and Conversations endpoints.")
            fd_grp_rest = E("developers.freshdesk.com/api/", 794, 802, "Freshdesk API v2 exposes core helpdesk resources including /api/v2/contacts and /api/v2/tickets.")
            fd_rate = E("developers.freshdesk.com/api/", 523, 540, "Freshdesk API v2 enforces plan-tiered per-minute rate limits and endpoint sub-limits with optional paid limit increases.")

            r["identity"]["resolution"] = claim("identity", "Freshdesk and Freshdesk Omni customer support helpdesk by Freshworks; original Freshdesk identity matched (refreshed from Task 04 pilot).", [fd_id, fd_api_id])
            r["purpose"] = claim("purpose", "Customer support ticketing and omnichannel helpdesk platform providing REST API v2, FDK OAuth apps, and an official hosted MCP server.", [fd_id, fd_api_id, fd_oauth, fd_mcp_ov])

            items(
                r["auth"],
                [
                    auth("api_key_basic", "basic", "Personal agent API key passed via HTTP Basic Authentication (Base64-encoded apikey:X); inherits the agent's Freshdesk role permissions.", [fd_basic, fd_api_id], "Direct Freshdesk REST API v2 calls"),
                    auth("oauth2_fdk", "oauth2", "OAuth authorization and access tokens supported in Freshworks Marketplace apps and Custom apps built with the FDK.", [fd_oauth], "Freshworks/Custom FDK apps"),
                    auth("mcp_api_key", "api_key", "Official Freshdesk MCP server currently authenticates via Authorization: <api-key> header only (no OAuth on MCP transport).", [fd_mcp_ov, fd_mcp_url], "Official Freshdesk MCP server"),
                ],
                "Verified directly against freshly captured 31,897-line developers.freshdesk.com/api/ (resolving Task 04 pilot capture gap), FDK OAuth docs, and official MCP article.",
            )

            elig("testing", "trial_access", True, [fd_price], "Freshdesk Growth, Pro, and Enterprise plans offer a self-serve Try it free trial.")
            elig("testing", "sandbox_access", True, [fd_price], "Sandbox is listed as a feature on the Freshdesk Enterprise plan ($89/agent/month annually).")
            elig("testing", "self_serve", True, [fd_price], "Free trial signup is self-serve on the Freshdesk pricing page.")
            elig("production", "paid_required", True, [fd_price, fd_mcp_ov], "Production Growth, Pro, and Enterprise plans (and GA MCP action allowances) require paid per-agent subscriptions.")
            elig("production", "self_serve", True, [fd_price, fd_basic], "Paid plans and personal agent API keys are self-serve within an authorized Freshdesk account.")

            items(r["api_surface"]["protocols"], [claim("api.protocol.rest", "REST", [fd_api_id, fd_rate])], "Freshdesk REST API v2 captured directly from developers.freshdesk.com/api/.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [fd_api_id, fd_basic])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("tickets_forms_fields", "Tickets, ticket fields, sections, ticket forms, and conversations", [fd_grp_tkt]),
                    group("contacts_core", "Contacts and core helpdesk resources under /api/v2/", [fd_grp_rest]),
                ],
                "Core REST v2 resource groups captured from developers.freshdesk.com/api/.",
            )
            breadth("moderate", ["tickets_forms_fields", "contacts_core"], [fd_grp_tkt, fd_grp_rest], "Captured sections establish core ticketing, forms/fields, conversations, and contacts across the v2 REST reference.")

            set_mcp_entries(
                [("hosted_official", "official", "Freshworks MCP Server for Freshdesk", [fd_mcp_ov, fd_mcp_url], "50000012670",
                  "Official vendor-hosted HTTP MCP server (callable server direction) at tenant-specific URL https://<subdomain>.freshdesk.com/mcp using API key auth only; metered annual action allowances (1,200/6,000/12,000 by plan)",
                  None, None)],
                [fd_mcp_ov, fd_mcp_url],
            )
            buildability(
                "build_now",
                "Freshdesk ticket triage, reply, and contact lookup toolkit via REST API v2 or official Freshdesk MCP server",
                ["Official MCP server supports API key auth only (no OAuth) and enforces metered annual action allowances", "Sandbox requires Enterprise tier", "OAuth is documented for FDK Marketplace/Custom apps rather than standalone external MCP clients"],
                ["Prototype with free trial + personal API key on REST API v2 or tenant /mcp endpoint", "Evaluate FDK OAuth app path if multi-tenant Marketplace distribution is needed"],
                ["auth.api_key_basic", "auth.oauth2_fdk", "testing.trial_access", "production.paid_required", "api.protocol.rest", "api.breadth", "mcp.hosted_official"],
                [fd_basic, fd_price, fd_api_id, fd_mcp_ov],
            )

        # =====================================================================
        # 14. Front
        # =====================================================================
        elif app == 14:
            fr_id = E("front.com/pricing", 14, 18, "Front is an all-in-one customer service and collaborative shared-inbox email management platform.")
            fr_auth_tok = E("docs/authentication.md", 6, 18, "Front Core API uses Bearer tokens obtained either via company-level API tokens in Settings or via OAuth 2.0.")
            fr_tok_admin = E("create-and-revoke-api-tokens.md", 7, 46, "Front API tokens apply at the company level, require admin privileges in Settings > Developers, and support granular features, namespaces, and permissions (read, write, delete, send).")
            fr_oauth = E("docs/oauth", 100, 117, "Front OAuth 2.0 (Authorization Code grant at app.frontapp.com/oauth/authorize and /oauth/token) is required for public integrations; end users authorizing OAuth apps must be admins (except MCP server user-scoped OAuth).")
            fr_price = E("front.com/pricing", 71, 103, "Front offers annually billed paid Starter ($25/seat/mo, Try for Free), Professional ($65, omnichannel, Request a Demo), and Enterprise ($105, Request a Demo) plans.")
            fr_rest = E("reference/introduction", 10, 37, "Front Core API is a REST API documenting Accounts, Custom Fields, Analytics, and Applications endpoints.")
            fr_grp_msg = E("reference/introduction", 38, 72, "Front Core API documents Channels, Drafts, Messages, Comments, and Attachments.")
            fr_grp_conv = E("reference/introduction", 118, 204, "Front Core API documents Contacts, Conversations, Events, Inboxes, and Knowledge Bases/Articles.")
            fr_mcp = E("docs/mcp-server.md", 6, 26, "Front hosts an official Streamable HTTP MCP server at https://mcp.frontapp.com/mcp using OAuth 2.1 + PKCE with per-user teammate tokens (read, write, send scopes); Dynamic Client Registration is not supported.")
            fr_admin_mcp = E("docs/admin-mcp-server.md", 6, 27, "Front hosts a separate Admin MCP server (open beta, free on all plans during beta) at https://mcp.frontapp.com/admin-mcp for managing rules, AI teammates, knowledge bases, and workspace config via admin-scoped OAuth 2.1 + PKCE.")

            r["identity"]["resolution"] = claim("identity", "Front collaborative shared-inbox and customer service platform; original Front identity matched.", [fr_id, fr_auth_tok])
            r["purpose"] = claim("purpose", "Collaborative shared-inbox and omnichannel customer service platform providing a Core REST API and official hosted Front and Admin MCP servers.", [fr_id, fr_price, fr_rest, fr_mcp, fr_admin_mcp])

            items(
                r["auth"],
                [
                    auth("api_token", "api_key", "Company-level Bearer API tokens created by admins in Settings > Developers with granular feature/namespace/permission scopes (read, write, delete, send).", [fr_auth_tok, fr_tok_admin], "Internal/single-tenant Core API integrations"),
                    auth("oauth2", "oauth2", "OAuth 2.0 Authorization Code grant required for public App Store integrations; authorizing user must be an admin (except per-user MCP OAuth).", [fr_oauth], "Multi-tenant public Front apps"),
                ],
                "Checked Front authentication.md, create-and-revoke-api-tokens.md, and oauth docs.",
            )

            elig("testing", "trial_access", True, [fr_price], "Front Starter plan offers a Try for Free trial on the pricing page.")
            elig("testing", "self_serve", True, [fr_price], "Starter tier free trial is self-serve; Professional and Enterprise show Request a Demo.")
            elig("production", "paid_required", True, [fr_price], "Production Front workspaces require paid per-seat plans (Starter $25, Professional $65, Enterprise $105/seat/mo annual).")
            elig("production", "admin_approval_required", True, [fr_tok_admin, fr_oauth], "Front admins are required to create company-level API tokens and to authorize standard private/public OAuth apps (individual teammates can authorize MCP OAuth once configured).")

            items(r["api_surface"]["protocols"], [claim("api.protocol.rest", "REST", [fr_rest, fr_auth_tok])], "Front Core REST API captured from reference/introduction and authentication.md.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [fr_rest, fr_auth_tok])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("accounts_analytics_channels", "Accounts, custom fields, analytics exports/reports, channels, drafts, messages, comments, and attachments", [fr_rest, fr_grp_msg]),
                    group("contacts_conversations_kb", "Contacts, conversations, events, inboxes, and knowledge bases/articles", [fr_grp_conv]),
                ],
                "Resource groups captured from Front Core API reference index.",
            )
            breadth("broad", ["accounts_analytics_channels", "contacts_conversations_kb"], [fr_rest, fr_grp_msg, fr_grp_conv], "Covers omnichannel conversations, messaging, contacts/accounts, inboxes, rules/tags, analytics, and knowledge bases.")

            set_mcp_entries(
                [
                    ("hosted_official", "official", "Front MCP Server", [fr_mcp], "docs/mcp-server.md",
                     "Official vendor-hosted Streamable HTTP MCP server (callable server direction) for teammate-scoped conversation data (read, write, send) using confidential OAuth 2.1 + PKCE (no DCR)",
                     "https://mcp.frontapp.com/mcp", None),
                    ("admin_hosted_official", "official", "Front Admin MCP Server (Open Beta)", [fr_admin_mcp], "docs/admin-mcp-server.md",
                     "Official vendor-hosted Streamable HTTP Admin MCP server (callable server direction, open beta) for admin configuration of rules, inboxes, AI teammates, and knowledge bases via confidential OAuth 2.1 + PKCE",
                     "https://mcp.frontapp.com/admin-mcp", None),
                ],
                [fr_mcp, fr_admin_mcp],
            )
            buildability(
                "build_now",
                "Front shared-inbox triage, conversation management, and configuration automation via Core REST API or official Front/Admin MCP servers",
                ["Admin role required to create API tokens or authorize standard OAuth apps", "MCP servers do not support Dynamic Client Registration (require confidential OAuth client ID/secret)"],
                ["Create a Starter trial workspace to test Core API Bearer tokens or confidential OAuth MCP connector", "Register a public OAuth app for multi-tenant distribution"],
                ["auth.api_token", "auth.oauth2", "testing.trial_access", "production.admin_approval_required", "api.protocol.rest", "api.breadth", "mcp.hosted_official"],
                [fr_auth_tok, fr_oauth, fr_price, fr_rest, fr_mcp],
            )

        # =====================================================================
        # 15. Pylon
        # =====================================================================
        elif app == 15:
            py_id = E("developer/api", 130, 136, "Pylon provides a programmatic API (plus TypeScript, Python, Go SDKs and experimental CLI) for fetching customers and managing support issues.")
            py_auth = E("api/authentication.md", 4, 33, "Pylon REST API uses non-expiring Bearer API tokens (region-prefixed pylon_api_ / pylon_api_eu_) created only by Admins, with role-based access (no separate scopes) and optional IP allowlist.")
            py_price = E("usepylon.com/pricing", 74, 113, "Pylon paid plans ($89/seat and $139/seat on annual contracts, plus Enterprise) include MCP, API, and Integrations.")
            py_price_api = E("usepylon.com/pricing", 1207, 1215, "Pylon pricing matrix lists REST API and Scoped API Tokens across tiers.")
            py_grp1 = E("api/api-reference.md", 4, 36, "Pylon API Reference documents Accounts, Activities, Attachments, Audit Logs, Call Recordings, Contacts, Custom Fields, Custom Objects, Email, Feature Requests, and Issues.")
            py_grp2 = E("api/api-reference.md", 37, 72, "Pylon API Reference documents Knowledge Base, Macros, Me, Messages, Surveys, Tags, Tasks & Projects, Teams, Ticket Forms, Training Data, User roles, and Users.")
            py_mcp = E("integrations/pylon-mcp.md", 4, 30, "Pylon hosts an official stateless Streamable HTTP MCP server at https://mcp.usepylon.com (US) and https://mcp.eu.usepylon.com (EU), authenticating via OAuth 2.0 or Bearer API token for identities with MCP Access permission.")
            py_mcp_tools = E("integrations/pylon-mcp.md", 99, 100, "Pylon MCP server lists callable write tools including create_activity and delete_account.")

            r["identity"]["resolution"] = claim("identity", "Pylon B2B customer support platform (usepylon.com); original Pylon identity matched.", [py_id, py_price])
            r["purpose"] = claim("purpose", "B2B customer support platform providing regional REST APIs, official SDKs/CLI, and a hosted MCP server for issues, accounts, contacts, and knowledge bases.", [py_id, py_auth, py_grp1, py_grp2, py_mcp])

            items(
                r["auth"],
                [
                    auth("api_token_bearer", "api_key", "Admin-created Bearer API tokens (Authorization: Bearer <token>, US/EU regional prefixes) controlled by assigned role or user/bot identity, with optional public IP allowlist.", [py_auth], "Pylon REST API and headless MCP clients"),
                    auth("mcp_oauth2", "oauth2", "Interactive OAuth 2.0 user sign-in supported on the hosted Pylon MCP server; requests execute under the signed-in user's role and MCP Access permission.", [py_mcp], "Interactive Pylon MCP server connections"),
                ],
                "Checked Pylon api/authentication.md and integrations/pylon-mcp.md.",
            )

            elig("production", "paid_required", True, [py_price], "Pylon plans are paid annual per-seat subscriptions ($89/seat, $139/seat, Enterprise) that include REST API and MCP access.")
            elig("production", "admin_approval_required", True, [py_auth], "Only Pylon Admins can create and manage REST API tokens and view API request logs.")
            elig("testing", "admin_approval_required", True, [py_auth], "Creating an API token in any Pylon workspace requires an Admin role.")

            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.rest", "REST", [py_auth, py_price_api]),
                    claim("api.protocol.sdk", "SDK", [py_id]),
                    claim("api.protocol.cli", "CLI", [py_id]),
                ],
                "Pylon REST API (US/EU), official TypeScript/Python/Go SDKs, and experimental CLI captured.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [py_id, py_auth, py_grp1])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("accounts_contacts_issues", "Accounts, activities, contacts, issues, feature requests, custom fields/objects, and audit logs", [py_grp1]),
                    group("kb_messages_tasks_admin", "Knowledge base, macros, messages, surveys, tags, tasks & projects, teams, ticket forms, training data, and users/roles", [py_grp2]),
                ],
                "Resource groups captured from Pylon API reference index.",
            )
            breadth("broad", ["accounts_contacts_issues", "kb_messages_tasks_admin"], [py_grp1, py_grp2], "Spans B2B support issues, accounts/contacts, knowledge base, tasks/projects, call recordings, surveys, custom objects, and admin/audit logs.")

            set_mcp_entries(
                [("hosted_official", "official", "Pylon MCP Server", [py_mcp, py_mcp_tools], "integrations/pylon-mcp.md",
                  "Official vendor-hosted stateless Streamable HTTP MCP server (callable server direction) at https://mcp.usepylon.com (US) and https://mcp.eu.usepylon.com (EU) supporting OAuth 2.0 or Bearer API token auth for read/write workspace tools",
                  "https://mcp.usepylon.com", None)],
                [py_mcp, py_mcp_tools],
            )
            buildability(
                "conditional",
                "Pylon B2B support issue/account workflow automation via REST API or official hosted MCP server",
                ["No self-serve free tier or public free-trial path established in checked pricing/docs (annual paid contracts listed)", "Admin role required to generate REST API tokens; MCP Access permission required for MCP"],
                ["Obtain access to a Pylon workspace (sales/trial evaluation) with Admin or MCP Access permissions", "Connect via regional REST API (api.usepylon.com / api.eu.usepylon.com) or hosted MCP endpoint"],
                ["auth.api_token_bearer", "auth.mcp_oauth2", "production.paid_required", "production.admin_approval_required", "api.protocol.rest", "api.breadth", "mcp.hosted_official"],
                [py_auth, py_price, py_grp1, py_mcp],
            )

        # =====================================================================
        # 16. LiveAgent
        # =====================================================================
        elif app == 16:
            la_id = E("061754-Complete-API-reference", 128, 128, "LiveAgent is a cloud customer support software, ticketing system, live chat, social helpdesk, and voice helpdesk.")
            la_qu = E("061754-Complete-API-reference", 147, 147, "LiveAgent helpdesk software is provided by Quality Unit, LLC.")
            la_rest = E("061754-Complete-API-reference", 10, 48, "LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.")
            la_price = E("liveagent.com/pricing/", 23, 27, "LiveAgent offers a 30-day free trial with no credit card required across help desk plans.")
            la_plans = E("liveagent.com/pricing/", 109, 160, "LiveAgent offers paid per-agent plans (Starter $15/mo regular, Team $29/mo regular, and Business).")
            la_apikeys = E("liveagent.com/pricing/", 438, 440, "LiveAgent pricing comparison table documents tiered API key allowances across plans.")
            la_mcp = E("647358-MCP-Integration-for-Agents", 17, 57, "LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry).")
            la_mcp_tools = E("647358-MCP-Integration-for-Agents", 58, 62, "LiveAgent MCP integration gives external AI tools access to the full set of LiveAgent MCP tools under the agent's identity and role permissions, counting toward a shared AI budget.")

            r["identity"]["resolution"] = claim("identity", "LiveAgent help desk, ticketing, live chat, and call center software by Quality Unit; original LiveAgent identity matched.", [la_id, la_qu, la_price])
            r["purpose"] = claim("purpose", "Multichannel help desk, ticketing, live chat, social, and voice helpdesk platform providing a REST API and a built-in agent MCP server.", [la_id, la_rest, la_mcp])

            items(
                r["auth"],
                [
                    auth("api_key", "api_key", "API key authentication documented for LiveAgent REST API calls (v1 PHP reference passes apikey; tiered API key counts listed on pricing page).", [la_rest, la_apikeys], "LiveAgent REST API calls"),
                    auth("mcp_oauth2_pkce", "oauth2", "OAuth 2.1 (Authorization Code + PKCE) with automatic metadata discovery for connecting external AI clients to LiveAgent's built-in MCP server.", [la_mcp], "Built-in LiveAgent MCP server"),
                    auth("mcp_bearer_token", "api_key", "Profile-generated MCP Bearer access tokens (up to 10 active per account, 2-year automatic expiry) for MCP clients without OAuth.", [la_mcp], "Built-in LiveAgent MCP server (non-OAuth clients)"),
                ],
                "Checked LiveAgent REST API article, pricing page, and MCP Integration for agents article.",
            )

            elig("testing", "trial_access", True, [la_price], "LiveAgent offers a 30-day free trial with no credit card required.")
            elig("testing", "self_serve", True, [la_price, la_plans], "30-day free trial signup is self-serve on liveagent.com/pricing/.")
            elig("production", "paid_required", True, [la_plans], "Production LiveAgent usage requires a paid subscription plan (Starter, Team, or Business).")
            elig("production", "self_serve", True, [la_plans], "Standard LiveAgent plans (Starter, Team, Business) are available via self-serve trial and checkout.")

            items(r["api_surface"]["protocols"], [claim("api.protocol.rest", "REST", [la_rest])], "LiveAgent REST API documented; captured support article covers REST API v1 PHP examples.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [la_rest, la_mcp])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("conversations_messages", "Conversations, messages, and departments", [la_rest]),
                ],
                "Partial resource coverage: captured support article demonstrates conversations, messages, and departments.",
            )
            breadth("narrow", ["conversations_messages"], [la_rest], "Captured public API reference snapshot only explicitly documents conversation, message, and department operations.")

            set_mcp_entries(
                [("hosted_official", "official", "LiveAgent Built-in MCP Server", [la_mcp, la_mcp_tools], "647358-MCP-Integration-for-Agents",
                  "Official built-in Streamable HTTP MCP server (callable server direction) at tenant URL https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 + PKCE or Bearer token auth under agent permissions and shared AI budget",
                  None, None)],
                [la_mcp, la_mcp_tools],
            )
            buildability(
                "build_now",
                "LiveAgent ticket/conversation support agent toolkit via built-in MCP server or REST API",
                ["Captured public REST API documentation reflects older API v1 PHP examples", "MCP tool calls count against a shared workspace AI budget"],
                ["Start a 30-day no-credit-card free trial to test the built-in /api/mcp endpoint and REST API", "Authenticate via OAuth 2.1 + PKCE or personal MCP Bearer token"],
                ["auth.api_key", "auth.mcp_oauth2_pkce", "testing.trial_access", "production.paid_required", "api.protocol.rest", "mcp.hosted_official"],
                [la_rest, la_price, la_mcp, la_mcp_tools],
            )

        # =====================================================================
        # 17. Plain
        # =====================================================================
        elif app == 17:
            pl_id = E("graphql/introduction.md", 4, 7, "Plain is a customer support platform built entirely on its public GraphQL API with full UI-to-API parity.")
            pl_price_id = E("plain.com/pricing", 1, 45, "Plain offers B2B support plans (Foundation $45/user/mo annual, Horizon $99, Frontier custom) with a 7-day free trial (no credit card required).")
            pl_apikey = E("graphql/authentication.md", 4, 21, "Plain authenticates API calls via Machine User API keys (Authorization: Bearer plainApiKey_xxx) with fine-grained permissions.")
            pl_oauth = E("graphql/oauth.md", 55, 70, "Plain supports OAuth 2.0 Authorization Code + PKCE (signin.auth.plain.com/oauth2/authorize and /oauth2/token) to call the API as a workspace user; apps work in the workspace where created.")
            pl_gql = E("graphql/introduction.md", 13, 24, "Plain GraphQL API uses POST to https://core-api.uk.plain.com/graphql/v1 with downloadable schema at /graphql/v1/schema.graphql.")
            pl_sdk = E("_llms/developer.txt", 16, 16, "Plain provides a typed GraphQL SDK auto-generated from its schema.")
            pl_grp1 = E("_llms/developer.txt", 17, 57, "Plain GraphQL API documents Customers, Customer Groups, Accounts, Threads, Tiers & SLAs, and SLA Policies.")
            pl_grp2 = E("_llms/developer.txt", 60, 116, "Plain GraphQL API documents Reporting/Insights, Events, Labels, Messaging, Snippets, Tasks, Knowledge Gaps, Webhook Targets, Discussions, and Help Center.")
            pl_mcp = E("integrations/mcp-server.md", 4, 27, "Plain hosts an official remote HTTP MCP server at https://mcp.plain.com/mcp for Claude, ChatGPT, Cursor, and other MCP clients.")
            pl_mcp_auth = E("integrations/mcp-server.md", 66, 70, "Plain MCP server uses OAuth user sign-in so tool calls inherit the authenticated user's web app permissions with no API keys needed.")

            r["identity"]["resolution"] = claim("identity", "Plain B2B customer support platform (plain.com); original Plain identity matched.", [pl_id, pl_price_id])
            r["purpose"] = claim("purpose", "API-first B2B customer support platform built on a public GraphQL API with Machine User keys, OAuth, webhooks, and an official hosted MCP server.", [pl_id, pl_gql, pl_apikey, pl_oauth, pl_grp2, pl_mcp])

            items(
                r["auth"],
                [
                    auth("machine_user_api_key", "api_key", "Machine User API keys (Authorization: Bearer plainApiKey_xxx) scoped with fine-grained permissions.", [pl_apikey], "Backend integrations, bots, and custom agents"),
                    auth("oauth2_pkce", "oauth2", "OAuth 2.0 Authorization Code + PKCE (signin.auth.plain.com/oauth2/authorize & /token) for calling the GraphQL API as a workspace user (and for hosted MCP).", [pl_oauth, pl_mcp_auth], "User-scoped workspace apps and hosted MCP server"),
                ],
                "Checked Plain graphql/authentication.md, graphql/oauth.md, and integrations/mcp-server.md.",
            )

            elig("testing", "trial_access", True, [pl_price_id], "Plain offers a 7-day free trial with no credit card required on Foundation.")
            elig("testing", "self_serve", True, [pl_price_id], "7-day free trial on Foundation is self-serve; Horizon and Frontier show Book a Demo.")
            elig("production", "paid_required", True, [pl_price_id], "Production Plain workspaces require paid per-user plans (Foundation $45/user/mo annual, Horizon $99, Frontier custom).")

            items(
                r["api_surface"]["protocols"],
                [
                    claim("api.protocol.graphql", "GraphQL", [pl_gql]),
                    claim("api.protocol.sdk", "SDK", [pl_sdk]),
                ],
                "Plain GraphQL API (v1) and auto-generated typed GraphQL SDK captured.",
            )
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [pl_gql, pl_apikey])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("customers_accounts_threads_sla", "Customers, customer groups, accounts, threads, tiers, and SLA policies", [pl_grp1]),
                    group("messaging_reporting_kb_webhooks", "Messaging, reporting metrics, events, labels, snippets, tasks, knowledge gaps, webhook targets, discussions, and help center", [pl_grp2]),
                ],
                "Resource groups captured from Plain developer documentation index (184 developer pages, 178 queries, 268 mutations).",
            )
            breadth("broad", ["customers_accounts_threads_sla", "messaging_reporting_kb_webhooks"], [pl_grp1, pl_grp2], "Full UI-to-API parity across threads, customers/accounts, SLAs, messaging, help center, reporting, tasks, and webhooks.")

            set_mcp_entries(
                [("hosted_official", "official", "Plain Hosted MCP Server", [pl_mcp, pl_mcp_auth], "integrations/mcp-server.md",
                  "Official vendor-hosted remote HTTP MCP server (callable server direction) at https://mcp.plain.com/mcp using user-scoped OAuth authentication",
                  "https://mcp.plain.com/mcp", None)],
                [pl_mcp, pl_mcp_auth],
            )
            buildability(
                "build_now",
                "Plain support thread triage, customer/account context, and reply automation via GraphQL API or official hosted MCP server",
                ["OAuth apps are scoped to the workspace where created (workspace-level OAuth)", "7-day trial window is short for extended prototyping"],
                ["Start a 7-day no-credit-card trial and create a Machine User API key or connect to https://mcp.plain.com/mcp via OAuth"],
                ["auth.machine_user_api_key", "auth.oauth2_pkce", "testing.trial_access", "production.paid_required", "api.protocol.graphql", "api.breadth", "mcp.hosted_official"],
                [pl_apikey, pl_gql, pl_price_id, pl_mcp],
            )

        # =====================================================================
        # 18. Help Scout (developer.helpscout.com returned compressed binary; cite ONLY readable pricing snapshot!)
        # =====================================================================
        elif app == 18:
            hs_id = E("helpscout.com/pricing/", 1, 16, "Help Scout is a customer support software platform with shared Inbox, Copilot, Envoy AI assistant, and Signal insights.")
            hs_free = E("helpscout.com/pricing/", 68, 77, "Help Scout offers a Free Basic plan ($0, 1 shared email Inbox, 1 public knowledge base, 25 contacts/month, no AI tools).")
            hs_paid = E("helpscout.com/pricing/", 78, 121, "Help Scout offers paid Standard ($25/user/mo annual), Plus ($45/user/mo annual), and Pro ($75/user/mo annual, Book a Demo) plans.")
            hs_kb_rep = E("helpscout.com/pricing/", 292, 335, "Help Scout pricing feature matrix documents Knowledge base Docs sites, Beacon, Messaging, and Reporting.")
            hs_trial = E("helpscout.com/pricing/", 398, 403, "Help Scout offers a 15-day free trial with no credit card required for Standard and Plus plans; trialing Pro requires talking to sales.")
            hs_api = E("helpscout.com/pricing/", 371, 376, "Help Scout pricing feature matrix documents read/write API access (200/400/800 calls/minute on paid tiers) and Webhooks & OAuth apps.")

            r["identity"]["resolution"] = claim("identity", "Help Scout customer support software platform (helpscout.com); original Help Scout identity matched.", [hs_id])
            r["purpose"] = claim("purpose", "Customer support platform providing shared inboxes, knowledge base Docs sites, messaging, reporting, webhooks, OAuth apps, and tiered API access.", [hs_id, hs_kb_rep, hs_api])

            items(
                r["auth"],
                [
                    auth("oauth_apps", "oauth2", "Help Scout pricing feature table confirms OAuth apps support; detailed grant flows and Docs API key mechanics were not readable because developer.helpscout.com snapshots returned compressed binary bytes.", [hs_api], "Help Scout OAuth apps (plan-tiered)"),
                ],
                "Partial coverage: developer.helpscout.com returned compressed binary responses that could not be read as plain text; only readable helpscout.com/pricing/ evidence is cited.",
            )

            elig("testing", "free_access", True, [hs_free], "Free Basic plan ($0) exists for product use (1 Inbox, 25 contacts/mo), though API access rate tiers on pricing apply to paid plans.")
            elig("testing", "trial_access", True, [hs_trial], "15-day cardless free trial is available for Standard and Plus plans (Pro trial requires contacting sales).")
            elig("testing", "self_serve", True, [hs_trial, hs_free], "Free Basic and 15-day Standard/Plus trials are self-serve without a credit card.")
            elig("production", "paid_required", True, [hs_paid, hs_api], "Tiered API access (200/400/800 calls/min) is listed on paid Standard, Plus, and Pro plans.")
            elig("production", "self_serve", True, [hs_paid, hs_trial], "Standard and Plus plans are self-serve; Pro requires Book a Demo / talking to sales.")

            items(r["api_surface"]["protocols"], [claim("api.protocol.api_access", "other", [hs_api])], "Pricing matrix confirms read/write API access and Webhooks & OAuth apps; exact REST/protocol details on developer.helpscout.com were unreadable due to compressed response.")
            # public_documentation, resource_groups, breadth, and mcp.discovery remain honestly unknown.

            buildability(
                "conditional",
                "Help Scout shared-inbox and customer-support automation via API and OAuth apps",
                ["Primary developer.helpscout.com documentation snapshots returned compressed binary responses (unreadable in current collector)", "API access is tied to paid Standard/Plus/Pro tiers rather than Free Basic"],
                ["Capture uncompressed Help Scout Mailbox API v2, Docs API, and MCP documentation to confirm endpoints, OAuth flows, and scopes", "Prototype on a 15-day Standard or Plus free trial"],
                ["auth.oauth_apps", "testing.trial_access", "production.paid_required", "api.protocol.api_access"],
                [hs_api, hs_trial, hs_paid],
            )

        # =====================================================================
        # 19. Gorgias
        # =====================================================================
        elif app == 19:
            go_id = E("gorgias.com/pricing", 1, 18, "Gorgias is an AI-powered ecommerce customer experience (CX) and helpdesk platform with AI Agent, Gaia, Helpdesk, Voice, and SMS.")
            go_pricing_tiers = E("gorgias.com/pricing", 140, 154, "Gorgias pricing states Helpdesk scales from 50 to 5,000 tickets a month (never priced per agent), with AI Agent paid per resolution and Voice/SMS add-ons.")
            go_auth_ov = E("reference/authentication", 184, 190, "Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps.")
            go_oauth = E("oauth2-authentication-for-creating-apps-with-gorgias.md", 6, 55, "Gorgias OAuth2 uses Authorization Code flow on tenant subdomains (https://{subdomain}.gorgias.com/oauth/authorize & /oauth/token) with 24-hour Bearer access tokens, non-expiring refresh tokens, and granular scopes (e.g., customers:read, tickets:read).")
            go_partner = E("docs/overview.md", 7, 17, "Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review.")
            go_review = E("docs/5-submit-app-for-review.md", 11, 13, "Gorgias tech partnership team reviews submitted public apps before approving them for the App Store.")
            go_rest = E("reference/introduction", 188, 190, "Gorgias API is a JSON REST API with resource-oriented URLs and standard HTTP verbs/status codes.")
            go_grp1 = E("reference/introduction", 16, 74, "Gorgias REST API documents Account/Settings, Customers, Custom Fields, Events, Files, Integrations, Jobs, and Macros.")
            go_grp2 = E("reference/introduction", 79, 179, "Gorgias REST API documents Rules, Satisfaction Surveys, Search, Statistics, Tags, Teams, Tickets, Ticket Messages, Users, Views, Voice Calls, and Widgets.")
            go_mcp = E("Gorgias-MCP-Server", 138, 179, "Community GitHub repository mattcoatsworth/Gorgias-MCP-Server implements a Node.js MCP server authenticating with Gorgias API key or OAuth access token and exposing ticket and customer tools (list_tickets, get_ticket, create_ticket, add_message_to_ticket, list_customers, get_customer).")

            r["identity"]["resolution"] = claim("identity", "Gorgias ecommerce customer experience and helpdesk platform; original Gorgias identity matched.", [go_id, go_rest])
            r["purpose"] = claim("purpose", "Ecommerce helpdesk and CX platform providing a REST API (private API keys and public OAuth2) for tickets, messages, customers, macros, rules, and voice.", [go_id, go_rest, go_auth_ov, go_grp1, go_grp2])

            items(
                r["auth"],
                [
                    auth("api_key", "api_key", "API key authentication for private apps and direct testing in the API Reference.", [go_auth_ov], "Private Gorgias apps and API testing"),
                    auth("oauth2", "oauth2", "OAuth 2.0 Authorization Code flow (24h Bearer access tokens + non-expiring refresh tokens) mandatory for public Gorgias App Store apps.", [go_auth_ov, go_oauth], "Multi-tenant public Gorgias apps", ["customers:read", "tickets:read", "integrations:read"]),
                ],
                "Checked Gorgias reference/authentication and oauth2-authentication-for-creating-apps-with-gorgias.md.",
            )

            elig("testing", "trial_access", True, [go_partner], "Gorgias public-app guide directs developers to create a trial account at gorgias.com/signup.")
            elig("testing", "sandbox_access", True, [go_partner], "Gorgias provides Sandbox accounts by converting a trial account after contacting techpartners@gorgias.com.")
            elig("testing", "partner_approval_required", True, [go_partner], "Converting a trial account to a Gorgias Sandbox requires emailing techpartners@gorgias.com after creating a Draft app.")
            elig("production", "paid_required", True, [go_pricing_tiers], "Production Gorgias helpdesk plans scale by monthly ticket volume (50 to 5,000 tickets/month) plus pay-per-resolution AI Agent and Voice/SMS add-ons.")
            elig("production", "partner_approval_required", True, [go_partner, go_review], "Public OAuth2 apps must be created in a partners account and reviewed/approved by the Gorgias tech partnership team.")

            items(r["api_surface"]["protocols"], [claim("api.protocol.rest", "REST", [go_rest])], "Gorgias JSON REST API captured.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [go_rest, go_auth_ov])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("customers_macros_integrations", "Account/settings, customers, custom fields, events, files, integrations, jobs, and macros", [go_grp1]),
                    group("tickets_rules_voice_stats", "Tickets, ticket messages, rules, surveys, search, statistics, tags, teams, users, views, voice calls, and widgets", [go_grp2]),
                ],
                "Resource groups captured from Gorgias REST API reference index.",
            )
            breadth("broad", ["customers_macros_integrations", "tickets_rules_voice_stats"], [go_grp1, go_grp2], "Covers ticketing, messaging, customers, macros, rules, surveys, statistics, voice calls, and integrations.")

            set_mcp_entries(
                [("community_mattcoatsworth", "community", "mattcoatsworth/Gorgias-MCP-Server", [go_mcp], "Gorgias-MCP-Server",
                  "Third-party community Node.js MCP server (callable server direction) exposing Gorgias ticket and customer tools via API key or OAuth token; not vendor-endorsed",
                  None, "https://github.com/mattcoatsworth/Gorgias-MCP-Server")],
                [go_mcp],
            )
            buildability(
                "conditional",
                "Gorgias ecommerce helpdesk ticket/customer automation via REST API (private API key or public OAuth2)",
                ["Converting a trial to a Sandbox requires contacting techpartners@gorgias.com", "Public multi-tenant OAuth2 apps require Gorgias tech partnership review and approval", "Official Gorgias MCP docs were not captured in checked developer portal sources"],
                ["Use private API key on a trial/paid tenant for single-tenant prototyping", "Register on Gorgias Developer Portal and contact techpartners@gorgias.com for Sandbox and public OAuth2 review"],
                ["auth.api_key", "auth.oauth2", "testing.trial_access", "testing.partner_approval_required", "production.partner_approval_required", "api.protocol.rest", "api.breadth"],
                [go_auth_ov, go_oauth, go_partner, go_review, go_rest],
            )

        # =====================================================================
        # 20. Gladly
        # =====================================================================
        elif app == 20:
            gl_id = E("developer.gladly.com/rest/", 152, 168, "Gladly provides a customer service platform with a JSON REST API (1.0, OpenAPI downloadable) and Lookup API for customer profiles, timelines, conversations, and orders.")
            gl_price_id = E("gladly.com/pricing/", 1, 20, "Gladly positions itself as an agentic commerce and customer service platform with Get a demo and Try it yourself entry points.")
            gl_contact = E("gladly.com/pricing/", 166, 169, "Gladly pricing/product page footer offers View demo and Contact sales links without a public self-serve checkout.")
            gl_auth = E("developer.gladly.com/rest/", 181, 219, "Gladly REST API uses token-based HTTP Basic Authentication (agent email as username, API token as password) requiring an Administrator to grant the API User permission; tokens have unrestricted API access.")
            gl_sandbox = E("developer.gladly.com/rest/", 174, 176, "Gladly enables its API in a separate sandbox environment at https://{organization}.gladly.qa so developers can test without impacting production.")
            gl_grp1 = E("developer.gladly.com/rest/", 13, 66, "Gladly REST API documents Agents, Public Answers, Answer Management, Audiences, Business Hours, Communications (SMS/email), and Conversations/Items/Notes/Transcripts.")
            gl_grp2 = E("developer.gladly.com/rest/", 67, 134, "Gladly REST API documents Customers, Endpoints, Events, Export jobs, Inboxes, Organization, Proactive Conversations, Reports, Tasks, Teams, Topics, Webhooks, and Lookup API.")
            gl_mcp_check = E("developer.gladly.com/rest/", 1, 15, "Checked Gladly developer API overview/index (REST API, Lookup API, Testing, Permissions, Authentication) and gladly.com/pricing/; no official or community MCP server is documented in checked sources.")

            r["identity"]["resolution"] = claim("identity", "Gladly customer service and agentic commerce platform (gladly.com); original Gladly identity matched.", [gl_id, gl_price_id])
            r["purpose"] = claim("purpose", "Customer service and agentic commerce platform providing a REST API and Lookup API for customer profiles, conversation timelines, tasks, answers, and webhooks.", [gl_id, gl_price_id, gl_grp1, gl_grp2])

            items(
                r["auth"],
                [
                    auth("api_token_basic", "basic", "Token-based HTTP Basic Authentication (agent email as username, API token as password) over HTTPS; requires Admin-granted API User permission and grants unrestricted API access.", [gl_auth], "Gladly REST API v1 (production and .gladly.qa sandbox)"),
                ],
                "Checked official Gladly API 1.0 ReDoc reference; token-based Basic Auth captured.",
            )

            elig("testing", "sandbox_access", True, [gl_sandbox], "Gladly provides a separate sandbox environment at https://{organization}.gladly.qa with API enabled.")
            elig("testing", "admin_approval_required", True, [gl_auth], "A Gladly Administrator must grant the API User permission on a user profile before API tokens can be created.")
            elig("production", "admin_approval_required", True, [gl_auth], "A Gladly Administrator must enable the API User permission to create and use production API tokens.")
            # production.contact_sales_required remains unknown per Contract v1.1 (View demo / Contact sales links do not explicitly prove mandatory sales gating).

            items(r["api_surface"]["protocols"], [claim("api.protocol.rest", "REST", [gl_id])], "Gladly REST API 1.0 (OpenAPI downloadable) and REST-based Lookup API captured.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [gl_id, gl_auth])
            items(
                r["api_surface"]["resource_groups"],
                [
                    group("agents_answers_conversations", "Agents, public/managed answers, audiences, business hours, SMS/email communications, and conversations/items/notes", [gl_grp1]),
                    group("customers_tasks_reports_webhooks", "Customers, events, exports, inboxes, organization, proactive conversations, reports, tasks, teams, topics, webhooks, and Lookup API", [gl_grp2]),
                ],
                "Resource groups captured from Gladly API 1.0 ReDoc reference.",
            )
            breadth("broad", ["agents_answers_conversations", "customers_tasks_reports_webhooks"], [gl_grp1, gl_grp2], "Covers conversations, customer profiles, knowledge answers, tasks, reports, exports, webhooks, and custom Lookup API.")

            set_mcp_not_found(
                [gl_mcp_check],
                "Bounded check of developer.gladly.com/, developer.gladly.com/rest/, and gladly.com/pricing/ found no documented official or community MCP server; does not prove no MCP exists elsewhere.",
            )
            buildability(
                "conditional",
                "Gladly customer profile, conversation timeline, and task automation via REST API v1",
                ["Public pricing/product page offers View demo / Contact sales links with no public self-serve checkout or free tier documented", "Administrator must enable API User permission; tokens carry unrestricted API access without granular scopes", "No official MCP server documented in checked sources"],
                ["Engage Gladly sales or an existing customer administrator to obtain a .gladly.qa sandbox and API User token", "Wrap Gladly REST API v1 (OpenAPI spec available) using HTTP Basic Auth"],
                ["auth.api_token_basic", "testing.sandbox_access", "production.admin_approval_required", "api.protocol.rest", "api.breadth"],
                [gl_auth, gl_sandbox, gl_contact, gl_id],
            )

    destination.write_text(json.dumps({"records": records}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} records to {destination}")


if __name__ == "__main__":
    build("task08-capture-004", Path(__file__).parent / "extracted-002.json")
