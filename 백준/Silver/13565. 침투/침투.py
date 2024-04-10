import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def possible(a, b):
    return 0 <= a < n and 0 <= b < m

def dfs(x, y):
    visited[x][y] = True
    if x == n - 1:
        print('YES')
        exit()

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        if arr[nx][ny] == '1':
            continue
        dfs(nx, ny)


for i in range(m):
    if arr[0][i] == '0':
        dfs(0, i)

print('NO')