import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        parents[nxt] = cur
        depth[nxt] = depth[cur] + 1
        dfs(nxt, cur)

def find_parents(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parents[a]
        else:
            b = parents[b]
    while a != b:
        a = parents[a]
        b = parents[b]
    return a

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parents = [0] * (n + 1)
depth = [0] * (n + 1)
dfs(1, 0)
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(find_parents(x, y))