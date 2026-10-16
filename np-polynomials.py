# https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy
coefficients = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(coefficients, x))
