import sys
input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

# 바텀 업과 다르게 순서를 바꿔서 뒤에서부터 확인하면서 dp 배열 채워나가기
dp = [0] * (n + 1)

for i in range(n)[::-1]:
    if i + ls[i][0] < n + 1:
        dp[i] = max(dp[i + ls[i][0]] + ls[i][1], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])