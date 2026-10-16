# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
from string import ascii_lowercase

def print_rangoli(size):
    rows = []
    for i in range(size):
        left = ascii_lowercase[size - 1:i:-1]
        row = '-'.join(left + ascii_lowercase[i] + left[::-1])
        rows.append(row.center(4 * size - 3, '-'))
    print(*rows[:0:-1], *rows, sep='\n')

if __name__ == '__main__':
    print_rangoli(int(input()))
