import sys
from collections import deque
input = sys.stdin.readline

def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for i in graph[cur]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visited = [False] * (N + 1)
DFS(V)
print()
visited = [False] * (N + 1)
BFS(V)