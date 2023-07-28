import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    global ans
    q = deque()
    q.append(v)
    visited = [-1] * n
    visited[v] = 0
    while q:
        cur = q.popleft()
        for nxt in relationship[cur]:
            if visited[nxt] != -1:
                continue
            visited[nxt] = visited[cur] + 1
            q.append(nxt)

    cnt = 0
    for i in range(1, 3):
        cnt += visited.count(i)
    ans = max(ans, cnt)

n = int(input())
relationship = [[] for _ in range(n)]
for i in range(n):
    temp = list(input().strip())
    for j in range(n):
        if temp[j] == 'Y':
            relationship[i].append(j)
ans = 0
for i in range(n):
    bfs(i)
print(ans)