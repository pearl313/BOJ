import sys, heapq
input = sys.stdin.readline
from collections import deque

def possible(a, b):
    return 0 <= a < N and 0 <= b < M

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def cheese(x, y):
    q = []
    INF = 1e10
    dist = [[INF] * M for _ in range(N)]
    heapq.heappush(q, (board[x][y], x, y))
    dist[x][y] = board[x][y]
    while q:
        dist_xy, cur_x, cur_y = heapq.heappop(q)
        if dist_xy != dist[cur_x][cur_y]:
            continue
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if dist[nx][ny] > dist[cur_x][cur_y] + board[nx][ny]:
                dist[nx][ny] = dist[cur_x][cur_y] + board[nx][ny]
                heapq.heappush(q, (dist[nx][ny], nx, ny))
    time = 0
    for i in dist:
        time = max(time, max(i))
    print(time)
    last = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and dist[i][j] == time:
                last += 1
    print(last)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cheese(0, 0)