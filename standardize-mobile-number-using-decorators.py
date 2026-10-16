# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
def wrapper(f):
    def fun(numbers):
        normalized = ['+91 ' + number[-10:-5] + ' ' + number[-5:] for number in numbers]
        return f(normalized)
    return fun

@wrapper
def sort_phone(numbers):
    print(*sorted(numbers), sep='\n')

if __name__ == '__main__':
    sort_phone([input() for _ in range(int(input()))])
