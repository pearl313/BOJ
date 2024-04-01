import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

def bfs(x):
    visited = [-1] * 100001
    visited[x] = 0
    q = deque()
    q.append(x)

    while q:
        cur = q.popleft()
        if cur == k:
            return visited[k]
        for nx in (cur - 1, cur + 1, 2 * cur):
            if nx < 0 or nx > 100000:
                continue
            if visited[nx] != -1:
                continue
            visited[nx] = visited[cur] + 1
            q.append(nx)

print(bfs(n))