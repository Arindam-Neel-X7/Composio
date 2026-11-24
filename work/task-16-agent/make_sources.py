import json
from pathlib import Path
SCOPES={91:'NotebookLM Enterprise on Google Cloud; personal NotebookLM API excluded; public documentary research, no execution',92:'Otter AI public API and callable Otter MCP server; public documentary research, no execution',93:'Fathom video meeting assistant public developer API; public documentary research, no execution',94:'Consensus scholarly research API and MCP; public documentary research, no execution',95:'Reducto document processing API and agent integrations; public documentary research, no execution',96:'Devin API and callable Devin MCP server; outgoing MCP clients distinguished; public documentary research, no execution',97:'Higgsfield content generation API, CLI and MCP; separate billing paths; public documentary research, no execution',98:'Official mermaid-js Mermaid CLI local diagram rendering; public documentary research, no execution',99:'YouTube Transcript via TranscriptAPI.com API and MCP; public documentary research, no execution',100:'Grain personal/workspace APIs and callable MCP server; public documentary research, no execution'}
URLS={
91:['https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks','https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-sources','https://developers.google.com/notebook/docs/authentication'],
92:['https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server','https://otter.ai/developers'],
93:['https://fathom.video/','https://developers.fathom.ai/','https://developers.fathom.ai/llms.txt'],
94:['https://help.consensus.app/en/articles/16516328-the-consensus-api','https://docs.consensus.app/','https://docs.consensus.app/llms.txt','https://www.consensus.app/home/api/'],
95:['https://docs.reducto.ai/','https://docs.reducto.ai/llms.txt'],
96:['https://docs.devin.ai/api-reference/authentication','https://docs.devin.ai/llms.txt'],
97:['https://higgsfield.ai/blog/higgsfield-cli','https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api','https://higgsfield.ai/enterprise-help-center/platform/integrations'],
98:['https://github.com/mermaid-js/mermaid-cli','https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md','https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE'],
99:['https://transcriptapi.com/docs/getting-started/','https://transcriptapi.com/docs/mcp/','https://transcriptapi.com/docs/'],
100:['https://developers.grain.com/mcp/faq.html','https://developers.grain.com/mcp/','https://support.grain.com/en/articles/15297887-export-meetings','https://developers.grain.com/']}
def specs(urls):
 return [dict(app_id=a,url=u,kind='official_repository' if a==98 else 'primary_docs',scope=SCOPES[a],environments=['testing','production'],attribution_basis=('Official mermaid-js repository identified in assignment' if a==98 else 'Vendor-controlled documentation/help/product domain matching roster product; ownership is researcher attribution, requires independent review'),attribution_by='task16-codex-researcher') for a,us in urls.items() for u in us]
if __name__=='__main__':
 Path('work/task-16-agent/sources-001.json').write_text(json.dumps({'sources':specs(URLS)},indent=2)+'\n',encoding='utf-8')
