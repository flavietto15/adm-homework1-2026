# https://www.hackerrank.com/challenges/np-arrays/problem
import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1]

if __name__ == '__main__':
    print(arrays(input().split()))
