import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = list(int(input()) for _ in range(N))
coin = coin[::-1]
cnt = 0
for i in range(N):
    if coin[i] <= K:
        cnt += K // coin[i]
        K %= coin[i]
print(cnt)