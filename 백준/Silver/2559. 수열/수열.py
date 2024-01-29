import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ls = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + ls[i]

ans = float('-inf')
for i in range(K, N + 1):
    ans = max(ans, prefix_sum[i] - prefix_sum[i - K])
print(ans)