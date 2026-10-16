# https://www.hackerrank.com/challenges/validate-a-roman-number/problem
import re
regex_pattern = r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
if __name__ == '__main__':
    s = input()
    print(bool(s and re.fullmatch(regex_pattern, s)))
