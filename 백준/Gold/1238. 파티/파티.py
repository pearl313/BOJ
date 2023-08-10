import sys, heapq
input = sys.stdin.readline

def dijkstra(s):
    global ans, dist
    INF = 1e10
    dist = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        dist_x, x = heapq.heappop(q)
        if dist_x != dist[x]:
            continue
        for num, time in graph[x]:
            if dist[num] > dist[x] + time:
                dist[num] = dist[x] + time
                heapq.heappush(q, (dist[num], num))


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
ans = []
dijkstra(x)
ans = dist[:]
for i in range(1, n + 1):
    if i == x:
        continue
    dijkstra(i)
    ans[i] += dist[x]
print(max(ans[1:]))