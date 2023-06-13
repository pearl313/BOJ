import sys
input = sys.stdin.readline

def recur(cur):
    if len(selected) == M:
        print(*selected)
        return
    for i in range(1, N + 1):
        if not visited[i]:
            selected.append(i)
            visited[i] = True
            recur(i + 1)
            selected.pop()
            visited[i] = False

N, M = map(int, input().split())
selected = []
visited = [False] * (N + 1)
recur(0)