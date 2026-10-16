# https://www.hackerrank.com/challenges/ginorts/problem
s = input()
def order(c):
    if c.islower():
        return 0, c
    if c.isupper():
        return 1, c
    return 2 + (int(c) % 2 == 0), c
print(''.join(sorted(s, key=order)))
