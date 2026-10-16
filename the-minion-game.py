# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    kevin = sum(len(string) - i for i, c in enumerate(string) if c in 'AEIOU')
    stuart = len(string) * (len(string) + 1) // 2 - kevin
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Stuart', stuart)

if __name__ == '__main__':
    minion_game(input())
