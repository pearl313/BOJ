import sys
input = sys.stdin.readline

def recur(cur):
    if cur == M:
        print(*selected)
        return
    for i in range(N):
        if visited[i]:
            continue
        selected.append(ls[i])
        visited[i] = True
        recur(cur + 1)
        selected.pop()
        visited[i] = False

N, M = map(int, input().split())
ls = sorted(map(int, input().split()))
selected = []
visited = [False] * N
recur(0)