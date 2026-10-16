# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
import re
for _ in range(int(input())):
    card = input()
    valid_format = re.fullmatch(r'[456][0-9]{15}|[456][0-9]{3}(?:-[0-9]{4}){3}', card)
    repeats = re.search(r'([0-9])\1{3}', card.replace('-', ''))
    print('Valid' if valid_format and not repeats else 'Invalid')
