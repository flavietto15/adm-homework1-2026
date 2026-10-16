# https://www.hackerrank.com/challenges/np-linear-algebra/problem
import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
print(round(float(numpy.linalg.det(a)), 2))
