import sys, heapq
input = sys.stdin.readline

def possible(a, b):
    return 0 <= a < N and 0 <= b < M

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dijkstra(x, y):
    q = []
    INF = 1e10
    dist = [[INF] * M for _ in range(N)]
    dist[x][y] = 0
    heapq.heappush(q, (0, x, y))

    while q:
        dist_xy, cur_x, cur_y = heapq.heappop(q)
        if dist_xy != dist[cur_x][cur_y]:
            continue
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if dist[nx][ny] > dist[cur_x][cur_y] + int(maze[nx][ny]):
                if int(maze[nx][ny]) == 0:
                    dist[nx][ny] = dist[cur_x][cur_y]
                elif int(maze[nx][ny]) == 1:
                    dist[nx][ny] = dist[cur_x][cur_y] + 1
                heapq.heappush(q, (dist[nx][ny], nx, ny))

    return dist[N - 1][M - 1]

M, N = map(int, input().split())
maze = [input().strip() for _ in range(N)]
print(dijkstra(0, 0))