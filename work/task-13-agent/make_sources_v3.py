import json
from pathlib import Path
W=Path('D:/Composio/work/task-13-agent');ss=json.loads((W/'sources-001.json').read_text())['sources']
new={62:['https://vercel.com/docs/rest-api/deployments/get-a-deployment-by-id-or-url','https://vercel.com/docs/rest-api/reference','https://vercel.com/docs/accounts/create-an-account'],69:['https://docs.datadoghq.com/account_management/api-app-keys.md','https://docs.datadoghq.com/mcp_server.md','https://docs.datadoghq.com/mcp_server/setup.md']}
out=[dict(next(s for s in ss if s['app_id']==aid),url=u) for aid,urls in new.items() for u in urls]
(W/'sources-003.json').write_text(json.dumps({'sources':out},indent=2),encoding='utf8')
