import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = sorted(map(int, input().split()))
s, e = 1, ls[-1]
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(n):
        if mid < ls[i]:
            cnt += ls[i] - mid
    if cnt >= k:
        ans = max(ans, mid)
        s = mid + 1
    else:
        e = mid - 1
print(ans)