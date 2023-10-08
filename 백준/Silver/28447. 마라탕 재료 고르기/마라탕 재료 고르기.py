import sys
input = sys.stdin.readline

def recur(cur, start):
    global ans
    if cur == k:
        temp = 0
        for a in range(k):
            for b in range(a + 1, k):
                temp += taste[selected[a]][selected[b]]
        ans = max(ans, temp)
        return
    for i in range(start, n):
        selected.append(i)
        recur(cur + 1, i + 1)
        selected.pop()

n, k = map(int, input().split())
taste = [list(map(int, input().split())) for _ in range(n)]
selected = []
ans = -1e10
recur(0, 0)
print(ans)