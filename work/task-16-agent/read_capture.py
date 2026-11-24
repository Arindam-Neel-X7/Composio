import json,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
run=sys.argv[1]; app=int(sys.argv[2]); selector=sys.argv[3] if len(sys.argv)>3 else ''
start=int(sys.argv[4]) if len(sys.argv)>4 else 1
end=int(sys.argv[5]) if len(sys.argv)>5 else 100000
D=Path('work/research-runs')/run
for c in json.loads((D/'captures.json').read_text()):
 if c['spec']['app_id']==app and selector in c['spec']['url']:
  print('\nURL',c['spec']['url'],'SNAPSHOT',c['snapshot_ref'])
  for i,l in enumerate((D/c['snapshot_ref']).read_text(encoding='utf-8').splitlines(),1):
   if start<=i<=end: print(f'{i}: {l}')
