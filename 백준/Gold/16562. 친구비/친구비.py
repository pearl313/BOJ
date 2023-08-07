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
    if ls[a] < ls[b]:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
ls = [0] + list(map(int, input().split()))
parent = list(range(n + 1))
for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)
    
total = 0
for i in range(1, n + 1):
    x = find(i)
    if x != parent[0]:
        total += ls[x]
        union(x, 0)
print(total if total <= k else "Oh no")
