import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
s, e = 0, k
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid // i, n)
    if cnt >= k:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
print(ans)