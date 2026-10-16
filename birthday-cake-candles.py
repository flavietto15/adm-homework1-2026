# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)

if __name__ == '__main__':
    input()
    print(birthdayCakeCandles(list(map(int, input().split()))))
