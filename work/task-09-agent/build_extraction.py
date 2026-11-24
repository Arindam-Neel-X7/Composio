"""Task 09 researcher-authored extraction (Communications and Messaging, IDs 21-30, contract v1.1).

Every claim and paraphrase was authored after directly reading the captured primary
and community snapshots in task09-capture-004. No model API, synthetic fixture,
authenticated account operation, independent review, or accuracy measurement occurs here.
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

        AUTH_MAP = {
            "oauth2": "OAuth2",
            "api_key": "API_key",
            "basic": "Basic",
            "bearer_token": "Bearer_token",
            "jwt": "JWT",
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
                refs,
                "Feasibility inference from captured primary documentation; no live integration or credential test executed.",
            )

        # =====================================================================
        # 21. SLACK
        # =====================================================================
        if app == 21:
            r["identity"]["resolution"] = claim(
                "identity",
                "Slack (Slack Technologies, LLC, a Salesforce company) — team messaging, collaboration, and app platform with HTTP RPC-style Web API and hosted MCP server.",
                [E("apis/web-api/", 41, 47, "Slack Web API overview for querying information from and enacting change in a Slack workspace."),
                 E("apis/web-api/", 177, 177, "Footer identifies Slack Technologies, LLC, a Salesforce company."),
                 E("slack.com/pricing", 167, 168, "Slack is a chat and collaboration platform."),
                 E("ai/slack-mcp-server", 43, 46, "Slack provides an official hosted MCP server.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Workspace messaging and collaboration platform with HTTP RPC-style Web API (200+ methods), OAuth 2.0 bot/user tokens, and an official hosted MCP server.",
                [E("apis/web-api/", 41, 47, "Slack Web API is an HTTP RPC-style interface for querying and enacting change in a Slack workspace."),
                 E("apis/web-api/", 130, 131, "Web API exposes over 200 methods organized by method family."),
                 E("slack.com/pricing", 167, 168, "Team chat and collaboration platform."),
                 E("authentication/installing-with-oauth", 41, 51, "Slack apps use OAuth 2.0 v2 flow to request bot and user scopes."),
                 E("authentication/installing-with-oauth", 162, 186, "OAuth 2.0 code exchange returns xoxb bot tokens and xoxp user tokens."),
                 E("ai/slack-mcp-server", 43, 46, "Slack provides an official MCP server for workspace actions."),
                 E("ai/slack-mcp-server", 107, 110, "Official hosted MCP server endpoint at https://mcp.slack.com/mcp.")],
            )
            items(r["auth"], [
                auth("oauth2_v2", "oauth2",
                     "OAuth 2.0 v2 Authorization Code flow via https://slack.com/oauth/v2/authorize and https://slack.com/api/oauth.v2.access (plus user-centric v2_user/authorize and oauth.v2.user.access for MCP/user tokens), issuing xoxb bot tokens and xoxp user tokens.",
                     [E("authentication/installing-with-oauth", 41, 65, "OAuth 2.0 v2 flow requests bot scopes (scope) and user scopes (user_scope) at /oauth/v2/authorize."),
                      E("authentication/installing-with-oauth", 162, 186, "Code exchange at /api/oauth.v2.access returns xoxb bot token and authed_user xoxp user token."),
                      E("authentication/installing-with-oauth", 194, 206, "User-centric /oauth/v2_user/authorize and /api/oauth.v2.user.access flow for user tokens and MCP clients.")],
                     "Slack Web API and MCP OAuth 2.0 apps",
                     scopes=["chat:write", "channels:history", "search:read", "incoming-webhook", "commands"]),
                auth("bearer_token", "bearer_token",
                     "Bearer token (xoxb bot token or xoxp user token) sent in the Authorization: Bearer header (required for application/json POST bodies) or as a POST form parameter.",
                     [E("apis/web-api/", 68, 78, "JSON POST bodies require Authorization: Bearer xoxp-... header."),
                      E("apis/web-api/", 112, 115, "Web API requests authenticate via bearer token identifying a user or bot user."),
                      E("authentication/installing-with-oauth", 221, 229, "Access tokens presented as Authorization: Bearer xoxb-... header or form POST token parameter.")],
                     "Slack Web API runtime request authentication"),
            ], "Slack documents OAuth 2.0 v2 (standard and user-centric) issuing Bearer tokens; token rotation and PKCE are also referenced.")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "free_access", True,
                 [E("slack.com/pricing", 167, 176, "Slack offers a Free forever plan ($0/INR 0) supporting up to 10 apps.")],
                 "Free workspace tier allows installing up to 10 apps for development and testing.")
            elig("testing", "self_serve", True,
                 [E("slack.com/pricing", 167, 176, "Self-serve Get started CTA for Free forever plan with up to 10 apps."),
                  E("apis/web-api/", 113, 114, "Developers register an application with Slack to obtain OAuth 2.0 credentials.")],
                 "Developers can self-serve create a free workspace and register an internal Slack app.")
            elig("production", "free_access", True,
                 [E("slack.com/pricing", 167, 176, "Free forever plan supports up to 10 apps (with 90-day message history).")],
                 "Free tier supports up to 10 apps in production; Pro/Business+/Enterprise+ unlock unlimited apps and history.")
            elig("production", "paid_required", False,
                 [E("slack.com/pricing", 167, 176, "Free forever plan includes up to 10 apps without requiring a paid subscription.")],
                 "Paid plan is not required for basic workspace usage up to 10 apps, though paid plans are needed for unlimited apps and Enterprise features.")
            elig("production", "admin_approval_required", True,
                 [E("ai/slack-mcp-server", 44, 44, "Workspace admins can approve and manage MCP client integrations."),
                  E("ai/slack-mcp-server", 112, 117, "Registered Slack apps allow admins to manage and approve apps using Slack's app approval process."),
                  E("authentication/installing-with-oauth", 84, 84, "Org-level installations require an Org Owner or Org Admin.")],
                 "Workspace or org admins govern app installation/approval in managed workspaces and org-wide installs.")
            elig("production", "vendor_approval_required", True,
                 [E("ai/slack-mcp-server", 117, 121, "Only apps published in the Slack Marketplace and internal apps can use MCP; unlisted apps are prohibited."),
                  E("authentication/installing-with-oauth", 247, 247, "Published apps require Slack review/approval of requested scopes (unapproved_scope error otherwise).")],
                 "Public distribution on the Slack Marketplace (and public MCP distribution) requires Slack review/approval; internal apps do not.")
            elig("production", "self_serve", True,
                 [E("slack.com/pricing", 167, 229, "Free, Pro, and Business+ plans offer self-serve Get started flows."),
                  E("ai/slack-mcp-server", 116, 121, "Internal apps can be created and used on your own workspace without Marketplace listing.")],
                 "Internal workspace apps and Free/Pro/Business+ workspaces are self-serve; public Marketplace apps require Slack review.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rpc", "RPC", [E("apis/web-api/", 46, 47, "Slack Web API is a collection of HTTP RPC-style methods (not REST) at https://slack.com/api/METHOD_FAMILY.method.")]),
                claim("api.protocol.sdk", "SDK", [E("apis/web-api/", 145, 147, "Slack provides Bolt frameworks and official Slack SDKs.")]),
                claim("api.protocol.cli", "CLI", [E("apis/web-api/", 145, 145, "Slack provides the Slack CLI developer tool.")]),
            ], "HTTP RPC-style Web API (200+ methods), plus Bolt frameworks, SDKs, Slack CLI, and Events API.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("apis/web-api/", 41, 47, "Publicly accessible Slack Web API guide at docs.slack.dev/apis/web-api/."),
                 E("reference/methods", 12, 57, "Public method family reference at docs.slack.dev/reference/methods.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("messaging_conversations", "Messages, channels, conversations, reactions, pins, and search (chat, conversations, reactions, search)",
                      [E("reference/methods", 24, 40, "Method families include chat, conversations, reactions, pins, reminders, search."),
                       E("apis/web-api/", 61, 89, "Examples show conversations.create and chat.postMessage.")]),
                group("users_teams_admin", "Users, usergroups, team, admin, SCIM, and audit logs",
                      [E("reference/methods", 13, 56, "Method families include admin, team, usergroups, users, plus Audit Logs API and SCIM API.")]),
                group("files_canvases_lists", "Files, canvases, lists, bookmarks, and calls",
                      [E("reference/methods", 20, 32, "Method families include bookmarks, calls, canvases, files, lists.")]),
                group("workflows_apps_agents", "Workflows, functions, apps, assistant, agents, and Slack Connect",
                      [E("reference/methods", 14, 52, "Method families include agents, apps, assistant, functions, workflows, and Slack Connect API.")]),
            ], "Representative method families from docs.slack.dev/reference/methods (200+ Web API methods).")
            breadth("broad", ["messaging_conversations", "users_teams_admin", "files_canvases_lists", "workflows_apps_agents"],
                    [E("apis/web-api/", 130, 131, "Over 200 Web API methods across families."),
                     E("reference/methods", 12, 57, "Method families span messaging, users/admin, files/canvases/lists, workflows, agents, SCIM, and audit logs.")],
                    "Over 200 Web API methods spanning messaging, workspace administration, files/canvases/lists, workflows, and enterprise compliance APIs.")
            set_mcp_entries([(
                "official", "official", "Slack MCP Server",
                [E("ai/slack-mcp-server", 43, 78, "Official Slack MCP server provides tools for searching messages/files/users/channels, sending/scheduling/drafting messages, canvases, files, and lists."),
                 E("ai/slack-mcp-server", 107, 132, "Hosted JSON-RPC 2.0 Streamable HTTP endpoint at https://mcp.slack.com/mcp using confidential OAuth 2.0 (no SSE or DCR).")],
                "ai/slack-mcp-server",
                "Callable official hosted MCP server (JSON-RPC 2.0 over Streamable HTTP) exposing search, messaging, threads, reactions, canvases, users, files, and lists tools via confidential OAuth 2.0 (internal or Marketplace-published apps only; no DCR).",
                "https://mcp.slack.com/mcp", None,
            )], [E("ai/slack-mcp-server", 43, 46, "Official Slack MCP server documented at docs.slack.dev/ai/slack-mcp-server."),
                 E("ai/slack-mcp-server", 107, 110, "Official endpoint https://mcp.slack.com/mcp.")])
            buildability(
                "build_now",
                "Build a Slack workspace messaging, search, canvas, and list agent toolkit via the Web API or official Slack MCP server.",
                ["Public multi-tenant distribution on Slack Marketplace (and public MCP use) requires Slack app review; unlisted apps cannot use Slack MCP.",
                 "Slack MCP server does not support Dynamic Client Registration (DCR); clients must use a registered Slack app ID with confidential OAuth."],
                ["Register a Slack app and configure OAuth 2.0 v2 scopes (bot and/or user tokens).",
                 "Target https://slack.com/api/* Web API methods or https://mcp.slack.com/mcp for internal testing, and submit for Slack Marketplace review for public multi-tenant distribution."],
                ["identity", "auth.oauth2_v2", "auth.bearer_token", "testing.free_access", "testing.self_serve", "api.protocol.rpc", "api.breadth", "mcp"],
                [E("apis/web-api/", 41, 47, "Public HTTP RPC Web API."),
                 E("ai/slack-mcp-server", 107, 125, "Official hosted MCP server with confidential OAuth and no DCR."),
                 E("slack.com/pricing", 167, 176, "Free forever workspace tier with up to 10 apps.")],
            )

        # =====================================================================
        # 22. TWILIO
        # =====================================================================
        elif app == 22:
            r["identity"]["resolution"] = claim(
                "identity",
                "Twilio (Twilio Inc.) — cloud communications platform providing REST APIs for SMS/MMS/WhatsApp/RCS messaging, voice, video, conversations, email, and authentication (Verify/Lookup).",
                [E("docs/usage/api", 77, 80, "Twilio APIs are organized around REST connecting communications networks for messaging, phone calls, and phone number lookups."),
                 E("docs/usage/api", 90, 90, "Copyright Twilio Inc."),
                 E("en-us/pricing", 685, 764, "Product suite covers SMS/MMS, RCS, WhatsApp, Conversations, Email, Voice, Video, Verify, and Lookup.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Cloud communications API platform for programmable SMS, WhatsApp, voice, video, conversations, and verification, with REST APIs, API Key/Basic auth, and an official MCP monorepo.",
                [E("docs/usage/api", 77, 80, "Twilio REST APIs enable sending messages, making phone calls, and looking up phone numbers over HTTPS or SDKs."),
                 E("en-us/pricing", 685, 764, "Communications and authentication APIs spanning SMS, WhatsApp, Conversations, Voice, Video, and Verify."),
                 E("docs/iam/api-keys", 75, 101, "API keys (Main, Standard, Restricted) and Account SID/Auth Token authenticate Twilio REST APIs."),
                 E("twilio-labs/mcp", 164, 171, "Official twilio-labs/mcp monorepo exposes Twilio's public APIs as MCP tools.")],
            )
            items(r["auth"], [
                auth("api_key", "api_key",
                     "Twilio API Keys (Main, Standard, and Restricted v1 keys) — preferred authentication method for Twilio REST APIs and for generating client SDK Access Tokens.",
                     [E("docs/iam/api-keys", 75, 88, "API keys are the preferred way to authenticate with Twilio's REST APIs and can be scoped with Restricted API keys."),
                      E("docs/iam/api-keys", 97, 101, "Three API key types: Main (full access), Standard (all except Accounts/Keys), and Restricted (fine-grained v1).")],
                     "Twilio REST APIs and SDK Access Token minting"),
                auth("basic_account_sid", "basic",
                     "Account SID and Auth Token credentials retrieved from the Twilio Console home page (equivalent to Main API Key permissions; same credentials used in trial and upgraded accounts).",
                     [E("docs/iam/api-keys", 99, 99, "Main API key is equivalent to using Account SID and Auth Token for API requests."),
                      E("how-to-use-your-free-trial-account", 137, 138, "Account SID and Auth Token available on Console home page for API authentication."),
                      E("how-to-use-your-free-trial-account", 236, 237, "Trial and upgraded accounts use the same Account SID and Auth Token credentials.")],
                     "Twilio REST APIs (Account SID + Auth Token)"),
                auth("oauth2", "oauth2",
                     "Twilio IAM documents OAuth Apps (Account OAuth Apps, Organization OAuth Apps, and OAuth Token API) and webhook OAuth 2.0 authentication.",
                     [E("docs/iam/api-keys", 16, 17, "IAM navigation lists OAuth Apps: Account OAuth Apps, Organization OAuth Apps, OAuth Token API, and OAuth App resource."),
                      E("docs/usage/api", 25, 26, "Webhooks configuration API supports authenticating with OAuth 2.0, Basic, or Digest.")],
                     "Twilio Account/Organization OAuth Apps and webhooks"),
            ], "Primary IAM docs establish API Keys (preferred), Account SID/Auth Token, and OAuth Apps.")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "trial_access", True,
                 [E("how-to-use-your-free-trial-account", 115, 120, "Free 30-day trial account without a credit card, including product-specific free units (e.g., 100 SMS, 100 WhatsApp, 3,000 emails, 75 voice minutes)."),
                  E("en-us/pricing", 650, 653, "Start for free trial with no credit card required.")],
                 "Cardless 30-day free trial provides free product units and API credentials (restricted to verified recipients, sign-up country, and pre-defined templates).")
            elig("testing", "self_serve", True,
                 [E("how-to-use-your-free-trial-account", 115, 138, "Self-serve signup with email and personal phone verification yields immediate Console access and Account SID/Auth Token.")],
                 "Self-serve signup immediately issues API credentials for trial testing.")
            elig("production", "paid_required", True,
                 [E("how-to-use-your-free-trial-account", 256, 270, "Trial expires after 30 days and restricts recipients/templates; upgrading to a paid account with payment details and starting balance is required for production."),
                  E("en-us/pricing", 651, 653, "Pay as you go with usage-based pricing after free trial.")],
                 "Production messaging/calling requires upgrading from the 30-day trial to a pay-as-you-go paid account.")
            elig("production", "self_serve", True,
                 [E("how-to-use-your-free-trial-account", 267, 271, "Self-serve Upgrade button in Twilio Console to add address, starting balance, and payment details."),
                  E("en-us/pricing", 650, 654, "Self-serve Start for free and pay-as-you-go usage-based pricing.")],
                 "Upgrading to a pay-as-you-go production account is self-serve in the Twilio Console (carrier/regulatory registrations such as US A2P 10DLC still apply per country).")
            elig("production", "contact_sales_required", False,
                 [E("how-to-use-your-free-trial-account", 267, 270, "Users upgrade directly in Console by adding payment details and a starting balance without contacting sales.")],
                 "Self-serve Console upgrade is documented for standard pay-as-you-go production accounts.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [E("docs/usage/api", 79, 80, "Twilio APIs are organized around REST over HTTPS.")]),
                claim("api.protocol.sdk", "SDK", [E("docs/usage/api", 80, 80, "Twilio provides official SDKs across several programming languages.")]),
                claim("api.protocol.cli", "CLI", [E("docs/iam/api-keys", 82, 82, "Twilio CLI supports creating regional profiles and managing API keys."),
                                                 E("docs/iam/api-keys", 107, 107, "Manage API keys using CLI profiles for regional authentication.")]),
            ], "REST APIs over HTTPS, multi-language SDKs, Twilio CLI, webhooks, and TwiML.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("docs/usage/api", 77, 85, "Public REST API overview and documentation at twilio.com/docs/usage/api."),
                 E("docs/iam/api-keys", 75, 108, "Public IAM and API Keys documentation at twilio.com/docs/iam/api-keys.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("messaging_conversations", "Programmable Messaging (SMS, MMS, WhatsApp, RCS) and Conversations API",
                      [E("docs/usage/api", 42, 48, "Products include Programmable Messaging, Conversations."),
                       E("en-us/pricing", 685, 703, "SMS, RCS, WhatsApp Business API, and Conversations API.")]),
                group("voice_video", "Programmable Voice, Elastic SIP Trunking, and Video API",
                      [E("docs/usage/api", 42, 47, "Products include Programmable Voice and Video."),
                       E("en-us/pricing", 720, 738, "Voice APIs, Elastic SIP Trunking, and Twilio Video.")]),
                group("verify_lookup", "Authentication and phone intelligence (Verify API and Lookup API)",
                      [E("docs/usage/api", 9, 9, "Trials and products include Verify and Lookup."),
                       E("en-us/pricing", 755, 764, "Verify (anti-fraud verification) and Lookup (phone number validation).")]),
                group("accounts_iam_monitor", "Accounts, Subaccounts, IAM Keys/OAuth Apps, BulkExport, Usage, and Monitor REST API",
                      [E("docs/usage/api", 12, 19, "Accounts, Subaccounts, BulkExport API, Usage records/triggers, and Monitor REST API (Alerts/Events)."),
                       E("docs/iam/api-keys", 8, 23, "Accounts, Organizations, SCIM API, Keys, OAuth Apps, and RBAC.")]),
            ], "Representative API domains from twilio.com/docs/usage/api, docs/iam/api-keys, and pricing.")
            breadth("broad", ["messaging_conversations", "voice_video", "verify_lookup", "accounts_iam_monitor"],
                    [E("docs/usage/api", 12, 50, "Covers Accounts, BulkExport, Monitor, Messaging, Voice, Video, Conversations, Flex, Studio, and Verify."),
                     E("en-us/pricing", 658, 765, "Full communications, conversations, voice/video, and Verify/Lookup API suite.")],
                    "Multiple distinct communications and infrastructure domains: Messaging/Conversations, Voice/Video/SIP, Verify/Lookup, and IAM/Accounts/Monitoring.")
            set_mcp_entries([(
                "official", "official", "Twilio MCP Server (@twilio-alpha/mcp)",
                [E("twilio-labs/mcp", 164, 189, "Official twilio-labs/mcp monorepo exposing Twilio's public APIs as MCP tools via npx -y @twilio-alpha/mcp with ACCOUNT_SID/API_KEY:API_SECRET."),
                 E("twilio-labs/mcp", 191, 195, "Supports --services and --tags filtering; ETI team notes official Twilio MCP servers.")],
                "twilio-labs/mcp",
                "Callable official local stdio MCP server (@twilio-alpha/mcp from github.com/twilio-labs/mcp) exposing Twilio's public OpenAPI endpoints as MCP tools, filterable via --services and --tags.",
                None, "https://github.com/twilio-labs/mcp",
            )], [E("twilio-labs/mcp", 164, 171, "Official Twilio MCP Monorepo exposing Twilio's public APIs as MCP tools.")])
            buildability(
                "build_now",
                "Build a Twilio SMS/WhatsApp/Voice/Verify agent toolkit via REST APIs or the official @twilio-alpha/mcp server.",
                ["Free trial expires after 30 days and restricts sends to verified phone numbers (up to 5), sign-up country, and pre-defined templates.",
                 "Production US/Canada 10DLC SMS requires regulatory compliance (paid A2P 10DLC registration)."],
                ["Create a cardless Twilio trial account and generate a Restricted or Standard API Key.",
                 "Use REST APIs or npx @twilio-alpha/mcp --services <domain>, then upgrade to pay-as-you-go and complete country-specific telecom compliance for production."],
                ["identity", "auth.api_key", "auth.basic_account_sid", "testing.trial_access", "testing.self_serve", "production.paid_required", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp"],
                [E("docs/usage/api", 79, 80, "REST APIs over HTTPS and SDKs."),
                 E("how-to-use-your-free-trial-account", 115, 120, "Cardless 30-day free trial with free units."),
                 E("how-to-use-your-free-trial-account", 183, 188, "US A2P 10DLC registration requires a paid account."),
                 E("how-to-use-your-free-trial-account", 256, 263, "Trial restrictions: 30-day expiration, sign-up country, up to 5 verified recipients, and pre-defined templates."),
                 E("twilio-labs/mcp", 164, 188, "Official Twilio MCP server package.")],
            )

        # =====================================================================
        # 23. ZOHO CLIQ
        # =====================================================================
        elif app == 23:
            r["identity"]["resolution"] = claim(
                "identity",
                "Zoho Cliq — team messaging and unified communications (UCaaS) platform by Zoho with a multi-datacenter REST API v2.",
                [E("cliq/help/restapi/v2/", 211, 249, "Cliq REST API v2 at https://cliq.zoho.com across multiple regional Zoho data centers allows performing read and write operations available in the web client."),
                 E("cliq/pricing.html", 1, 3, "Zoho Cliq UCaaS team chat and communications platform.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Team messaging and UCaaS collaboration platform offering a regionalized JSON REST API v2 with OAuth 2.0 authentication and downloadable OpenAPI 3.0 specifications.",
                [E("cliq/help/restapi/v2/", 211, 249, "REST API v2 across regional Zoho data centers (.com, .eu, .in, .com.au, .com.cn, .jp, .sa, .uk, .zohocloud.ca)."),
                 E("cliq/help/restapi/v2/", 252, 267, "Uses OAuth 2.0 authorization via Zoho Developer Console."),
                 E("cliq/help/restapi/v2/", 397, 412, "Provides downloadable OpenAPI Specification (OAS) 3.0.0 YAML files.")],
            )
            items(r["auth"], [
                auth("oauth2", "oauth2",
                     "OAuth 2.0 Authorization Code flow registered at https://accounts.zoho.<dc>/developerconsole (auth at /oauth/v2/auth, token at /oauth/v2/token, refresh tokens with access_type=offline), sent via header Authorization: Zoho-oauthtoken <access_token>.",
                     [E("cliq/help/restapi/v2/", 252, 290, "OAuth 2.0 registration at accounts.zoho.com/developerconsole and grant token request at /oauth/v2/auth with endpoint-specific scopes."),
                      E("cliq/help/restapi/v2/", 303, 347, "Token exchange at /oauth/v2/token yields 1-hour access_token and permanent refresh_token."),
                      E("cliq/help/restapi/v2/", 375, 387, "Mandatory request header: Authorization: Zoho-oauthtoken <access_token>.")],
                     "Zoho Cliq REST API v2 (domain-specific per Zoho data center)",
                     scopes=["ZohoCliq.Channels.CREATE", "ZohoCliq.Channels.READ", "ZohoCliq.Channels.UPDATE", "ZohoCliq.Channels.DELETE"]),
            ], "Zoho Cliq REST API v2 mandates OAuth 2.0 with Zoho-oauthtoken header over HTTPS.")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "free_access", True,
                 [E("cliq/pricing.html", 6, 11, "Zoho Cliq offers a Free plan with messaging, channels, file storage, meetings, and chat export."),
                  E("cliq/help/restapi/v2/", 265, 278, "Developers register a client in Zoho Developer Console to receive client_id and client_secret.")],
                 "Free Cliq edition and self-serve Zoho Developer Console registration enable free testing.")
            elig("testing", "trial_access", True,
                 [E("cliq/pricing.html", 12, 33, "Standard, Professional, and Enterprise tiers each offer Start free trial.")],
                 "Paid tiers offer free trials alongside the Free edition.")
            elig("testing", "self_serve", True,
                 [E("cliq/pricing.html", 6, 12, "Self-serve Try Now / Get Started / Start free trial CTAs."),
                  E("cliq/help/restapi/v2/", 265, 278, "Self-serve OAuth client creation in accounts.zoho.com/developerconsole.")],
                 "Workspace creation and Zoho Developer Console OAuth app registration are self-serve.")
            elig("production", "free_access", True,
                 [E("cliq/pricing.html", 6, 11, "Free plan provides messaging, channels, file storage, meetings, and chat export.")],
                 "Free edition is available for production small-team use; Standard/Professional/Enterprise expand limits and admin features.")
            elig("production", "paid_required", False,
                 [E("cliq/pricing.html", 6, 35, "Free plan exists alongside paid Standard, Professional (min 10 users), and Enterprise (min 10 users) plans.")],
                 "Paid plan is not strictly required to use Zoho Cliq, though Professional/Enterprise features (teams, custom roles, audit history, DLP) require paid plans.")
            elig("production", "self_serve", True,
                 [E("cliq/pricing.html", 48, 65, "Free, Standard, Professional, and Enterprise plans provide self-serve Get Started / Start free trial flows.")],
                 "Self-serve signup and OAuth client registration are documented across tiers.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [E("cliq/help/restapi/v2/", 211, 223, "Zoho Cliq REST API v2 returns JSON objects over HTTPS.")]),
            ], "REST API v2 with downloadable OpenAPI 3.0.0 specs across 9 regional Zoho domains.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("cliq/help/restapi/v2/", 1, 14, "Full public REST API v2 reference at zoho.com/cliq/help/restapi/v2/."),
                 E("cliq/help/restapi/v2/", 397, 412, "Publicly downloadable OpenAPI 3.0.0 YAML specification.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("chats_channels_messages", "Chats, Channels, Threads, Messages, Reactions, Scheduled Messages, and Files",
                      [E("cliq/help/restapi/v2/", 76, 145, "REST endpoints for Chats, Channels, Threads, Messages, Scheduled Messages, Bots, and Files.")]),
                group("users_org_structure", "Users, Userfields, User Status, Departments, Roles, Designations, Teams, and Remote Work",
                      [E("cliq/help/restapi/v2/", 22, 75, "REST endpoints for Users, Userfields, User Status, Departments, Roles, Designation, and Remote Work."),
                       E("cliq/help/restapi/v2/", 114, 122, "Teams CRUD and member management endpoints.")]),
                group("calls_events_reminders", "Calls & Meetings, Calendar Events, Reminders, and Cliq Database",
                      [E("cliq/help/restapi/v2/", 146, 189, "REST endpoints for Calls & Meetings, Events, Reminders, Cliq Database, Widget Map Tickers, Custom Domain, and Custom Email.")]),
            ], "Full REST endpoint catalog captured from zoho.com/cliq/help/restapi/v2/ (10,572 lines).")
            breadth("broad", ["chats_channels_messages", "users_org_structure", "calls_events_reminders"],
                    [E("cliq/help/restapi/v2/", 15, 190, "Spans Bulk Export Maintenance APIs, Users/Roles/Departments/Teams, Chats/Channels/Threads/Messages/Files/Bots, Calls/Meetings, Events, Reminders, and Cliq Database.")],
                    "Covers messaging/channels, org directory/RBAC, calls/meetings, calendar events, reminders, and custom database tables.")
            set_mcp_entries([(
                "community", "community", "Cliq-MCP (rohansen856/cliq-mcp)",
                [E("rohansen856/cliq-mcp", 154, 178, "Community Python MCP server and webhook bot for Zoho Cliq providing summarization, task extraction, meeting minutes, and issue classification."),
                 E("rohansen856/cliq-mcp", 225, 270, "Runs in --mode mcp, webhook, or both; configures CLIQ_BOT_TOKEN, CLIQ_CLIENT_ID, CLIQ_CLIENT_SECRET.")],
                "rohansen856/cliq-mcp",
                "Callable community local MCP server (Python, github.com/rohansen856/cliq-mcp) exposing Zoho Cliq summarization, task extraction, meeting minutes, and classification tools; not vendor-endorsed.",
                None, "https://github.com/rohansen856/cliq-mcp",
            )], [E("rohansen856/cliq-mcp", 154, 165, "Community MCP server repository for Zoho Cliq.")])
            buildability(
                "build_now",
                "Build a Zoho Cliq messaging, channels, reminders, and org-directory agent toolkit using REST API v2 and OAS 3.0 specs.",
                ["Multi-datacenter routing required: OAuth and API base URLs vary across 9 regional Zoho domains (.com, .eu, .in, etc.).",
                 "No official Zoho Cliq MCP server was found in checked primary docs; only a community MCP repo was captured."],
                ["Register an OAuth 2.0 client in Zoho Developer Console and select required ZohoCliq.* scopes.",
                 "Use the downloadable OAS 3.0 YAML spec to generate typed REST API v2 tools with regional domain support and Zoho-oauthtoken header handling."],
                ["identity", "auth.oauth2", "testing.free_access", "testing.self_serve", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp"],
                [E("cliq/help/restapi/v2/", 234, 249, "Multi-datacenter regional base URIs."),
                 E("cliq/help/restapi/v2/", 252, 278, "Self-serve OAuth 2.0 registration in Zoho Developer Console."),
                 E("cliq/help/restapi/v2/", 397, 412, "Downloadable OpenAPI 3.0.0 YAML specs."),
                 E("cliq/pricing.html", 6, 12, "Free and paid plans with self-serve onboarding.")],
            )

        # =====================================================================
        # 24. LARK (LARKSUITE)
        # =====================================================================
        elif app == 24:
            r["identity"]["resolution"] = claim(
                "identity",
                "Lark (Larksuite / international counterpart to Feishu) — enterprise messaging and workplace collaboration platform with the Lark Open Platform (https://open.larksuite.com), official SDKs, and official OpenAPI MCP server.",
                [E("lark-openapi-mcp", 172, 178, "Feishu/Lark official OpenAPI MCP encapsulating Feishu/Lark Open Platform API interfaces."),
                 E("lark-openapi-mcp", 241, 249, "Distinguishes Feishu (China, https://open.feishu.cn) and Lark (International, https://open.larksuite.com)."),
                 E("oapi-sdk-python", 151, 158, "Official Feishu OpenPlatform Server SDK for Python."),
                 E("node-sdk", 183, 188, "Official Feishu open interface SDK for Node.js/TypeScript.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Enterprise collaboration and messaging suite with the Lark Open Platform REST APIs (https://open.larksuite.com), official Python/Node SDKs, and an official OpenAPI MCP server.",
                [E("lark-openapi-mcp", 178, 178, "Encapsulates Feishu/Lark Open Platform APIs for document processing, conversation management, calendar scheduling, and more."),
                 E("lark-openapi-mcp", 246, 248, "International Lark uses https://open.larksuite.com."),
                 E("oapi-sdk-python", 151, 158, "Official Python Server SDK for messaging, contacts, approval, sheets, Base, and other product capabilities."),
                 E("node-sdk", 183, 188, "Official Node.js/TypeScript open interface SDK.")],
            )
            items(r["auth"], [
                auth("app_tenant_token", "bearer_token",
                     "App ID and App Secret obtained from Lark Open Platform Console, exchanged for tenant_access_token (or keyless ClientAssertion JWT mode for self-built/eligible ISV apps via official SDKs).",
                     [E("lark-openapi-mcp", 181, 185, "Create an app in Lark Open Platform Console to obtain App ID and App Secret for API authentication."),
                      E("lark-openapi-mcp", 240, 240, "Server-side calls use tenant_access_token by default when not using user_access_token."),
                      E("oapi-sdk-python", 171, 202, "Official Python SDK authenticates with app_id/app_secret or keyless ClientAssertion mode for tenant tokens.")],
                     "Lark Open Platform server-side / app-identity APIs (self-built and ISV apps)"),
                auth("oauth2_user_token", "oauth2",
                     "OAuth 2.0 user authorization flow (configurable redirect URL, e.g., http://localhost:3000/callback, or OAuth device flow via register_app) issuing user_access_token for user-scoped resources.",
                     [E("lark-openapi-mcp", 186, 186, "OAuth 2.0 redirect URL configuration for calling APIs as a user."),
                      E("lark-openapi-mcp", 216, 240, "OAuth login flow with scopes (e.g., offline_access, docx:document) and --token-mode user_access_token."),
                      E("oapi-sdk-python", 203, 236, "One-click OAuth device flow (register_app) supporting tenant and user scopes.")],
                     "Lark Open Platform user-scoped OAuth 2.0 APIs",
                     scopes=["offline_access", "docx:document", "im:message:send_as_bot", "calendar:calendar:read"]),
            ], "Captured from official larksuite GitHub repos (open.larksuite.com web docs returned a 1-line JS shell).")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "self_serve", True,
                 [E("lark-openapi-mcp", 180, 186, "Developers log in to Lark Open Platform Console, create an application, obtain App ID/App Secret, and add permissions.")],
                 "App creation and credential generation in Lark Open Platform Console are self-serve; workspace plan pricing was not captured because larksuite.com/en_us/plans returned a 1-line JS shell.")
            elig("production", "self_serve", True,
                 [E("lark-openapi-mcp", 180, 186, "Self-built enterprise applications can be created and configured in the Lark Open Platform Console."),
                  E("node-sdk", 199, 201, "Distinguishes Enterprise self-built applications (installed within the enterprise) from ISV store applications.")],
                 "Self-built enterprise app creation is self-serve; pricing/tier requirements and ISV store review requirements remain unknown from captured non-JS snapshots.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [E("lark-openapi-mcp", 178, 178, "Feishu/Lark Open Platform OpenAPI HTTP interfaces."),
                                                   E("node-sdk", 280, 285, "SDK sends HTTP API calls via axios to https://open.larksuite.com or https://open.feishu.cn.")]),
                claim("api.protocol.sdk", "SDK", [E("oapi-sdk-python", 151, 167, "Official Python Server SDK (lark-oapi)."),
                                                 E("node-sdk", 183, 206, "Official Node.js/TypeScript SDK (@larksuiteoapi/node-sdk).")]),
            ], "OpenAPI REST interfaces plus official Python and Node.js SDKs (and WebSocket event client in node-sdk).")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("lark-openapi-mcp", 174, 178, "Links to public Official Document and Developer Documentation Retrieval MCP."),
                 E("oapi-sdk-python", 159, 164, "Public SDK README and documentation links.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("messaging_im", "Instant messaging and chats (im.v1.message.create, im.v1.message.list, im.v1.chat.create)",
                      [E("lark-openapi-mcp", 283, 283, "IM API tools: im.v1.message.create, im.v1.message.list, im.v1.chat.create."),
                       E("oapi-sdk-python", 170, 183, "lark_oapi.api.im.v1 message creation.")]),
                group("docs_drive_sheets_base", "Cloud documents, Drive, Sheets, and Base",
                      [E("oapi-sdk-python", 154, 155, "Server-side APIs for sheets and Base."),
                       E("lark-openapi-mcp", 178, 178, "Document processing APIs."),
                       E("oapi-sdk-python", 242, 242, "Drive metadata scope drive:drive.metadata:readonly.")]),
                group("calendar_contacts_approval", "Calendar, Contacts, Approvals, and Attendance",
                      [E("oapi-sdk-python", 154, 155, "Server-side APIs for contacts and approval."),
                       E("lark-openapi-mcp", 178, 178, "Calendar scheduling APIs."),
                       E("node-sdk", 191, 195, "Tutorials cover Personnel/Attendance, Contact API, and Approval.")]),
            ], "Captured from official larksuite/lark-openapi-mcp, oapi-sdk-python, and node-sdk repositories.")
            breadth("broad", ["messaging_im", "docs_drive_sheets_base", "calendar_contacts_approval"],
                    [E("oapi-sdk-python", 154, 158, "Spans messaging, contacts, approval, sheets, Base, and other capabilities."),
                     E("lark-openapi-mcp", 178, 178, "Covers document processing, conversation management, calendar scheduling, and more.")],
                    "Multiple enterprise collaboration domains: IM/chats, cloud docs/Drive/Sheets/Base, calendar, contacts, approvals, and attendance.")
            set_mcp_entries([(
                "official", "official", "Feishu/Lark OpenAPI MCP (@larksuiteoapi/lark-mcp)",
                [E("lark-openapi-mcp", 172, 178, "Official Feishu/Lark OpenAPI MCP (Beta) encapsulating Open Platform APIs as MCP tools."),
                 E("lark-openapi-mcp", 200, 271, "Runs via npx -y @larksuiteoapi/lark-mcp mcp -a <app_id> -s <app_secret> --domain https://open.larksuite.com; supports tenant_access_token and OAuth user_access_token; notes file upload/download and direct document editing are not yet supported.")],
                "lark-openapi-mcp",
                "Callable official local stdio MCP server (@larksuiteoapi/lark-mcp, Beta) exposing Lark Open Platform APIs (with --domain https://open.larksuite.com for international Lark); notes file upload/download and direct doc editing are not yet supported.",
                None, "https://github.com/larksuite/lark-openapi-mcp",
            )], [E("lark-openapi-mcp", 172, 178, "Official repository github.com/larksuite/lark-openapi-mcp.")])
            buildability(
                "build_now",
                "Build a Lark (Larksuite) messaging, docs, and calendar agent toolkit via official OpenAPI SDKs or @larksuiteoapi/lark-mcp.",
                ["International Lark apps (https://open.larksuite.com) and China Feishu apps (https://open.feishu.cn) are strictly separate domain environments.",
                 "Official lark-mcp is Beta and does not yet support file upload/download or direct document editing."],
                ["Create an international Lark app at https://open.larksuite.com to obtain App ID and App Secret.",
                 "Configure --domain https://open.larksuite.com in @larksuiteoapi/lark-mcp or Domain.Lark in @larksuiteoapi/node-sdk, and enable OAuth user_access_token where user-private access is needed."],
                ["identity", "auth.app_tenant_token", "auth.oauth2_user_token", "testing.self_serve", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp"],
                [E("lark-openapi-mcp", 177, 186, "Beta official OpenAPI MCP and Console app setup."),
                 E("lark-openapi-mcp", 246, 268, "International Lark domain separation (open.larksuite.com vs open.feishu.cn)."),
                 E("lark-openapi-mcp", 270, 271, "Current MCP limitations on file upload/download and direct doc editing.")],
            )

        # =====================================================================
        # 25. PUMBLE
        # =====================================================================
        elif app == 25:
            r["identity"]["resolution"] = claim(
                "identity",
                "Pumble (by CAKE.com Inc.) — team communication and collaboration app offering an API Keys addon, Incoming Webhooks, Node.js SDK/CLI, and MCP server support.",
                [E("pumble.com/", 1, 8, "Pumble team communication tool powered by CAKE.com alongside Clockify and Plaky."),
                 E("api-keys/", 59, 62, "Pumble API addon enables HTTP requests via generated API keys on all plans."),
                 E("api-keys/", 183, 183, "Copyright Pumble by CAKE.com Inc."),
                 E("incoming-webhooks/", 58, 58, "Supports incoming webhooks for posting messages into Pumble."),
                 E("pumble-node-sdk", 143, 146, "Provides Pumble SDK for Node.js and pumble-cli."),
                 E("pumble.com/", 195, 197, "Product page announces Pumble's MCP server for AI agents.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Business team chat and collaboration app by CAKE.com with a REST API Keys addon (Swagger-documented), Incoming Webhooks, Node.js SDK/CLI, and MCP support.",
                [E("api-keys/", 59, 86, "Pumble API addon exposes HTTP REST endpoints (Swagger docs, up to 1,000 req/min/user) for messages, threads, reactions, and channels."),
                 E("incoming-webhooks/", 58, 86, "Incoming webhooks post formatted JSON messages to channels via unique URLs."),
                 E("pumble-node-sdk", 143, 159, "Official CAKE-com/pumble-node-sdk provides Pumble SDK and pumble-cli for building Pumble apps."),
                 E("pumble.com/", 183, 197, "Product page announces Pumble's MCP server for AI agents.")],
            )
            items(r["auth"], [
                auth("api_key_addon", "api_key",
                     "User-scoped API key generated via the Pumble API addon (sidebar Add API key or /api-keys generate slash command; available to Owner, Admin, and Member on all plans; up to 1,000 req/min/user).",
                     [E("api-keys/", 59, 64, "Owner, Admin, and Member on all plans can use the Pumble API addon; rate limit up to 1,000 req/min/user."),
                      E("api-keys/", 71, 97, "Generate unlimited API keys via sidebar or /api-keys generate; enter key in Swagger Authorize.")],
                     "Pumble API Addon REST endpoints"),
                auth("incoming_webhook_url", "other",
                     "Unique per-channel Incoming Webhook URL (https://api.pumble.com/workspaces/WORKSPACE-ID/incomingWebhooks/postMessage/WEBHOOK-CODE) for HTTP POST message delivery (1 req/sec per webhook).",
                     [E("incoming-webhooks/", 58, 86, "Workspace Settings -> Incoming Webhooks generates a unique URL accepting JSON or form-encoded POST payloads at 1 req/sec.")],
                     "Pumble Incoming Webhooks (outbound-to-Pumble one-way posting)"),
            ], "Primary help docs cover API Keys addon and Incoming Webhooks; pumble-cli uses email-code login for app creation.")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "free_access", True,
                 [E("pumble.com/", 1, 1, "Pumble marketed as a FREE Business Communication Tool."),
                  E("pumble.com/", 148, 148, "Try Pumble - it's free!"),
                  E("api-keys/", 60, 62, "Pumble API addon is available on all plans to Owner, Admin, and Member.")],
                 "Free plan includes the Pumble API addon for generating API keys.")
            elig("testing", "self_serve", True,
                 [E("pumble.com/", 14, 15, "Self-serve Sign Up CTA."),
                  E("api-keys/", 65, 78, "Users self-install the API addon and generate API keys inside their workspace.")],
                 "Workspace signup, API addon installation, and API key generation are self-serve.")
            elig("production", "free_access", True,
                 [E("api-keys/", 59, 62, "API addon is available on all plans."),
                  E("api-keys/", 125, 129, "Plans include Free, Pro, Business, and Enterprise.")],
                 "Free plan supports API addon usage without requiring a paid tier; paid tiers add enterprise workspace features.")
            elig("production", "paid_required", False,
                 [E("api-keys/", 60, 62, "API addon is explicitly marked Available on all plans."),
                  E("api-keys/", 125, 129, "Plans include Free, Pro, Business, and Enterprise."),
                  E("pumble.com/", 148, 148, "Try Pumble - it's free!")],
                 "Paid subscription is not required for Pumble API addon access.")
            elig("production", "self_serve", True,
                 [E("api-keys/", 65, 78, "Self-serve API addon install and key generation inside any Pumble workspace.")],
                 "Self-serve API key generation works for Owner, Admin, and Member roles.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [E("api-keys/", 62, 86, "HTTP REST API via Pumble API addon with Swagger documentation.")]),
                claim("api.protocol.sdk", "SDK", [E("pumble-node-sdk", 143, 145, "Official Pumble SDK for Node.js (CAKE-com/pumble-node-sdk).")]),
                claim("api.protocol.cli", "CLI", [E("pumble-node-sdk", 146, 158, "Official pumble-cli tool to log in, scaffold, and run Pumble apps.")]),
            ], "HTTP REST API (via API addon + Swagger), Incoming Webhooks, official Node.js SDK, and pumble-cli.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("api-keys/", 56, 86, "Public help documentation for Pumble API addon and reference to Swagger documentation."),
                 E("incoming-webhooks/", 55, 86, "Public Incoming Webhooks documentation with cURL and JSON examples.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("messages_threads_reactions", "Messages, thread replies, message deletion, and reactions",
                      [E("api-keys/", 78, 84, "API addon supports sending messages, replying to messages, deleting messages, adding reactions, and listing channel messages.")]),
                group("channels_dms", "Channels and direct messages (creation and listing)",
                      [E("api-keys/", 83, 85, "API addon supports channel creation and listing channels and DMs belonging to the key creator.")]),
                group("webhooks", "Incoming webhooks for channel posting with rich formatting",
                      [E("incoming-webhooks/", 58, 111, "Incoming webhooks support text, user/channel mentions, and attachments.")]),
            ], "Grounded strictly in primary Pumble Help articles (community pumble-mcp also lists scheduled messages and user status endpoints).")
            breadth("moderate", ["messages_threads_reactions", "channels_dms", "webhooks"],
                    [E("api-keys/", 78, 86, "Covers messaging, threads, reactions, and channel/DM management."),
                     E("incoming-webhooks/", 58, 86, "Covers incoming webhook delivery.")],
                    "Multiple related team-messaging resource groups (messages/threads/reactions, channels/DMs, webhooks), narrower than full enterprise admin/telephony suites.")
            set_mcp_entries([
                ("official", "official", "Pumble MCP Server (product-page announcement)",
                 [E("pumble.com/", 183, 183, "Feature list includes MCP Server."),
                  E("pumble.com/", 195, 197, "Use Pumble's MCP server to optimize collaboration with AI agents (summarize conversations, find lost files, automate updates).")],
                 "pumble.com/",
                 "Callable official Pumble MCP server announced on pumble.com for AI agent collaboration (endpoint URL and technical setup doc not yet captured).",
                 None, None),
                ("community", "community", "@infralayers/pumble-mcp",
                 [E("infralayers/pumble-mcp", 154, 161, "Community MCP server exposing 26 tools over Pumble's REST API."),
                  E("infralayers/pumble-mcp", 196, 216, "Runs via npx -y @infralayers/pumble-mcp with PUMBLE_API_KEY env var.")],
                 "infralayers/pumble-mcp",
                 "Callable community local stdio MCP server (@infralayers/pumble-mcp, 26 tools covering messages, threads, scheduled messages, reactions, channels, and users via PUMBLE_API_KEY); not vendor-endorsed.",
                 None, "https://github.com/infralayers/pumble-mcp"),
            ], [E("pumble.com/", 195, 197, "Official Pumble MCP server feature section on pumble.com."),
                E("infralayers/pumble-mcp", 154, 161, "Community Pumble MCP server repository.")])
            buildability(
                "build_now",
                "Build a Pumble team-messaging and channel agent toolkit using the Pumble API addon REST API or community MCP wrapper.",
                ["API key is user-scoped (only lists channels/DMs belonging to the key creator; private channels require Addon Bot membership).",
                 "Official Pumble MCP server endpoint/auth spec was not captured beyond the pumble.com product feature announcement."],
                ["Sign up for a free Pumble workspace, install the API addon, and generate an API key.",
                 "Inspect the Swagger documentation referenced in Pumble Help or evaluate @infralayers/pumble-mcp for local testing."],
                ["identity", "auth.api_key_addon", "testing.free_access", "testing.self_serve", "production.free_access", "api.protocol.rest", "api.breadth", "mcp"],
                [E("api-keys/", 59, 86, "Self-serve API addon available on all plans with Swagger docs and 1,000 req/min rate limit."),
                 E("pumble.com/", 148, 148, "Free tier signup."),
                 E("pumble.com/", 195, 197, "Official Pumble MCP server feature announcement.")],
            )

        # =====================================================================
        # 26. DISCORD
        # =====================================================================
        elif app == 26:
            r["identity"]["resolution"] = claim(
                "identity",
                "Discord — real-time text, voice, and community communications platform with the Discord Developer Platform (HTTP REST API v10, Gateway WebSocket API, OAuth2, and Social/Embedded App SDKs).",
                [E("docs/intro", 58, 68, "Discord Developer Platform for building bots, apps, activities, and integrations with voice chat and social features inside Discord servers."),
                 E("docs/reference", 33, 35, "Provides Social SDK and Embedded App SDK."),
                 E("docs/reference", 92, 92, "Provides Gateway (WebSocket) API."),
                 E("docs/reference", 104, 114, "Discord API is a REST API at https://discord.com/api (v10/v9 available)."),
                 E("docs/reference", 178, 183, "Supports Bot tokens, OAuth2 bearer tokens, and Basic authentication.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Community chat, voice, and app platform exposing HTTP REST API v10, WebSocket Gateway, Bot Token and OAuth2 authentication, and Social/Embedded App SDKs.",
                [E("docs/intro", 58, 68, "Bots, apps, voice chat, and social features inside Discord servers."),
                 E("docs/reference", 92, 92, "Gateway (WebSocket) API."),
                 E("docs/reference", 104, 114, "REST API at https://discord.com/api (v10/v9 available)."),
                 E("docs/reference", 178, 190, "Supports Bot tokens, OAuth2 Bearer tokens, and Basic auth (for OAuth2 token endpoints)."),
                 E("docs/reference", 33, 35, "Provides Social SDK and Embedded App SDK.")],
            )
            items(r["auth"], [
                auth("bot_token", "other",
                     "Bot Token from the Discord Developer Portal (Bot page), sent in HTTP header Authorization: Bot <BOT_TOKEN> for automated bots and server integrations.",
                     [E("docs/reference", 179, 185, "Bot token found on the Bot page of app settings; sent as Authorization: Bot <token>.")],
                     "Discord HTTP API and Gateway bot automation"),
                auth("oauth2", "oauth2",
                     "OAuth 2.0 (Authorization Code, Implicit, Client Credentials, plus modified Bot and Webhook flows) at https://discord.com/oauth2/authorize and https://discord.com/api/oauth2/token, issuing Authorization: Bearer tokens.",
                     [E("docs/reference", 181, 187, "OAuth2 bearer token sent as Authorization: Bearer <token>."),
                      E("docs/topics/oauth2", 93, 103, "Supports authorization code, implicit, client credentials, and bot/webhook flows via /oauth2/authorize and /api/oauth2/token."),
                      E("docs/topics/oauth2", 113, 126, "Documented scopes include applications.commands, bot, email, guilds, and identify."),
                      E("docs/topics/oauth2", 146, 190, "Authorization code exchange and refresh token flow returning Bearer access_token (expires_in 604800s).")],
                     "Discord OAuth 2.0 user/guild authorization and bot installation",
                     scopes=["identify", "email", "guilds", "bot", "applications.commands", "webhook.incoming"]),
                auth("basic_oauth_client", "basic",
                     "HTTP Basic authentication using Base64-encoded client_id:client_secret strictly for OAuth2 API token endpoints.",
                     [E("docs/reference", 182, 189, "Basic auth with client_id:client_secret Base64-encoded, only applicable for OAuth2 API token endpoints."),
                      E("docs/topics/oauth2", 148, 148, "Calls to OAuth2 endpoints require HTTP Basic auth or form-body client_id/client_secret.")],
                     "Discord OAuth2 token exchange endpoints only"),
            ], "Discord documents Bot tokens, OAuth2 Bearer tokens, and Basic auth (restricted to OAuth2 token endpoints).")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "self_serve", True,
                 [E("docs/topics/oauth2", 95, 95, "Developers register an application in the Developer Portal to retrieve client_id and client_secret."),
                  E("docs/reference", 180, 180, "Bot token is retrieved from the Bot page within app settings.")],
                 "Registering a Discord developer application and obtaining a Bot token / OAuth2 client credentials is self-serve.")
            elig("production", "partner_approval_required", True,
                 [E("docs/topics/oauth2", 105, 136, "Certain sensitive OAuth2 scopes (e.g., dm_channels.read, rpc, voice, applications.builds.upload, identify.premium) are 'only available to approved partners' or require Discord approval.")],
                 "Restricted scopes (dm_channels.read, rpc.*, voice, etc.) require Discord partner approval; standard bot and OAuth2 scopes (bot, identify, guilds, applications.commands) do not.")
            elig("production", "self_serve", True,
                 [E("docs/topics/oauth2", 95, 127, "Standard application registration and standard OAuth2/bot scopes are self-serve via Developer Portal (partner-only scopes excluded).")],
                 "Standard bot and OAuth2 app credentials are self-serve; partner-only scopes require Discord approval.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [E("docs/reference", 104, 114, "Discord HTTP REST API at https://discord.com/api/v10.")]),
                claim("api.protocol.other_gateway", "other", [E("docs/reference", 62, 64, "Gateway (WebSocket) API for real-time events and Webhook Events."),
                                                             E("docs/reference", 92, 92, "Gateway (WebSocket) API.")]),
                claim("api.protocol.sdk", "SDK", [E("docs/reference", 33, 35, "Social SDK and Embedded App SDK.")]),
            ], "HTTP REST API v10, WebSocket Gateway API, Webhook Events, and Social/Embedded App SDKs.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("docs/intro", 1, 68, "Public Discord Developer Platform docs at discord.com/developers/docs/intro."),
                 E("docs/reference", 101, 114, "Public API Reference at discord.com/developers/docs/reference.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("messages_channels_threads", "Messages, Channels, Threads, Polls, Emoji, Stickers, and Webhooks",
                      [E("docs/reference", 32, 59, "HTTP API resources include Channel, Emoji, Message, Poll, Sticker, Webhook, plus Threads.")]),
                group("guilds_users_moderation", "Guilds (servers), Users, Invites, Audit Log, Auto Moderation, and Guild Scheduled Events",
                      [E("docs/reference", 40, 57, "HTTP API resources include Audit Log, Auto Moderation, Guild, Guild Scheduled Event, Guild Template, Invite, User.")]),
                group("voice_stage_apps_commerce", "Voice, Stage Instance, Soundboard, Applications, Entitlements, SKUs, and Subscriptions",
                      [E("docs/reference", 37, 58, "HTTP API resources include Application, Entitlement, Lobby, SKU, Soundboard, Stage Instance, Subscription, Voice.")]),
            ], "HTTP API resource catalog from discord.com/developers/docs/reference.")
            breadth("broad", ["messages_channels_threads", "guilds_users_moderation", "voice_stage_apps_commerce"],
                    [E("docs/reference", 36, 71, "23+ distinct HTTP API resource families plus Gateway WebSocket events, Voice, RPC, and Monetization/Commerce.")],
                    "Covers messaging/channels, server administration/moderation, voice/stage, and app monetization/entitlements.")
            set_mcp_entries([(
                "community", "community", "Discord MCP Server (hanweg/mcp-discord)",
                [E("hanweg/mcp-discord", 146, 167, "Community Python MCP server providing tools for server info, channels, members, sending/reading/moderating messages, reactions, and role management."),
                 E("hanweg/mcp-discord", 168, 199, "Runs locally via uv with DISCORD_TOKEN bot token and privileged intents.")],
                "hanweg/mcp-discord",
                "Callable community local stdio MCP server (Python, github.com/hanweg/mcp-discord) wrapping Discord Bot API for server, channel, message, reaction, and role operations; not vendor-endorsed.",
                None, "https://github.com/hanweg/mcp-discord",
            )], [E("hanweg/mcp-discord", 146, 150, "Community Discord MCP server repository.")])
            buildability(
                "build_now",
                "Build a Discord server/channel/messaging agent toolkit via HTTP REST API v10 (Bot token + OAuth2) or community MCP wrapper.",
                ["Sensitive OAuth2 scopes (e.g., dm_channels.read, rpc.*, voice) are restricted to Discord-approved partners.",
                 "No official Discord MCP server was found in checked primary docs; only community MCP implementations were captured.",
                 "Discord pricing/free-tier billing terms for developer portal usage were not captured on a dedicated pricing page (left unknown rather than assumed)."],
                ["Create a Discord application in the Developer Portal, generate a Bot token, and configure required privileged intents (e.g., Message Content Intent for reading messages).",
                 "Build against https://discord.com/api/v10 REST endpoints and OAuth2 bot installation flow."],
                ["identity", "auth.bot_token", "auth.oauth2", "testing.self_serve", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp"],
                [E("docs/reference", 104, 114, "Public REST API v10."),
                 E("docs/reference", 178, 189, "Bot token and OAuth2 authentication."),
                 E("docs/topics/oauth2", 105, 136, "Standard scopes self-serve; partner-only scopes (dm_channels.read, rpc.*, voice) gated.")],
            )

        # =====================================================================
        # 27. TELEGRAM
        # =====================================================================
        elif app == 27:
            r["identity"]["resolution"] = claim(
                "identity",
                "Telegram — cloud-based mobile and desktop messaging platform offering three developer APIs: Telegram Bot API (HTTPS), Telegram MTProto API / TDLib (custom clients), and Telegram Gateway API (verification codes).",
                [E("core.telegram.org/bots", 90, 91, "Telegram is a cloud-based mobile and desktop messaging app."),
                 E("core.telegram.org/api", 10, 16, "Offers three APIs: Bot API (HTTPS interface), Telegram MTProto API / TDLib, and Gateway API.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Cloud messaging platform offering free HTTPS Bot API (v10.5) via @BotFather tokens, free MTProto/TDLib client APIs, and the Telegram Gateway verification API.",
                [E("core.telegram.org/bots", 15, 15, "Telegram Bot Platform hosts 10M+ bots and is free for both users and developers."),
                 E("core.telegram.org/bots", 80, 83, "Register bots via @BotFather to receive a bot authentication token."),
                 E("core.telegram.org/bots/api", 13, 18, "HTTP-based Bot API (v10.5, Nov 22, 2026)."),
                 E("core.telegram.org/api", 11, 28, "Bot API, MTProto Telegram API/TDLib (free of charge), and Gateway API (free to test).")],
            )
            items(r["auth"], [
                auth("bot_token", "other",
                     "Bot authentication token obtained from @BotFather (format <bot_id>:<secret>), embedded directly in HTTPS request URLs as https://api.telegram.org/bot<token>/METHOD_NAME.",
                     [E("core.telegram.org/bots", 80, 83, "Message @BotFather on Telegram to register a bot and receive its unique authentication token."),
                      E("core.telegram.org/bots/api", 127, 132, "Bot token passed in HTTPS URL path: https://api.telegram.org/bot<token>/METHOD_NAME.")],
                     "Telegram Bot API (HTTPS)"),
                auth("mtproto_api_id_hash", "other",
                     "MTProto application registration identifier combined with user phone/QR/passkey authorization and optional two-factor authentication (2FA).",
                     [E("core.telegram.org/api", 27, 43, "Telegram MTProto API requires registering an application for an application identifier and authorizing a user via phone, 2FA, QR code login, or passkeys.")],
                     "Telegram MTProto API / TDLib (user-account client protocol)"),
            ], "Telegram separates Bot API (@BotFather URL-embedded token) from MTProto API (api_id/api_hash + user login).")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "free_access", True,
                 [E("core.telegram.org/bots", 15, 15, "Telegram Bot Platform is free for both users and developers."),
                  E("core.telegram.org/api", 11, 26, "Bot API and Telegram API/TDLib are free of charge; Gateway API is free to test.")],
                 "Bot API and MTProto API are completely free to use for testing.")
            elig("testing", "self_serve", True,
                 [E("core.telegram.org/bots", 80, 83, "Developers self-serve create a bot and receive a token immediately via @BotFather.")],
                 "Bot creation via @BotFather is immediate and self-serve.")
            elig("production", "free_access", True,
                 [E("core.telegram.org/bots", 15, 15, "Telegram Bot Platform is free for both users and developers."),
                  E("core.telegram.org/api", 11, 28, "Bot API and Telegram MTProto API/TDLib are free of charge and 100% open for all developers.")],
                 "Bot API and MTProto API are free for production use (optional local Bot API server is also open-source).")
            elig("production", "paid_required", False,
                 [E("core.telegram.org/bots", 15, 15, "Free for both users and developers."),
                  E("core.telegram.org/api", 11, 11, "Developers are welcome to use both Bot API and Telegram API/TDLib free of charge.")],
                 "No paid subscription is required for Bot API or MTProto API.")
            elig("production", "self_serve", True,
                 [E("core.telegram.org/bots", 80, 83, "Self-serve bot registration via @BotFather.")],
                 "Production bot deployment is self-serve.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rpc", "RPC", [E("core.telegram.org/bots/api", 13, 13, "HTTP-based Bot API interface."),
                                                 E("core.telegram.org/bots/api", 130, 137, "RPC-style HTTPS GET/POST method calls at /bot<token>/METHOD_NAME returning JSON {ok, result}.")]),
                claim("api.protocol.other_mtproto", "other", [E("core.telegram.org/api", 16, 28, "MTProto encrypted client protocol and open-source TDLib library.")]),
            ], "HTTPS RPC-style Bot API (plus open-source self-hostable Local Bot API Server), MTProto protocol, TDLib, and Gateway API.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("core.telegram.org/bots/api", 1, 18, "Complete public Bot API reference at core.telegram.org/bots/api (14,067 lines)."),
                 E("core.telegram.org/api", 1, 28, "Public Telegram APIs and MTProto documentation at core.telegram.org/api.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("bot_messaging_media", "Bot messages, rich messages, ephemeral messages, media, reactions, inline queries, callbacks, and webhooks/getUpdates",
                      [E("core.telegram.org/bots/api", 47, 116, "Send/edit/delete text, rich messages, ephemeral messages, photos, audio, video, documents, stickers, locations."),
                       E("core.telegram.org/bots/api", 155, 220, "Updates via getUpdates or webhooks covering messages, channel posts, business messages, reactions, inline queries, callbacks, and widgets.")]),
                group("chats_business_miniapps", "Chats, groups/channels/forums, Telegram Business connections, Mini Apps, HTML5 games, and Payments/Stars",
                      [E("core.telegram.org/bots", 28, 62, "Mini Apps, Telegram Business Mode, Telegram Stars & third-party payments, games, and affiliate programs."),
                       E("core.telegram.org/bots/api", 179, 190, "Business connections and business messages updates.")]),
                group("mtproto_client_surface", "Full user-client MTProto surface (dialogs, channels/supergroups, stories, calls, search, admin logs, scheduled messages)",
                      [E("core.telegram.org/api", 52, 188, "Channels/supergroups/forums, E2E calls, stories, search/filters, polls, checklists, admin logs, scheduled messages, Passport, Payments.")]),
            ], "Grounded in core.telegram.org/bots, core.telegram.org/bots/api, and core.telegram.org/api.")
            breadth("broad", ["bot_messaging_media", "chats_business_miniapps", "mtproto_client_surface"],
                    [E("core.telegram.org/bots/api", 13, 220, "Extensive Bot API v10.5 surface."),
                     E("core.telegram.org/api", 11, 188, "Full Bot API, MTProto/TDLib client API, and Gateway API.")],
                    "Comprehensive messaging, bot automation, Mini Apps, business accounts, payments, and full MTProto client capabilities.")
            set_mcp_entries([
                ("community_bot", "community", "Telegram Bot MCP Server (node2flow-th/telegram-bot-mcp-community)",
                 [E("telegram-bot-mcp-community", 155, 198, "Community MCP server (@node2flow/telegram-bot-mcp) exposing 27 Telegram Bot API tools via stdio or Streamable HTTP using TELEGRAM_BOT_TOKEN."),
                  E("telegram-bot-mcp-community", 199, 260, "Tools cover bot info, sending messages/media/polls, edit/delete, chat management, webhooks, and callbacks.")],
                 "telegram-bot-mcp-community",
                 "Callable community MCP server (stdio & Streamable HTTP, github.com/node2flow-th/telegram-bot-mcp-community) exposing 27 Telegram Bot API tools via @BotFather token; not vendor-endorsed.",
                 None, "https://github.com/node2flow-th/telegram-bot-mcp-community"),
                ("community_mtproto", "community", "Telegram MTProto MCP Server (sparfenyuk/mcp-telegram)",
                 [E("sparfenyuk/mcp-telegram", 154, 196, "Community uv-installed MCP server bridging Telegram MTProto API for read-only dialog/message/contact access, media download, and drafting."),
                  E("sparfenyuk/mcp-telegram", 202, 230, "Authenticates via TELEGRAM_API_ID, TELEGRAM_API_HASH, and user phone sign-in.")],
                 "sparfenyuk/mcp-telegram",
                 "Callable community local stdio MCP server (uv-installed, github.com/sparfenyuk/mcp-telegram) targeting personal/user MTProto API (read/draft scope); not vendor-endorsed.",
                 None, "https://github.com/sparfenyuk/mcp-telegram"),
            ], [E("telegram-bot-mcp-community", 155, 157, "Community Telegram Bot API MCP server."),
                E("sparfenyuk/mcp-telegram", 154, 173, "Community Telegram MTProto MCP server.")])
            buildability(
                "build_now",
                "Build a Telegram Bot API messaging/notification/group-management agent toolkit (and optional MTProto user-client toolkit).",
                ["Bots cannot initiate private conversations with users first (users must message the bot or add it to a group) and have Privacy Mode enabled in groups by default.",
                 "No official Telegram MCP server was found in checked primary docs; only community Bot API and MTProto MCP servers were captured."],
                ["Register a bot via @BotFather to obtain a free bot token.",
                 "Wrap HTTPS Bot API v10.5 methods (or evaluate @node2flow/telegram-bot-mcp), choosing webhooks or getUpdates for inbound events."],
                ["identity", "auth.bot_token", "testing.free_access", "testing.self_serve", "production.free_access", "api.protocol.rpc", "api.breadth", "mcp"],
                [E("core.telegram.org/bots", 15, 15, "Free for users and developers."),
                 E("core.telegram.org/bots", 74, 83, "Bot conversation-initiation constraint and @BotFather setup."),
                 E("core.telegram.org/bots/api", 127, 137, "HTTPS Bot API request/response format.")],
            )

        # =====================================================================
        # 28. WHATSAPP BUSINESS
        # =====================================================================
        elif app == 28:
            r["identity"]["resolution"] = claim(
                "identity",
                "WhatsApp Business Platform (Cloud API, Business Management API, and Marketing Messages API by Meta) — enterprise customer messaging and calling platform built on Meta Graph API.",
                [E("whatsapp/cloud-api/", 1, 51, "WhatsApp Business Platform includes Cloud API (messaging, calling, groups), Business Management API, Marketing Messages API, Webhooks, and Meta Business Agent."),
                 E("whatsapp/cloud-api/", 53, 54, "Built on Meta Graph API over HTTP.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Meta's enterprise WhatsApp messaging and calling platform built on Graph API with OAuth Bearer system-user tokens, free test phone numbers, per-message delivery pricing, and Meta App Review for multi-tenant apps.",
                [E("whatsapp/cloud-api/", 5, 29, "Cloud API for messaging, calling, and groups; Business Management API for accounts, phone numbers, templates, and analytics."),
                 E("whatsapp/cloud-api/", 53, 94, "Built on Meta Graph API using Authorization: Bearer OAuth access tokens."),
                 E("whatsapp/access-tokens", 3, 7, "Direct developers use long-lived System User access tokens."),
                 E("whatsapp/cloud-api/", 121, 122, "Automatic free test WhatsApp account and test phone number without payment method."),
                 E("whatsapp/pricing", 5, 7, "Per-message delivery pricing by category and market (effective July 1, 2025)."),
                 E("app-review.md", 5, 7, "Direct developers use Standard Access without App Review; multi-tenant apps require Advanced Access via App Review.")],
            )
            items(r["auth"], [
                auth("system_user_token", "bearer_token",
                     "Long-lived System User access token (Admin or Employee system user in Meta Business Settings) for direct developers, sent as Authorization: Bearer <token> against graph.facebook.com.",
                     [E("whatsapp/access-tokens", 3, 32, "Direct developers use System User access tokens generated in Meta Business Settings with business_management, whatsapp_business_management, and whatsapp_business_messaging permissions."),
                      E("whatsapp/access-tokens", 44, 49, "Passed in HTTP header Authorization: Bearer <token>.")],
                     "WhatsApp Business Cloud API (direct developer / single-business)",
                     scopes=["business_management", "whatsapp_business_management", "whatsapp_business_messaging"]),
                auth("embedded_signup_oauth", "oauth2",
                     "Business Integration System User access token obtained via Embedded Signup (Facebook Login for Business OAuth flow) for Tech Providers and Solution Partners accessing onboarded customer accounts.",
                     [E("whatsapp/access-tokens", 4, 5, "Tech Providers and Solution Partners use Business Integration System User access tokens."),
                      E("whatsapp/access-tokens", 33, 37, "Generated by implementing Embedded Signup (Facebook Login for Businesses) and exchanging the returned code.")],
                     "WhatsApp Business Cloud API (multi-tenant Tech Providers and Solution Partners)"),
                auth("user_access_token", "bearer_token",
                     "Short-lived User access token auto-generated in Meta App Dashboard > WhatsApp > API Setup (or Graph API Explorer / Facebook Login) for initial testing.",
                     [E("whatsapp/access-tokens", 38, 43, "User access tokens expire every few hours; primarily used for initial test messages from App Dashboard."),
                      E("cloud-api/get-started", 34, 34, "Temporary access token generated in API Setup panel to send first test message.")],
                     "WhatsApp Business Cloud API (initial development/testing)"),
            ], "Meta documents System User tokens (direct), Business Integration System User tokens via Embedded Signup (multi-tenant), and short-lived User tokens.")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "free_access", True,
                 [E("whatsapp/cloud-api/", 121, 122, "Test WhatsApp account, test Messaging account, and test business phone number are automatically created and do not require a payment method to send template messages.")],
                 "Free test account and test phone number are provisioned automatically with no payment method required.")
            elig("testing", "sandbox_access", True,
                 [E("whatsapp/cloud-api/", 121, 133, "Auto-created test resources with relaxed messaging limits plus API Playground in developer docs."),
                  E("cloud-api/get-started", 15, 39, "Self-serve Meta App creation with WhatsApp use case and test phone number setup.")],
                 "Built-in test WhatsApp/Messaging accounts, test phone number, and API Playground support sandbox testing.")
            elig("testing", "self_serve", True,
                 [E("cloud-api/get-started", 9, 39, "Self-serve Meta developer registration, app creation, and temporary/system-user token generation.")],
                 "Direct developer testing setup is self-serve via Meta App Dashboard.")
            elig("production", "free_access", True,
                 [E("whatsapp/pricing", 104, 108, "Meta does not charge for user-to-business messages, messages in Free Entry Point windows, or the first 1,000 service messages per business phone number per month."),
                  E("whatsapp/pricing", 130, 136, "Every business phone number receives a free tier of 1,000 delivered service messages/month (no rollover); payment method needed after free tier.")],
                 "1,000 free monthly service messages per business phone number (and free user-initiated/FEP windows); template messages and >1,000 service messages incur per-message delivery charges.")
            elig("production", "paid_required", True,
                 [E("whatsapp/pricing", 5, 29, "Marketing, utility, authentication templates, and non-free service messages are billed per delivered message by market and category."),
                  E("whatsapp/pricing", 135, 135, "Without a payment method in Billing Hub, Meta stops delivering service messages after the 1,000/month free tier.")],
                 "Paid billing (payment method in Meta Billing Hub) is required for outbound template messaging and service messages beyond the 1,000/month free tier.")
            elig("production", "vendor_approval_required", True,
                 [E("app-review.md", 5, 21, "Direct developers do not need App Review (Standard Access); apps used by other businesses must obtain Advanced Access via Meta App Review (written explanation + screen recording per permission)."),
                  E("whatsapp/cloud-api/", 116, 117, "Template messages generally require Meta approval before sending.")],
                 "Multi-tenant apps serving other businesses require Meta App Review for Advanced Access (and outbound message templates require approval); single-business direct developers can use Standard Access.")
            elig("production", "self_serve", True,
                 [E("app-review.md", 5, 5, "Direct developers are automatically approved for Standard Access without App Review."),
                  E("cloud-api/get-started", 96, 111, "Direct developers self-serve create a System User and generate permanent tokens in Meta Business Settings.")],
                 "Direct-developer single-business production setup is self-serve; multi-tenant Tech Provider apps require Meta App Review.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [E("whatsapp/cloud-api/", 53, 73, "Built on Meta Graph API over HTTP with JSON request/response bodies.")]),
            ], "Meta Graph API HTTP/JSON REST endpoints (with OpenAPI spec on github.com/meta/openapi) plus Webhooks.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("whatsapp/cloud-api/", 1, 195, "Public WhatsApp Business Platform documentation and llms.txt index at developers.facebook.com."),
                 E("whatsapp/llms.txt", 1, 357, "Full machine-readable documentation index covering 300+ markdown doc pages.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("messaging_calling_groups", "Cloud API Messaging (text, rich media, interactive), Calling, and Groups",
                      [E("whatsapp/cloud-api/", 5, 17, "Cloud API covers messaging (text, rich media, interactive), calling, and groups."),
                       E("whatsapp/llms.txt", 34, 52, "Calling API including SIP, recording, transcription, and sandbox.")]),
                group("business_management_templates", "Business Management API (WhatsApp/Messaging accounts, phone numbers, templates, billing, and analytics)",
                      [E("whatsapp/cloud-api/", 19, 29, "Account management, phone numbers, message templates, billing, and messaging/pricing/template analytics.")]),
                group("commerce_payments_marketing", "Catalogs, Payments (India/Brazil/Mexico), Marketing Messages API, and Meta Business Agent",
                      [E("whatsapp/cloud-api/", 30, 51, "Marketing Messages API and Meta Business Agent."),
                       E("whatsapp/llms.txt", 53, 71, "Product Catalogs API."),
                       E("whatsapp/llms.txt", 230, 256, "Payments APIs for India, Brazil, and Mexico.")]),
                group("webhooks_partners", "Webhooks (messages, statuses, templates, account alerts) and Embedded Signup / Partner Solutions",
                      [E("whatsapp/cloud-api/", 39, 42, "Webhooks for incoming messages, delivery statuses, and error handling."),
                       E("whatsapp/llms.txt", 177, 229, "Partner Solutions, Embedded Signup, and Tech Provider onboarding APIs.")]),
            ], "Grounded in developers.facebook.com/docs/whatsapp/cloud-api/ and whatsapp/llms.txt.")
            breadth("broad", ["messaging_calling_groups", "business_management_templates", "commerce_payments_marketing", "webhooks_partners"],
                    [E("whatsapp/cloud-api/", 4, 51, "Covers Cloud API, Business Management API, Marketing Messages API, Webhooks, and Meta Business Agent."),
                     E("whatsapp/llms.txt", 4, 357, "300+ documentation pages spanning messaging, calling, groups, catalogs, payments, analytics, and partner onboarding.")],
                    "Spans messaging, calling, groups, templates, catalogs, regional payments, analytics, AI agents, and multi-partner onboarding.")
            set_mcp_entries([(
                "community", "community", "WhatsApp Business MCP Server (tkhattar14/whatsapp-business-mcp)",
                [E("tkhattar14/whatsapp-business-mcp", 155, 190, "Community Python MCP server targeting official Meta Graph API (graph.facebook.com) with 50+ tools across 8 modules: messaging, templates, media, analytics, flows, webhooks, business profile, account management."),
                 E("tkhattar14/whatsapp-business-mcp", 206, 237, "Runs via stdio or HTTP using META_ACCESS_TOKEN and META_PHONE_NUMBER_ID.")],
                "tkhattar14/whatsapp-business-mcp",
                "Callable community MCP server (stdio & HTTP, github.com/tkhattar14/whatsapp-business-mcp) wrapping official WhatsApp Business Cloud API on graph.facebook.com (50+ tools); not vendor-endorsed.",
                None, "https://github.com/tkhattar14/whatsapp-business-mcp",
            )], [E("tkhattar14/whatsapp-business-mcp", 155, 162, "Community MCP server targeting official WhatsApp Business Cloud API.")])
            buildability(
                "conditional",
                "Build a multi-tenant WhatsApp Business Cloud API agent toolkit (messaging, templates, webhooks) for customer businesses.",
                ["Multi-tenant apps accessing other businesses' WhatsApp accounts require Meta App Review for Advanced Access (with written explanations and per-permission screen recordings) and Embedded Signup implementation.",
                 "Outbound template messages require Meta template approval, user opt-in, and a payment method in Meta Billing Hub (per-message delivery billing).",
                 "No official Meta WhatsApp MCP doc page was captured in whatsapp/llms.txt (only a community Cloud API MCP server was captured)."],
                ["Prototype using the free auto-provisioned test WhatsApp/Messaging account and System User access token (self-serve under Standard Access).",
                 "Implement Embedded Signup (Facebook Login for Business) and submit for Meta App Review (Advanced Access) before onboarding external customer businesses."],
                ["identity", "auth.system_user_token", "auth.embedded_signup_oauth", "testing.free_access", "testing.sandbox_access", "production.paid_required", "production.vendor_approval_required", "api.protocol.rest", "api.breadth", "mcp"],
                [E("whatsapp/cloud-api/", 116, 117, "Template messages generally require Meta approval before sending."),
                 E("whatsapp/cloud-api/", 121, 122, "Free test account and phone number."),
                 E("whatsapp/cloud-api/", 181, 182, "User opt-in required before sending message templates."),
                 E("app-review.md", 5, 21, "Standard Access for direct developers vs. Meta App Review for multi-tenant Advanced Access."),
                 E("whatsapp/pricing", 5, 29, "Per-message delivery pricing."),
                 E("whatsapp/pricing", 135, 135, "Payment method in Meta Billing Hub required beyond free tier.")],
            )

        # =====================================================================
        # 29. AIRCALL
        # =====================================================================
        elif app == 29:
            r["identity"]["resolution"] = claim(
                "identity",
                "Aircall — AI-powered cloud business phone and customer communications platform offering a Public REST API (v1), Webhooks, Embed SDK (Aircall Anywhere SDK), and AI Virtual Agents.",
                [E("developer.aircall.io/", 17, 44, "Aircall Developer Platform for AI communication: AI API, MCP, REST API, Webhooks, Embed SDK (Aircall Anywhere SDK), and AI Virtual Agents."),
                 E("developer.aircall.io/api-references/", 354, 356, "Aircall Public API is a classic REST API at https://api.aircall.io/v1.")],
            )
            r["purpose"] = claim(
                "purpose",
                "Cloud business phone and customer conversation platform with Public REST API v1 (Basic Auth for customers, OAuth 2.0 for Marketplace partners), Webhooks, and Embed SDK (Aircall Anywhere SDK).",
                [E("developer.aircall.io/api-references/", 354, 375, "REST API at https://api.aircall.io/v1 with HTTP Basic Auth for customers and OAuth 2.0 for Technology Partners."),
                 E("developer.aircall.io/api-references/", 339, 339, "Webhooks for real-time account events (e.g., contact added, call created, user switched off)."),
                 E("developer.aircall.io/", 39, 40, "Embed SDK (Aircall Anywhere SDK) for embedding the workspace.")],
            )
            items(r["auth"], [
                auth("basic_customer", "basic",
                     "HTTP Basic Authentication (Authorization: Basic base64(api_id:api_token)) generated by Aircall customers in Company Settings > API Keys for single-company internal integrations.",
                     [E("developer.aircall.io/api-references/", 370, 370, "Aircall customers building for their own account use Basic Auth."),
                      E("developer.aircall.io/api-references/", 474, 488, "Generate api_id and api_token in Company Settings > API Keys; send Authorization: Basic base64(api_id:api_token).")],
                     "Aircall Public API v1 (single-company customer integrations)"),
                auth("oauth2_partner", "oauth2",
                     "OAuth 2.0 Authorization Code flow for Technology Partners (https://dashboard.aircall.io/oauth/authorize and POST https://api.aircall.io/v1/oauth/token) issuing non-expiring Authorization: Bearer access tokens; requires Aircall-issued client_id/client_secret and Admin install.",
                     [E("developer.aircall.io/api-references/", 369, 425, "Technology Partners use OAuth 2.0 (scope=public_api) with Aircall-provided client_id/client_secret; only Aircall Admins can install; access_token used as Bearer token and does not expire."),
                      E("developer.aircall.io/api-references/", 448, 468, "POST /v1/oauth/token returns Bearer access_token tested via GET /v1/ping.")],
                     "Aircall Public API v1 (multi-tenant Technology Partner / Marketplace apps)",
                     scopes=["public_api"]),
            ], "Aircall separates Basic Auth (customers) from OAuth 2.0 (Technology Partners / Marketplace apps).")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "trial_access", True,
                 [E("aircall.io/pricing/", 42, 44, "Pricing page offers Try for free / Get free access CTAs."),
                  E("aircall.io/pricing/", 134, 154, "Get free access buttons on Essentials ($30/license/mo) and Professional ($50/license/mo) tiers.")],
                 "Free trial/access CTA is offered for Aircall workspaces; developer sandboxes are also provided through the Technology Partner program.")
            elig("testing", "sandbox_access", True,
                 [E("developer.aircall.io/", 89, 92, "Technology partner program provides developer sandboxes, dedicated support, and App Marketplace distribution.")],
                 "Developer sandboxes are documented via Aircall's Technology Partner program.")
            elig("testing", "partner_approval_required", True,
                 [E("developer.aircall.io/api-references/", 407, 409, "To build OAuth apps, developers must fill in a form to request OAuth client_id and client_secret from Aircall ('We will get back to you shortly')."),
                  E("developer.aircall.io/", 89, 92, "Developer sandboxes are provisioned through the technology partner program.")],
                 "OAuth credentials (client_id/client_secret) and partner developer sandboxes require submitting an application to Aircall's technology partnerships team.")
            elig("production", "paid_required", True,
                 [E("aircall.io/pricing/", 134, 185, "Paid plans start at Essentials ($30/license/mo, 3-user minimum), Professional ($50/license/mo, 3-user minimum, includes 'Full API access' L163), and Enterprise (custom, 25-user minimum).")],
                 "Production Aircall accounts require paid seat licenses (3-user minimum; Professional tier explicitly lists Full API access).")
            elig("production", "admin_approval_required", True,
                 [E("developer.aircall.io/api-references/", 374, 374, "Integrations are enabled at the Company level and can only be set by an Admin user."),
                  E("developer.aircall.io/api-references/", 415, 421, "Only Admin users can view the OAuth authorization window and install integrations.")],
                 "Company Admin privileges are required to install integrations or create company API keys.")
            elig("production", "partner_approval_required", True,
                 [E("developer.aircall.io/api-references/", 369, 369, "OAuth flow is required for Technology Partners to be listed on Aircall App Marketplace."),
                  E("developer.aircall.io/api-references/", 407, 409, "Aircall manually provisions OAuth client_id and client_secret after form submission."),
                  E("developer.aircall.io/", 51, 57, "Marketplace apps launch with tech partnerships team support; private workspace apps need no marketplace approval.")],
                 "Multi-tenant OAuth / Marketplace apps require Aircall technology partner onboarding and credential provisioning; private single-tenant Basic Auth apps do not.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [E("developer.aircall.io/api-references/", 354, 357, "Classic REST API at https://api.aircall.io/v1 over HTTPS.")]),
                claim("api.protocol.sdk", "SDK", [E("developer.aircall.io/tutorials/oauth/", 92, 111, "Aircall Everywhere JavaScript SDK to embed the agent workspace inside web products.")]),
            ], "REST API v1, Webhooks, and Aircall Everywhere JavaScript Embed SDK.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("developer.aircall.io/api-references/", 1, 25, "Public REST API Reference (13,223 lines) at developer.aircall.io/api-references/."),
                 E("developer.aircall.io/", 1, 25, "Public Developer Portal and llms.txt index at developer.aircall.io/.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("calls_conversations_ai", "Calls, Conversations, Conversation Intelligence (transcriptions, summaries, sentiments, topics, evaluations, trackers), and AI Voice Agents",
                      [E("developer.aircall.io/api-references/", 52, 75, "Call and Conversation endpoints."),
                       E("developer.aircall.io/api-references/", 141, 156, "Conversation Intelligence (transcriptions, sentiments, predicted CSAT, topics, summaries, action items, evaluations, trackers)."),
                       E("developer.aircall.io/api-references/", 219, 225, "AI Voice Agent outbound call endpoints.")]),
                group("messaging_campaigns", "SMS/WhatsApp Messages, High Volume Messages, Dialer Campaigns, and Outbound Campaigns",
                      [E("developer.aircall.io/api-references/", 76, 133, "Dialer Campaigns and Outbound Campaigns (AIVA campaigns, contacts, queues, outcomes)."),
                       E("developer.aircall.io/api-references/", 159, 178, "Message and High Volume Messages (SMS, group messages, WhatsApp).")]),
                group("users_teams_contacts_numbers", "Users (V1/V2), Teams, Contacts, Tags, Numbers, Webhooks, Company, Integrations, and Analytics",
                      [E("developer.aircall.io/api-references/", 26, 51, "Users V1/V2 and Teams."),
                       E("developer.aircall.io/api-references/", 134, 140, "Numbers endpoints (list, retrieve, update, music/messages, registration status)."),
                       E("developer.aircall.io/api-references/", 179, 229, "Contacts, Tags, Webhooks, Company, Integration, and Analytics report exports.")]),
            ], "Full REST API v1 resource catalog captured from developer.aircall.io/api-references/ (13,223 lines).")
            breadth("broad", ["calls_conversations_ai", "messaging_campaigns", "users_teams_contacts_numbers"],
                    [E("developer.aircall.io/api-references/", 25, 229, "Spans Users/Teams, Calls/Conversations, Outbound/Dialer Campaigns, Numbers, Conversation Intelligence, SMS/WhatsApp Messages, Contacts/Tags, AI Voice Agents, Webhooks, and Analytics.")],
                    "Broad telephony, omnichannel messaging, outbound campaign, conversation intelligence, and workspace administration surface.")
            set_mcp_not_found(
                [E("developer.aircall.io/", 29, 32, "Checked developer.aircall.io/ describes outbound MCP client integration: 'Connect your tools and data to Aircall's AI Virtual Agents through MCP'."),
                 E("developer.aircall.io/tutorials/oauth/", 88, 90, "AI integrations section describes building MCP-compliant integrations for Aircall's AI Virtual Agent ('Coming soon')."),
                 E("aircall-ai/llms.txt", 7, 9, "Aircall AI docs index lists 'Connect with your MCP: Register a Public MCP / MCP FAQs' (outbound tool registration for Aircall AI, not a callable Aircall MCP server).")],
                "Checked Aircall developer docs describe outbound MCP client support (Aircall AI Virtual Agents calling external registered MCP servers) rather than a callable Aircall MCP server; bounded search does not prove no callable Aircall MCP server exists.",
            )
            buildability(
                "conditional",
                "Build a multi-tenant Aircall telephony, messaging, and conversation-intelligence agent toolkit using Public REST API v1.",
                ["Multi-tenant OAuth 2.0 credentials (client_id/client_secret) and developer sandboxes require submitting an application to Aircall's technology partner program.",
                 "Paid Aircall workspace licenses (3-user minimum; Professional tier lists Full API access) and Company Admin privileges are required.",
                 "Checked developer docs only describe outbound MCP client support for Aircall AI Virtual Agents, not a callable Aircall MCP server."],
                ["For single-company internal testing, generate Basic Auth api_id/api_token in Company Settings > API Keys.",
                 "For multi-tenant SaaS/Composio distribution, apply to the Aircall Technology Partner program for OAuth 2.0 credentials and a developer sandbox."],
                ["identity", "auth.basic_customer", "auth.oauth2_partner", "testing.partner_approval_required", "production.paid_required", "production.partner_approval_required", "api.protocol.rest", "api.breadth"],
                [E("developer.aircall.io/api-references/", 368, 425, "Basic Auth for single-company customers vs. partner-provisioned OAuth 2.0 for multi-tenant apps."),
                 E("aircall.io/pricing/", 134, 185, "Paid plans with 3-user minimum and Professional tier Full API access."),
                 E("developer.aircall.io/", 29, 32, "Checked docs describe outbound MCP client integration for Aircall AI Virtual Agents."),
                 E("developer.aircall.io/tutorials/oauth/", 88, 90, "MCP-compliant integrations for Aircall AI Virtual Agent marked Coming soon."),
                 E("developer.aircall.io/", 89, 92, "Technology partner program for sandboxes and Marketplace.")],
            )

        # =====================================================================
        # 30. VONAGE
        # =====================================================================
        elif app == 30:
            r["identity"]["resolution"] = claim(
                "identity",
                "Vonage Communications APIs (Vonage) — cloud communications (CPaaS) platform providing REST APIs for SMS, Messages (WhatsApp/RCS/MMS), Voice, Video, Verify, Conversations, and Network APIs.",
                [E("developer.vonage.com/en/api", 26, 111, "Vonage API Reference covering Messaging, Voice, Network Features, Core Services, Numbers, Account, Verify, and Security/Compliance."),
                 E("communications-apis/pricing/", 935, 936, "Messages API supports SMS, MMS, RCS, WhatsApp, and Facebook Messenger."),
                 E("vonage-kiro-power", 176, 176, "Identifies the Vonage CPaaS platform."),
                 E("communications-apis/pricing/", 1037, 1037, "Copyright Vonage.")],
            )
            r["purpose"] = claim(
                "purpose",
                "CPaaS communications API platform for SMS, multichannel Messages, Voice, Video, Verify, and Network Insights with API Key/Basic and RSA JWT authentication, free credit trial, and official MCP servers.",
                [E("developer.vonage.com/en/api", 26, 105, "APIs for Messages, SMS, Dispatch, Conversation, Voice, Media, Verify, Numbers, Reports, and Network Insights."),
                 E("concepts/authentication", 27, 105, "Supports API Key/Secret (Basic Auth) and RS256 Application JWTs."),
                 E("communications-apis/pricing/", 922, 1020, "Pay-as-you-go usage pricing with cardless free credit trial."),
                 E("vonage-mcp-server-api-bindings", 173, 211, "Official Vonage API MCP server (@vonage/vonage-mcp-server-api-bindings) exposes live account, number, messaging, voice, and reporting tools."),
                 E("vonage-kiro-power", 176, 182, "Official Vonage CPaaS Power documents two official MCP servers: vonage-api and vonage-docs.")],
            )
            items(r["auth"], [
                auth("basic_api_key", "basic",
                     "Account API Key and API Secret from Vonage Dashboard (sent as Authorization: Basic base64(API_KEY:API_SECRET) for newer APIs, with secret rotation supporting two simultaneous secrets).",
                     [E("concepts/authentication", 66, 94, "API Key and Secret created with Vonage account; Base64-encoded in Authorization: Basic header; supports dual-secret rotation.")],
                     "Vonage Account, SMS, Numbers, Pricing, and basic-auth-capable APIs"),
                auth("jwt_application", "jwt",
                     "RS256 JSON Web Token (JWT) signed with a Vonage Application ID and RSA private.key (15 min default, 30s–24h exp; recommended for Messages, Verify, Voice, Conversation, and Client/Video SDKs).",
                     [E("concepts/authentication", 57, 58, "Messages and Verify recommend JWT over Basic Auth (Basic lacks webhooks/ACLs)."),
                      E("concepts/authentication", 95, 151, "RS256 JWT containing application_id, iat, jti, nbf, exp; mintable via Vonage CLI (vonage jwt create) or SDKs; also used by Vonage Client and Video SDKs.")],
                     "Vonage Application-based APIs (Voice, Messages, Verify, Conversation, Video/Client SDKs)"),
            ], "Vonage documents API Key/Secret (Basic Auth and Digest for SIP Trunking) and RS256 Application JWTs.")
            r["credential_eligibility"]["testing"]["context"] = scope
            r["credential_eligibility"]["production"]["context"] = scope
            elig("testing", "free_access", True,
                 [E("communications-apis/pricing/", 1018, 1020, "Try it free: Start developing now with free credit. No credit card required."),
                  E("vonage-kiro-power", 186, 187, "A Vonage API account is free to create and provides API Key and Secret from Vonage Dashboard.")],
                 "Free developer account creation with free starting credit and no credit card required.")
            elig("testing", "trial_access", True,
                 [E("communications-apis/pricing/", 1018, 1030, "Free credit trial with no credit card required to test Vonage Communications APIs.")],
                 "Cardless free credit trial lets developers test Vonage Communications APIs.")
            elig("testing", "self_serve", True,
                 [E("concepts/authentication", 67, 67, "When you create a Vonage account, an API key and secret are created automatically in the Vonage Dashboard."),
                  E("communications-apis/pricing/", 1018, 1020, "Self-serve Try it free / Start coding flow.")],
                 "Self-serve account creation immediately generates API Key/Secret and allows creating Applications/JWT keys.")
            elig("production", "paid_required", True,
                 [E("communications-apis/pricing/", 922, 998, "All Vonage API pricing is usage-based pay-as-you-go (e.g., SMS $0.00860/msg, Messages $0.00129/msg, Voice $0.01538/min, Verify $0.06084/success, Video $0.0041/min).")],
                 "Production traffic beyond initial free trial credit is billed pay-as-you-go by usage.")
            elig("production", "self_serve", True,
                 [E("communications-apis/pricing/", 990, 1001, "Pay-as-you-go usage model with no fixed subscription fee; Reports API offers automated scaling discounts with no negotiation necessary.")],
                 "Standard pay-as-you-go production usage is self-serve (custom/enterprise volume pricing available via sales).")
            elig("production", "contact_sales_required", False,
                 [E("communications-apis/pricing/", 990, 1001, "Pay-as-you-go usage pricing with automated scaling discounts and no negotiation necessary.")],
                 "Contacting sales is optional for custom pricing, not required for standard pay-as-you-go API usage.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [E("developer.vonage.com/en/api", 26, 111, "HTTP REST APIs across Messaging, Voice, Network, Core Services, Numbers, Account, Verify, and Compliance."),
                                                   E("concepts/authentication", 71, 77, "HTTP Authorization header requests.")]),
                claim("api.protocol.sdk", "SDK", [E("concepts/authentication", 149, 151, "Vonage server libraries and Vonage Client and Video SDKs.")]),
                claim("api.protocol.cli", "CLI", [E("concepts/authentication", 121, 148, "Vonage CLI (vonage apps create, vonage jwt create, vonage auth set).")]),
            ], "HTTP REST APIs, multi-language server/client/video SDKs, Vonage CLI, and webhooks/NCCO.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", True,
                [E("developer.vonage.com/en/api", 1, 111, "Public API Reference index at developer.vonage.com/en/api."),
                 E("concepts/authentication", 1, 200, "Public authentication guide at developer.vonage.com/en/getting-started/concepts/authentication.")],
            )
            items(r["api_surface"]["resource_groups"], [
                group("messaging_conversations", "Messages API (SMS/MMS/WhatsApp/RCS/Viber), SMS API, Dispatch API, Conversation API, and WhatsApp Provisioning",
                      [E("developer.vonage.com/en/api", 27, 51, "Messages, Dispatch, SMS, External Accounts, WhatsApp Provisioning, Conversation, and Alerts APIs."),
                       E("communications-apis/pricing/", 935, 936, "Messages API supports SMS, MMS, RCS, WhatsApp, and Facebook Messenger.")]),
                group("voice_video_media", "Voice API (with NCCO & Webhooks), Media API, and Video API",
                      [E("developer.vonage.com/en/api", 52, 67, "Voice API, NCCO, Voice Webhooks, Media API, and Conversation API."),
                       E("communications-apis/pricing/", 955, 960, "Video API streaming, recording, broadcasting, and SIP.")]),
                group("verify_network_compliance", "Verify API (2FA), Identity Insights, Device Location Retrieval, Redact API (GDPR), and Audit API",
                      [E("developer.vonage.com/en/api", 68, 72, "Identity Insights and Device Location Retrieval Network APIs."),
                       E("developer.vonage.com/en/api", 99, 111, "Verify API, Redact API, and Audit API.")]),
                group("accounts_numbers_reports", "Application API, Number Management & Pools API, Account API, Pricing API, and Reports API",
                      [E("developer.vonage.com/en/api", 73, 98, "Application, Reports, Number Management, Number Pools, US Number Deactivation, Account, and Pricing APIs.")]),
            ], "Grounded in developer.vonage.com/en/api and vonage.com/communications-apis/pricing/.")
            breadth("broad", ["messaging_conversations", "voice_video_media", "verify_network_compliance", "accounts_numbers_reports"],
                    [E("developer.vonage.com/en/api", 26, 111, "Spans Messaging, Voice/Media, Network Features, Core Services/Reports, Numbers, Account, Verify, and Security/Compliance.")],
                    "Full CPaaS suite across omnichannel messaging, voice/video, 2FA verification, carrier network insights, numbers, and compliance.")
            set_mcp_entries([
                ("official_api_bindings", "official", "Vonage API MCP Server (@vonage/vonage-mcp-server-api-bindings)",
                 [E("vonage-mcp-server-api-bindings", 173, 211, "Official Vonage API MCP server exposing live tools for balance, applications, number search/linking, reports, SMS, WhatsApp/RCS (with SMS failover), outbound voice, and charts."),
                  E("vonage-mcp-server-api-bindings", 250, 267, "Runs locally via stdio (npx -y @vonage/vonage-mcp-server-api-bindings) using VONAGE_API_KEY, VONAGE_API_SECRET, VONAGE_APPLICATION_ID, and VONAGE_PRIVATE_KEY64."),
                  E("vonage-kiro-power", 176, 182, "Official Vonage/vonage-kiro-power documents vonage-api and vonage-docs MCP servers.")],
                 "vonage-mcp-server-api-bindings",
                 "Callable official local stdio MCP server (@vonage/vonage-mcp-server-api-bindings) exposing live Vonage account, number management, reports, SMS, WhatsApp, RCS, and outbound voice tools.",
                 None, "https://github.com/Vonage-Community/vonage-mcp-server-api-bindings"),
                ("official_docs", "official", "Vonage Docs MCP Server (via Vonage/vonage-kiro-power)",
                 [E("vonage-kiro-power", 176, 182, "Official Vonage CPaaS Power bundles vonage-docs MCP server for Vonage developer documentation, SDK references, and code examples."),
                  E("vonage-kiro-power", 280, 282, "Vonage Docs MCP Server provides documentation lookups, code examples, SDK references, and concept explanations.")],
                 "vonage-kiro-power",
                 "Callable official documentation MCP server (vonage-docs, bundled in github.com/Vonage/vonage-kiro-power) providing Vonage developer docs, SDK references, and code examples.",
                 None, "https://github.com/Vonage/vonage-kiro-power"),
            ], [E("vonage-mcp-server-api-bindings", 173, 175, "Official Vonage API MCP server repository."),
                E("vonage-kiro-power", 176, 182, "Official Vonage Kiro Power referencing both vonage-api and vonage-docs MCP servers.")])
            buildability(
                "build_now",
                "Build a Vonage SMS/WhatsApp/RCS/Voice/Verify agent toolkit via REST APIs or @vonage/vonage-mcp-server-api-bindings.",
                ["Production traffic beyond free credit is pay-as-you-go; messaging/voice apps require RSA private-key JWT minting (VONAGE_PRIVATE_KEY64) and purchased virtual numbers.",
                 "Vonage notes its Messages API is labeled Beta on the captured API index page (expect changes; SMS API is stable)."],
                ["Create a free cardless Vonage developer account to obtain API Key/Secret and free credit.",
                 "Create a Vonage Application + RSA private key (via Dashboard or Vonage CLI) and integrate via REST APIs or npx -y @vonage/vonage-mcp-server-api-bindings."],
                ["identity", "auth.basic_api_key", "auth.jwt_application", "testing.free_access", "testing.self_serve", "production.paid_required", "production.self_serve", "api.protocol.rest", "api.breadth", "mcp"],
                [E("concepts/authentication", 66, 148, "API Key/Secret Basic auth and RS256 Application JWT auth."),
                 E("communications-apis/pricing/", 997, 1001, "Pay-as-you-go usage pricing model."),
                 E("communications-apis/pricing/", 1018, 1020, "Cardless free credit signup."),
                 E("developer.vonage.com/en/api", 28, 36, "Messages API (Beta) and stable SMS API."),
                 E("vonage-mcp-server-api-bindings", 173, 267, "Official @vonage/vonage-mcp-server-api-bindings MCP server.")],
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
    build("task09-capture-004", Path(__file__).parent / "extracted-records-003.json")
