import sys
input = sys.stdin.readline

word = input().strip()

ans = ''
for i in word:
    if i.isupper():
        ans += i

print(ans)