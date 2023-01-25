import sys
input = sys.stdin.readline
from collections import deque

def BFS(v):
    visited[v] += 1
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] != -1:
                continue
            q.append(i)
            visited[i] = visited[cur] + 1
    nothing = True
    for j in range(N + 1):
        if visited[j] == K:
            print(j)
            nothing = False
    if nothing:
        print(-1)
    return

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
BFS(X)