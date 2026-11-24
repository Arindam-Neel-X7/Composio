import json
from pathlib import Path
W=Path('D:/Composio/work/task-13-agent');ss=json.loads((W/'sources-001.json').read_text())['sources']
new={62:['https://vercel.com/docs/limits/fair-use-guidelines'],68:['https://www.mongodb.com/docs/atlas/api/api-resources/']}
out=[dict(next(s for s in ss if s['app_id']==aid),url=u) for aid,urls in new.items() for u in urls]
(W/'sources-004.json').write_text(json.dumps({'sources':out},indent=2),encoding='utf8')
