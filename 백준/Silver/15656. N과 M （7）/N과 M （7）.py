import sys
input = sys.stdin.readline

def nPm(k):
    if k == M:
        print(*selected)
        return
    for i in range(N):
        selected.append(ls[i])
        nPm(k + 1)
        selected.pop()

N, M = map(int, input().split())
ls = sorted(map(int, input().split()))
selected = []
nPm(0)