import sys
input = sys.stdin.readline

def nCm(k):
    if len(selected) == M:
        print(*selected)
        return
    for i in range(k, N + 1):
        selected.append(i)
        nCm(i)
        selected.pop()

N, M = map(int, input().split())
selected = []
nCm(1)