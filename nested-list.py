# https://www.hackerrank.com/challenges/nested-list/problem
students = [(input(), float(input())) for _ in range(int(input()))]
second = sorted({score for _, score in students})[1]
print(*sorted(name for name, score in students if score == second), sep='\n')
