# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
a = set(map(int, input().split()))
results = [a > set(map(int, input().split())) for _ in range(int(input()))]
print(all(results))
