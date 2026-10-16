# https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    print(wrap(input(), int(input())))
