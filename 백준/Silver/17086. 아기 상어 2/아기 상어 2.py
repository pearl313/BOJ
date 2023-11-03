import sys
input = sys.stdin.readline
from collections import deque

dxy = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def possible(a, b):
    return 0 <= a < n and 0 <= b < m

def bfs():
    global distance
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            dist[nx][ny] = dist[cur_x][cur_y] + 1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dist = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            q.append((i, j))
            dist[i][j] = 0
            visited[i][j] = True
bfs()
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dist[i][j])
print(ans)