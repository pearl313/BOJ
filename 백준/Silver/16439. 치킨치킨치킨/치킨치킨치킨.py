import sys
input = sys.stdin.readline

def recur(cur, start):
    global ans
    if cur == 3:
        total = 0
        for j in range(n):
            total += max(arr[j][selected[0]], arr[j][selected[1]], arr[j][selected[2]])
        ans = max(ans, total)
        return
    for i in range(start, m):
        selected.append(i)
        recur(cur + 1, i + 1)
        selected.pop()

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
selected = []
ans = 0
recur(0, 0)
print(ans)