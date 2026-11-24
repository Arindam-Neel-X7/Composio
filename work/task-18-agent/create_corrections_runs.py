"""
Create the 10 immutable child correction runs for Task 18 Phase A.
Applies targeted error corrections for all 50 unsupported statements identified in Task 17 human baseline.
Enforces pipeline validation, contract compliance, and immutable child run creation.
"""

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from research_pipeline import create_run, read_json, require, run_path, verify_seal

TASK_RUNS = {
    7: "task07-first-pass-003",
    8: "task08-first-pass-003",
    9: "task09-first-pass-004",
    10: "task10-first-pass-003",
    11: "task11-first-pass-004",
    12: "task12-first-pass-005",
    13: "task13-first-pass-003",
    14: "task14-first-pass-003",
    15: "task15-first-pass-002",
    16: "task16-first-pass-001",
}

STORE = ROOT / "work/research-runs"


def apply_corrections(batch_num: int, records: list) -> tuple[list, str]:
    """Apply targeted corrections to sample apps in batch."""
    records = copy.deepcopy(records)
    rec_by_id = {r["identity"]["id"]: r for r in records}
    reason = "Task 18 Phase A error corrections addressing Task 17 human baseline review findings."

    # Batch 07: Apps 4 & 8
    if batch_num == 7:
        # App 4: Attio
        r4 = rec_by_id[4]
        r4["api_surface"]["breadth"]["rationale"] = (
            "Attio documentation defines four distinct top-level functional domains: (1) Core CRM Objects & Records, "
            "(2) Collaboration & Tasks (Lists, Notes, Tasks, Comments), (3) Interaction Tracking (Activities, Call Recordings), "
            "and (4) Workspace Administration (SCIM 2.0 provisioning, Webhooks). Per evidence rules, multiple distinct "
            "business domains substantiate a broad API surface."
        )
        r4["buildability"]["rationale"] = (
            "Buildability inference is anchored directly to the verified prerequisite chain: free self-serve workspace "
            "access (4.testing.free_access), public JSON REST API v2 (4.api.rest), and official hosted MCP endpoint "
            "https://mcp.attio.com/mcp (4.mcp.hosted_official) with zero vendor gating or partner blockers."
        )

        # App 8: Close
        r8 = rec_by_id[8]
        r8["api_surface"]["breadth"]["rationale"] = (
            "Close documentation defines multiple distinct business domains: (1) Lead & Contact Management, "
            "(2) Multi-channel Communications (Calls, Emails, SMS), (3) Workflow Automation (Sequences), and "
            "(4) Sales Analytics/Reporting. Per evidence rules, multiple distinct business domains substantiate a broad API surface."
        )
        r8["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Close platform documentation: REST API and official "
            "hosted MCP server are fully documented and functional, but require an active Close plan ($49+/seat/mo) or active trial "
            "for API key / OAuth access (8.testing.paid_required, 8.auth.api_key, 8.mcp.hosted_official)."
        )

    # Batch 08: Apps 16 & 19
    elif batch_num == 8:
        # App 16: LiveAgent
        r16 = rec_by_id[16]
        r16["api_surface"]["breadth"]["rationale"] = (
            "LiveAgent API v1 reference focuses on a single core workflow domain: helpdesk ticket/conversation management, "
            "message posting, and department assignments. Per evidence rules, a single focused workflow domain constitutes narrow breadth."
        )
        r16["buildability"]["rationale"] = (
            "Buildability inference is anchored to verified LiveAgent documentation: built-in MCP server support and REST API with "
            "self-serve API key generation on free trial or paid accounts (16.testing.free_access, 16.auth.api_key, 16.mcp.builtin_mcp)."
        )

        # App 19: Gorgias
        r19 = rec_by_id[19]
        r19["api_surface"]["breadth"]["rationale"] = (
            "Gorgias API documentation covers multiple distinct functional domains: (1) Helpdesk Tickets & Messages, "
            "(2) Customer Management, (3) Ecommerce Order/Store Data, and (4) Third-party Integrations/HTTP Webhooks. "
            "Per evidence rules, spanning multiple distinct functional domains substantiates broad breadth."
        )
        r19["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Gorgias documentation: REST API and OAuth 2.0 app registration "
            "are fully documented, but require an active Gorgias paid helpdesk account (19.testing.paid_required, 19.auth.oauth2)."
        )

    # Batch 09: Apps 21 & 27
    elif batch_num == 9:
        # App 21: Slack
        r21 = rec_by_id[21]
        r21["api_surface"]["breadth"]["rationale"] = (
            "Slack Web API spans multiple major distinct business domains: (1) Messaging & Conversations, (2) User & Team Management, "
            "(3) File & Canvas Content, (4) Workspace Search, and (5) Enterprise Administration/SCIM. Per evidence rules, multiple "
            "distinct business domains substantiate broad breadth."
        )
        r21["buildability"]["rationale"] = (
            "Buildability inference is anchored to verified Slack platform documentation: self-serve app registration, free workspace "
            "tier (21.testing.free_access), Bot token authentication (21.auth.oauth2), and extensive Web API methods (21.api.rest)."
        )

        # App 27: Telegram
        r27 = rec_by_id[27]
        r27["api_surface"]["breadth"]["rationale"] = (
            "Telegram Bot API encompasses multiple distinct domains: (1) Chat & Direct Messaging, (2) Inline Queries & Payments, "
            "(3) Webhook Event Delivery, (4) Group & Channel Administration, and (5) Media/Sticker Processing. Per evidence rules, "
            "multiple distinct business domains substantiate broad breadth."
        )
        r27["buildability"]["rationale"] = (
            "Buildability inference is anchored to verified Telegram Bot platform documentation: instant self-serve bot creation via "
            "BotFather with zero approval gating or fees (27.testing.free_access, 27.testing.self_serve, 27.auth.bearer_token)."
        )

    # Batch 10: Apps 31 & 40
    elif batch_num == 10:
        # App 31: Google Ads
        r31 = rec_by_id[31]
        # 31.testing.vendor_approval_required was asserted as false in error (silence mistaken for negative proof)
        r31["credential_eligibility"]["testing"]["vendor_approval_required"]["status"] = "unknown"
        r31["credential_eligibility"]["testing"]["vendor_approval_required"]["value"] = None
        r31["credential_eligibility"]["testing"]["vendor_approval_required"]["rationale"] = (
            "Research correction: In first-pass research, vendor approval was asserted as false based on automatic test account enablement. "
            "However, primary documentation does not explicitly state that vendor approval is not required, and under evidence rules silence is unknown. "
            "Relabeled from observed (false) to unknown."
        )
        r31["api_surface"]["breadth"]["rationale"] = (
            "Google Ads API documentation covers multiple distinct advertising business domains: (1) Account Hierarchy & Budgets, "
            "(2) Campaigns & AdGroups, (3) GAQL Reporting & Metrics, (4) Conversion Tracking, and (5) Bidding Strategies. "
            "Per evidence rules, multiple distinct advertising business domains substantiate broad breadth."
        )
        r31["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Google Ads documentation: Test access against test accounts "
            "is immediately available upon enabling the API, but production access requires Explorer, Basic, or Standard access level approval "
            "(31.testing.free_access, 31.production.vendor_approval_required, 31.api.rest, 31.mcp.official_mcp)."
        )

        # App 40: SendGrid
        r40 = rec_by_id[40]
        r40["api_surface"]["breadth"]["rationale"] = (
            "Twilio SendGrid REST API spans multiple distinct functional domains: (1) Transactional Mail Send (v3), (2) Marketing "
            "Campaigns & Automation, (3) Contact & List Management, (4) Subuser Provisioning, and (5) Event Webhooks & Statistics. "
            "Per evidence rules, multiple distinct domains substantiate broad breadth."
        )
        r40["buildability"]["rationale"] = (
            "Buildability inference is anchored to verified SendGrid documentation: Free tier (100 emails/day), self-serve API key "
            "generation with granular scopes, and full public REST API (40.testing.free_access, 40.auth.api_key, 40.api.rest)."
        )

    # Batch 11: Apps 46 & 50
    elif batch_num == 11:
        # App 46: Squarespace
        r46 = rec_by_id[46]
        r46["api_surface"]["breadth"]["rationale"] = (
            "Squarespace Commerce API documentation covers multiple distinct ecommerce domains: (1) Orders & Fulfillment, "
            "(2) Inventory Management, (3) Products, (4) Transactions & Finances, and (5) Webhook Subscriptions. "
            "Per evidence rules, multiple distinct commercial domains substantiate broad breadth."
        )
        r46["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Squarespace documentation: Commerce APIs are fully functional "
            "via API keys or OAuth, but require an active Squarespace Commerce plan (Commerce Advanced or Core) (46.testing.paid_required, 46.auth.api_key)."
        )

        # App 50: fanbasis
        r50 = rec_by_id[50]
        r50["buildability"]["rationale"] = (
            "Outreach required buildability inference is anchored to verified FanBasis / Commas documentation: developer API keys and "
            "beta MCP server access require contacting Commas sales or requesting developer access (50.identity, 50.api.protocol.sdk, 50.mcp.commas_mcp_beta)."
        )

    # Batch 12: Apps 52 & 60
    elif batch_num == 12:
        # App 52: SE Ranking
        r52 = rec_by_id[52]
        r52["api_surface"]["breadth"]["rationale"] = (
            "SE Ranking API documentation spans multiple related SEO data groups: (1) Keyword Rank Tracking, (2) Competitor & Organic Search Data, "
            "and (3) Backlink/Local Marketing Analysis. Per evidence rules, multiple related workflow groups substantiate moderate breadth."
        )
        r52["buildability"]["rationale"] = (
            "Buildability inference is anchored to verified SE Ranking documentation: REST API keys available on paid plans (or trial) "
            "with clear JSON endpoints for SEO data retrieval (52.testing.trial_access, 52.auth.api_key, 52.api.rest)."
        )

        # App 60: Clay
        r60 = rec_by_id[60]
        r60["api_surface"]["breadth"]["rationale"] = (
            "Clay API documentation covers multiple related enrichment groups: (1) Table & Record Management, (2) People/Company Enrichment "
            "Actions, and (3) Webhook Integration Sources. Per evidence rules, multiple related groups substantiate moderate breadth."
        )
        r60["buildability"]["rationale"] = (
            "Buildability inference is anchored to verified Clay documentation: self-serve API keys available on Pro/Enterprise accounts "
            "or trial for automating table enrichment runs (60.testing.trial_access, 60.auth.api_key, 60.api.rest)."
        )

    # Batch 13: Apps 64 & 65
    elif batch_num == 64 or batch_num == 13:
        # App 64: Cloudflare
        r64 = rec_by_id[64]
        r64["api_surface"]["breadth"]["rationale"] = (
            "Cloudflare v4 REST API spans multiple distinct infrastructure domains: (1) Authoritative DNS & Domains, (2) Serverless "
            "Compute (Workers/Pages), (3) Storage (KV/R2/D1), (4) Security/WAF Rules, and (5) Zero Trust Access. "
            "Per evidence rules, multiple distinct infrastructure domains substantiate broad breadth."
        )
        r64["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Cloudflare documentation: Free tier accounts support scoped API tokens "
            "for managing DNS and Workers, with enterprise features gated behind plan upgrades (64.testing.free_access, 64.auth.bearer_token, 64.api.rest)."
        )

        # App 65: Supabase
        r65 = rec_by_id[65]
        r65["api_surface"]["breadth"]["rationale"] = (
            "Supabase API covers multiple related backend services: (1) PostgreSQL Database (PostgREST), (2) GoTrue Auth, (3) Storage, "
            "and (4) Edge Functions. Per evidence rules, multiple related service modules substantiate moderate breadth."
        )
        r65["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Supabase documentation: Free plan (up to 2 active projects), "
            "instant project API keys (anon / service_role), and community MCP server (65.testing.free_access, 65.auth.api_key, 65.api.rest)."
        )

    # Batch 14: Apps 76 & 77
    elif batch_num == 14:
        # App 76: Monday.com
        r76 = rec_by_id[76]
        r76["api_surface"]["breadth"]["rationale"] = (
            "Monday.com GraphQL API covers multiple related work management domains: (1) Boards & Workspaces, (2) Items & Column Values, "
            "(3) Updates/Comments, and (4) Users & Teams. Per evidence rules, multiple related workflow entities substantiate moderate breadth."
        )
        r76["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Monday.com documentation: GraphQL API supports personal API tokens "
            "and OAuth 2.0 apps, gated by workspace permission scopes and plan tiers (76.testing.free_access, 76.auth.api_key, 76.api.graphql)."
        )

        # App 77: ClickUp
        r77 = rec_by_id[77]
        r77["api_surface"]["breadth"]["rationale"] = (
            "ClickUp REST API v2 covers multiple related task management domains: (1) Workspaces, Spaces, and Folders, (2) Lists & Tasks, "
            "(3) Time Tracking, and (4) Comments & Attachments. Per evidence rules, multiple related workflow modules substantiate moderate breadth."
        )
        r77["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified ClickUp documentation: Free Forever plan includes API access with "
            "personal API keys or OAuth 2.0, with team-level rate limits (77.testing.free_access, 77.auth.api_key, 77.api.rest)."
        )

    # Batch 15: Apps 83 & 84
    elif batch_num == 15:
        # App 83: Binance
        r83 = rec_by_id[83]
        # Relabel unsupported negative/absence claims to unknown
        for field in ["vendor_approval_required", "partner_approval_required", "contact_sales_required"]:
            r83["credential_eligibility"]["testing"][field]["status"] = "unknown"
            r83["credential_eligibility"]["testing"][field]["value"] = None
            r83["credential_eligibility"]["testing"][field]["rationale"] = (
                f"Research correction: Absence of {field.replace('_', ' ')} was asserted as false based on self-serve Spot Testnet key generation. "
                "Under evidence rules, absence of gating requires explicit vendor proof; silence is unknown. Relabeled from observed (false) to unknown."
            )
        r83["credential_eligibility"]["production"]["sandbox_access"]["status"] = "unknown"
        r83["credential_eligibility"]["production"]["sandbox_access"]["value"] = None
        r83["credential_eligibility"]["production"]["sandbox_access"]["rationale"] = (
            "Research correction: Host separation between api.binance.com and testnet.binance.vision does not conclusively prove "
            "absence of sandbox access for production. Relabeled from observed (false) to unknown."
        )

        r83["api_surface"]["breadth"]["rationale"] = (
            "Binance Spot API covers multiple distinct financial domains: (1) Market Data & Order Book Feeds, (2) Spot Order Execution, "
            "(3) Account Balance & Trade History, and (4) WebSocket Real-time Streams. Per evidence rules, multiple distinct domains substantiate broad breadth."
        )
        r83["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Binance documentation: Public market data REST/WebSocket feeds are "
            "open without authentication, but signed production trading depends on regional compliance and account verification (83.api.rest, 83.mcp.community_mcp)."
        )

    # Batch 16: Apps 97 & 98
    elif batch_num == 16:
        # App 97: Higgsfield
        r97 = rec_by_id[97]
        r97["api_surface"]["breadth"]["rationale"] = (
            "Higgsfield API reference focuses on related media generation workflows: (1) Image/Video Generation Task Submissions, "
            "(2) Task Status & Asset Polling, and (3) Model Configurations. Per evidence rules, multiple related workflow endpoints substantiate moderate breadth."
        )
        r97["buildability"]["rationale"] = (
            "Conditional buildability inference is anchored to verified Higgsfield documentation: REST API and CLI require paid API credits "
            "($5+ credit pack) and API key authentication (97.testing.paid_required, 97.auth.api_key, 97.api.rest)."
        )

        # App 98: Mermaid CLI
        r98 = rec_by_id[98]
        # Mermaid CLI is an offline open-source CLI with no credentials. Relabel credential gating conditions to not_applicable
        for env in ["testing", "production"]:
            for cond in ["admin_approval_required", "vendor_approval_required", "partner_approval_required", "contact_sales_required"]:
                claim = r98["credential_eligibility"][env][cond]
                claim["status"] = "not_applicable"
                claim["value"] = None
                claim["rationale"] = (
                    "Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. "
                    "Credential gating conditions do not apply to local software that executes without accounts or API keys. "
                    "Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software."
                )

        r98["api_surface"]["breadth"]["rationale"] = (
            "Mermaid CLI (@mermaid-js/mermaid-cli) is focused strictly on a single operational workflow: converting .mmd definitions "
            "and Markdown mermaid blocks into rendered SVG, PNG, or PDF files. Per evidence rules, a single focused workflow constitutes narrow breadth."
        )
        r98["buildability"]["rationale"] = (
            "Buildability inference is anchored to verified Mermaid CLI repository documentation: open-source MIT license, local npm/npx "
            "execution (mmdc), Node.js run() programmatic API, zero cloud credentials, and zero vendor gating (98.identity, 98.auth.none, 98.api.cli)."
        )

    return records, reason


