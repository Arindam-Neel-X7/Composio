"""Generate initial primary-source list for Task 07 (CRM and Sales, IDs 1-10)."""
import json
from pathlib import Path

ATTRIBUTION_BY = "task07-research-agent-gemini"

SCOPES = {
    1: "Salesforce CRM REST API, OAuth 2.0, Developer Edition/Sandbox access, and official Salesforce MCP servers",
    2: "HubSpot CRM APIs and remote CRM MCP; developer testing and authorized production tenants; current and explicitly labeled legacy auth; plan-specific capabilities not generalized",
    3: "Pipedrive CRM REST API (v1/v2), OAuth 2.0/API token auth, developer sandbox, paid plans, and native MCP server",
    4: "Attio CRM REST API v2, OAuth 2.0/access token auth, Free/paid plans, and official hosted MCP server",
    5: "Twenty open-source CRM REST/GraphQL APIs, API key/OAuth auth, self-hosted and cloud plans, and MCP ecosystem",
    6: "Podio REST API, OAuth 2.0/App auth flows, Free/paid plans, and bounded MCP discovery",
    7: "Zoho CRM REST API (v8), OAuth 2.0 auth, Sandbox/Free/paid editions, and official Zoho MCP servers",
    8: "Close CRM REST API, API key/OAuth 2.0 auth, trial/paid plans, and official hosted MCP server",
    9: "Copper CRM Developer REST API, API key/OAuth 2.0 auth, trial/paid plans, and MCP discovery",
    10: "Intapp DealCloud REST API, OAuth 2.0 auth, enterprise licensing/sandbox, and official DealCloud MCP server",
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
    # 1. Salesforce
    src(1, "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm", "primary_docs", []),
    src(1, "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_supported_editions.htm", "primary_docs", ["testing", "production"]),
    src(1, "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_oauth.htm", "primary_docs", ["testing", "production"]),
    src(1, "https://developer.salesforce.com/signup", "official_product_page", ["testing"]),
    src(1, "https://github.com/salesforcecli/mcp", "official_repository", ["testing", "production"], "Official Salesforce CLI GitHub organization repository"),

    # 2. HubSpot (continuing verified Task 04 sources + current OAuth & pricing)
    src(2, "https://developers.hubspot.com/developer-platform-basics", "official_product_page", ["testing", "production"]),
    src(2, "https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/overview", "primary_docs", ["testing", "production"]),
    src(2, "https://developers.hubspot.com/docs/apps/legacy-apps/private-apps/overview", "primary_docs", ["production"]),
    src(2, "https://developers.hubspot.com/docs/api-reference/latest/overview", "primary_docs", []),
    src(2, "https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server", "primary_docs", ["testing", "production"]),
    src(2, "https://www.hubspot.com/pricing/crm", "official_product_page", ["production"]),

    # 3. Pipedrive
    src(3, "https://pipedrive.readme.io/llms.txt", "primary_docs", []),
    src(3, "https://pipedrive.readme.io/docs/core-api-concepts-authentication", "primary_docs", ["testing", "production"]),
    src(3, "https://pipedrive.readme.io/docs/oauth-authorization", "primary_docs", ["testing", "production"]),
    src(3, "https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app", "primary_docs", ["testing", "production"]),
    src(3, "https://www.pipedrive.com/en/pricing", "official_product_page", ["testing", "production"]),

    # 4. Attio
    src(4, "https://docs.attio.com/rest-api/overview", "primary_docs", ["testing", "production"]),
    src(4, "https://docs.attio.com/rest-api/guides/authentication", "primary_docs", ["testing", "production"]),
    src(4, "https://attio.com/pricing", "official_product_page", ["testing", "production"]),

    # 5. Twenty
    src(5, "https://github.com/twentyhq/twenty", "official_repository", ["testing", "production"], "Official Twenty open-source CRM repository"),
    src(5, "https://docs.twenty.com/developers/extend/api", "primary_docs", ["testing", "production"]),
    src(5, "https://twenty.com/pricing", "official_product_page", ["testing", "production"]),
    src(5, "https://github.com/jezweb/twenty-mcp", "community_repository", ["testing", "production"], "Third-party community GitHub repository implementing a Twenty CRM MCP server"),

    # 6. Podio
    src(6, "https://developers.podio.com/", "primary_docs", ["testing", "production"]),
    src(6, "https://developers.podio.com/authentication", "primary_docs", ["testing", "production"]),
    src(6, "https://developers.podio.com/doc", "primary_docs", []),
    src(6, "https://www.podio.com/site/pricing", "official_product_page", ["testing", "production"]),

    # 7. Zoho CRM
    src(7, "https://www.zoho.com/crm/developer/docs/api/v8/", "primary_docs", ["testing", "production"]),
    src(7, "https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html", "primary_docs", ["testing", "production"]),
    src(7, "https://www.zoho.com/crm/pricing.html", "official_product_page", ["testing", "production"]),
    src(7, "https://www.zoho.com/mcp/", "official_product_page", ["testing", "production"]),

    # 8. Close
    src(8, "https://developer.close.com/", "primary_docs", ["testing", "production"]),
    src(8, "https://developer.close.com/topics/authentication/", "primary_docs", ["testing", "production"]),
    src(8, "https://developer.close.com/topics/oauth/", "primary_docs", ["testing", "production"]),
    src(8, "https://www.close.com/pricing", "official_product_page", ["testing", "production"]),

    # 9. Copper
    src(9, "https://developer.copper.com/", "primary_docs", ["testing", "production"]),
    src(9, "https://www.copper.com/pricing", "official_product_page", ["testing", "production"]),

    # 10. DealCloud
    src(10, "https://api.docs.dealcloud.com/", "primary_docs", ["testing", "production"]),
    src(10, "https://www.intapp.com/dealcloud/", "official_product_page", ["production"]),
]

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-001.json"
    out.write_text(json.dumps({"sources": SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(SOURCES)} sources to {out}")
