import json
from pathlib import Path
p=Path('work/task-15-agent');s=json.loads((p/'scopes.json').read_text());src=[]
for a,u in [(86,'https://static.developer.intuit.com/output_html/qbo/docs/api/accounting/all-entities.html'),(89,'https://docs.ramp.com/llms-guides/sandbox-access.txt'),(90,'https://www.pitchbook.com/help/PitchBook-api'),(90,'https://www.pitchbook.com/products/pitchbooks-ai-capabilities')]:
 src.append(dict(app_id=a,url=u,kind='primary_docs' if a!=90 else 'official_product_page',scope=s[str(a)],environments=['testing','production'],attribution_basis='Official vendor documentation domain; alternate static export or canonical hostname for previously inaccessible page.',attribution_by='codex-task15-researcher'))
(p/'sources-003.json').write_text(json.dumps({'sources':src},indent=2),encoding='utf8')
