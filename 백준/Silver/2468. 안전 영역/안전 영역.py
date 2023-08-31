import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def possible(x, y):
    return 0 <= x < n and 0 <= y < n

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y, num):
    visited[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not possible(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        if area[nx][ny] <= num:
            continue
        dfs(nx, ny, num)

# 모든 범위에서 영역 개수 다 확인해보기
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for a in range(n):
        for b in range(n):
            if not visited[a][b] and area[a][b] > i:
                dfs(a, b, i)
                cnt += 1
    if cnt == 0:
        break
    ans = max(ans, cnt)
print(ans)