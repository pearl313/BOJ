import sys, heapq
input = sys.stdin.readline
from collections import deque

def possible(a, b):
    return 0 <= a < n and 0 <= b < n

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dijkstra(x, y):
    q = []
    INF = 1e10
    dist = [[INF] * n for _ in range(n)]
    heapq.heappush(q, (cave[x][y], x, y))
    dist[x][y] = cave[x][y]

    while q:
        dist_xy, cur_x, cur_y = heapq.heappop(q)
        if dist_xy != dist[cur_x][cur_y]:
            continue
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if dist[nx][ny] > dist[cur_x][cur_y] + cave[nx][ny]:
                dist[nx][ny] = dist[cur_x][cur_y] + cave[nx][ny]
                heapq.heappush(q, (dist[nx][ny], nx, ny))
    return dist[n - 1][n - 1]

t = 1
while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    print(f'Problem {t}: {dijkstra(0, 0)}')
    t += 1