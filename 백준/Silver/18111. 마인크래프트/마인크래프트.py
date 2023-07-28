import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
time = 1e10
height = 0
# 가능한 모든 높이에서 다 해보기
for i in range(257):
    # 제거할 양, 사용할 양 확인
    remove = 0
    use = 0
    for x in range(n):
        for y in range(m):
            # 지금 높이가 블럭의 높이보다 높다면, 추가해야함
            if i > ground[x][y]:
                use += i - ground[x][y]
            # 반대라면, 제거해야함
            else:
                remove += ground[x][y] - i
    # 가져다 쓰는 양이 가능한 양인지 확인하고, 아니면 넘기기
    if use > remove + b:
        continue
    # 걸리는 시간 확인해보기
    temp = remove * 2 + use
    if temp <= time:
        time = temp
        height = i
print(time, height)