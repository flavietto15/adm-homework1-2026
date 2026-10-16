# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
import xml.etree.ElementTree as ET

def get_attr_number(node):
    return sum(len(element.attrib) for element in node.iter())

if __name__ == '__main__':
    root = ET.fromstring('\n'.join(input() for _ in range(int(input()))))
    print(get_attr_number(root))
