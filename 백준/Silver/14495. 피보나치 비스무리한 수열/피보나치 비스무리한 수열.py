import sys
input = sys.stdin.readline

def recur(cur):
    if dp[cur] != -1:
        return dp[cur]
    if cur <= 3:
        dp[cur] = 1
        return dp[cur]
    dp[cur] = recur(cur - 1) + recur(cur - 3)
    return dp[cur]

n = int(input())
dp = [-1] * (n + 1)
print(recur(n))