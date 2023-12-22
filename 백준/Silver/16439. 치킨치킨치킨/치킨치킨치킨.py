import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == 3:
        total = 0
        for j in range(n):
            total += max(arr[j][selected[0]], arr[j][selected[1]], arr[j][selected[2]])
        ans = max(ans, total)
        return
    for i in range(m):
        if not visited[i]:
            selected.append(i)
            visited[i] = True
            recur(cur + 1)
            selected.pop()
            visited[i] = False

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
selected = []
visited = [False] * m
ans = 0
recur(0)
print(ans)