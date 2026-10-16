"""Run one independent HackerRank solution by its challenge slug."""
import json
from pathlib import Path
import runpy
import sys

root = Path(__file__).resolve().parent
solutions = json.loads((root / 'manifest.json').read_text())
if len(sys.argv) != 2:
    print('Usage: python scripts.py CHALLENGE-SLUG\n')
    print('\n'.join(item['slug'] for item in solutions))
    raise SystemExit(0)
for item in solutions:
    if item['slug'] == sys.argv[1]:
        runpy.run_path(str(root / item['path']), run_name='__main__')
        break
else:
    raise SystemExit('Unknown challenge: ' + sys.argv[1])
