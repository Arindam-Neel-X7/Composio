import json
from pathlib import Path
from make_sources import specs
U={92:['https://help.otter.ai/api/v2/help_center/en-us/articles/36130822688279.json']}
Path('work/task-16-agent/sources-007.json').write_text(json.dumps({'sources':specs(U)},indent=2)+'\n',encoding='utf-8')
