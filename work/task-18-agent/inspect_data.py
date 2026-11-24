import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

with open(ROOT / 'schemas/record.json', 'r', encoding='utf-8') as f:
    schema = json.load(f)

defs = schema.get('$defs', {})
import sys
sys.path.insert(0, str(ROOT))
import inspect
import research_pipeline

print("Source of claim_map:")
print(inspect.getsource(research_pipeline.claim_map))
print("\nSource of claims:")
print(inspect.getsource(research_pipeline.claims))
