import sys
input = sys.stdin.readline

t = int(input())
dp = [0, 1, 2, 2, 3, 3, 6] + [0] * 1000001
for _ in range(t):
    n = int(input())
    for i in range(7, n + 1):
        dp[i] = (dp[i - 6] + dp[i - 4] + dp[i - 2]) % 1000000009
    print(dp[n])