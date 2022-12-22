import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# dp[i] := i번째까지의 연속합 중 제알 큰 값
dp = [[] for _ in range(n)]
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])
print(max(dp))