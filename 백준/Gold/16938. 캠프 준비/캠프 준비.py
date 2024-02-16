import sys
input = sys.stdin.readline

n, l, r, x = map(int, input().split())
ls = list(map(int, input().split()))
arr = [0 for _ in range(n)]

def recur(cur, start, cnt):
    global ans
    if cur == cnt:
        if sum(arr) >= l and sum(arr) <= r:
            if max(arr[:cnt]) - min(arr[:cnt]) >= x:
                ans += 1
        return
    for i in range(start, n):
        arr[cur] = ls[i]
        recur(cur + 1, i + 1, cnt)

ans = 0
for i in range(2, n + 1):
    recur(0, 0, i)
print(ans)