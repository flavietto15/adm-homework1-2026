# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
import re
for _ in range(int(input())):
    line = input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )',
                 lambda m: 'and' if m[0] == '&&' else 'or', line))
