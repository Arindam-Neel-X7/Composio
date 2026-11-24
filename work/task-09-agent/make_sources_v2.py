"""Generate supplemental primary-source list for Task 09 (task09-capture-003)."""
import json
from pathlib import Path
from make_sources import SOURCES, src

EXTRA = [
    # 24. Lark (official GitHub SDKs since open.larksuite.com is a 1-line JS shell)
    src(24, "https://github.com/larksuite/oapi-sdk-python", "official_repository", ["testing", "production"], "Official Larksuite Python OpenAPI SDK repository"),
    src(24, "https://github.com/larksuite/node-sdk", "official_repository", ["testing", "production"], "Official Larksuite Node.js OpenAPI SDK repository"),

    # 25. Pumble (official SDK repo and landing/help pages)
    src(25, "https://github.com/CAKE-com/pumble-node-sdk", "official_repository", ["testing", "production"], "Official CAKE.com Pumble Node SDK repository"),
    src(25, "https://pumble.com/", "official_product_page", ["testing", "production"]),
    src(25, "https://pumble.com/help/", "primary_docs", ["testing", "production"]),

    # 28. WhatsApp Business (llms.txt index + access tokens doc)
    src(28, "https://developers.facebook.com/documentation/business-messaging/whatsapp/llms.txt", "primary_docs", []),
    src(28, "https://developers.facebook.com/documentation/business-messaging/whatsapp/access-tokens", "primary_docs", ["testing", "production"]),

    # 29. Aircall (llms.txt index)
    src(29, "https://developer.aircall.io/llms.txt", "primary_docs", []),

    # 30. Vonage (official Kiro power / docs MCP reference)
    src(30, "https://github.com/Vonage/vonage-kiro-power", "official_repository", ["testing", "production"], "Official Vonage GitHub repository documenting Vonage MCP servers"),
]

# Keep only URLs that weren't known 404s from 002, plus EXTRA
SKIP_404 = {
    "https://www.zoho.com/cliq/help/restapi/v2/oauth.html",
    "https://github.com/CAKE-com/pumble-sdk",
    "https://pumble.com/pricing/",
}
ALL = [s for s in SOURCES if s["url"] not in SKIP_404] + EXTRA

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-002.json"
    out.write_text(json.dumps({"sources": ALL}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(ALL)} sources to {out}")
