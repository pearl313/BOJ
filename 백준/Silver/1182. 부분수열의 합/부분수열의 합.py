import sys
input = sys.stdin.readline

def recur(cur, start):
    global ans
    if cur == cnt:
        if sum(selected) == S:
            ans += 1
        return
    for i in range(start, N):
        selected[cur] = ls[i]
        recur(cur + 1, i + 1)

N, S = map(int, input().split())
ls = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    selected = [0] * i
    cnt = i
    recur(0, 0)
print(ans)