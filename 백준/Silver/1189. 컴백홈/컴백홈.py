import sys
input = sys.stdin.readline

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def possible(a, b):
    return 0 <= a < r and 0 <= b < c

def dfs(x, y, cnt):
    global ans
    if x == 0 and y == c - 1:
        if cnt == k:
            ans += 1
        return
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if arr[nx][ny] == 'T':
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, cnt + 1)
        visited[nx][ny] = False

r, c, k = map(int, input().split())
arr = [input().strip() for _ in range(r)]
visited = [[False] * c for _ in range(r)]
ans = 0
visited[r - 1][0] = True
dfs(r - 1, 0, 1)
print(ans)