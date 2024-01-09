import sys
input = sys.stdin.readline

k = int(input())
dp = [[] for _ in range(k + 1)]
dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, k + 1):
    dp[i] = [dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]]
print(*dp[k])