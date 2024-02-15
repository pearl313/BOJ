import sys
input = sys.stdin.readline

m, n = map(int, input().split())
ls = sorted(map(int, input().split()))
arr = [0 for _ in range(n)]
visited = [False for _ in range(m)]

def recur(cur):
    if cur == n:
        print(*arr)
        return
    for i in range(m):
        if visited[i]:
            continue
        visited[i] = True
        arr[cur] = ls[i]
        recur(cur + 1)
        visited[i] = False

recur(0)