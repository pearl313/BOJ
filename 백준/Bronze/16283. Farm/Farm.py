import sys
input = sys.stdin.readline

a, b, n, w = map(int, input().split())
ans = []
for x in range(1, 1001):
    if n - x > 0 and (a * x) + b * (n - x) == w:
        ans.append(x)
if len(ans) == 1:
    print(ans[0], n - ans[0])
else:
    print(-1)