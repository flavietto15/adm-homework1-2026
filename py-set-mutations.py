# https://www.hackerrank.com/challenges/py-set-mutations/problem
input()
a = set(map(int, input().split()))
for _ in range(int(input())):
    command, _ = input().split()
    getattr(a, command)(set(map(int, input().split())))
print(sum(a))
