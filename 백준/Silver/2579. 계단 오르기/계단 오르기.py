import sys
input = sys.stdin.readline

n = int(input())
ls = [0] + list(int(input()) for _ in range(n))

# 현재 꺼만, 이전 꺼 + 현재 꺼
dp = [(0, 0) for _ in range(n + 1)]

if n == 1:
    print(ls[1])
elif n == 2:
    print(ls[1] + ls[2])
else:
    dp[1] = (ls[0], ls[0] + ls[1])
    dp[2] = (ls[2], ls[1] + ls[2])

    for i in range(3, n + 1):
        # 연속 3개면 안되니까 두번째 앞선 값들 중에서 최댓값 + 현재 위치 값 또는 바로 앞전 값들 중 앞전 꺼만 더한 값에 + 현재 위치 값
        dp[i] = (max(dp[i - 2]) + ls[i], dp[i - 1][0] + ls[i])
    print(max(dp[n]))