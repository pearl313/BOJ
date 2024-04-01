import sys, heapq
input = sys.stdin.readline
from collections import deque

l, w = map(int, input().split())
arr = [input().strip() for _ in range(l)]

def possible(a, b):
    return 0 <= a < l and 0 <= b < w

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y):
    visited = [[-1] * w for _ in range(l)]
    visited[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if visited[nx][ny] != -1:
                continue
            if arr[nx][ny] == 'W':
                continue
            visited[nx][ny] = visited[cur_x][cur_y] + 1
            q.append((nx, ny))

    max_val = -1e10
    for i in visited:
        max_val = max(max_val, max(i))
    return max_val

ans = -1e10
for i in range(l):
    for j in range(w):
        if arr[i][j] == 'W':
            continue
        ans = max(ans, bfs(i, j))

print(ans)