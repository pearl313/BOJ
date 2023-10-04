import sys
input = sys.stdin.readline

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 100
t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 10:
        print(dp[n])
        continue
    for i in range(11, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2]
    print(dp[n])