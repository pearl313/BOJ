import sys
from collections import deque
input = sys.stdin.readline

def possible(x, y):
    return 0 <= x < N and 0 <= y < M

# 사람 찾는 BFS 함수
def BFS(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if possible(nx, ny) and not visited[nx][ny]:
                if campus[nx][ny] == 'X':
                    continue
                elif campus[nx][ny] == 'P':
                    cnt += 1
                q.append((nx, ny))
                visited[nx][ny] = 1

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
campus = list(input() for _ in range(N))

# 우선 도연이 위치 찾기
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            doy_x, doy_y = i, j

visited = [[0] * M for _ in range(N)]
cnt = 0
BFS(doy_x, doy_y)

print(cnt if cnt else 'TT')