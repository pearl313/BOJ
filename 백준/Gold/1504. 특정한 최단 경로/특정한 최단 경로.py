import sys, heapq
input = sys.stdin.readline

INF = 1e10

def dijkstra(s):
    q = []
    dist = [INF] * (N + 1)
    dist[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist_x, x = heapq.heappop(q)

        if dist_x != dist[x]:
            continue
        for node, cost in graph[x]:
            if dist[node] > dist[x] + cost:
                dist[node] = dist[x] + cost
                heapq.heappush(q, (dist[node], node))

    return dist

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
start_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

ans = min(start_dist[v1] + v1_dist[v2] + v2_dist[N], start_dist[v2] + v2_dist[v1] + v1_dist[N])

if ans >= INF:
    print(-1)
else:
    print(ans)