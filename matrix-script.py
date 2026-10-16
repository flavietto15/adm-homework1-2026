# https://www.hackerrank.com/challenges/matrix-script/problem
import re
n, m = map(int, input().split())
rows = [input() for _ in range(n)]
text = ''.join(''.join(column) for column in zip(*rows))
print(re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', text))
