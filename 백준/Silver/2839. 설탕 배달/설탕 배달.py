import sys
input = sys.stdin.readline

n = int(input())
ans = 1e10
for i in range(5000 // 3 + 1):
    for j in range(5000 // 5 + 1):
        if 3 * i + 5 * j == n:
            ans = min(ans, i + j)
print(-1 if ans == 1e10 else ans)