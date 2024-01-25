import sys
input = sys.stdin.readline

s = input().strip()
ans = set()
for i in range(1, len(s) + 1):
    for j in range(len(s)):
        if i == j:
            continue
        if s[j:i] == '':
            continue
        ans.add(s[j:i])
print(len(ans))