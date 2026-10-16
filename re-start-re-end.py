# https://www.hackerrank.com/challenges/re-start-re-end/problem
import re
s, k = input(), input()
# A lookahead permits overlapping matches without consuming characters.
matches = list(re.finditer('(?=(' + re.escape(k) + '))', s))
for match in matches:
    print((match.start(), match.start() + len(k) - 1))
if not matches:
    print((-1, -1))
