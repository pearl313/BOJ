import sys
input = sys.stdin.readline
from collections import deque

def possible(a, b):
    return 0 <= a < r and 0 <= b < c

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y):
    global visited, temp_v, temp_c
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if garden[nx][ny] == '#':
                continue
            if garden[nx][ny] == 'v':
                temp_v += 1
            if garden[nx][ny] == 'o':
                temp_c += 1
            q.append((nx, ny))
            visited[nx][ny] = True

r, c = map(int, input().split())
garden = [input().strip() for _ in range(r)]
visited = [[False] * c for _ in range(r)]

cnt_v, cnt_c = 0, 0
temp_v, temp_c = 0, 0
for i in range(r):
    for j in range(c):
        if garden[i][j] != '#' and not visited[i][j]:
            if garden[i][j] == 'v':
                temp_v += 1
            elif garden[i][j] == 'o':
                temp_c += 1
            bfs(i, j)
            if temp_v >= temp_c:
                cnt_v += temp_v
            else:
                cnt_c += temp_c
            temp_v, temp_c = 0, 0
print(cnt_c, cnt_v)