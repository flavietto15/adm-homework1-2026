# https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter
for letter, count in sorted(Counter(input()).items(), key=lambda p: (-p[1], p[0]))[:3]:
    print(letter, count)
