# https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
for result in (a + b, a - b, a * b, a // b, a % b, a ** b):
    print(result)
