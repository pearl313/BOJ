import sys
input = sys.stdin.readline

dp = [[0] * 15 for _ in range(15)]
dp[0] = list(range(15))
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    for i in range(1, 15):
        for j in range(15):
            dp[i][j] = sum(dp[i - 1][1:j + 1])
    print(dp[k][n])