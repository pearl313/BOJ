import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
arr = [1] * (N + 1)
for _ in range(B):
    n = int(input())
    arr[n] = 0
cnt = sum(arr[1:1 + K])
ans = min(float('inf'), K - cnt)
for i in range(1, N - K + 1):
    cnt = cnt - arr[i] + arr[K + i]
    ans = min(ans, K - cnt)
print(ans)