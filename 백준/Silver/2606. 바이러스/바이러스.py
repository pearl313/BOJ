import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
    global cnt
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        cnt += 1
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = True

com = int(input())
N = int(input())
graph = [[] for _ in range(com + 1)]
visited = [False] * (com + 1)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
BFS(1)
print(cnt - 1)