import json,sys
from pathlib import Path
from make_sources import specs
D=Path('work/research-runs/task16-capture-001')
c=json.loads((D/'captures.json').read_text())
print('CAPTURES',[(x['spec']['app_id'],x['spec']['url'],x['line_count']) for x in c])
r=json.loads((D/'records.json').read_text())
print('FAILURES',[(x['identity']['id'],f['source_url'],f['error']) for x in r for f in x['fetches'] if f['status']!='fetched'])
U={92:['https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server'],93:['https://help.fathom.video/en/articles/8368641','https://developers.fathom.ai/quickstart.md','https://developers.fathom.ai/oauth.md','https://developers.fathom.ai/sdks/oauth.md','https://developers.fathom.ai/faq.md','https://developers.fathom.ai/mcp-docs/index.md','https://developers.fathom.ai/mcp-docs/claude.md'],94:['https://docs.consensus.app/api-get-started.md','https://docs.consensus.app/api-plans-and-access.md','https://docs.consensus.app/consensus-mcp.md','https://docs.consensus.app/enterprise/connection-reference.md'],95:['https://docs.reducto.ai/quickstart/index.md','https://docs.reducto.ai/mcp-server/index.md','https://docs.reducto.ai/studio-account/index.md','https://docs.reducto.ai/agent-guide/index.md'],96:['https://docs.devin.ai/api-reference/authentication.md','https://docs.devin.ai/work-with-devin/devin-mcp.md','https://docs.devin.ai/_llms/en/api.txt'],100:['https://developers.grain.com/mcp/faq.html','https://developers.grain.com/mcp/','https://developers.grain.com/reference/introduction']}
Path('work/task-16-agent/sources-002.json').write_text(json.dumps({'sources':specs(U)},indent=2)+'\n',encoding='utf-8')
