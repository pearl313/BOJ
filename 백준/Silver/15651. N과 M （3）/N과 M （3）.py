import sys
input = sys.stdin.readline

def recur(cur):
    if cur == M:
        print(*selected)
        return
    for i in range(1, N + 1):
        selected.append(i)
        recur(cur + 1)
        selected.pop()

N, M = map(int, input().split())
selected = []
recur(0)