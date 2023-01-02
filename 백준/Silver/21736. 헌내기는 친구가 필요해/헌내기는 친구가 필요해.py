import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def possible(x, y):
    return 0 <= x < N and 0 <= y < M

# 사람 찾는 DFS 함수
def DFS(x, y):
    global cnt
    visited[x][y] = 1
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if possible(nx, ny) and not visited[nx][ny]:
            if campus[nx][ny] == 'O':
                DFS(nx, ny)
            elif campus[nx][ny] == 'P':
                cnt += 1
                DFS(nx, ny)
            elif campus[nx][ny] == 'X':
                continue

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
DFS(doy_x, doy_y)
if cnt == 0:
    cnt = 'TT'
print(cnt)