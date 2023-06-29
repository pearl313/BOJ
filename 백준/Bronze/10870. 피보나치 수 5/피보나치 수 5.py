import sys
input = sys.stdin.readline

def recur(cur):
    if cur <= 1:
        return cur
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = recur(cur - 2) + recur(cur - 1)
    return dp[cur]

n = int(input())
dp = [-1] * (n + 1)
print(recur(n))