import sys
input = sys.stdin.readline

n = int(input())
condo = sorted(list(map(int, input().split())) for _ in range(n))
ans = 0
cost = 1e10
for i in range(n):
    c = condo[i][1]
    if c < cost:
        cost = c
        ans += 1
print(ans)