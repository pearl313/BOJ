import sys
input = sys.stdin.readline

N = int(input())
region = [0] * 1001
last = 0
first = 0
for _ in range(N):
    L, H = map(int, input().split())
    region[L] = H
    last = max(L, last)
    first = max(H, first)
first_idx = region.index(first)
val = []
# 제일 높은 거 처음으로 나올 때까지 / 그 이후, 이렇게 나눠서 해보기
for i in range(first_idx + 1):
    # 리스트 비어있으면,
    if not val:
        if not region[i]:
            continue
        else:
            val.append(region[i])

    # 리스트에 값이 있으면,
    else:
        if region[i] > val[-1]:
            val.append(region[i])
        else:
            val.append(val[-1])

# 제일 높은 층 한 개인 경우,
for i in range(first_idx + 1, last + 1):
    second = max(region[i:])
    if region[i] <= second:
        val.append(second)

print(sum(val))