import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
s = list(map(int, input().split()))

# 한 번에 만들 수 있는 짜장면 수
once = set()

# 한 개 골라
for i in range(m):
    once.add(s[i])
# 두 개 골라
for i in range(m):
    for j in range(i + 1, m):
        once.add(s[i] + s[j])

once = sorted(once, reverse=True)

def bfs(dish, cnt):
    q = deque()
    q.append((dish, cnt))
    visited = [False] * (n + 1)
    visited[dish] = True

    while q:
        cur_dish, cur_cnt = q.popleft()
        if cur_dish == n:
            return cur_cnt

        for i in once:
            nxt_dish = cur_dish + i
            if nxt_dish > n:
                continue
            if visited[nxt_dish]:
                continue
            q.append((nxt_dish, cur_cnt + 1))
            visited[nxt_dish] = True

    return -1

print(bfs(0, 0))