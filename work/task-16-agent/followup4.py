import json
from pathlib import Path
from make_sources import specs
U={92:['https://help.otter.ai/hc/en-us/articles/4412365535895-Does-Otter-offer-an-open-API'],95:['https://docs.reducto.ai/reference/llms.txt','https://docs.reducto.ai/reference/credit-usage/index.md'],99:['https://transcriptapi.com/docs/api-reference/','https://transcriptapi.com/docs/billing/']}
Path('work/task-16-agent/sources-004.json').write_text(json.dumps({'sources':specs(U)},indent=2)+'\n',encoding='utf-8')
