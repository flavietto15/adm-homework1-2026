# https://www.hackerrank.com/challenges/python-sort-sort/problem
n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for row in sorted(rows, key=lambda row: row[k]):
    print(*row)
