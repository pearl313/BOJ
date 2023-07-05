import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def recur(cur):
    if cur > n:
        return -1000000
    if cur == n:
        return 0
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = max(recur(cur + ls[cur][0]) + ls[cur][1], recur(cur + 1))
    return dp[cur]

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * (n + 1)
print(recur(0))