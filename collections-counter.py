# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
input()
stock = Counter(map(int, input().split()))
revenue = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if stock[size]:
        stock[size] -= 1
        revenue += price
print(revenue)
