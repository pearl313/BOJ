import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q_stack = list(map(int, input().split()))
q_stack_ls = list(map(int, input().split()))
m = int(input())
ls = list(map(int, input().split()))

ans = deque()
for i in range(n):
    if q_stack[i]:
        continue
    ans.append(q_stack_ls[i])
    
if ans:
    for i in range(m):
        ans.appendleft(ls[i])
        if i == m - 1:
            print(ans.pop())
        else:
            print(ans.pop(), end=' ')
else:
    print(*ls)