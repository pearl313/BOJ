import sys
input = sys.stdin.readline

def recur(cur, time):
    global ans
    if cur > N:
        return
    if cur == N:
        ans = max(ans, time)
        return
    recur(cur + ls[cur][0], time + ls[cur][1])
    recur(cur + 1, time)

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
ans = 0
recur(0, 0)
print(ans)