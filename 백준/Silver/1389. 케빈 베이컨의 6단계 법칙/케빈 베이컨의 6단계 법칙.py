import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    visited = [-1] * (n + 1)
    visited[x] = 0
    q = deque()
    q.append(x)

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] != -1:
                continue
            visited[i] = visited[cur] + 1
            q.append(i)

    return sum(visited[1:])

ans = [1e10]
for i in range(1, n + 1):
    ans.append(bfs(i))
print(ans.index(min(ans)))