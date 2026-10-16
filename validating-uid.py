# https://www.hackerrank.com/challenges/validating-uid/problem
import re
for _ in range(int(input())):
    uid = input()
    valid = (re.fullmatch(r'[A-Za-z0-9]{10}', uid) is not None
             and len(set(uid)) == 10
             and len(re.findall(r'[A-Z]', uid)) >= 2
             and len(re.findall(r'[0-9]', uid)) >= 3)
    print('Valid' if valid else 'Invalid')
