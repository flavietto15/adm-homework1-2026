# https://www.hackerrank.com/challenges/designer-door-mat/problem
n, m = map(int, input().split())
rows = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
print(*rows, 'WELCOME'.center(m, '-'), *reversed(rows), sep='\n')
