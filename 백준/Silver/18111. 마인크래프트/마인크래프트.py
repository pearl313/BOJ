import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
ans = 1e10
level = 0
for i in range(257):
    # 가능한 각 높이마다 사용할 블럭과 제거할 블럭 개수 세어주기
    use_block = 0
    take_block = 0
    for a in range(N):
        for b in range(M):
            # 주어진 위치에서의 블럭 높이가 가능한 현재 높이보다 높으면,
            if ground[a][b] > i:
                # 제거해야하므로 take에 차이만큼 더해줌
                take_block += ground[a][b] - i
            # 그게 아니면,
            else:
                # 추가해야하므로 블럭을 갖고올 use에 차이만큼 더해줌
                use_block += i - ground[a][b]
    # 추가해야하는 블럭 수가 제거하는 블럭 수 + 주어진 블럭 수 보다 크면 -> 불가능하므로 넘어가기
    if use_block > take_block + B:
        continue
    # 소요 시간은 제거는 2초, 추가는 1초니까 그만큼 곱해서 더해줌
    time = take_block * 2 + use_block
    # 최소 시간 찾고, 그때의 높이 구하기
    if time <= ans:
        ans = time
        level = i
print(ans, level)