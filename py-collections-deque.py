# https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque
values = deque()
for _ in range(int(input())):
    command, *args = input().split()
    getattr(values, command)(*args)
print(*values)
