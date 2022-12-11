import sys
from collections import deque
input = sys.stdin.readline

def BFS(a):
    q = deque()
    q.append(a)
    visited[a] = 0
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] != -1:
                continue
            q.append(i)
            visited[i] = visited[cur] + 1

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
BFS(a)
print(visited[b])