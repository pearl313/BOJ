import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[False] * 5 for _ in range(5)]

def possible(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def dfs(x, y, apple, cnt):
    global ans
    if apple == 3:
        ans = min(ans, cnt)
        return
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        if board[nx][ny] == -1:
            continue
        if board[nx][ny] == 1:
            visited[nx][ny] = True
            new_board[x][y] = -1
            dfs(nx, ny, apple + 1, cnt + 1)
            visited[nx][ny] = False
            new_board[x][y] = board[x][y]

        visited[nx][ny] = True
        new_board[x][y] = -1
        dfs(nx, ny, apple, cnt + 1)
        visited[nx][ny] = False
        new_board[x][y] = board[x][y]

ans = 1e10
new_board = [i[:] for i in board]
visited[r][c] = True
dfs(r, c, 0, 0)
print(ans if ans != 1e10 else -1)