import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
s = 1
e = max(trees)
ans = 0
while s <= e:
    mid = (s + e) // 2
    home = 0
    for i in range(N):
        if mid >= trees[i]:
            continue
        home += trees[i] - mid
    if home >= M:
        ans = max(ans, mid)
        s = mid + 1
    else:
        e = mid - 1
print(ans)