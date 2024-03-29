import sys
input = sys.stdin.readline

def recur(cur):
    if cur == n:
        print(*selected)
    for i in range(1, n + 1):
        if visited[i]:
            continue
        selected.append(i)
        visited[i] = True
        recur(cur + 1)
        selected.pop()
        visited[i] = False

n = int(input())
selected = []
visited = [False] * (n + 1)
recur(0)