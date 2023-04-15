import sys
input = sys.stdin.readline

def nPm(k):
    if len(selected) == M:
        print(*selected)
        return 
    for i in range(1, N + 1):
        if not visited[i]:
            selected.append(i)
            visited[i] = True
            nPm(i)
            selected.pop()
            visited[i] = False

N, M = map(int, input().split())
selected = []
visited = [False] * (N + 1)
nPm(0)