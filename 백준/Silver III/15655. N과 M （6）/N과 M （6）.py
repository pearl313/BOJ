import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == M:
        print(*selected)
        return
    for i in range(start, N):
        selected.append(ls[i])
        recur(cur + 1, i + 1)
        selected.pop()

N, M = map(int, input().split())
ls = sorted(map(int, input().split()))
selected = []
recur(0, 0)