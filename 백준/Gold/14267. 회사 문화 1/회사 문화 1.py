import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def DFS(v):
    for i in graph[v]:
        value[i] += value[v]
        DFS(i)

n, m = map(int, input().split())
num = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    graph[num[i]].append(i + 1)

value = [0 for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    value[a] += b

DFS(1)
print(*value[1:])