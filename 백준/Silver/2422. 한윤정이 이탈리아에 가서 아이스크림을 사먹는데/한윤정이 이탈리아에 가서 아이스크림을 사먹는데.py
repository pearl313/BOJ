import sys
input = sys.stdin.readline

n, m = map(int, input().split())
no = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    no[a][b] = True
    no[b][a] = True

ans = 0
for i in range(1, n - 1):
    for j in range(i + 1, n):
        for k in range(j + 1, n + 1):
            if no[i][j] or no[i][k] or no[j][k]:
                continue
            ans += 1
print(ans)