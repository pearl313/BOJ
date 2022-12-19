import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + list(int(input()) for _ in range(n))
dp = [[0, 0] for _ in range(n + 1)]

if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1] + stairs[2])
else:
    dp[0] = [0, 0]
    dp[1] = [stairs[1], 0]
    dp[2] = [stairs[1] + stairs[2], stairs[2]]

    for i in range(3, n + 1):
        dp[i] = [dp[i - 1][1] + stairs[i], max(dp[i - 2]) + stairs[i]]
    
    print(max(dp[n]))