import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000000)
def recur(k): # 현재 k일이고, 앞으로 최선을 다해서 일을 했을 때, 얻을 수 있는 이득
    if k > n:
        return -213123212
    if k == n:
        return 0
    if dp[k] != -1:
        return dp[k]
    dp[k] = max(recur(k + ls[k][0]) + ls[k][1], recur(k + 1))
    return dp[k]

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * (n + 1)
print(recur(0))