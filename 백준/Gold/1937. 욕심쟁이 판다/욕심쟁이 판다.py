import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def possible(a, b):
    return 0 <= a < n and 0 <= b < n

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if ls[nx][ny] <= ls[x][y]:
            continue
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        dfs(i, j)

ans = 0
for i in dp:
    ans = max(max(i), ans)
print(ans)