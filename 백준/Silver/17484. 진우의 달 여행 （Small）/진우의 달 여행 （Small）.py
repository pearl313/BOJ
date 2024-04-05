import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dxy = [(1, -1), (1, 0), (1, 1)]

def possible(x, y):
    return 0 <= x < n and 0 <= y < m

def go(x, y, val,d):
    global ans
    if x == n - 1:
        ans = min(ans, val)
        return
    for i in range(3):
        nx, ny = x + dxy[i][0], y + dxy[i][1]
        if not possible(nx, ny):
            continue
        if i == d:
            continue
        go(nx, ny, val + arr[nx][ny], i)
        
ans = 1e10
for i in range(m):
    go(0, i, arr[0][i], 0)
    go(0, i, arr[0][i], 1)
    go(0, i, arr[0][i], 2)
    
print(ans)