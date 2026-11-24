import json
from pathlib import Path
W=Path('D:/Composio/work/task-13-agent')
ss=json.loads((W/'sources-001.json').read_text())['sources']
new={62:['https://vercel.com/docs/rest-api/reference/welcome','https://vercel.com/docs/rest-api/reference/authentication'],63:['https://www.netlify.com/pricing/'],69:['https://docs.datadoghq.com/account_management/api-app-keys/?_task13=identity','https://docs.datadoghq.com/mcp_server/index.md','https://docs.datadoghq.com/mcp_server/setup/index.md','https://raw.githubusercontent.com/DataDog/documentation/master/content/en/account_management/api-app-keys.md','https://raw.githubusercontent.com/DataDog/documentation/master/content/en/mcp_server/_index.md','https://raw.githubusercontent.com/DataDog/documentation/master/content/en/mcp_server/setup.md']}
out=[]
for aid,urls in new.items():
 base=next(s for s in ss if s['app_id']==aid)
 for u in urls:
  s=dict(base,url=u,kind='official_repository' if 'raw.github' in u else ('official_product_page' if '/pricing' in u else 'primary_docs'))
  out.append(s)
(W/'sources-002.json').write_text(json.dumps({'sources':out},indent=2),encoding='utf8')
print(len(out))
