import sys
input = sys.stdin.readline
from collections import deque

def possible(a, b):
    return 0 <= a < N and 0 <= b < M

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def set_wall(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                set_wall(cnt + 1)
                arr[i][j] = 0

def virus():
    q = deque()
    check = [i[:] for i in arr]
    for i in virus_ls:
        q.append(i)
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if check[nx][ny] == 1:
                continue
            if check[nx][ny] == 0:
                check[nx][ny] = 2
                q.append((nx, ny))
    global ans
    cnt = 0
    for i in range(N):
        cnt += check[i].count(0)
    ans = max(ans, cnt)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
zero_ls = []
virus_ls = []
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_ls.append((i, j))
        if arr[i][j] == 2:
            virus_ls.append((i, j))
visited_wall = [False for _ in range(len(zero_ls))]
set_wall(0)
print(ans)