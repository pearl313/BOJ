import sys
input = sys.stdin.readline
from collections import deque

def possible(a, b):
    return 0 <= a < I and 0 <= b < I

dxy = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2))

def bfs(x, y):
    dist[x][y] += 1
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        if cur_x == end_x and cur_y == end_y:
            return
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if dist[nx][ny] != -1:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[cur_x][cur_y] + 1

T = int(input())
for _ in range(T):
    I = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    dist = [[-1] * I for _ in range(I)]
    bfs(start_x, start_y)
    print(dist[end_x][end_y])