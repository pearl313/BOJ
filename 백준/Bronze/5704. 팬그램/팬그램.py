import sys
input = sys.stdin.readline

while True:
    word = input().strip()
    if word == '*':
        exit()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    check = [0] * 26

    for i in word:
        if i == ' ':
            continue
        check[alphabet.index(i)] = 1

    print('Y' if sum(check) == 26 else 'N')