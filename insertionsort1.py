# https://www.hackerrank.com/challenges/insertionsort1/problem
def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = value
    print(*arr)

if __name__ == '__main__':
    n = int(input())
    insertionSort1(n, list(map(int, input().split())))
