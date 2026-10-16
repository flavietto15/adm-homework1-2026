# https://www.hackerrank.com/challenges/re-split/problem
import re
regex_pattern = r'[,.]'
if __name__ == '__main__':
    print(*re.split(regex_pattern, input()), sep='\n')
