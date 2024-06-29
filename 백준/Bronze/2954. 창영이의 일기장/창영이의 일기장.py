import sys
input = sys.stdin.readline

s = input().strip()
ans = ''
i = 0
while i < len(s):
    ans += s[i]
    if s[i] in 'aeiou':
        i += 3
    else:
        i += 1
print(ans)