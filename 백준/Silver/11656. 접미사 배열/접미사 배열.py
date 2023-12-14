import sys
input = sys.stdin.readline

s = input().strip()
ans = []
for i in range(len(s)):
    ans.append(s[i:])
for i in sorted(ans):
    print(i)