# https://www.hackerrank.com/challenges/strange-advertising/problem
def viralAdvertising(n):
    shared, total = 5, 0
    for _ in range(n):
        liked = shared // 2
        total += liked
        shared = liked * 3
    return total

if __name__ == '__main__':
    print(viralAdvertising(int(input())))
