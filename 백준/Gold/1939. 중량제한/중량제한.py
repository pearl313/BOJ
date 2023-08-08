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
        return
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1


n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)
arr = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[-1], reverse=True)
answer = 0
x, y = map(int, input().split())
for a, b, weight in arr:
    union(a, b)
    if find(x) == find(y):
        print(weight)
        exit()