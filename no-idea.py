# https://www.hackerrank.com/challenges/no-idea/problem
input()
values = list(map(int, input().split()))
a, b = set(map(int, input().split())), set(map(int, input().split()))
print(sum((x in a) - (x in b) for x in values))
