import sys, heapq
input = sys.stdin.readline
from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def possible(a, b):
    return 0 <= a < N and 0 <= b < M

def dfs():
    global cnt
    check = [i[:] for i in box]
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if box[nx][ny] == -1 or box[nx][ny] == 1:
                continue
            if dist[nx][ny] != -1:
                continue
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))
            check[nx][ny] = 1

    ans = 0
    for i in range(N):
        if 0 in check[i]:
            print('-1')
            exit()
        else:
            ans = max(ans, max(dist[i]))
    return ans

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
no = True
dist = [[-1] * M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0
    if 0 in box[i]:
        no = False
if no:
    print(0)
else:
    cnt = 0
    print(dfs())
