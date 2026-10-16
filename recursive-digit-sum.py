# https://www.hackerrank.com/challenges/recursive-digit-sum/problem
def superDigit(n, k):
    total = sum(map(int, n)) * k
    while total >= 10:
        total = sum(map(int, str(total)))
    return total

if __name__ == '__main__':
    n, k = input().split()
    print(superDigit(n, int(k)))
