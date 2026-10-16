# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
input()
scores = sorted(set(map(int, input().split())))
print(scores[-2])
