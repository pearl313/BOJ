import sys
input = sys.stdin.readline

N = int(input())

# 각 숫자에서 만들 수 있는 계단 수
# ex) dp[5][3] 5로 시작하는 3자리 계단 수의 개수
dp = [[0] * (N + 1) for i in range(10)]

# now: 현재 숫자, l: 숫자의 길이
# now로 시작하는 길이가 l인 계단 수의 개수 반환하는 함수
def stair(now, l):
    # 현재 숫자가 0 ~ 9 벗어나면 0
    if now < 0 or now > 9:
        return 0
    # 길이가 1이면 무조건 1 반환
    if l <= 1:
        return 1
    # 이미 구한 값이 있으면 그대로 반환
    if dp[now][l]:
        return dp[now][l]
    # 현재 숫자에서 이 길이로 만들 수 있는 계단 수는, 1씩 차이나는 숫자와 길이가 1씩 차이나는 길이로 만들 수 있는 계단 수의 합
    dp[now][l] = stair(now - 1, l - 1) + stair(now + 1, l - 1)
    return dp[now][l]

total = 0
# 1부터 9까지의 시작 숫자를 넣어서 다 더해줌
for i in range(1, 10):
    total += stair(i, N)
print(total % 1000000000)