import sys
input = sys.stdin.readline

def dfs(start, end, distance):
    visited[start] = True
    if start == end:
        print(distance)
        return
    for n in graph[start]:
        i, j = n
        if not visited[i]:
            dfs(i, end, distance + j)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))
for _ in range(M):
    start, end = map(int, input().split())
    visited = [False for _ in range(N + 1)]
    dfs(start, end, 0)
