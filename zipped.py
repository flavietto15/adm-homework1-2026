# https://www.hackerrank.com/challenges/zipped/problem
n, x = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(x)]
for marks in zip(*subjects):
    print(sum(marks) / x)
