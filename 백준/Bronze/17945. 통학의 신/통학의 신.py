import sys
input = sys.stdin.readline

A, B = map(int, input().split())
ans = []
for x in range(-1000, 1001):
    if x ** 2 + 2 * A * x + B == 0:
        ans.append(x)
print(*ans)