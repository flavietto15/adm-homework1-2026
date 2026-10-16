# https://www.hackerrank.com/challenges/validating-postalcode/problem
import re
regex_integer_in_range = r'[1-9][0-9]{5}$'
regex_alternating_repetitive_digit_pair = r'(?=([0-9])[0-9]\1)'
if __name__ == '__main__':
    p = input()
    print(bool(re.fullmatch(regex_integer_in_range, p)) and
          len(re.findall(regex_alternating_repetitive_digit_pair, p)) < 2)
