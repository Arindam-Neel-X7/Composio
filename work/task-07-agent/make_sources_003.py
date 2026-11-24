"""Generate v3 primary-source list adding exact Attio/Close .md URLs and DealCloud/Zoho pages."""
import json
from pathlib import Path
from make_sources_002 import ALL_SOURCES, src

EXTRA_V3 = [
    # 4. Attio (exact .md URLs from docs.attio.com/llms.txt)
    src(4, "https://docs.attio.com/rest-api/tutorials/connect-an-app-through-oauth.md", "primary_docs", ["testing", "production"]),
    src(4, "https://docs.attio.com/mcp/overview.md", "primary_docs", ["testing", "production"]),

    # 8. Close (exact .md URLs from developer.close.com/llms.txt)
    src(8, "https://developer.close.com/api/overview/oauth-authentication.md", "primary_docs", ["testing", "production"]),
    src(8, "https://developer.close.com/integrations/create-an-oauth-app.md", "primary_docs", ["testing", "production"]),
    src(8, "https://developer.close.com/mcp/tools.md", "primary_docs", ["testing", "production"]),

    # 10. DealCloud (REST auth pages)
    src(10, "https://api.docs.dealcloud.com/getting-started/api-keys", "primary_docs", ["testing", "production"]),
    src(10, "https://api.docs.dealcloud.com/getting-started/authorization-token", "primary_docs", ["testing", "production"]),
]

SKIP_DEAD_V2 = {
    "https://docs.attio.com/rest-api/guides/oauth",
    "https://attio.com/help/reference/integrations-automations/attio-mcp",
    "https://developer.close.com/build-an-integration/create-an-oauth-app/",
    "https://developer.copper.com/oauth/overview.html",
    "https://www.copper.com/blog/copper-mcp-server",
    "https://api.docs.dealcloud.com/api-reference/getting-started/api-keys",
    "https://api.docs.dealcloud.com/api-reference/getting-started/authorization-token",
    "https://api.docs.dealcloud.com/mcp/available-tools",
    "https://help.zoho.com/portal/en/kb/crm/developer-space/sandbox/articles/sandbox-overview",
}

V3_SOURCES = [s for s in ALL_SOURCES if s["url"] not in SKIP_DEAD_V2] + EXTRA_V3

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-003.json"
    out.write_text(json.dumps({"sources": V3_SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(V3_SOURCES)} sources to {out}")
