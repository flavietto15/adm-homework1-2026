# https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque
for _ in range(int(input())):
    input()
    blocks = deque(map(int, input().split()))
    previous = float('inf')
    possible = True
    while blocks:
        current = blocks.popleft() if blocks[0] >= blocks[-1] else blocks.pop()
        if current > previous:
            possible = False
            break
        previous = current
    print('Yes' if possible else 'No')
