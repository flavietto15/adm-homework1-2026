# https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    distance, speed = x2 - x1, v1 - v2
    if speed == 0:
        return 'YES' if distance == 0 else 'NO'
    return 'YES' if distance % speed == 0 and distance // speed >= 0 else 'NO'

if __name__ == '__main__':
    print(kangaroo(*map(int, input().split())))
