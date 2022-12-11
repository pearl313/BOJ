import sys
input = sys.stdin.readline

def DFS(v):
    global cnt
    cnt += 1
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

com = int(input())
N = int(input())
graph = [[] for _ in range(com + 1)]
visited = [False] * (com + 1)
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
DFS(1)
print(cnt - 1)