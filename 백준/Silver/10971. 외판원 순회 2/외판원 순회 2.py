import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == n:
        route = selected[:] + [selected[0]]
        total = 0
        go = True
        for i in range(n):
            if cost[route[i]][route[i + 1]] == 0:
                go = False
                break
            total += cost[route[i]][route[i + 1]]
        if go:
            ans = min(ans, total)
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        selected.append(i)
        visited[i] = True
        recur(cur + 1)
        selected.pop()
        visited[i] = False

n = int(input())
cost = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
selected = []
visited = [False] * (n + 1)
ans = 1e10
recur(0)
print(ans)