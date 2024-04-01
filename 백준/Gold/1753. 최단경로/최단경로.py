import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

k = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [1 << 30] * (V + 1)
dist[k] = 0

pq = []
heapq.heappush(pq, [0, k])

while pq:
    mn, cur = heapq.heappop(pq)

    if dist[cur] != mn:
        continue

    for j in range(len(graph[cur])):
        nxt = graph[cur][j][0]
        nd = dist[cur] + graph[cur][j][1]
        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(pq, [nd, nxt])

for i in range(1, V + 1):
    print(dist[i] if dist[i] != 1 << 30 else 'INF')