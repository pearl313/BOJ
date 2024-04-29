import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

ls = [0] * (n + 1)

for i in range(2, n + 1):
    if ls[i]:
        continue
    for j in range(i, n + 1, i):
        if j % i == 0:
            ls[j] = max(ls[j], i)

ans = 0
for i in ls:
    if i <= k:
        ans += 1
print(ans - 1)