import sys
input = sys.stdin.readline

def find_row():
    global ans
    for i in range(n):
        row_cnt = 1
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                row_cnt += 1
                ans = max(ans, row_cnt)
            else:
                row_cnt = 1

def find_column():
    global ans
    for i in range(n):
        col_cnt = 1
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                col_cnt += 1
                ans = max(ans, col_cnt)
            else:
                col_cnt = 1

n = int(input())
board = [list(input().strip()) for _ in range(n)]
ans = 0
find_row()
find_column()
for i in range(n):
    for j in range(n - 1):
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            find_row()
            find_column()
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if board[j][i] != board[j + 1][i]:
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
            find_row()
            find_column()
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
print(ans)