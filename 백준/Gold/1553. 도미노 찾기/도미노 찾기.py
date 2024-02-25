import sys
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(8)]
visited = [[False] * 7 for _ in range(8)]
domino = [[False] * 7 for _ in range(7)]

# 범위 벗어나는지 확인
def possible(a, b):
    return 0 <= a < 8 and 0 <= b < 7

dxy = [(0, 1), (1, 0)]

# 현재 위치에서 가로 세로에 있는 수인데, 안썼어
def check(x, y):
    ls = []
    for i, (dx, dy) in enumerate(dxy):
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        one = min(int(arr[x][y]), int(arr[nx][ny]))
        two = max(int(arr[x][y]), int(arr[nx][ny]))
        if domino[one][two]:
            continue
        ls.append((one, two, i))
    return ls


cnt = 0
# 모든 도미노 숫자 넣어보기
def recur(cur):
    global cnt
    if cur == 28:
        cnt += 1
        return

    x, y = 0, 0
    # 방문하지 않은 곳 찾기
    for i in range(8):
        for j in range(7):
            if not visited[i][j]:
                x, y = i, j
                break
        if x == i and y == j:
            break
    ls = check(x, y)
    for i in ls:
        visited[x][y] = True
        if i[2] == 0:
            visited[x][y + 1] = True
        else:
            visited[x + 1][y] = True
        domino[i[0]][i[1]] = True

        recur(cur + 1)
        visited[x][y] = False
        if i[2] == 0:
            visited[x][y + 1] = False
        else:
            visited[x + 1][y] = False
        domino[i[0]][i[1]] = False

recur(0)
print(cnt)