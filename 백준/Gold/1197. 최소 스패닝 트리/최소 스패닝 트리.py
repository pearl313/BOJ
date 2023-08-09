import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return a
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

v, e = map(int, input().split())
parent = list(range(v + 1))
rank = [0] * (v + 1)
ls = sorted([list(map(int, input().split())) for _ in range(e)], key= lambda x:x[-1])
ans = 0
for a, b, c in ls:
    if find(a) != find(b):
        union(a, b)
        ans += c
print(ans)