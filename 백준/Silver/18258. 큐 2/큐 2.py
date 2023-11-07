import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    order = list(input().split())
    if len(order) == 1:
        if order[0] == 'front':
            print(-1 if not q else q[0])
        elif order[0] == 'back':
            print(-1 if not q else q[-1])
        elif order[0] == 'empty':
            print(1 if not q else 0)
        elif order[0] == 'size':
            print(len(q))
        else:
            print(-1 if not q else q.popleft())
    else:
        q.append(order[1])