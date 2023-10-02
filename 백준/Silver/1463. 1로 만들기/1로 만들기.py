import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def recur(total):
    if total in dp.keys():
        return dp[total]
    if total % 3 == 0 and total % 2 == 0:
        dp[total] = min(recur(total // 3) + 1, recur(total // 2) + 1)
    elif total % 3 == 0:
        dp[total] = min(recur(total // 3) + 1, recur(total - 1) + 1)
    elif total % 2 == 0:
        dp[total] = min(recur(total // 2) + 1, recur(total - 1) + 1)
    else:
        dp[total] = recur(total - 1) + 1
    return dp[total]

x = int(input())
dp = {1:0}
print(recur(x))