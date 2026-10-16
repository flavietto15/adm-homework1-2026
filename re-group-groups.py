# https://www.hackerrank.com/challenges/re-group-groups/problem
import re
match = re.search(r'([A-Za-z0-9])\1', input())
print(match.group(1) if match else -1)
