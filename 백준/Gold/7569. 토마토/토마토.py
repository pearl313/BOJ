import sys
input = sys.stdin.readline
from collections import deque

# 인접한 6방향 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
dxyz = [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)]

def possible(x, y, z):
    return 0 <= x < h and 0 <= y < n and 0 <= z < m

def bfs():
   global visited, q
   while q:
       cur_x, cur_y, cur_z = q.popleft()
       for dx, dy, dz in dxyz:
           nx = cur_x + dx
           ny = cur_y + dy
           nz = cur_z + dz
           if not possible(nx, ny, nz):
               continue
           if boxes[nx][ny][nz] == -1:
               visited[nx][ny][nz] = 0
               continue
           if visited[nx][ny][nz] >= 0:
               continue
           visited[nx][ny][nz] = visited[cur_x][cur_y][cur_z] + 1
           q.append((nx, ny, nz))
   ans = -1e10
   for i in visited:
       for j in i:
           if -1 in j:
               print(-1)
               exit()
           ans = max(ans, max(j))
   print(ans)
   exit()

m, n, h = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(n)] for __ in range(h)]
q = deque()
visited = [[[-1] * m for _ in range(n)] for __ in range(h)]
zero = False
no = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                q.append((i, j, k))
                visited[i][j][k] = 0
            if boxes[i][j][k] == -1:
                visited[i][j][k] = 0
bfs()