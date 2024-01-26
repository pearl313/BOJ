import sys
input = sys.stdin.readline

s = list(input().strip())
cnt = 0
temp = s[0]
for i in range(len(s)):
    if s[i] == temp:
        continue
    else:
        if s[i] == s[i - 1]:
            continue
        else:
            cnt += 1
print(cnt)