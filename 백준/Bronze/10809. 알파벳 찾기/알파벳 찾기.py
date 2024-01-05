import sys
input = sys.stdin.readline

ans = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = list(input().strip())
for i in alphabet:
    if i in s:
        ans.append(s.index(i))
    else:
        ans.append(-1)
print(*ans)