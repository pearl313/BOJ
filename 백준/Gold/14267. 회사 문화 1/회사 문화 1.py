import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        value[nxt] += value[cur]
        dfs(nxt, cur)

n, m = map(int, input().split())
num = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    graph[num[i]].append(i)
value = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    value[a] += b
dfs(1, 0)
print(*value[1:])