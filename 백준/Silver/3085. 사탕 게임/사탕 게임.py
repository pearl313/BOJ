import sys
input = sys.stdin.readline

def find_row():
    global ans
    for i in range(N):
        count_row = 1
        for j in range(N - 1):
            if board[i][j] == board[i][j + 1]:
                count_row += 1
                ans = max(ans, count_row)
            else:
                count_row = 1

def find_column():
    global ans
    for i in range(N):
        count_column = 1
        for j in range(N - 1):
            if board[j][i] == board[j + 1][i]:
                count_column += 1
                ans = max(ans, count_column)
            else:
                count_column = 1

N = int(input())
board = [list(input().strip()) for _ in range(N)]
ans = 0
# 사탕 개수 찾기
find_row()
find_column()
# 색이 다른 인접한 두 칸 자리 바꿔주기
for i in range(N):
    for j in range(N - 1):
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