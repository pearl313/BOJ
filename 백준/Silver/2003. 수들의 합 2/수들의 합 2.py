import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = list(map(int, input().split()))

s = 0
e = 0
cnt = 0
while e < N:
    total = sum(ls[s:e + 1])
    if total == M:
        cnt += 1
        s += 1
        e += 1
    elif total < M:
        e += 1
        if e == N:
            break
        total += ls[e]
    elif total > M:
        total -= ls[s]
        s += 1
print(cnt)