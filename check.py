"""Check local input/output cases; this does not prove HackerRank acceptance."""
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
items = json.loads((root / 'manifest.json').read_text())
cases = json.loads((root / 'cases.json').read_text())
failures = []
count = 0
for item in items:
    slug = item['slug']
    if slug not in cases:
        failures.append(slug + ': missing test cases')
    for index, case in enumerate(cases.get(slug, []), 1):
        count += 1
        result = subprocess.run([sys.executable, str(root / item['path'])],
                                input=case['input'], text=True, capture_output=True,
                                timeout=10)
        actual = '\n'.join(line.rstrip() for line in result.stdout.splitlines()).rstrip()
        expected = '\n'.join(line.rstrip() for line in case['output'].splitlines()).rstrip()
        if result.returncode or actual != expected:
            failures.append(f'{slug} case {index}: expected {expected!r}, '
                            f'got {actual!r}; {result.stderr}')
print(f'{count} local cases across {len(items)} exercises; {len(failures)} failures.')
for failure in failures:
    print(failure)
raise SystemExit(bool(failures))
