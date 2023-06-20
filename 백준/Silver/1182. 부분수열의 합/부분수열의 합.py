import sys
input = sys.stdin.readline

def recur(cur, cnt):
    global ans
    if cur == N:
        if sum(selected) == S and len(selected) != 0:
            ans += 1
            return
    else:
        selected.append(ls[cur])
        recur(cur + 1, cnt + 1)
        selected.pop()
        recur(cur + 1, cnt)

N, S = map(int, input().split())
ls = list(map(int, input().split()))
selected = []
ans = 0
recur(0, 0)
print(ans)