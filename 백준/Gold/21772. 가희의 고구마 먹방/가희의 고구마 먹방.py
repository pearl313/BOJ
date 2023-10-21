import sys
input = sys.stdin.readline

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def possible(a, b):
    return 0 <= a < r and 0 <= b < c

def dfs(x, y, yam):
    global t, ans
    if t == 0:
        ans = max(ans, yam)
        return
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if board[nx][ny] == '#':
            continue
        if board[nx][ny] == 'S':
            t -= 1
            board[nx][ny] = '.'
            dfs(nx, ny, yam + 1)
            t += 1
            board[nx][ny] = 'S'
        t -= 1
        dfs(nx, ny, yam)
        t += 1


r, c, t = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
ans = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'G':
            dfs(i, j, 0)
            print(ans)
            exit()