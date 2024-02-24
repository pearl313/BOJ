import sys
input = sys.stdin.readline

n = int(input())
taste = [list(map(int, input().split())) for _ in range(n)]
ans = 1e10

def recur(cur, cnt, total_sour, total_bitter):
    global ans
    if cur == n:
        if cnt > 0:
            ans = min(ans, abs(total_sour - total_bitter))
        return

    recur(cur + 1, cnt + 1, total_sour * taste[cur][0], total_bitter + taste[cur][1])
    recur(cur + 1, cnt, total_sour, total_bitter)

recur(0, 0, 1, 0)
print(ans)