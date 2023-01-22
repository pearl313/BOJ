import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def possible(x, y):
    return 0 <= x < N and 0 <= y < M

def DFS(x, y, cnt):
    global ans
    visited[x][y] = True
    for k in range(4):
        dx, dy = dxy[k]
        nx = x + dx
        ny = y + dy
        if possible(nx, ny) and not visited[nx][ny] and board[x][y] == board[nx][ny]:
            DFS(nx, ny, cnt + 1)
        elif nx == start_i and ny == start_j and cnt >= 4:
            print('Yes')
            exit()
    visited[x][y] = False

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            start_i, start_j = i, j
            ans = False
            cnt = 1
            DFS(i, j, cnt)
            visited[i][j] = True
print('No')