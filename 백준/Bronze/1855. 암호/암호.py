import sys
input = sys.stdin.readline

k = int(input())
s = input().strip()

ans = [['' for _ in range(k)] for _ in range(len(s) // k)]
n = 0
for i in range(len(s) // k):
    if i % 2 == 0:
        for j in range(k):
            ans[i][j] = s[n]
            n += 1
    else:
        for j in range(k - 1, -1, -1):
            ans[i][j] = s[n]
            n += 1

pw = ''
for i in range(k):
    for j in range(len(s) // k):
        pw += ans[j][i]

print(pw)