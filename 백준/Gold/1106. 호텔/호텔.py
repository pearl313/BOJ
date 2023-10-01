import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def recur(cur_p):
    if cur_p >= c:
        return 0
    if dp[cur_p] != -1:
        return dp[cur_p]
    dp[cur_p] = 1e10
    for i in range(n):
        dp[cur_p] = min(recur(cur_p + city[i][1]) + city[i][0], dp[cur_p])
    return dp[cur_p]

c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * 1001
print(recur(0))