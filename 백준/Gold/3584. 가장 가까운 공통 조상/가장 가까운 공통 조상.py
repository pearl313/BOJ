import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        depth[nxt] = depth[cur] + 1
        dfs(nxt, cur)

def find_parents(x, y):
    while depth[x] != depth[y]:
        if depth[x] > depth[y]:
            x = parents[x]
        else:
            y = parents[y]

    while x != y:
        x = parents[x]
        y = parents[y]
    return x

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    depth = [0] * (n + 1)
    parents = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        parents[b] = a
    for i in range(1, n + 1):
        if parents[i] == 0:
            dfs(i, 0)
            break
    x, y = map(int, input().split())
    print(find_parents(x, y))