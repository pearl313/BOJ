import sys
from collections import deque
input = sys.stdin.readline

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            # print('*', nx, ny)
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == -1:
                continue
            if visited[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[-1] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        # graph[X].append(Y)
        graph[Y][X] = X
    cnt = 0
    # print(graph)
    # print(visited)
    for i in range(N):
        for j in range(M):
            # print(i, j)
            if graph[i][j] != -1 and not visited[i][j]:
                # print('!')
                cnt += 1
                BFS(i, j)
    print(cnt)
    # print(graph)
    # print(visited)