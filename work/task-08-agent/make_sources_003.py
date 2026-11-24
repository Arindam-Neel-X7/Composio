"""Generate final primary-source list (sources-003.json) adding Plain .md docs."""
import json
from pathlib import Path
from make_sources_002 import SOURCES as PREV_SOURCES, src

DROP_404_002 = {
    "https://support.zendesk.com/hc/en-us/articles/8244243105178-Using-the-Zendesk-MCP-client-to-access-MCP-tools-in-action-flows-and-advanced-action-flows",
    "https://developers.intercom.com/docs/build-an-integration/getting-started/build-an-app-for-your-workspace",
    "https://www.helpscout.com/blog/mcp-server/",
    "https://developer.gladly.com/lookup/",
    "https://help.gladly.com/docs/create-api-tokens",
    "https://help.gladly.com/docs/what-is-the-sandbox-environment",
}

EXTRA_003 = [
    # 17. Plain exact .md URLs discovered from developer.txt
    src(17, "https://www.plain.com/docs/graphql/introduction.md", "primary_docs", ["testing", "production"]),
    src(17, "https://www.plain.com/docs/graphql/authentication.md", "primary_docs", ["testing", "production"]),
    src(17, "https://www.plain.com/docs/graphql/oauth.md", "primary_docs", ["testing", "production"]),
    src(17, "https://www.plain.com/docs/integrations/mcp-server.md", "primary_docs", ["testing", "production"]),
]

SOURCES = [s for s in PREV_SOURCES if s["url"] not in DROP_404_002] + EXTRA_003

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-003.json"
    out.write_text(json.dumps({"sources": SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(SOURCES)} sources to {out}")
