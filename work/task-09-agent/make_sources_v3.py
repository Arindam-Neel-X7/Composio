"""Generate final supplemental primary-source list for Task 09 (task09-capture-004)."""
import json
from pathlib import Path
from make_sources_v2 import ALL, src

MORE = [
    src(28, "https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/app-review.md", "primary_docs", ["production"]),
    src(28, "https://github.com/tkhattar14/whatsapp-business-mcp", "community_repository", ["testing", "production"], "Community-authored GitHub repository for WhatsApp Business Cloud API MCP"),
    src(29, "https://developer.aircall.io/docs/aircall-ai/llms.txt", "primary_docs", []),
]

FINAL = ALL + MORE

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-003.json"
    out.write_text(json.dumps({"sources": FINAL}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(FINAL)} sources to {out}")
