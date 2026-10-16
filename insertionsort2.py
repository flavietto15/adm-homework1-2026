# https://www.hackerrank.com/challenges/insertionsort2/problem
def insertionSort2(n, arr):
    for j in range(1, n):
        value = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > value:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = value
        print(*arr)

if __name__ == '__main__':
    n = int(input())
    insertionSort2(n, list(map(int, input().split())))
