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
    ans = []
    for j in range(N + 1):
        if visited[j] == K:
            ans.append(j)
    if ans:
        for a in ans:
            print(a)
    else:
        print(-1)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (N + 1)
BFS(X)