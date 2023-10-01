import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def possible(a, b):
    return 0 <= a < m and 0 <= b < n

def dfs(x, y):
    global ans
    if x == m - 1 and y == n - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if ls[nx][ny] >= ls[x][y]:
            continue
        dp[x][y] += dfs(nx, ny)
    return dp[x][y]

m, n = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * (n + 1) for _ in range(m + 1)]
print(dfs(0, 0))