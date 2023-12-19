import sys
input = sys.stdin.readline
from collections import deque

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def possible(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs_normal(color, x, y):
    global visited, normal
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx = cur_x + dx
            ny = cur_y + dy
            if not possible(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if paint[nx][ny] != color:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    normal += 1

def bfs_abnormal(color, x, y):
    global visited, abnormal
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx = cur_x + dx
            ny = cur_y + dy
            if not possible(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if paint[nx][ny] != color:
                if color == 'R' or color == 'G':
                    if paint[nx][ny] == 'R' or paint[nx][ny] == 'G':
                        q.append((nx, ny))
                        visited[nx][ny] = True
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    abnormal += 1


n = int(input())
paint = [input().strip() for _ in range(n)]
normal = 0
abnormal = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_normal(paint[i][j], i, j)

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_abnormal(paint[i][j], i, j)
            
print(normal, abnormal)