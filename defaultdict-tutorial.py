# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict
n, m = map(int, input().split())
positions = defaultdict(list)
for i in range(1, n + 1):
    positions[input()].append(i)
for _ in range(m):
    print(*positions.get(input(), [-1]))
