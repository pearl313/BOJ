import sys
from collections import deque
input = sys.stdin.readline

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == '0':
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[cur_x][cur_y] + 1

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
BFS(0, 0)
print(visited[N - 1][M - 1])