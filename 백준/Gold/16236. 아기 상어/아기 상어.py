import sys
input = sys.stdin.readline
from collections import deque

def possible(a, b):
    return 0 <= a < N and 0 <= b < N

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(x, y, dist):
    global can_eat
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((x, y, dist))
    visited[x][y] = True
    compare = 10e9
    while q:
        cur_x, cur_y, dist = q.popleft()
        if dist > compare:
            continue
        for dx, dy in dxy:
            nx, ny = cur_x + dx, cur_y + dy
            if not possible(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if space[nx][ny] > shark_size:
                continue
            if space[nx][ny] < shark_size and space[nx][ny]:
                can_eat.append((nx, ny, dist + 1))
                compare = dist
            visited[nx][ny] = True
            q.append((nx, ny, dist + 1))

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
time = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_i, shark_j = i, j
            space[i][j] = 0
can_eat = []
bfs(shark_i, shark_j, 0)
while can_eat:
    fish_i, fish_j, dist = sorted(can_eat).pop(0)
    space[fish_i][fish_j] = 0
    time += dist
    cnt += 1
    shark_i, shark_j = fish_i, fish_j
    if cnt == shark_size:
        cnt = 0
        shark_size += 1
    can_eat = []
    bfs(shark_i, shark_j, 0)

print(time)