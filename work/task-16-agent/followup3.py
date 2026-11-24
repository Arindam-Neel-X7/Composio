import json
from pathlib import Path
from make_sources import specs
U={91:['https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources','https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-licensing'],92:['https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server?preview=false','https://help.otter.ai/api/v2/help_center/en-us/articles/35287607569687.json','https://otter.ai/mcp','https://otter.ai/developers'],95:['https://docs.reducto.ai/pricing/index.md'],96:['https://docs.devin.ai/api-reference/getting-started/teams-quickstart.md','https://docs.devin.ai/api-reference/v3/overview.md'],100:['https://developers.grain.com/authentication.html','https://developers.grain.com/mcp/claude-setup.html']}
Path('work/task-16-agent/sources-003.json').write_text(json.dumps({'sources':specs(U)},indent=2)+'\n',encoding='utf-8')
