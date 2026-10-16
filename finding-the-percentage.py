# https://www.hackerrank.com/challenges/finding-the-percentage/problem
scores = {}
for _ in range(int(input())):
    name, *marks = input().split()
    scores[name] = list(map(float, marks))
marks = scores[input()]
print(f'{sum(marks) / len(marks):.2f}')
