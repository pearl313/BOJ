import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        dfs(nxt, cur)
        size[cur] += size[nxt]

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
size = [1] * (N + 1)
dfs(R, 0)
for _ in range(Q):
    U = int(input())
    print(size[U])