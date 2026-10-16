# https://www.hackerrank.com/challenges/string-validators/problem
s = input()
for check in (str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper):
    print(any(map(check, s)))
