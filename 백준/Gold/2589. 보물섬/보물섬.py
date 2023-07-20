import sys
input = sys.stdin.readline
from collections import deque

def possible(a, b):
    return 0 <= a < sero and 0 <= b < garo

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    visited[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if treasure_map[nx][ny] == 'W':
                continue
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = visited[cur_x][cur_y] + 1
            q.append((nx, ny))
    ans = 0
    for i in range(sero):
        temp = max(visited[i])
        ans = max(ans, temp)
    return ans

sero, garo = map(int, input().split())
treasure_map = list(input().strip() for _ in range(sero))
treasure = 0
for i in range(sero):
    for j in range(garo):
        if treasure_map[i][j] == 'L':
            visited = [[-1] * garo for _ in range(sero)]
            treasure = max(treasure, bfs(i, j))
print(treasure)