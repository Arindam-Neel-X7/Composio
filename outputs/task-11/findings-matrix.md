# Task 11: Findings Matrix (Ecommerce, IDs 41–50)

- **Run ID**: `task11-first-pass-004` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)
- **Frozen 20-App Sample Members in Batch**: App `46` (Squarespace) and App `50` (fanbasis / Commas)

| ID | App | Auth Methods (Observed) | Testing / Sandbox | Production Access | Protocols & Breadth | MCP Discovery | Buildability |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 41 | Shopify | OAuth2, Bearer_token | trial_access, sandbox_access, self_serve | paid_required, admin_approval_required, vendor_approval_required | GraphQL, REST, CLI (broad) | `found` (official, 1) | `build_now` |
| 42 | WooCommerce | Basic, other, Basic | free_access, self_serve | free_access, !paid_required, self_serve, admin_approval_required | REST, SDK, CLI (broad) | `found` (official, 1) | `build_now` |
| 43 | BigCommerce | OAuth2, Bearer_token | trial_access, sandbox_access, partner_approval_required | paid_required, self_serve | REST, GraphQL (broad) | `found` (official, 2) | `build_now` |
| 44 | Salesforce Commerce Cloud | OAuth2, other | unknown | paid_required, contact_sales_required | REST, SDK, CLI (moderate) | `found` (official, 1) | `outreach_required` |
| 45 | Magento (Adobe Commerce) | Bearer_token, other, session_cookie, OAuth2 | free_access, self_serve | free_access, admin_approval_required | REST, GraphQL (moderate) | `not_found_in_checked_sources` | `conditional` |
| 46 | Squarespace | API_key, OAuth2 | trial_access | paid_required, self_serve, vendor_approval_required | REST (broad) | `unknown` | `conditional` |
| 47 | Ecwid | OAuth2 | unknown | paid_required | REST, SDK (broad) | `not_found_in_checked_sources` | `conditional` |
| 48 | Gumroad | OAuth2, Bearer_token | free_access, self_serve | free_access, !paid_required, self_serve | REST, CLI (moderate) | `found` (community/official, 2) | `build_now` |
| 49 | Amazon Selling Partner | OAuth2, OAuth2 | sandbox_access, vendor_approval_required | paid_required, admin_approval_required, vendor_approval_required | REST, SDK (broad) | `found` (community/official, 2) | `conditional` |
| 50 | fanbasis | unknown | unknown | unknown | SDK (unknown) | `found` (official, 1) | `outreach_required` |
