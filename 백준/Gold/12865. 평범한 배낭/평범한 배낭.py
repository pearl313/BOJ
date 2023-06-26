import sys
input = sys.stdin.readline

def recur(cur, weight):
    if weight > K:
        return -1000000
    if cur >= N:
        return 0
    if dp[cur][weight] != -1:
        return dp[cur][weight]
    dp[cur][weight] = max(recur(cur + 1, weight + things[cur][0]) + things[cur][1], recur(cur + 1, weight))
    return dp[cur][weight]

N, K = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * 100001 for _ in range(N)]
print(recur(0, 0))