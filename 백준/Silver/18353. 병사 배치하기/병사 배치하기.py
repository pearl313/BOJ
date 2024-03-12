import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if ls[i] < ls[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))