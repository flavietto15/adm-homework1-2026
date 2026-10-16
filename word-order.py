# https://www.hackerrank.com/challenges/word-order/problem
from collections import Counter
counts = Counter(input() for _ in range(int(input())))
print(len(counts))
print(*counts.values())
