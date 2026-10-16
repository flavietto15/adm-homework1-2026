# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    unique = set(array)
    return sum(unique) / len(unique)

if __name__ == '__main__':
    input()
    print(average(list(map(int, input().split()))))
