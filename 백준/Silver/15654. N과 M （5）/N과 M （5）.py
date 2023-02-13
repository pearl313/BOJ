import sys
input = sys.stdin.readline

def nPm(k):
    if k == M:
        print(*selected)
        return
    for i in range(N):
        if not visited[i]:
            selected.append(ls[i])
            visited[i] = True
            nPm(k + 1)
            selected.pop()
            visited[i] = False

N, M = map(int, input().split())
ls = sorted(map(int, input().split()))
visited = [False] * (N + 1)
selected = []
nPm(0)