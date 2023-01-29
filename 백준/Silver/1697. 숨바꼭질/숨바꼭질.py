import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
    graph[v] = 0
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        if cur == K:
            print(graph[cur])
            break
        for nx in (cur + 1, cur - 1, cur * 2):
            if 0 <= nx <= 100000 and  graph[nx] == -1:
                graph[nx] = graph[cur] + 1
                q.append(nx)

N, K = map(int, input().split())
graph = [-1] * 100001
BFS(N)