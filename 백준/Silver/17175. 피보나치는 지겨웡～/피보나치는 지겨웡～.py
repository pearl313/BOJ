import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def recur(cur):
    if cur <= 1:
        dp[cur] = 1
        return dp[cur]
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = recur(cur - 1) + recur(cur - 2) + 1
    return dp[cur]

n = int(input())
dp = [-1] * (n + 1)
print(recur(n) % 1000000007)