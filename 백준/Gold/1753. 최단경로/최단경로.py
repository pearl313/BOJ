import sys, heapq
input = sys.stdin.readline

INF = 1e10

def dijkstra(s):
    q = []
    dist = [INF] * (V + 1)
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        dist_x, x = heapq.heappop(q)

        if dist_x != dist[x]:
            continue

        for node, cost in graph[x]:
            if dist[node] > dist[x] + cost:
                dist[node] = dist[x] + cost
                heapq.heappush(q, (dist[node], node))

    for i in dist[1:]:
        if i == INF:
            print("INF")
        else:
            print(i)

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)