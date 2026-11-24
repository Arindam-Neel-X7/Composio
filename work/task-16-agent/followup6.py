import json
from pathlib import Path
from make_sources import specs
U={92:['https://help.otter.ai/hc/en-us/articles/36130822688279','https://help.otter.ai/hc/en-us/articles/36130822688279-Otter-ai-Public-API?preview=false']}
Path('work/task-16-agent/sources-006.json').write_text(json.dumps({'sources':specs(U)},indent=2)+'\n',encoding='utf-8')
