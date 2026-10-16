# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
import xml.etree.ElementTree as ET
maxdepth = 0

def depth(elem, level):
    global maxdepth
    level += 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    root = ET.fromstring('\n'.join(input() for _ in range(int(input()))))
    depth(root, -1)
    print(maxdepth)
