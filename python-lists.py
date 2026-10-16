# https://www.hackerrank.com/challenges/python-lists/problem
values = []
for _ in range(int(input())):
    command, *args = input().split()
    if command == 'print':
        print(values)
    else:
        getattr(values, command)(*map(int, args))
