"""Generate expanded/repaired primary-source list for Task 11 (task11-capture-004)."""
import json
from pathlib import Path

from make_sources import ATTRIBUTION_BY, SCOPES, src

SOURCES = [
    # 41. Shopify (existing captured + replacements for 404s)
    src(41, "https://shopify.dev/docs/api", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/api/admin-graphql", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/apps/build/authentication/other-flows/authorization-code-grant", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/api/development-stores", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/agents", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/apps/tools/ai-toolkit", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/api/storefront/customer-accounts/mcp", "primary_docs", ["testing", "production"]),
    src(41, "https://www.shopify.com/pricing", "official_product_page", ["testing", "production"]),

    # 42. WooCommerce (all 5 captured)
    src(42, "https://developer.woocommerce.com/docs/apis/rest-api/", "primary_docs", ["testing", "production"]),
    src(42, "https://woocommerce.github.io/woocommerce-rest-api-docs/", "primary_docs", ["testing", "production"]),
    src(42, "https://developer.woocommerce.com/docs/features/mcp/", "primary_docs", ["testing", "production"]),
    src(42, "https://woocommerce.com/pricing/", "official_product_page", ["testing", "production"]),
    src(42, "https://github.com/woocommerce/woocommerce", "official_repository", ["testing", "production"], "Official WooCommerce GitHub repository"),

    # 43. BigCommerce (all 6 captured + official MCP doc)
    src(43, "https://developer.bigcommerce.com/docs/start/authentication", "primary_docs", ["testing", "production"]),
    src(43, "https://developer.bigcommerce.com/docs/start/about/sandboxes", "primary_docs", ["testing", "production"]),
    src(43, "https://developer.bigcommerce.com/docs/rest-management", "primary_docs", ["testing", "production"]),
    src(43, "https://developer.bigcommerce.com/docs/storefront/graphql", "primary_docs", ["testing", "production"]),
    src(43, "https://www.bigcommerce.com/essentials/pricing/", "official_product_page", ["testing", "production"]),
    src(43, "https://docs.bigcommerce.com/llms.txt", "primary_docs", ["testing", "production"]),

    # 44. Salesforce Commerce Cloud (existing 2 + official GitHub SDK repos to replace 403-blocked developer.salesforce.com)
    src(44, "https://www.salesforce.com/commerce/pricing/", "official_product_page", ["testing", "production"]),
    src(44, "https://github.com/SalesforceCommerceCloud/b2c-developer-tooling", "official_repository", ["testing", "production"], "Official Salesforce Commerce Cloud GitHub repository"),
    src(44, "https://github.com/SalesforceCommerceCloud/commerce-sdk", "official_repository", ["testing", "production"], "Official Salesforce Commerce Cloud Node.js SCAPI SDK repository"),
    src(44, "https://github.com/SalesforceCommerceCloud/commerce-sdk-isomorphic", "official_repository", ["testing", "production"], "Official Salesforce Commerce Cloud Isomorphic SCAPI SDK repository"),

    # 45. Magento (Adobe Commerce) (existing 4 + OAuth/SaaS/use-rest docs)
    src(45, "https://developer.adobe.com/commerce/webapi/rest/", "primary_docs", ["testing", "production"]),
    src(45, "https://developer.adobe.com/commerce/webapi/graphql/", "primary_docs", ["testing", "production"]),
    src(45, "https://developer.adobe.com/commerce/webapi/get-started/authentication/", "primary_docs", ["testing", "production"]),
    src(45, "https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-oauth/", "primary_docs", ["testing", "production"]),
    src(45, "https://developer.adobe.com/commerce/webapi/rest/use-rest/", "primary_docs", ["testing", "production"]),
    src(45, "https://github.com/magento/magento2", "official_repository", ["testing", "production"], "Official Magento Open Source GitHub repository"),

    # 46. Squarespace (existing 3 + orders overview + pricing retry with 30s timeout)
    src(46, "https://developers.squarespace.com/commerce-apis", "primary_docs", ["testing", "production"]),
    src(46, "https://developers.squarespace.com/commerce-apis/authentication-and-permissions", "primary_docs", ["testing", "production"]),
    src(46, "https://developers.squarespace.com/oauth", "primary_docs", ["testing", "production"]),
    src(46, "https://developers.squarespace.com/commerce-apis/orders-overview", "primary_docs", ["testing", "production"]),
    src(46, "https://www.squarespace.com/pricing", "official_product_page", ["testing", "production"]),
    src(46, "https://support.squarespace.com/hc/en-us/articles/206545657-Choosing-the-right-Squarespace-plan", "primary_docs", ["testing", "production"]),

    # 47. Ecwid (existing 3 + auth & getting started)
    src(47, "https://docs.ecwid.com/api-reference/rest-api/overview", "primary_docs", ["testing", "production"]),
    src(47, "https://api-docs.ecwid.com/reference/overview", "primary_docs", ["testing", "production"]),
    src(47, "https://api-docs.ecwid.com/reference/authentication", "primary_docs", ["testing", "production"]),
    src(47, "https://www.ecwid.com/pricing", "official_product_page", ["testing", "production"]),

    # 48. Gumroad (existing + official antiwork/gumroad-cli + community MCP)
    src(48, "https://gumroad.com/pricing", "official_product_page", ["testing", "production"]),
    src(48, "https://github.com/antiwork/gumroad", "official_repository", ["testing", "production"], "Official Gumroad GitHub repository"),
    src(48, "https://github.com/antiwork/gumroad-cli", "official_repository", ["testing", "production"], "Official Antiwork Gumroad CLI GitHub repository"),
    src(48, "https://github.com/rmarescu/gumroad-mcp", "community_repository", ["testing", "production"], "Community-authored GitHub repository for Gumroad MCP server"),

    # 49. Amazon Selling Partner (existing 4 good + llms.txt + auth/onboarding .md + community MCP)
    src(49, "https://developer-docs.amazon.com/sp-api/docs/what-is-the-selling-partner-api", "primary_docs", ["testing", "production"]),
    src(49, "https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox", "primary_docs", ["testing", "production"]),
    src(49, "https://developer-docs.amazon.com/sp-api/llms.txt", "primary_docs", ["testing", "production"]),
    src(49, "https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer", "primary_docs", ["testing", "production"]),
    src(49, "https://developer-docs.amazon.com/sp-api/docs/authorizing-selling-partner-api-applications", "primary_docs", ["testing", "production"]),
    src(49, "https://developer-docs.amazon.com/sp-api/docs/connecting-to-the-selling-partner-api", "primary_docs", ["testing", "production"]),
    src(49, "https://github.com/amzn/selling-partner-api-models", "official_repository", ["testing", "production"], "Official Amazon SP-API OpenAPI models GitHub repository"),
    src(49, "https://github.com/amzn/selling-partner-agentic-toolkit", "official_repository", ["testing", "production"], "Official Amazon SP-API Agentic Toolkit GitHub repository"),
    src(49, "https://github.com/jay-trivedi/amazon_sp_mcp", "community_repository", ["testing", "production"], "Community-authored GitHub repository for Amazon SP-API MCP server"),

    # 50. fanbasis / Commas (existing 3 + commasdocs.com retry with 30s timeout)
    src(50, "https://www.fanbasis.com/", "official_product_page", ["testing", "production"]),
    src(50, "https://commas.com/", "official_product_page", ["testing", "production"]),
    src(50, "https://dev-docs.fanbasis.com/", "primary_docs", ["testing", "production"]),
    src(50, "https://commasdocs.com/", "primary_docs", ["testing", "production"]),
    src(50, "https://commasdocs.com/llms.txt", "primary_docs", ["testing", "production"]),
]


def main():
    out = Path(__file__).resolve().parent / "sources-002.json"
    out.write_text(json.dumps({"sources": SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(SOURCES)} sources to {out}")


if __name__ == "__main__":
    main()
