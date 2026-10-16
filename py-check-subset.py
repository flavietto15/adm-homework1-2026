# https://www.hackerrank.com/challenges/py-check-subset/problem
for _ in range(int(input())):
    input()
    a = set(map(int, input().split()))
    input()
    b = set(map(int, input().split()))
    print(a <= b)
