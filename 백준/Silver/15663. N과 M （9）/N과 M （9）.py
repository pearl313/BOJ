import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def recur(cur):
    if cur == m:
        temp = tuple(selected[:])
        ans.add(temp)
        return
    for i in range(n):
        if not visited[i]:
            selected.append(ls[i])
            visited[i] = True
            recur(cur + 1)
            selected.pop()
            visited[i] = False

n, m = map(int, input().split())
ls = list(map(int, input().split()))
selected = []
visited = [False] * (n + 1)
ans = set()
recur(0)
for j in sorted(ans):
    print(*j)