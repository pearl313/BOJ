import sys
input = sys.stdin.readline

def recur(cur, size, time):
    global ans
    if cur == n:
        ans = max(ans, size)
        return
    if time == 0:
        ans = max(ans, size)
        return
    if cur + 1 <= n:
        recur(cur + 1, size + ls[cur + 1], time - 1)
    if cur + 2 <= n:
        recur(cur + 2, size // 2 + ls[cur + 2], time - 1)

n, m = map(int, input().split())
ls = [0] + list(map(int, input().split()))
ans = 0
recur(0, 1, m)
print(ans)