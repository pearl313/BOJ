import sys
input = sys.stdin.readline

n = int(input())
s, e = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
def dfs(s, e, cnt):
    if s == e:
        print(cnt)
        exit()
        return cnt
    visited[s] = True
    for i in graph[s]:
        if visited[i]:
            continue
        dfs(i, e, cnt + 1)

dfs(s, e, 0)
print(-1)