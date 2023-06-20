import sys
input = sys.stdin.readline

def choose(cur, total):
    global ans
    if cur > N:
        return
    if cur == N:
        ans = max(ans, total)
        return
    choose(cur + schedule[cur][0], total + schedule[cur][1])
    choose(cur + 1, total)

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

ans = 0
selected = []
choose(0, 0)

print(ans)