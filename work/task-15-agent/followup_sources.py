import json
from pathlib import Path
p=Path('work/task-15-agent'); old=json.loads((p/'sources-001.json').read_text())['sources']; scopes=json.loads((p/'scopes.json').read_text()); sources=[]
urls={82:['https://support.plaid.com/hc/en-us/articles/16110110883479-How-are-Sandbox-Production-Trial-plan-and-Limited-Production-different','https://plaid.com/docs/resources/mcp/'],83:['https://raw.githubusercontent.com/mujeeb8/Binance-MCP/main/README.md'],85:['https://raw.githubusercontent.com/iPAYX-Technologies/mcp-fx-audit/main/README.md'],86:['https://raw.githubusercontent.com/intuit/QuickBooks-V3-PHP-SDK/master/README.md'],87:['https://developer.xero.com/faq/getting-started','https://raw.githubusercontent.com/XeroAPI/xero-node/master/README.md'],88:['https://developer.brex.com/docs/mcp.md'],89:['https://docs.ramp.com/llms-guides/authorization.txt','https://docs.ramp.com/llms-guides/ramp-mcp.txt','https://docs.ramp.com/llms-guides/getting-started.txt'],90:['https://pitchbook.com/help/PitchBook-api','https://pitchbook.com/products/pitchbooks-ai-capabilities']}
for app,links in urls.items():
 for url in links:
  if any(s['url']==url for s in old): continue
  kind='community_repository' if app in (83,85) else 'official_repository' if 'raw.githubusercontent.com' in url else 'official_product_page' if app==90 else 'primary_docs'
  sources.append(dict(app_id=app,url=url,kind=kind,scope=scopes[str(app)],environments=['testing','production'],attribution_basis='Public vendor documentation or vendor-owned SDK repository; MCP repositories for Binance and iPayX conservatively treated as community implementations without established vendor endorsement.',attribution_by='codex-task15-researcher'))
(p/'sources-002.json').write_text(json.dumps({'sources':sources},indent=2),encoding='utf8')
print(len(sources))
