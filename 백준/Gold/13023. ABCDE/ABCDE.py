import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(n, cnt):
    if cnt == 5:
        print(1)
        exit()
    for j in ls[n]:
        if not visited[j]:
            visited[j] = True   
            dfs(j, cnt + 1)
            visited[j] = False

n, m = map(int, input().split())
ls = [[] for _ in range(2001)]
for _ in range(m):
    a, b = map(int, input().split())
    ls[a].append(b)
    ls[b].append(a)

for i in range(2001):
    if not ls[i]:
        continue
    visited = [False] * 2001
    visited[i] = True
    dfs(i, 1)
print(0)