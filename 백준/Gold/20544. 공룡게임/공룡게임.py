import sys
input = sys.stdin.readline

n = int(input())

# 인자만큼 dp 배열 만들어줌 (cur -> cnt_1 -> cnt_2 -> two)
dp = [[[[-1 for i in range(2)] for j in range(2)] for k in range(3)] for l in range(n)]

def recur(cur, cnt_1, cnt_2, two):
    # 1이 3개 이상이거나 2가 2개 이상이면, 가능한 경우가 0
    if cnt_1 > 2 or cnt_2 >= 2:
        return 0
    # 가능한 걸 찾았으면 1을 리턴해서 경우의 수 +1 해주기
    if cur == n:
        return two
    if dp[cur][cnt_1][cnt_2][two] != -1:
        return dp[cur][cnt_1][cnt_2][two]

    dp[cur][cnt_1][cnt_2][two] = (recur(cur + 1, 0, 0, two) + recur(cur + 1, cnt_1 + 1, 0, two) + recur(cur + 1, cnt_1 + 1, cnt_2 + 1, 1)) % 1000000007
    return dp[cur][cnt_1][cnt_2][two]

print(recur(1, 0, 0, 0))