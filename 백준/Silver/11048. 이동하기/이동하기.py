import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

score = [[-1 for i in range(m)] for j in range(n)]
score[0][0] = mat[0][0]

dx = [1, 0]
dy = [0, 1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n:
                if score[ny][nx] < score[y][x] + mat[ny][nx]:
                    score[ny][nx] = score[y][x] + mat[ny][nx]
                    q.append([ny, nx])
bfs(0, 0)
print(score[-1][-1])