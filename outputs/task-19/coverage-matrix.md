# 100-Application Master Research & Buildability Coverage Matrix

> **Methodology & Provenance**: Reflects authoritative evidence captured across Tasks 07–16, audited by human reviewer ARINDAM KARMAKAR in Task 17 (baseline accuracy 84.71%), corrected in Task 18 Phase A across 50 unsupported statements, and verified via Task 18 Phase B human recheck (100.00% accuracy on frozen sample $N=327$). All 100 apps classified with explicit documentary evidence.

| ID | App Name | Category | Sample | Auth Methods | Testing Access | Production Gating | API Protocols | Breadth | MCP Status | Build Verdict |
| ---: | --- | --- | :---: | --- | --- | --- | --- | --- | --- | :---: |
| 01 | **Salesforce** | CRM and Sales | No | other | Trial/Sandbox | Paid | REST, other | Unknown | Official | `conditional` |
| 02 | **HubSpot** | CRM and Sales | No | OAuth2, Bearer_token, Bearer_token, API_key, OAuth2 | Free/Sandbox/Self-serve | Admin | REST | Unknown | Official | `build_now` |
| 03 | **Pipedrive** | CRM and Sales | No | API_key, OAuth2 | Sandbox | Admin+Vendor | REST | Unknown | Community | `conditional` |
| 04 | **Attio** | CRM and Sales | Yes | OAuth2, API_key | Free | Self-serve/Open | REST, other | Unknown | Official | `build_now` |
| 05 | **Twenty** | CRM and Sales | No | API_key, OAuth2 | Free/Trial | Self-serve/Open | REST, GraphQL | Unknown | Community | `build_now` |
| 06 | **Podio** | CRM and Sales | No | OAuth2, OAuth2, OAuth2 | Free/Trial/Self-serve | Self-serve/Open | REST | Unknown | None (Bounded) | `build_now` |
| 07 | **Zoho CRM** | CRM and Sales | No | OAuth2 | Free/Trial | Self-serve/Open | REST | Unknown | Official | `build_now` |
| 08 | **Close** | CRM and Sales | Yes | Basic, OAuth2 | Trial | Paid+Vendor | REST | Unknown | Official | `conditional` |
| 09 | **Copper** | CRM and Sales | No | API_key, OAuth2 | Trial | Paid | REST | Unknown | None (Bounded) | `conditional` |
| 10 | **DealCloud** | CRM and Sales | No | OAuth2 | Unknown | Paid+Admin | REST | Unknown | Official | `outreach_required` |
| 11 | **Zendesk** | Support and Helpdesk | No | OAuth2, OAuth2, Basic | Trial/Sandbox/Self-serve | Paid | REST | Unknown | Community | `build_now` |
| 12 | **Intercom** | Support and Helpdesk | No | API_key, OAuth2 | Free/Trial/Sandbox/Self-serve | Paid+Vendor | REST | Unknown | Official | `build_now` |
| 13 | **Freshdesk** | Support and Helpdesk | No | Basic, OAuth2, API_key | Trial/Sandbox/Self-serve | Paid | REST | Unknown | Official | `build_now` |
| 14 | **Front** | Support and Helpdesk | No | API_key, OAuth2 | Trial/Self-serve | Paid+Admin | REST | Unknown | Official | `build_now` |
| 15 | **Pylon** | Support and Helpdesk | No | API_key, OAuth2 | Unknown | Paid+Admin | REST, SDK, CLI | Unknown | Official | `conditional` |
| 16 | **LiveAgent** | Support and Helpdesk | Yes | API_key, OAuth2, API_key | Trial/Self-serve | Paid | REST | Unknown | Official | `build_now` |
| 17 | **Plain** | Support and Helpdesk | No | API_key, OAuth2 | Trial/Self-serve | Paid | GraphQL, SDK | Unknown | Official | `build_now` |
| 18 | **Help Scout** | Support and Helpdesk | No | OAuth2 | Free/Trial/Self-serve | Paid | other | Unknown | Unknown | `conditional` |
| 19 | **Gorgias** | Support and Helpdesk | Yes | API_key, OAuth2 | Trial/Sandbox | Paid+Partner | REST | Unknown | Community | `conditional` |
| 20 | **Gladly** | Support and Helpdesk | No | Basic | Sandbox | Admin | REST | Unknown | None (Bounded) | `conditional` |
| 21 | **Slack** | Communications and Messaging | Yes | OAuth2, Bearer_token | Free/Self-serve | Admin+Vendor | RPC, SDK, CLI | Unknown | Official | `build_now` |
| 22 | **Twilio** | Communications and Messaging | No | API_key, Basic, OAuth2 | Trial/Self-serve | Paid | REST, SDK, CLI | Unknown | Official | `build_now` |
| 23 | **Zoho Cliq** | Communications and Messaging | No | OAuth2 | Free/Trial/Self-serve | Self-serve/Open | REST | Unknown | Community | `build_now` |
| 24 | **Lark (Larksuite)** | Communications and Messaging | No | Bearer_token, OAuth2 | Self-serve | Self-serve/Open | REST, SDK | Unknown | Official | `build_now` |
| 25 | **Pumble** | Communications and Messaging | No | API_key, other | Free/Self-serve | Self-serve/Open | REST, SDK, CLI | Unknown | Official+Community | `build_now` |
| 26 | **Discord** | Communications and Messaging | No | other, OAuth2, Basic | Self-serve | Partner | REST, other, SDK | Unknown | Community | `build_now` |
| 27 | **Telegram** | Communications and Messaging | Yes | other, other | Free/Self-serve | Self-serve/Open | RPC, other | Unknown | Community | `build_now` |
| 28 | **WhatsApp Business** | Communications and Messaging | No | Bearer_token, OAuth2, Bearer_token | Free/Sandbox/Self-serve | Paid+Vendor | REST | Unknown | Community | `conditional` |
| 29 | **Aircall** | Communications and Messaging | No | Basic, OAuth2 | Trial/Sandbox | Paid+Admin+Partner | REST, SDK | Unknown | None (Bounded) | `conditional` |
| 30 | **Vonage** | Communications and Messaging | No | Basic, JWT | Free/Trial/Self-serve | Paid | REST, SDK, CLI | Unknown | Official | `build_now` |
| 31 | **Google Ads** | Marketing, Ads, Email and Social | Yes | OAuth2 | Free/Sandbox/Self-serve | Vendor | REST, SDK | Unknown | Official | `conditional` |
| 32 | **Meta Ads** | Marketing, Ads, Email and Social | No | OAuth2, Bearer_token | Self-serve | Vendor | REST, SDK, CLI | Unknown | Official+Community | `conditional` |
| 33 | **LinkedIn Ads** | Marketing, Ads, Email and Social | No | OAuth2 | Unknown | Admin+Vendor | REST | Unknown | Community | `conditional` |
| 34 | **GoHighLevel** | Marketing, Ads, Email and Social | No | OAuth2, Bearer_token | Trial/Self-serve | Paid+Admin | REST, SDK, CLI | Unknown | Official | `build_now` |
| 35 | **Mailchimp** | Marketing, Ads, Email and Social | No | API_key, OAuth2 | Free/Self-serve | Self-serve/Open | REST, SDK | Unknown | Community | `build_now` |
| 36 | **Klaviyo** | Marketing, Ads, Email and Social | No | API_key, OAuth2, API_key | Free/Self-serve | Admin | REST, SDK | Unknown | Official | `build_now` |
| 37 | **systeme.io** | Marketing, Ads, Email and Social | No | API_key, API_key | Free/Self-serve | Self-serve/Open | REST | Unknown | Official | `build_now` |
| 38 | **Pinterest** | Marketing, Ads, Email and Social | No | OAuth2, Bearer_token | Trial/Sandbox | Vendor | REST, SDK | Unknown | None (Bounded) | `conditional` |
| 39 | **Threads (Meta)** | Marketing, Ads, Email and Social | No | OAuth2 | Self-serve | Vendor | REST | Unknown | Community | `conditional` |
| 40 | **SendGrid** | Marketing, Ads, Email and Social | Yes | API_key, Basic | Trial/Self-serve | Paid | REST, SDK | Unknown | Community | `build_now` |
| 41 | **Shopify** | Ecommerce | No | OAuth2, Bearer_token | Trial/Sandbox/Self-serve | Paid+Admin+Vendor | GraphQL, REST, CLI | Unknown | Official | `build_now` |
| 42 | **WooCommerce** | Ecommerce | No | Basic, other, Basic | Free/Self-serve | Admin | REST, SDK, CLI | Unknown | Official | `build_now` |
| 43 | **BigCommerce** | Ecommerce | No | OAuth2, Bearer_token | Trial/Sandbox | Paid | REST, GraphQL | Unknown | Official | `build_now` |
| 44 | **Salesforce Commerce Cloud** | Ecommerce | No | OAuth2, other | Gated | Paid | REST, SDK, CLI | Unknown | Official | `outreach_required` |
| 45 | **Magento (Adobe Commerce)** | Ecommerce | No | Bearer_token, other, session_cookie, OAuth2 | Free/Self-serve | Admin | REST, GraphQL | Unknown | None (Bounded) | `conditional` |
| 46 | **Squarespace** | Ecommerce | Yes | API_key, OAuth2 | Trial | Paid+Vendor | REST | Unknown | Unknown | `conditional` |
| 47 | **Ecwid** | Ecommerce | No | OAuth2 | Gated | Paid | REST, SDK | Unknown | None (Bounded) | `conditional` |
| 48 | **Gumroad** | Ecommerce | No | OAuth2, Bearer_token | Free/Self-serve | Self-serve/Open | REST, CLI | Unknown | Official+Community | `build_now` |
| 49 | **Amazon Selling Partner** | Ecommerce | No | OAuth2, OAuth2 | Sandbox | Paid+Admin+Vendor | REST, SDK | Unknown | Official+Community | `conditional` |
| 50 | **fanbasis** | Ecommerce | Yes | None | Gated | Self-serve/Open | SDK | Unknown | Official | `outreach_required` |
| 51 | **DataForSEO** | Data, SEO and Scraping | No | Basic, OAuth2 | Free/Sandbox/Self-serve | Paid | REST, SDK, CLI | Unknown | Official | `build_now` |
| 52 | **SE Ranking** | Data, SEO and Scraping | Yes | API_key, OAuth2 | Trial/Self-serve | Paid | REST | Unknown | Official | `build_now` |
| 53 | **Ahrefs** | Data, SEO and Scraping | No | Bearer_token, OAuth2 | Self-serve | Paid+Admin | REST | Unknown | Official | `build_now` |
| 54 | **MrScraper** | Data, SEO and Scraping | No | API_key, Bearer_token, OAuth2 | Free/Self-serve | Self-serve/Open | REST, CLI, SDK | Unknown | Official | `build_now` |
| 55 | **Apify** | Data, SEO and Scraping | No | Bearer_token, OAuth2, none | Free/Self-serve | Self-serve/Open | REST, SDK, CLI | Unknown | Official | `build_now` |
| 56 | **Firecrawl** | Data, SEO and Scraping | No | Bearer_token, OAuth2, none | Free/Self-serve | Self-serve/Open | REST, SDK, CLI | Unknown | Official | `build_now` |
| 57 | **Bright Data** | Data, SEO and Scraping | No | Bearer_token, Basic | Free/Trial/Self-serve | Self-serve/Open | REST, CLI, SDK | Unknown | Official | `build_now` |
| 58 | **Sherlock** | Data, SEO and Scraping | No | none | Free/Self-serve | Self-serve/Open | CLI | Unknown | None (Bounded) | `build_now` |
| 59 | **Waterfall.io** | Data, SEO and Scraping | No | API_key | Unknown | Paid+Vendor | REST | Unknown | None (Bounded) | `outreach_required` |
| 60 | **Clay** | Data, SEO and Scraping | Yes | API_key, OAuth2 | Free/Trial/Self-serve | Self-serve/Open | REST, CLI | Unknown | Official | `build_now` |
| 61 | **GitHub** | Developer, Infra and Data platforms | No | Bearer_token, OAuth2, Basic | Self-serve | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 62 | **Vercel** | Developer, Infra and Data platforms | No | Bearer_token, OAuth2 | Free/Trial | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 63 | **Netlify** | Developer, Infra and Data platforms | No | Bearer_token, OAuth2 | Free/Self-serve | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 64 | **Cloudflare** | Developer, Infra and Data platforms | Yes | Bearer_token | Self-serve | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 65 | **Supabase** | Developer, Infra and Data platforms | Yes | API_key, Bearer_token, OAuth2 | Free/Sandbox | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 66 | **Neo4j** | Developer, Infra and Data platforms | No | Basic, Bearer_token | Free | Self-serve/Open | other | Unknown | Official | `conditional` |
| 67 | **Snowflake** | Developer, Infra and Data platforms | No | OAuth2, JWT, Bearer_token | Trial/Self-serve | Paid | REST, SQL | Unknown | Official | `conditional` |
| 68 | **MongoDB Atlas** | Developer, Infra and Data platforms | No | OAuth2, API_key | Free/Self-serve | Self-serve/Open | CLI, SDK | Unknown | Official | `conditional` |
| 69 | **Datadog** | Developer, Infra and Data platforms | No | API_key, OAuth2, Bearer_token | Trial/Self-serve | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 70 | **Sentry** | Developer, Infra and Data platforms | No | Bearer_token, OAuth2, OAuth2 | Free/Self-serve | Self-serve/Open | other | Unknown | Official | `conditional` |
| 71 | **Notion** | Productivity and Project Management | No | Bearer_token, Bearer_token, OAuth2 | Unknown | Self-serve/Open | REST, SDK | Unknown | Official | `conditional` |
| 72 | **Airtable** | Productivity and Project Management | No | other, OAuth2 | Free | Self-serve/Open | None/CLI | Unknown | Official | `conditional` |
| 73 | **Linear** | Productivity and Project Management | No | API_key, OAuth2, OAuth2 | Unknown | Self-serve/Open | GraphQL, SDK | Unknown | Official | `conditional` |
| 74 | **Jira** | Productivity and Project Management | No | Basic, OAuth2 | Unknown | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 75 | **Asana** | Productivity and Project Management | No | Bearer_token, OAuth2 | Free/Sandbox | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 76 | **Monday.com** | Productivity and Project Management | Yes | API_key, OAuth2, OAuth2 | Free/Trial/Sandbox | Self-serve/Open | GraphQL | Unknown | Official | `conditional` |
| 77 | **ClickUp** | Productivity and Project Management | Yes | API_key, OAuth2, OAuth2 | Unknown | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 78 | **Coda** | Productivity and Project Management | No | Bearer_token, Bearer_token, OAuth2 | Free | Self-serve/Open | REST | Unknown | Official | `conditional` |
| 79 | **Smartsheet** | Productivity and Project Management | No | Bearer_token, OAuth2 | Sandbox | Paid | REST, SDK | Unknown | Official | `conditional` |
| 80 | **Harvest** | Productivity and Project Management | No | Bearer_token, OAuth2, OAuth2 | Self-serve | Self-serve/Open | REST | Unknown | Community | `conditional` |
| 81 | **Stripe** | Finance and Fintech | No | API_key, Bearer_token, OAuth2, OAuth2 | Free/Sandbox/Self-serve | Vendor | REST, SDK, CLI | Unknown | Official | `build_now` |
| 82 | **Plaid** | Finance and Fintech | No | API_key, OAuth2 | Free/Trial/Sandbox/Self-serve | Paid+Vendor | REST, SDK | Unknown | Official | `conditional` |
| 83 | **Binance** | Finance and Fintech | Yes | none, API_key | Free/Sandbox/Self-serve | Self-serve/Open | REST, other, SDK | Unknown | Community | `conditional` |
| 84 | **Paygent Connect** | Finance and Fintech | Yes | None | Unknown | Self-serve/Open | None/CLI | Unknown | Unknown | `unknown` |
| 85 | **iPayX** | Finance and Fintech | No | None | Unknown | Self-serve/Open | None/CLI | Unknown | Community | `conditional` |
| 86 | **QuickBooks** | Finance and Fintech | No | OAuth2 | Sandbox/Self-serve | Vendor | REST, SDK | Unknown | Official | `conditional` |
| 87 | **Xero** | Finance and Fintech | No | OAuth2, OAuth2 | Free/Trial/Sandbox/Self-serve | Self-serve/Open | REST, SDK | Unknown | Official | `build_now` |
| 88 | **Brex** | Finance and Fintech | No | Bearer_token, OAuth2, OAuth2, OAuth2 | Unknown | Admin | REST | Unknown | Official | `conditional` |
| 89 | **Ramp** | Finance and Fintech | No | OAuth2, OAuth2, OAuth2 | Sandbox | Admin | REST, CLI | Unknown | Official | `conditional` |
| 90 | **PitchBook** | Finance and Fintech | No | None | Unknown | Self-serve/Open | None/CLI | Unknown | Unknown | `unknown` |
| 91 | **NotebookLM** | AI, Research and Media-native | No | Bearer_token | Free/Trial/Self-serve | Paid+Admin | REST | Unknown | None (Bounded) | `conditional` |
| 92 | **Otter AI** | AI, Research and Media-native | No | OAuth2, API_key | Self-serve | Self-serve/Open | REST, other | Unknown | Official | `conditional` |
| 93 | **Fathom** | AI, Research and Media-native | No | API_key, OAuth2 | Self-serve | Self-serve/Open | REST, SDK | Unknown | Official | `conditional` |
| 94 | **Consensus** | AI, Research and Media-native | No | API_key, OAuth2, API_key | Free/Self-serve | Self-serve/Open | REST, other | Unknown | Official | `build_now` |
| 95 | **Reducto** | AI, Research and Media-native | No | API_key, OAuth2 | Self-serve | Paid | REST, SDK, CLI, other | Unknown | Official | `build_now` |
| 96 | **Devin** | AI, Research and Media-native | No | API_key, Bearer_token, API_key | Self-serve | Admin | REST, other | Unknown | Official | `conditional` |
| 97 | **higgsfield** | AI, Research and Media-native | Yes | API_key, OAuth2, OAuth2 | Self-serve | Paid | REST, SDK, CLI, other | Unknown | Official | `conditional` |
| 98 | **Mermaid CLI** | AI, Research and Media-native | Yes | none | Free/Self-serve | Self-serve/Open | CLI, SDK | Unknown | None (Bounded) | `build_now` |
| 99 | **YouTube Transcript** | AI, Research and Media-native | No | API_key, OAuth2 | Free/Self-serve | Paid | REST, other | Unknown | Official | `build_now` |
| 100 | **Grain** | AI, Research and Media-native | No | Bearer_token, Bearer_token, OAuth2 | Free/Self-serve | Self-serve/Open | REST, other | Unknown | Official | `build_now` |
