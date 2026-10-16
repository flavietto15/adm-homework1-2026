# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
import numpy
shape = tuple(map(int, input().split()))
print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int))
