import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
dp = [1] * (n + 1)
for i in range(n):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))