import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
empty = []

# 빈 칸 위치 저장 및 개수 체크
cnt = 0
for i in range(9):
    for j in range(9):
        if arr[i][j]:
            continue
        cnt += 1
        empty.append((i, j))

arr2 = [i[:] for i in arr]


# 가능한 숫자 후보 찾는 함수
def possible(x, y):
    ls = []
    num = [False] * 10
    # 가로 확인
    for i in range(9):
        num[arr2[x][i]] = True
    # 세로 확인
    for i in range(9):
        num[arr2[i][y]] = True
    # 정사각형 확인
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            num[arr2[x + i][y + j]] = True

    for i in range(1, 10):
        if not num[i]:
            ls.append(i)

    return ls


def recur(cur):
    if cur == cnt:
        for k in arr2:
            print(*k)
        exit()

    x, y = empty[cur][0], empty[cur][1]
    ls = possible(x, y)
    for i in ls:
        arr2[x][y] = i
        recur(cur + 1)
        arr2[x][y] = 0

recur(0)