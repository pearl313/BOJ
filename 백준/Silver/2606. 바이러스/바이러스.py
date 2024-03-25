import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
cnt = 0

def dfs(x):
    global cnt
    visited[x] = True
    for i in graph[x]:
        if visited[i]:
            continue
        cnt += 1
        dfs(i)

dfs(1)
print(cnt)