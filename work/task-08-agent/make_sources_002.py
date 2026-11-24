"""Generate follow-up primary-source list (sources-002.json) for Task 08."""
import json
from pathlib import Path
from make_sources import SOURCES as BASE_SOURCES, src

EXTRA = [
    # 11. Zendesk
    src(11, "https://support.zendesk.com/hc/en-us/articles/8244243105178-Using-the-Zendesk-MCP-client-to-access-MCP-tools-in-action-flows-and-advanced-action-flows", "primary_docs", ["testing", "production"]),
    src(11, "https://support.zendesk.com/hc/en-us/articles/4408828617370-Testing-changes-in-your-sandbox", "primary_docs", ["testing"]),
    src(11, "https://github.com/reminia/zendesk-mcp-server", "community_repository", ["testing", "production"], "Third-party community GitHub repository implementing a Zendesk MCP server"),

    # 12. Intercom
    src(12, "https://developers.intercom.com/docs/build-an-integration/getting-started/build-an-app-for-your-workspace", "primary_docs", ["testing", "production"]),
    src(12, "https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/setting-up-oauth", "primary_docs", ["testing", "production"]),

    # 14. Front
    src(14, "https://dev.frontapp.com/docs/authentication.md", "primary_docs", ["testing", "production"]),
    src(14, "https://dev.frontapp.com/docs/create-and-revoke-api-tokens.md", "primary_docs", ["testing", "production"]),
    src(14, "https://dev.frontapp.com/docs/mcp-server.md", "primary_docs", ["testing", "production"]),
    src(14, "https://dev.frontapp.com/docs/admin-mcp-server.md", "primary_docs", ["testing", "production"]),

    # 15. Pylon
    src(15, "https://docs.usepylon.com/pylon-docs/developer/api/authentication.md", "primary_docs", ["testing", "production"]),
    src(15, "https://docs.usepylon.com/pylon-docs/integrations/pylon-mcp.md", "primary_docs", ["testing", "production"]),
    src(15, "https://docs.usepylon.com/pylon-docs/developer/api/api-reference.md", "primary_docs", ["testing", "production"]),

    # 16. LiveAgent
    src(16, "https://support.liveagent.com/647358-MCP-Integration-for-Agents", "primary_docs", ["testing", "production"]),

    # 17. Plain
    src(17, "https://www.plain.com/docs/_llms/developer.txt", "primary_docs", []),

    # 18. Help Scout
    src(18, "https://developer.helpscout.com/", "primary_docs", ["testing", "production"]),
    src(18, "https://www.helpscout.com/blog/mcp-server/", "official_product_page", ["testing", "production"]),

    # 19. Gorgias
    src(19, "https://developers.gorgias.com/docs/overview.md", "primary_docs", ["testing", "production"]),
    src(19, "https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias.md", "primary_docs", ["testing", "production"]),
    src(19, "https://developers.gorgias.com/docs/5-submit-app-for-review.md", "primary_docs", ["testing", "production"]),
    src(19, "https://github.com/mattcoatsworth/Gorgias-MCP-Server", "community_repository", ["testing", "production"], "Third-party community GitHub repository implementing a Gorgias MCP server"),

    # 20. Gladly
    src(20, "https://developer.gladly.com/lookup/", "primary_docs", ["testing", "production"]),
    src(20, "https://help.gladly.com/docs/create-api-tokens", "primary_docs", ["testing", "production"]),
    src(20, "https://help.gladly.com/docs/what-is-the-sandbox-environment", "primary_docs", ["testing"]),
]

# Keep only URLs that succeeded in capture-002 plus new EXTRA URLs
DROP_404 = {
    "https://dev.frontapp.com/docs/core-api-authentication",
    "https://www.liveagent.com/api/",
    "https://www.plain.com/docs/api-reference/overview",
    "https://www.plain.com/docs/api-reference/authentication",
}

SOURCES = [s for s in BASE_SOURCES if s["url"] not in DROP_404] + EXTRA

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-002.json"
    out.write_text(json.dumps({"sources": SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(SOURCES)} sources to {out}")
