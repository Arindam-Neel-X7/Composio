import json,sys
from pathlib import Path
ROOT=Path('D:/Composio'); sys.path.insert(0,str(ROOT/'work/task-14-agent'))
from make_sources import SCOPES
extra={
72:['https://support.airtable.com/docs/getting-started-with-airtables-web-api','https://support.airtable.com/docs/managing-api-call-limits-in-airtable'],
77:['https://developer.clickup.com/','https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1','https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP'],
78:['https://help.coda.io/en/articles/1337373-coda-api','https://coda.io/product/whats-new','https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP?output=1'],
80:['https://github.com/southleft/harvest-mcp','https://help.getharvest.com/api-v2/time-tracking-api/time-entries/time-entries/','https://help.getharvest.com/api-v2/time-tracking-api/time-entries/time-entries/']}
src=json.loads((ROOT/'work/task-14-agent/sources-001.json').read_text())
seen={x['url'] for x in src['sources']}
for a,urls in extra.items():
 for u in urls:
  if u in seen:continue
  seen.add(u)
  src['sources'].append(dict(app_id=a,url=u,kind='community_repository' if 'github.com/southleft/' in u else 'primary_docs',scope=SCOPES[a],environments=['testing','production'],attribution_basis='Community-maintainer repository, not Harvest vendor endorsement' if 'github.com/southleft/' in u else 'Vendor-controlled developer/support documentation selected by researcher',attribution_by='task14-codex-research-worker'))
(ROOT/'work/task-14-agent/sources-002.json').write_text(json.dumps(src,indent=2),encoding='utf-8')
