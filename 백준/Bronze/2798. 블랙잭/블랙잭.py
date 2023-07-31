import sys
input = sys.stdin.readline

def recur(cur, start):
    global ans
    if len(selected) == 3:
        if sum(selected) > M:
            return
        if abs(sum(selected) - M) < abs(ans - M):
            ans = sum(selected)
        return
    for i in range(start, N):
        selected.append(cards[i])
        recur(cur + 1, i + 1)
        selected.pop()

N, M = map(int, input().split())
cards = list(map(int, input().split()))
selected = []
ans = 1e10
recur(0, 0)
print(ans)