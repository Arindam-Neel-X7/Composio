"""Generate initial primary-source list for Task 09 (Communications and Messaging, IDs 21-30)."""
import json
from pathlib import Path

ATTRIBUTION_BY = "task09-research-agent-gemini"

SCOPES = {
    21: "Slack Web API, OAuth 2.0/bot and user token auth, free/paid workspace plans, and official hosted MCP server",
    22: "Twilio REST APIs, HTTP Basic Account SID/Auth Token and API Key auth, free trial/pay-as-you-go pricing, and official MCP servers",
    23: "Zoho Cliq REST API, OAuth 2.0 auth, free/paid workspace plans, and community MCP ecosystem",
    24: "Lark (Larksuite) Open Platform REST APIs, app/tenant/user access token auth, free/paid workspace plans, and official MCP server",
    25: "Pumble REST API/Addon and SDK, API key/webhook/app token auth, free/paid workspace plans, and community MCP ecosystem",
    26: "Discord HTTP REST API and Gateway, Bot token and OAuth 2.0 auth, free developer portal/app access, and community MCP ecosystem",
    27: "Telegram Bot API and MTProto API, BotFather token and api_id/api_hash auth, free API access, and community MCP ecosystem",
    28: "WhatsApp Business Cloud API, Meta Graph API access token/OAuth auth, sandbox/per-message pricing, and official/community MCP ecosystem",
    29: "Aircall Public REST API, HTTP Basic API key and OAuth 2.0 auth, paid plans/partner onboarding, and MCP ecosystem",
    30: "Vonage Communications APIs, API key/secret and JWT auth, free credit/pay-per-use pricing, and official MCP servers",
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
    # 21. Slack
    src(21, "https://docs.slack.dev/apis/web-api/", "primary_docs", ["testing", "production"]),
    src(21, "https://docs.slack.dev/authentication/installing-with-oauth", "primary_docs", ["testing", "production"]),
    src(21, "https://docs.slack.dev/ai/slack-mcp-server", "primary_docs", ["testing", "production"]),
    src(21, "https://docs.slack.dev/reference/methods", "primary_docs", ["testing", "production"]),
    src(21, "https://slack.com/pricing", "official_product_page", ["testing", "production"]),

    # 22. Twilio
    src(22, "https://www.twilio.com/docs/usage/api", "primary_docs", ["testing", "production"]),
    src(22, "https://www.twilio.com/docs/iam/api-keys", "primary_docs", ["testing", "production"]),
    src(22, "https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account", "primary_docs", ["testing", "production"]),
    src(22, "https://www.twilio.com/en-us/pricing", "official_product_page", ["testing", "production"]),
    src(22, "https://github.com/twilio-labs/mcp", "official_repository", ["testing", "production"], "Official Twilio Labs GitHub repository"),

    # 23. Zoho Cliq
    src(23, "https://www.zoho.com/cliq/help/restapi/v2/", "primary_docs", ["testing", "production"]),
    src(23, "https://www.zoho.com/cliq/help/restapi/v2/oauth.html", "primary_docs", ["testing", "production"]),
    src(23, "https://www.zoho.com/cliq/pricing.html", "official_product_page", ["testing", "production"]),
    src(23, "https://github.com/rohansen856/cliq-mcp", "community_repository", ["testing", "production"], "Community-authored GitHub repository for Zoho Cliq MCP"),

    # 24. Lark (Larksuite)
    src(24, "https://open.larksuite.com/document/home/index", "primary_docs", ["testing", "production"]),
    src(24, "https://open.larksuite.com/document/server-docs/authentication-management/access-token/tenant_access_token_internal", "primary_docs", ["testing", "production"]),
    src(24, "https://www.larksuite.com/en_us/plans", "official_product_page", ["testing", "production"]),
    src(24, "https://github.com/larksuite/lark-openapi-mcp", "official_repository", ["testing", "production"], "Official Larksuite GitHub repository for OpenAPI MCP"),

    # 25. Pumble
    src(25, "https://pumble.com/help/integrations/add-pumble-apps/api-keys/", "primary_docs", ["testing", "production"]),
    src(25, "https://pumble.com/help/integrations/add-pumble-apps/incoming-webhooks/", "primary_docs", ["testing", "production"]),
    src(25, "https://pumble.com/pricing/", "official_product_page", ["testing", "production"]),
    src(25, "https://github.com/CAKE-com/pumble-sdk", "official_repository", ["testing", "production"], "Official CAKE.com GitHub repository for Pumble SDK"),
    src(25, "https://github.com/infralayers/pumble-mcp", "community_repository", ["testing", "production"], "Community-authored GitHub repository for Pumble MCP"),

    # 26. Discord
    src(26, "https://discord.com/developers/docs/intro", "primary_docs", ["testing", "production"]),
    src(26, "https://discord.com/developers/docs/reference", "primary_docs", ["testing", "production"]),
    src(26, "https://discord.com/developers/docs/topics/oauth2", "primary_docs", ["testing", "production"]),
    src(26, "https://discord.com/developers/docs/resources/message", "primary_docs", ["testing", "production"]),
    src(26, "https://github.com/hanweg/mcp-discord", "community_repository", ["testing", "production"], "Community-authored GitHub repository for Discord MCP"),

    # 27. Telegram
    src(27, "https://core.telegram.org/bots", "primary_docs", ["testing", "production"]),
    src(27, "https://core.telegram.org/bots/api", "primary_docs", ["testing", "production"]),
    src(27, "https://core.telegram.org/api", "primary_docs", ["testing", "production"]),
    src(27, "https://github.com/sparfenyuk/mcp-telegram", "community_repository", ["testing", "production"], "Community-authored GitHub repository for Telegram MTProto MCP"),
    src(27, "https://github.com/node2flow-th/telegram-bot-mcp-community", "community_repository", ["testing", "production"], "Community-authored GitHub repository for Telegram Bot API MCP"),

    # 28. WhatsApp Business
    src(28, "https://developers.facebook.com/docs/whatsapp/cloud-api/", "primary_docs", ["testing", "production"]),
    src(28, "https://developers.facebook.com/docs/whatsapp/cloud-api/get-started", "primary_docs", ["testing", "production"]),
    src(28, "https://developers.facebook.com/docs/whatsapp/pricing", "primary_docs", ["testing", "production"]),
    src(28, "https://business.whatsapp.com/products/platform-pricing", "official_product_page", ["testing", "production"]),

    # 29. Aircall
    src(29, "https://developer.aircall.io/api-references/", "primary_docs", ["testing", "production"]),
    src(29, "https://developer.aircall.io/tutorials/oauth/", "primary_docs", ["testing", "production"]),
    src(29, "https://aircall.io/pricing/", "official_product_page", ["testing", "production"]),
    src(29, "https://developer.aircall.io/", "primary_docs", ["testing", "production"]),

    # 30. Vonage
    src(30, "https://developer.vonage.com/en/getting-started/concepts/authentication", "primary_docs", ["testing", "production"]),
    src(30, "https://developer.vonage.com/en/api", "primary_docs", ["testing", "production"]),
    src(30, "https://www.vonage.com/communications-apis/pricing/", "official_product_page", ["testing", "production"]),
    src(30, "https://github.com/Vonage-Community/vonage-mcp-server-api-bindings", "official_repository", ["testing", "production"], "Official Vonage Community GitHub repository for Vonage MCP Server API Bindings"),
]

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-001.json"
    out.write_text(json.dumps({"sources": SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(SOURCES)} sources to {out}")
