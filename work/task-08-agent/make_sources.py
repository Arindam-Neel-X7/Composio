"""Generate initial primary-source list for Task 08 (Support and Helpdesk, IDs 11-20)."""
import json
from pathlib import Path

ATTRIBUTION_BY = "task08-research-agent-gemini"

SCOPES = {
    11: "Zendesk Support/Suite REST APIs, OAuth 2.0/API token auth, trial/sandbox/paid plans, and MCP client/server ecosystem",
    12: "Intercom REST API, OAuth 2.0/Access Token auth, developer workspace/trial/paid plans, and official hosted MCP server",
    13: "Freshdesk REST API v2 and official MCP; verified agents and FDK apps; trial/free testing versus licensed production tenants; plan-specific capabilities not generalized",
    14: "Front Core REST API, API token/OAuth 2.0 auth, developer/trial/paid plans, and official hosted MCP server",
    15: "Pylon REST API, Bearer API token/OAuth auth, paid plans, and official hosted MCP server",
    16: "LiveAgent REST API v3, API key/OAuth auth, trial/paid plans, and built-in MCP server",
    17: "Plain GraphQL API, Machine User API key/OAuth auth, trial/paid plans, and official hosted MCP server",
    18: "Help Scout Mailbox API v2 and Docs API v1, OAuth 2.0/API key auth, free/paid plans, and official hosted MCP server",
    19: "Gorgias REST API, HTTP Basic API key/OAuth 2.0 auth, trial/paid plans, and MCP ecosystem",
    20: "Gladly REST API and Lookup API, HTTP Basic API token auth, sandbox/enterprise plans, and bounded MCP discovery",
}


def src(app_id, url, kind, envs, basis="Vendor-controlled official documentation or product page"):
    return {
        "app_id": app_id,
        "url": url,
        "kind": kind,
        "scope": SCOPES[app_id],
        "environments": envs,
        "attribution_basis": basis,
        "attribution_by": ATTRIBUTION_BY,
    }


SOURCES = [
    # 11. Zendesk
    src(11, "https://developer.zendesk.com/api-reference/introduction/security-and-auth/", "primary_docs", ["testing", "production"]),
    src(11, "https://developer.zendesk.com/api-reference/ticketing/introduction/", "primary_docs", ["testing", "production"]),
    src(11, "https://developer.zendesk.com/documentation/ticketing/getting-started/zendesk-api-quick-start/", "primary_docs", ["testing", "production"]),
    src(11, "https://www.zendesk.com/pricing/", "official_product_page", ["testing", "production"]),

    # 12. Intercom
    src(12, "https://developers.intercom.com/docs", "primary_docs", ["testing", "production"]),
    src(12, "https://developers.intercom.com/docs/build-an-integration/learn-more/authentication", "primary_docs", ["testing", "production"]),
    src(12, "https://developers.intercom.com/docs/guides/mcp", "primary_docs", ["testing", "production"]),
    src(12, "https://www.intercom.com/pricing", "official_product_page", ["testing", "production"]),

    # 13. Freshdesk (pilot-verified URLs + full API ref with 10MB cap + pricing)
    src(13, "https://developers.freshdesk.com/api/", "primary_docs", ["testing", "production"]),
    src(13, "https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/rest-apis/", "primary_docs", ["testing", "production"]),
    src(13, "https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/oauth-implementation-in-apps/", "primary_docs", ["testing", "production"]),
    src(13, "https://support.freshdesk.com/support/solutions/articles/215517-how-to-find-your-api-key", "primary_docs", ["testing", "production"]),
    src(13, "https://support.freshdesk.com/support/solutions/articles/50000011778", "primary_docs", ["testing", "production"]),
    src(13, "https://support.freshdesk.com/support/solutions/articles/50000012670", "primary_docs", ["production"]),
    src(13, "https://www.freshworks.com/freshdesk/pricing/", "official_product_page", ["testing", "production"]),

    # 14. Front
    src(14, "https://dev.frontapp.com/llms.txt", "primary_docs", []),
    src(14, "https://dev.frontapp.com/reference/introduction", "primary_docs", ["testing", "production"]),
    src(14, "https://dev.frontapp.com/docs/core-api-authentication", "primary_docs", ["testing", "production"]),
    src(14, "https://dev.frontapp.com/docs/oauth", "primary_docs", ["testing", "production"]),
    src(14, "https://front.com/pricing", "official_product_page", ["testing", "production"]),

    # 15. Pylon
    src(15, "https://docs.usepylon.com/llms.txt", "primary_docs", []),
    src(15, "https://docs.usepylon.com/pylon-docs/developer/api", "primary_docs", ["testing", "production"]),
    src(15, "https://usepylon.com/pricing", "official_product_page", ["testing", "production"]),

    # 16. LiveAgent
    src(16, "https://www.liveagent.com/api/", "official_product_page", ["testing", "production"]),
    src(16, "https://support.liveagent.com/061754-Complete-API-reference", "primary_docs", ["testing", "production"]),
    src(16, "https://www.liveagent.com/pricing/", "official_product_page", ["testing", "production"]),

    # 17. Plain
    src(17, "https://www.plain.com/docs/llms.txt", "primary_docs", []),
    src(17, "https://www.plain.com/docs/api-reference/overview", "primary_docs", ["testing", "production"]),
    src(17, "https://www.plain.com/docs/api-reference/authentication", "primary_docs", ["testing", "production"]),
    src(17, "https://www.plain.com/pricing", "official_product_page", ["testing", "production"]),

    # 18. Help Scout
    src(18, "https://developer.helpscout.com/mailbox-api/", "primary_docs", ["testing", "production"]),
    src(18, "https://developer.helpscout.com/mailbox-api/overview/authentication/", "primary_docs", ["testing", "production"]),
    src(18, "https://developer.helpscout.com/docs-api/", "primary_docs", ["testing", "production"]),
    src(18, "https://www.helpscout.com/pricing/", "official_product_page", ["testing", "production"]),

    # 19. Gorgias
    src(19, "https://developers.gorgias.com/llms.txt", "primary_docs", []),
    src(19, "https://developers.gorgias.com/reference/introduction", "primary_docs", ["testing", "production"]),
    src(19, "https://developers.gorgias.com/reference/authentication", "primary_docs", ["testing", "production"]),
    src(19, "https://www.gorgias.com/pricing", "official_product_page", ["testing", "production"]),

    # 20. Gladly
    src(20, "https://developer.gladly.com/", "primary_docs", ["testing", "production"]),
    src(20, "https://developer.gladly.com/rest/", "primary_docs", ["testing", "production"]),
    src(20, "https://www.gladly.com/pricing/", "official_product_page", ["testing", "production"]),
]

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-001.json"
    out.write_text(json.dumps({"sources": SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(SOURCES)} sources to {out}")
