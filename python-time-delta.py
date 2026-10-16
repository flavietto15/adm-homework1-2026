# https://www.hackerrank.com/challenges/python-time-delta/problem
from datetime import datetime

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return str(int(abs((datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)).total_seconds())))

if __name__ == '__main__':
    for _ in range(int(input())):
        print(time_delta(input(), input()))
