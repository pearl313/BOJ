import sys
input = sys.stdin.readline

n, c = map(int, input().split())
ls = list(int(input()) for _ in range(n))
ls = sorted(ls)
s, e = 1, ls[-1] - ls[0]
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 1
    cur = ls[0]
    for i in range(1, n):
        if ls[i] - cur >= mid:
            cnt += 1
            cur = ls[i]
    if cnt >= c:
        ans = max(ans, mid)
        s = mid + 1
    else:
        e = mid - 1
print(ans)