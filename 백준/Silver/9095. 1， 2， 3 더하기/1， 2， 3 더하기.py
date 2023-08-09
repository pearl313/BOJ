import sys
input = sys.stdin.readline

def recur(total):
    if total == n:
        return 1
    if total > n:
        return 0
    if dp[total] != -1:
        return dp[total]
    if dp[total] == -1:
        dp[total] = 0
    for i in range(1, 4):
        dp[total] += recur(total + i)
    return dp[total]

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [-1] * (n + 1)
    recur(0)
    print(dp[0])