# https://www.hackerrank.com/challenges/hex-color-code/problem
import re
inside = False
for _ in range(int(input())):
    for part in re.split(r'([{}])', input()):
        if part == '{':
            inside = True
        elif part == '}':
            inside = False
        elif inside:
            for color in re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b', part):
                print(color)
