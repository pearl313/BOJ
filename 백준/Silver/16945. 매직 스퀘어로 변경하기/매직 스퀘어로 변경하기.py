import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(3)]
arr2 = [[0] * 3 for _ in range(3)]
visited = [False] * 10
ans = 1e10

def check():
    # 행 확인
    for i in range(3):
        total = 0
        for j in range(3):
            total += arr2[i][j]
        # 각 행의 합이 모두 같아야 하므로 15가 아니면 안됨.
        if total != 15:
            return False

    # 열 확인
    for j in range(3):
        total = 0
        for i in range(3):
            total += arr2[i][j]
        if total != 15:
            return False

    # 대각선 확인
    if arr2[0][0] + arr2[1][1] + arr2[2][2] != 15:
        return False
    if arr2[0][2] + arr2[1][1] + arr2[2][0] != 15:
        return False

    return True

def recur(x, y, cost):
    global ans
    # 열 끝까지 가면, 다음 줄로 이동
    if y == 3:
        x += 1
        y = 0
    # 행 끝까지 가면,
    if x == 3:
        if not check():
            return
        ans = min(ans, cost)
        return
    # 1부터 10까지 하나씩 다 넣어서 바꿔보기 (순열)
    for i in range(1, 10):
        if visited[i]:
            continue
        visited[i] = True
        arr2[x][y] = i
        # 비용은 원래 배열에서 바꿔준 숫자와의 차이
        recur(x, y + 1, cost + abs(arr[x][y] - i))
        visited[i] = False

recur(0, 0, 0)
print(ans)