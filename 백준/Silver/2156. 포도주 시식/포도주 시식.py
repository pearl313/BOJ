import sys
input = sys.stdin.readline

n = int(input())
grape = [0] + list(int(input()) for _ in range(n))
dp = [0] * (n + 1)
dp[1] = grape[1]
if n > 1:
    dp[2] = grape[1] + grape[2]
    if n >= 3:
        dp[3] = max(dp[2], dp[1] + grape[3])
        for i in range(3, n + 1):
            dp[i] = max(dp[i - 3] + grape[i - 1] + grape[i], dp[i - 2] + grape[i], dp[i - 1])
print(dp[n])