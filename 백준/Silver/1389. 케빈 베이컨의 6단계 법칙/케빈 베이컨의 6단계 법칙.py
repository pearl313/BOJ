import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    visited[v] += 1
    q = deque()
    q.append(v)
    while q:
        current = q.popleft()
        for i in relationship[current]:
            if visited[i] != -1:
                continue
            q.append(i)
            visited[i] = visited[current] + 1

N, M = map(int, input().split())
relationship = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    relationship[a].append(b)
    relationship[b].append(a)
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    step = 0
    visited = [-1] * (N + 1)
    bfs(i)
    cnt[i] = sum(visited[1:])
print(cnt.index(min(cnt[1:])))