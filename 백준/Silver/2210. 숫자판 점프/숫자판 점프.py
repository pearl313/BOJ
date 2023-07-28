import sys
input = sys.stdin.readline

def possible(a, b):
    return 0 <= a < 5 and 0 <= b < 5

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def numbering(x, y, num):
    if len(num) == 6:
        ans.add(num)
        return
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        numbering(nx, ny, num + board[nx][ny])

board = [list(input().split()) for _ in range(5)]
ans = set()
for i in range(5):
    for j in range(5):
        numbering(i, j, board[i][j])
print(len(ans))