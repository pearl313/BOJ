import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
j = list(map(int, input().split()))

def recur(cur, cnt, loss, joy):
    global ans
    if loss <= 0:
        return
    if cur == n:
        ans = max(ans, joy)
        return

    recur(cur + 1, cnt + 1, loss - l[cur], joy + j[cur])
    recur(cur + 1, cnt, loss, joy)

ans = -1e10
recur(0, 0, 100, 0)
print(ans)