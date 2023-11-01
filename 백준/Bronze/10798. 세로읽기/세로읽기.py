import sys
input = sys.stdin.readline

ans = ''
word = [input().strip() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if i >= len(word[j]):
            continue
        ans += word[j][i]
print(ans)