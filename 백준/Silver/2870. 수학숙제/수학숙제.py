import sys
input = sys.stdin.readline

M = int(input())
ans = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
num = ''
for i in range(M):
    word = input().strip()
    for j in range(len(word)):
        if not word[j] in alphabet:
            num += word[j]
        elif word[j] in alphabet:
            if len(num) == 0:
                continue
            ans.append(int(num))
            num = ''
        if j == len(word) - 1 and not word[j] in alphabet and len(num) != 0:
            ans.append(int(num))
            num = ''
ans.sort()
for n in ans:
    print(n)