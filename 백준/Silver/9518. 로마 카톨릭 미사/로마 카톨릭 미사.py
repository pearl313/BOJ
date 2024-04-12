import sys
input = sys.stdin.readline


r, s = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

dxy = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def possible(x, y):
    return 0 <= x < r and 0 <= y < s

def handShake(arr):
    cnt = 0
    for x, y in people:
        for i in range(8):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if not possible(nx, ny):
                continue
            if arr[nx][ny] == '.':
                continue
            cnt += 1

    return cnt // 2

people = []
seat = []
for i in range(r):
    for j in range(s):
        if arr[i][j] == 'o':
            people.append((i, j))
        else:
            seat.append((i, j))

if not seat:
    print(handShake(arr))
    exit()
else:
    ans = -1e10
    for x, y in seat:
        arr[x][y] = 'o'
        people.append((x, y))
        ans = max(ans, handShake(arr))
        arr[x][y] = '.'
        people.pop()
    print(ans)