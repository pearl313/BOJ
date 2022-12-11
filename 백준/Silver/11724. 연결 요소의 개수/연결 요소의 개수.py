import sys
input = sys.stdin.readline

def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

N, M = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        DFS(i)
print(cnt)