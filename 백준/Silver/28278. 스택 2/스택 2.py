import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    order = list(map(int, input().split()))
    if len(order) == 2:
        stack.append(order[1])
    else:
        if order[0] == 2:
            print(-1 if not stack else stack.pop())
        elif order[0] == 3:
            print(len(stack))
        elif order[0] == 4:
            print(1 if not stack else 0)
        else:
            print(-1 if not stack else stack[-1])