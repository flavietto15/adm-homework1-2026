# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
items = OrderedDict()
for _ in range(int(input())):
    name, price = input().rsplit(' ', 1)
    items[name] = items.get(name, 0) + int(price)
for name, total in items.items():
    print(name, total)
