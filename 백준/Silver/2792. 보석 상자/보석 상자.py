import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = list(int(input()) for _ in range(M))

s = 1
e = max(ls)
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(M):
        if ls[i] % mid == 0:
            cnt += ls[i] // mid
        else:
            cnt += ls[i] // mid + 1
    if cnt > N:
        s = mid + 1
    else:
        e = mid - 1
print(s)