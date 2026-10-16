# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
input()
values = set(map(int, input().split()))
for _ in range(int(input())):
    command, *args = input().split()
    getattr(values, command)(*map(int, args))
print(sum(values))
