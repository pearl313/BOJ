import sys
input = sys.stdin.readline

def recur(cur):
    if cur == m:
        print(*selected)
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        selected.append(i)
        visited[i] = True
        recur(cur + 1)
        selected.pop()
        visited[i] = False

n, m = map(int, input().split())
selected = []
visited = [False] * (n + 1)
recur(0)