# https://www.hackerrank.com/challenges/html-parser-part-1/problem
from html.parser import HTMLParser

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        self.attributes(attrs)

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        self.attributes(attrs)

    def attributes(self, attrs):
        for name, value in attrs:
            print('->', name, '>', value)

Parser().feed('\n'.join(input() for _ in range(int(input()))))
