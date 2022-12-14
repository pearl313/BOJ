import sys
input = sys.stdin.readline

cambridge = 'CAMBRIDGE'
word = list(input().strip())
ans = ''
for i in range(len(word)):
    if not word[i] in cambridge:
        ans += word[i]
print(ans)