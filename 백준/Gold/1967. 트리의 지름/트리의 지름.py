import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, prev):
    for nxt, value in graph[cur]:
        if nxt == prev:
            continue
        depth[nxt] = depth[cur] + value
        dfs(nxt, cur)

n = int(input())
graph = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dfs(1, 0)
max_node = depth.index(max(depth))
depth = [0] * (n + 1)
dfs(max_node, 0)
print(max(depth))