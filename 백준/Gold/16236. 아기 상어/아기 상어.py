import sys
input = sys.stdin.readline
from collections import deque

def possible(a, b):
    return 0 <= a < N and 0 <= b < N

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

N = int(input())
space = [list(map(int, input().split()))for _ in range(N)]
size = 2
total = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            space[i][j] = 0
            start_i, start_j = i, j

while True:
    can_eat = []
    compare = 10e9
    time = 0
    q = deque()
    q.append((start_i, start_j, time))
    visited = [[False] * N for _ in range(N)]
    visited[start_i][start_j] = True
    while q:
        cur_i, cur_j, time = q.popleft()
        if time > compare:
            break
        for dx, dy in dxy:
            nx, ny = cur_i + dx, cur_j + dy
            if not possible(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if space[nx][ny] > size:
                continue
            if space[nx][ny] and space[nx][ny] < size:
                can_eat.append((nx, ny, time + 1))
                compare = time
            visited[nx][ny] = True
            q.append((nx, ny, time + 1))

    if can_eat:
        fish_i, fish_j, time = sorted(can_eat).pop(0)
        space[fish_i][fish_j] = 0
        start_i, start_j = fish_i, fish_j
        cnt += 1
        total += time
        if cnt == size:
            size += 1
            cnt = 0
    else:
        break
print(total)