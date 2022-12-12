import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    sentence = input().strip()
    if sentence == '#':
        break
    cnt = 0
    for i in sentence:
        if i in vowel:
            cnt += 1
    print(cnt)