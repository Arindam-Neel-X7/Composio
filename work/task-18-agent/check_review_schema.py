import json
from pathlib import Path

schema = json.loads(Path('schemas/record.json').read_text(encoding='utf-8'))
defs = schema.get('$defs', {})
print("review def:")
print(json.dumps(defs.get('review', {}), indent=2))
