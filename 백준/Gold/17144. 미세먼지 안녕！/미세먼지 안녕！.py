import sys
input = sys.stdin.readline
from collections import deque

# 인접한 4방향
dust_dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 위쪽 공기청정기의 방향
upper_air_dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# 아래쪽 공기청정기의 방향
lower_air_dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 범위 안에 드는지 확인하는 함수
def possible(x, y):
    return 0 <= x < r and 0 <= y < c

# 먼지 확산 함수
def dust_spread():
    # 미세먼지 있는 곳 찾아서 저장하기
    q = deque()
    for i in range(r):
        for j in range(c):
            if house[i][j] > 0:
                q.append((i, j))
            elif house[i][j] == -1:
                air_cleaner.append((i, j))
    while q:
        cur_x, cur_y = q.popleft()
        # 현 위치에서 인접한 4방향 중 확산될 수 있는 칸 개수 세기
        cnt = 0
        for dx, dy in dust_dxy:
            nx = cur_x + dx
            ny = cur_y + dy
            if not possible(nx, ny):
                continue
            if house[nx][ny] == -1:
                continue
            cnt += 1
        # 확산하기
        for dx, dy in dust_dxy:
            nx = cur_x + dx
            ny = cur_y + dy
            if not possible(nx, ny):
                continue
            if house[nx][ny] == -1:
                continue
            after_spread[nx][ny] += house[cur_x][cur_y] // 5
        after_spread[cur_x][cur_y] -= (house[cur_x][cur_y] // 5) * cnt

# 공기청정기 작동시키는 함수
def circulation():
    global after_circulation
    n = 1
    visited = [[False] * c for _ in range(r)]
    while air_cleaner:
        cur_x, cur_y = air_cleaner.popleft()
        after_circulation[cur_x][cur_y] = -1
        visited[cur_x][cur_y] = True
        # 위쪽 공기청정기 작동
        if n == 1:
            cur_x += upper_air_dxy[0][0]
            cur_y += upper_air_dxy[0][1]
            for dx, dy in upper_air_dxy:
                while possible(cur_x + dx, cur_y + dy):
                    nx = cur_x + dx
                    ny = cur_y + dy
                    visited[cur_x][cur_y] = True
                    if after_spread[cur_x][cur_y]:
                        if after_spread[nx][ny] == -1:
                            break
                        if possible(nx, ny):
                            after_circulation[nx][ny] = after_spread[cur_x][cur_y]
                    cur_x, cur_y = nx, ny
            n += 1
            continue
        # 아래쪽 공기청정기 작동
        cur_x += lower_air_dxy[0][0]
        cur_y += lower_air_dxy[0][1]
        visited[cur_x][cur_y] = True
        for dx, dy in lower_air_dxy:
            while possible(cur_x + dx, cur_y + dy):
                nx = cur_x + dx
                ny = cur_y + dy
                visited[cur_x][cur_y] = True
                if after_spread[cur_x][cur_y]:
                    if after_spread[nx][ny] == -1:
                        break
                    if possible(nx, ny):
                        after_circulation[nx][ny] = after_spread[cur_x][cur_y]
                cur_x, cur_y = nx, ny

    # 나머지 부분 채워주기
    for i in range(r):
        for j in range(c):
            if visited[i][j]:
                continue
            after_circulation[i][j] = after_spread[i][j]
            
r, c, t = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(r)]
air_cleaner = deque()
total = 0
for time in range(t):
    # 먼지 찾아서 동시에 확산 시키기
    after_spread = [i[:] for i in house]
    dust_spread()
    # 공기청정기 작동
    after_circulation = [[0] * c for _ in range(r)]
    circulation()
    house = [i[:] for i in after_circulation]
    if time == t - 1:
        # 남은 미세먼지 양 구하기
        for i in range(r):
            for j in range(c):
                if house[i][j] > 0:
                    total += house[i][j]
print(total)