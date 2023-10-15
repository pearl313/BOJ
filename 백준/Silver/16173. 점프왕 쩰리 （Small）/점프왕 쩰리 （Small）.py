import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (1, 0)]

def possible(a, b):
    return 0 < a <= n and 0 < b <= n

def bfs(x, y):
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx * board[cur_x][cur_y], cur_y + dy * board[cur_x][cur_y]
            if not possible(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == -1 or (nx == n and ny == n):
                print('HaruHaru')
                exit()
            visited[nx][ny] = True
            q.append((nx, ny))

n = int(input())
board = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
bfs(1, 1)
print('Hing')