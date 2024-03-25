import sys
input = sys.stdin.readline

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def DFS(x, y):
    global home
    visited[x][y] = True
    home += 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if arr[nx][ny] == '0':
            continue
        if visited[nx][ny]:
            continue
        DFS(nx, ny)

N = int(input())
arr = [input().strip() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = 0
home = 0
home_ls = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            cnt += 1
            DFS(i, j)
            home_ls.append(home)
            home = 0
print(cnt)
home_ls.sort()
for i in home_ls:
    print(i)