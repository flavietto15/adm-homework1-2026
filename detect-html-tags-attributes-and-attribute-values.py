# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
from html.parser import HTMLParser

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print('->', name, '>', value)

    handle_startendtag = handle_starttag

Parser().feed('\n'.join(input() for _ in range(int(input()))))
