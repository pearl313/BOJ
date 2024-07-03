import sys
input = sys.stdin.readline

n, x = map(int, input().split())
ls = list(map(int, input().split()))

ans = 1e10
for i in range(1, n):
    ans = min(ans, ls[i - 1] * x + ls[i] * x)
print(ans)