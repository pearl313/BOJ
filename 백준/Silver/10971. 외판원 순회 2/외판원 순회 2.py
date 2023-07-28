import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == n:
        travel = selected[:] + [selected[0]]
        temp = 0
        go = True
        for c in range(n):
            if cost[travel[c]][travel[c + 1]] == 0:
                go = False
                break
            temp += cost[travel[c]][travel[c + 1]]
        if go:
            ans = min(ans, temp)
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