import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [0 for _ in range(n)]
visited = [False for _ in range(m + 1)]

def recur(cur):
    if cur == n:
        print(*arr)
        return
    for i in range(1, m + 1):
        if visited[i]:
            continue
        visited[i] = True
        arr[cur] = i
        recur(cur + 1)
        visited[i] = False

recur(0)