import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
total = 0
for i in range(N):
    j = i
    while total < M and j != N:
        total += arr[j]
        j += 1
    if total == M:
        cnt += 1
    total = 0
print(cnt)