def main():
    print("=" * 60)
    print("TASK 18: CREATING IMMUTABLE CHILD CORRECTION RUNS")
    print("=" * 60)

    created_runs = {}

    for b, parent_run_id in sorted(TASK_RUNS.items()):
        child_run_id = f"task18-corrections-{b:02d}"
        parent_dir = STORE / parent_run_id
        require(parent_dir.exists(), f"Parent run {parent_run_id} missing")

        # Read parent records
        parent_records = read_json(parent_dir / "records.json")
        corrected_records, reason = apply_corrections(b, parent_records)

        # Check existing child run
        child_dir = STORE / child_run_id
        if child_dir.exists():
            print(f"Child run {child_run_id} already exists; verifying seal...")
            manifest = verify_seal(child_dir)
            created_runs[b] = child_run_id
            print(f"  [OK] Sealed child run: {child_run_id}")
            continue

        print(f"\nCreating immutable child run {child_run_id} from {parent_run_id}...")
        extraction_payload = {"records": corrected_records}

        created_dir = create_run(
            store=STORE,
            run_id=child_run_id,
            parent_id=parent_run_id,
            extraction=extraction_payload,
            reason=reason,
            extractor_label="task-18-error-corrections-agent",
        )
        created_runs[b] = child_run_id
        print(f"  [OK] Successfully created and sealed {child_run_id} at {created_dir}")

    # Summary
    print("\n" + "=" * 60)
    print("ALL 10 CHILD RUNS CREATED AND SEALED")
    print("=" * 60)
    for b, rid in created_runs.items():
        print(f"Batch {b:02d}: {rid} (parent: {TASK_RUNS[b]})")


if __name__ == "__main__":
    main()
