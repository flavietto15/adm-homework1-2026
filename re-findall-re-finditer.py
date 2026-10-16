# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
import re
vowels = re.findall(r'(?<=[b-df-hj-np-tv-z])[aeiou]{2,}(?=[b-df-hj-np-tv-z])', input(), re.I)
print(*vowels or [-1], sep='\n')
