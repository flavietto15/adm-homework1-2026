# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
import re
from email.utils import parseaddr
for _ in range(int(input())):
    line = input()
    _, address = parseaddr(line)
    if re.fullmatch(r'[A-Za-z][A-Za-z0-9_.-]*@[A-Za-z]+\.[A-Za-z]{1,3}', address):
        print(line)
