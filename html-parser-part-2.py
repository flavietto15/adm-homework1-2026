# https://www.hackerrank.com/challenges/html-parser-part-2/problem
from html.parser import HTMLParser

class Parser(HTMLParser):
    def handle_comment(self, data):
        print('>>> Multi-line Comment' if '\n' in data else '>>> Single-line Comment')
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)

Parser().feed('\n'.join(input() for _ in range(int(input()))))
