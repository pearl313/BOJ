import sys
input = sys.stdin.readline
from collections import deque

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def BFS(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = (cur_x + dx) % h, (cur_y + dy) % w
            if visited[nx][ny]:
                continue
            if map_ls[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True


h, w = map(int, input().split())
map_ls = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
island = 0
for i in range(h):
    for j in range(w):
        if map_ls[i][j] == 0 and not visited[i][j]:
            BFS(i, j)
            island += 1
print(island)