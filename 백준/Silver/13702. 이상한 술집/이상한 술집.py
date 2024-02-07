import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(int(input()) for _ in range(n))
ls = sorted(ls)
s, e = 1, ls[-1]
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(n):
        cnt += ls[i] // mid
    if cnt >= k:
        s = mid + 1
    else:
        e = mid - 1
print(e)