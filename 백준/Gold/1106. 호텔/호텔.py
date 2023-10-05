import sys
input = sys.stdin.readline

def recur(cur_p):
    if cur_p >= c:
        return 0
    if dp[cur_p] != -1:
        return dp[cur_p]
    dp[cur_p] = 9999999999
    for i in range(n):
        dp[cur_p] = min(dp[cur_p], recur(cur_p + city[i][1]) + city[i][0])
    return dp[cur_p]


c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * 1111
print(recur(0))
