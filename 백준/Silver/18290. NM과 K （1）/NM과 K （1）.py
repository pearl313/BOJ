import sys
input = sys.stdin.readline

def possible(a, b):
    return 0 <= a < n and 0 <= b < m

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y, total):
    global ans, k
    if k == 0:
        ans = max(ans, total)
        return
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if visited[i][j]:
                continue
            ok = True
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if not possible(nx, ny):
                    continue
                if visited[nx][ny]:
                    ok = False
            if ok:
                visited[i][j] = True
                k -= 1
                dfs(i, j, total + board[i][j])
                visited[i][j] = False
                k += 1


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = -10000
dfs(0, 0, 0)
print(ans)