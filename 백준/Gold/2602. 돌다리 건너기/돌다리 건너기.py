import sys
input = sys.stdin.readline

'''
1. 왼쪽 -> 오른쪽, 반드시 주어 문자열 순서대로진
2. 위 / 아래 번갈아가면서 오른쪽으로 움직여야 함
3. 반드시 한 칸 이상 오른쪽으로 전진해야하며, 건너뛰는 칸 수는 상관없음 
'''

word = input().strip()
devil = input().strip()
angel = input().strip()

# 배열에서 몇 번째 인덱스의 문자를 사용한 건지 -> 어떤 배열인지 -> 주어진 문자열 중에 몇 번째 문자인지
dp = [[[-1] * len(word) for _ in range(2)] for __ in range(len(devil) + 1)]

# 각 알파벳이 나타나는 위치 저장
devil_ls = [[] for _ in range(26)]
angel_ls = [[] for _ in range(26)]

for i in range(1, len(devil) + 1):
    devil_ls[ord(devil[i - 1]) - ord('A')].append(i)
    angel_ls[ord(angel[i - 1]) - ord('A')].append(i)


def dfs(depth, turn, cnt):
    # 종료 조건
    if cnt == len(word):
        return 1

    # 메모이제이션
    if dp[depth][turn][cnt] != -1:
        return dp[depth][turn][cnt]

    dp[depth][turn][cnt] = 0
    idx = ord(word[cnt]) - ord('A')

    # 천사 차례
    if turn == 0:
        for i in angel_ls[idx]:
            # 천사가 밟아야 하는 돌
            if depth < i:
                dp[depth][turn][cnt] += dfs(i, 0 if turn else 1, cnt + 1)

    # 악마 차례
    else:
        for i in devil_ls[idx]:
            if depth < i:
                dp[depth][turn][cnt] += dfs(i, 0 if turn else 1, cnt + 1)

    return dp[depth][turn][cnt]

dfs(0, 0, 0)
dfs(0, 1, 0)
print(dp[0][0][0] + dp[0][1][0])