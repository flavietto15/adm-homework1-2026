# https://www.hackerrank.com/challenges/py-set-union/problem
input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))
print(len(a | b))
