import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def parent(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        parent_ls[nxt] = cur
        parent(nxt, cur)

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent_ls = [0] * (N + 1)
parent(1, 0)
for i in parent_ls[2:]:
    print(i)