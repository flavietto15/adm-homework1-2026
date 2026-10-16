# https://www.hackerrank.com/challenges/symmetric-difference/problem
input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))
print(*sorted(a ^ b), sep='\n')
