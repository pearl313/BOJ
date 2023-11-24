import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == m:
        cnt = 0
        total = sum(selected)
        for j in range(1, int(total ** 0.5) + 1):
            if total % j == 0:
                cnt += 1
        if cnt == 1:
            ans.add(total)
        return
    for i in range(start, n):
        selected.append(weight[i])
        recur(cur + 1, i + 1)
        selected.pop()

n, m = map(int, input().split())
weight = list(map(int, input().split()))
selected = []
ans = set()
recur(0, 0)
if ans:
    print(*sorted(list(ans)))
else:
    print(-1)