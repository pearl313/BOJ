import sys
input = sys.stdin.readline

def gravity(ls):  # 중력 작용
    for i in range(len(ls[0])):
        last = len(ls)
        for j in range(len(ls) - 1, -1, -1):
            if ls[j][i] == 0:
                continue
            last -= 1
            ls[last][i] = ls[j][i]
        for j in range(last - 1, -1, -1):
            ls[j][i] = 0

def check_vertical(copy_board): # 세로
    for y in range(7):
        ls = []
        tmp = []
        for x in range(7):
            if copy_board[x][y] == 0:
                if tmp:
                    ls.append(tmp)
                    tmp = []
            elif x == 6:
                if copy_board[x][y] > 0:
                    tmp.append([copy_board[x][y], x, y])
                    ls.append(tmp)
                else:
                    ls.append(tmp)
            elif copy_board[x][y] > 0:
                tmp.append([copy_board[x][y], x, y])
        for tmp in ls:
            size = len(tmp)
            for num, a, b in tmp:
                if num == size:
                    check_bomb[a][b] = True

def check_horizontal(copy_board): # 가로
    for x in range(7):
        ls = []
        tmp = []
        for y in range(7):
            if copy_board[x][y] == 0:
                if tmp:
                    ls.append(tmp)
                    tmp = []
            elif y == 6:
                if copy_board[x][y] > 0:
                    tmp.append([copy_board[x][y], x, y])
                    ls.append(tmp)
                else:
                    ls.append(tmp)
            elif copy_board[x][y] > 0:
                tmp.append([copy_board[x][y], x, y])
        for tmp in ls:
            size = len(tmp)
            for num, a, b in tmp:
                if num == size:
                    check_bomb[a][b] = True



def can_bomb():  # 하나라도 True이면 True
    return any([any(x) for x in check_bomb])

def bomb():  # 폭발
    for x in range(7):
        for y in range(7):
            if check_bomb[x][y]:
                copy_board[x][y] = 0

def calc():  # 정답계산
    total = 0
    for i in range(7):
        for j in range(7):
            if copy_board[i][j] > 0:
                total += 1
    return total


board = [list(map(int, input().split())) for _ in range(7)]
ball = int(input())
ans = 55
for i in range(7):  # 1행의 모든 칸에 숫자를 놔보기
    copy_board = [i[:] for i in board]
    copy_board[0][i] = ball
    gravity(copy_board)
    while 1:  # 가로, 세로그룹들을 확인해서 터질게 있으면 무한반복
        check_bomb = [[False] * 7 for _ in range(7)]
        # 가로 체크
        check_horizontal(copy_board)
        # 세로 체크
        check_vertical(copy_board)
        # 폭발 가능한게 없으면 중단
        if not can_bomb():
            break
        # 폭발
        bomb()
        # 중력
        gravity(copy_board)
    # 정답 갱신
    ans = min(ans, calc())
print(ans)