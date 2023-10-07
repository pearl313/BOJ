import sys
input = sys.stdin.readline

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def possible(a, b):
    return 0 <= a < 5 and 0 <= b < 5

def dfs(x, y, time, apple):
    if time == 0:
        if apple >= 2:
            print(1)
            exit()
        return
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if board[nx][ny] == -1:
            continue
        if visited[nx][ny]:
            continue
        if board[nx][ny] == 1:
            time -= 1
            visited[nx][ny] = True
            apple += 1
            dfs(nx, ny, time, apple)
            time += 1
            visited[nx][ny] = False
            apple -= 1
        time -= 1
        visited[nx][ny] = True
        dfs(nx, ny, time, apple)
        time += 1
        visited[nx][ny] = False

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
visited = [[False] * 5 for _ in range(5)]
visited[r][c] = True
dfs(r, c, 3, 0)
print(0)