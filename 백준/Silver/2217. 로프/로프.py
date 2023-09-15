import sys
input = sys.stdin.readline

n = int(input())
rope = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0
for i in range(n):
    ans = max(ans, rope[i] * (i + 1))
print(ans)