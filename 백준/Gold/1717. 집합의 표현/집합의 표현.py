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
        size[b] += size[a]
    elif rank[a] > rank[b]:
        parent[b] = a
        size[a] += size[b]
    else:
        parent[a] = b
        size[b] += size[a]
        rank[b] += 1

n, m = map(int, input().split())
parent = list(range(1000001))
rank = list(range(1000001))
size = list(range(1000001))
for _ in range(m):
    what, a, b = map(int, input().split())
    if what == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")