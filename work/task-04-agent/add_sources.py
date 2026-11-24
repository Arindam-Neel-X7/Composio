import json
from pathlib import Path
from make_sources import SCOPES

p = Path(__file__).resolve().parent
sources = json.loads((p / 'sources.json').read_text())['sources']
for app, url, env in [
    (31, 'https://developers.google.com/google-ads/api/rest/overview', []),
    (58, 'https://sherlockproject.xyz/installation', ['testing','production']),
    (13, 'https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/rest-apis/', ['testing','production']),
]:
    sources.append(dict(app_id=app,url=url,kind='primary_docs',scope=SCOPES[app],environments=env,
        attribution_basis='Vendor/project documentation, read using web tool; additional precise protocol/install evidence',
        attribution_by='task04-research-agent-gpt-6.1-sol'))
with (p / 'sources-expanded.json').open('x', encoding='utf-8') as f:
    json.dump({'sources':sources}, f, indent=2)
print('27 selected sources; added transport, CLI installation, and alternate Freshdesk REST documentation')
