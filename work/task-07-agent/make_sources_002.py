"""Generate expanded primary-source list (v2) for Task 07 (IDs 1-10)."""
import json
from pathlib import Path
from make_sources import SCOPES, SOURCES, src

EXTRA_SOURCES = [
    # 1. Salesforce (additional primary sources since developer.salesforce.com returned 403)
    src(1, "https://www.salesforce.com/crm/pricing/", "official_product_page", ["testing", "production"]),
    src(1, "https://trailhead.salesforce.com/content/learn/modules/api_basics/api_basics_rest", "primary_docs", ["testing", "production"]),
    src(1, "https://github.com/forcedotcom/postman-salesforce-apis", "official_repository", ["testing", "production"], "Official Salesforce (forcedotcom) GitHub repository for Salesforce APIs"),
    src(1, "https://www.salesforce.com/form/developer-signup/", "official_product_page", ["testing"]),
    src(1, "https://help.salesforce.com/s/articleView?id=platform.integrate_what_is_api.htm&type=5", "primary_docs", ["testing", "production"]),

    # 2. HubSpot (current OAuth doc)
    src(2, "https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/oauth/working-with-oauth", "primary_docs", ["testing", "production"]),

    # 3. Pipedrive (exact .md docs from llms.txt + MCP)
    src(3, "https://pipedrive.readme.io/docs/developer-sandbox-account.md", "primary_docs", ["testing"]),
    src(3, "https://pipedrive.readme.io/docs/marketplace-oauth-api.md", "primary_docs", ["testing", "production"]),
    src(3, "https://pipedrive.readme.io/docs/pipedrive-api-v2.md", "primary_docs", []),
    src(3, "https://pipedrive.readme.io/docs/marketplace-app-approval-process.md", "primary_docs", ["production"]),
    src(3, "https://pipedrive.readme.io/docs/enabling-api-for-company-users.md", "primary_docs", ["production"]),
    src(3, "https://github.com/Wirasm/pipedrive-mcp", "community_repository", ["testing", "production"], "Community GitHub repository implementing a Pipedrive MCP server"),

    # 4. Attio (OAuth + MCP + index)
    src(4, "https://docs.attio.com/llms.txt", "primary_docs", []),
    src(4, "https://docs.attio.com/rest-api/guides/oauth", "primary_docs", ["testing", "production"]),
    src(4, "https://attio.com/help/reference/integrations-automations/attio-mcp", "primary_docs", ["testing", "production"]),

    # 5. Twenty (index)
    src(5, "https://docs.twenty.com/llms.txt", "primary_docs", []),

    # 7. Zoho CRM (additional v8 docs + sandbox)
    src(7, "https://www.zoho.com/crm/developer/docs/api/v8/register-client.html", "primary_docs", ["testing", "production"]),
    src(7, "https://www.zoho.com/crm/developer/docs/api/v8/api-limits.html", "primary_docs", ["testing", "production"]),
    src(7, "https://www.zoho.com/crm/developer/docs/api/v8/scopes.html", "primary_docs", ["testing", "production"]),
    src(7, "https://help.zoho.com/portal/en/kb/crm/developer-space/sandbox/articles/sandbox-overview", "primary_docs", ["testing"]),

    # 8. Close (index, OAuth, MCP)
    src(8, "https://developer.close.com/llms.txt", "primary_docs", []),
    src(8, "https://developer.close.com/mcp/", "primary_docs", ["testing", "production"]),
    src(8, "https://developer.close.com/build-an-integration/create-an-oauth-app/", "primary_docs", ["testing", "production"]),

    # 9. Copper (OAuth + MCP)
    src(9, "https://developer.copper.com/introduction/authentication.html", "primary_docs", ["testing", "production"]),
    src(9, "https://developer.copper.com/oauth/overview.html", "primary_docs", ["testing", "production"]),
    src(9, "https://www.copper.com/blog/copper-mcp-server", "official_product_page", ["testing", "production"]),

    # 10. DealCloud (API auth + MCP docs)
    src(10, "https://api.docs.dealcloud.com/api-reference/getting-started/api-keys", "primary_docs", ["testing", "production"]),
    src(10, "https://api.docs.dealcloud.com/api-reference/getting-started/authorization-token", "primary_docs", ["testing", "production"]),
    src(10, "https://api.docs.dealcloud.com/mcp/getting-started", "primary_docs", ["testing", "production"]),
    src(10, "https://api.docs.dealcloud.com/mcp/authentication", "primary_docs", ["testing", "production"]),
    src(10, "https://api.docs.dealcloud.com/mcp/available-tools", "primary_docs", ["testing", "production"]),
]

# Keep only successful sources from v1 (exclude known 404s so we don't retry dead URLs) + new sources
SKIP_DEAD = {
    "https://pipedrive.readme.io/docs/oauth-authorization",
    "https://developer.close.com/topics/oauth/",
    "https://www.hubspot.com/pricing/crm",
}
ALL_SOURCES = [s for s in SOURCES if s["url"] not in SKIP_DEAD] + EXTRA_SOURCES

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-002.json"
    out.write_text(json.dumps({"sources": ALL_SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(ALL_SOURCES)} sources to {out}")
