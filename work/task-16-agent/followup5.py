import json
from pathlib import Path
from make_sources import specs
U={92:['https://help.otter.ai/hc/en-us/articles/36130822688279-Otter-ai-Public-API']}
Path('work/task-16-agent/sources-005.json').write_text(json.dumps({'sources':specs(U)},indent=2)+'\n',encoding='utf-8')
