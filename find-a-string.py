# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    return sum(string.startswith(sub_string, i)
               for i in range(len(string) - len(sub_string) + 1))

if __name__ == '__main__':
    print(count_substring(input(), input()))
