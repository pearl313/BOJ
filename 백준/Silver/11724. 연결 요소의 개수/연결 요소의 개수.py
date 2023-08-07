import sys
input = sys.stdin.readline

def find(x):
    # 루트인 것!
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    # 크기 비교해서 더 작은 게 큰 쪽으로 붙기
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

n, m = map(int, input().split())
parent = list(range(1000001))
rank = list(0 for _ in range(1000001))
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

visited = [False for i in range(n + 1)]
cnt = 0

for i in range(1, n + 1):
    x = find(i)
    if not visited[x]:
       cnt += 1
    visited[x] = True
print(cnt)