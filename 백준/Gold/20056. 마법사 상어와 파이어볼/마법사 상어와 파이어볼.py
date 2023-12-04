import sys
input = sys.stdin.readline

# 파이어볼의 방향
dxy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 파이어볼이 움직인 후에 변한 위치 저장
def change_board():
    global board
    board = [[[] for _ in range(N)] for _ in range(N)]
    for x, y, m, s, d in fire:
        board[x][y].append([m, s, d])

# 파이어볼이 합쳐진 후에 변한 정보 저장
def change_fire():
    global fire
    fire = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                for k in range(len(board[i][j])):
                    fire.append([i, j, board[i][j][k][0], board[i][j][k][1], board[i][j][k][2]])

# 파이어볼 움직이는 함수
def move():
    global fire
    for i in range(len(fire)):
        x, y, m, s, d = fire[i][0], fire[i][1], fire[i][2], fire[i][3], fire[i][4]
        nx = (x + dxy[d][0] * s + 2500) % N
        ny = (y + dxy[d][1] * s + 2500) % N
        fire[i] = [nx, ny, m, s, d]
    change_board()

# 파이어볼 합쳐지는 함수
def merge():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                cnt = len(board[i][j])
                total_m = 0
                total_s = 0
                d_ls = []
                for m, s, d in board[i][j]:
                    total_m += m
                    total_s += s
                    d_ls.append(d % 2)
                board[i][j] = []
                if total_m // 5:
                    if sum(d_ls) == 0 or sum(d_ls) == cnt:
                        for k in range(4):
                            board[i][j].append([total_m // 5, total_s // cnt, k * 2])
                    else:
                        for k in range(4):
                            board[i][j].append([total_m // 5, total_s // cnt, k * 2 + 1])
    change_fire()


N, M, K = map(int, input().split())
# 파이어볼 정보 저장
fire = [list(map(int, input().split())) for _ in range(M)]
# 각 파이어볼 위치에 정보 저장
board = [[[] for _ in range(N)] for _ in range(N)]
for x, y, m, s, d in fire:
    board[x - 1][y - 1].append([m, s, d])
for i in range(K):
    move()
    merge()

ans = 0
for x, y, m, s, d in fire:
    ans += m
print(ans)