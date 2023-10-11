import sys
input = sys.stdin.readline

def recur(start):
    if len(selected) == m:
        print(*selected)
        return
    for i in range(start, len(ls)):
        selected.append(ls[i])
        recur(i)
        selected.pop()

n, m = map(int, input().split())
ls = sorted(list(set(map(int, input().split()))))
selected = []
recur(0)