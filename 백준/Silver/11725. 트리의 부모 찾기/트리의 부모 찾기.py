import sys
input = sys.stdin.readline
from collections import deque

def BFS(v):
    visited[v] = True
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = True
            ans[i] = cur

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
ans = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
BFS(1)
print(*ans[2:], sep='\n')