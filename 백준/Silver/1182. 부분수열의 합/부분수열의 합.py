import sys
input = sys.stdin.readline

n, s = map(int, input().split())
ls = list(map(int, input().split()))
ans = 0

def recur(cur, cnt, total):
    global ans
    if cur == n:
        if cnt > 0 and total == s:
            ans += 1
        return

    recur(cur + 1, cnt + 1, total + ls[cur])
    recur(cur + 1, cnt, total)

recur(0, 0, 0)
print(ans)