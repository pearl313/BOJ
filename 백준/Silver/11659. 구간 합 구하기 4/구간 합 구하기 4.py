import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = [0] + list(map(int, input().split()))

# 누적합 구하기
prefix_sum = [0]
for i in range(1, N + 1):
    prefix_sum.append(prefix_sum[i - 1] + ls[i])

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])