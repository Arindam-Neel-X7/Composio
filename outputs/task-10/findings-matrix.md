# Task 10: Findings Matrix (Marketing, Ads, Email and Social, IDs 31–40)

- **Run ID**: `task10-first-pass-003` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)
- **Eligible Assertions**: `191` (`171` observed, `20` inferred)

| ID | App | Auth Methods | Testing Access | Production Access | API Protocols / Breadth | MCP Discovery | Buildability |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 31 | Google Ads | OAuth2 | free=yes, sandbox=yes, vendor_appr=no, self_serve=yes | vendor_appr=yes, self_serve=no | REST/SDK / `broad` | `found (official)` | `conditional` |
| 32 | Meta Ads | OAuth2, Bearer_token | sandbox=no, vendor_appr=no, self_serve=yes | vendor_appr=yes, self_serve=no | REST/SDK/CLI / `broad` | `found (official, community)` | `conditional` |
| 33 | LinkedIn Ads | OAuth2 | vendor_appr=yes, self_serve=no | vendor_appr=yes, admin_appr=yes, self_serve=no | REST / `broad` | `found (community)` | `conditional` |
| 34 | GoHighLevel | OAuth2, Bearer_token | trial=yes, self_serve=yes | paid_req=yes, admin_appr=yes, self_serve=yes | REST/SDK/CLI / `broad` | `found (official)` | `build_now` |
| 35 | Mailchimp | API_key, OAuth2 | free=yes, paid_req=no, self_serve=yes | free=yes, paid_req=no, self_serve=yes | REST/SDK / `broad` | `found (community)` | `build_now` |
| 36 | Klaviyo | API_key, OAuth2, API_key | free=yes, paid_req=no, self_serve=yes | free=yes, paid_req=no, admin_appr=yes, self_serve=yes | REST/SDK / `broad` | `found (official)` | `build_now` |
| 37 | systeme.io | API_key, API_key | free=yes, paid_req=no, self_serve=yes | free=yes, paid_req=no, self_serve=yes | REST / `broad` | `found (official)` | `build_now` |
| 38 | Pinterest | OAuth2, Bearer_token | trial=yes, sandbox=yes, vendor_appr=yes, self_serve=no | vendor_appr=yes, self_serve=no | REST/SDK / `moderate` | `not_found_in_checked_sources` | `conditional` |
| 39 | Threads (Meta) | OAuth2 | vendor_appr=no, self_serve=yes | vendor_appr=yes, self_serve=no | REST / `broad` | `found (community)` | `conditional` |
| 40 | SendGrid | API_key, Basic | trial=yes, paid_req=no, self_serve=yes | paid_req=yes, self_serve=yes | REST/SDK / `broad` | `found (community)` | `build_now` |
