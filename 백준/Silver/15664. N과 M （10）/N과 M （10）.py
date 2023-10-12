import sys

input = sys.stdin.readline


def recur(start):
    if len(selected) == m:
        ans.add(tuple(selected))
        return
    for i in range(start, len(ls)):
        selected.append(ls[i])
        recur(i + 1)
        selected.pop()


n, m = map(int, input().split())
ls = sorted(map(int, input().split()))
selected = []
ans = set()
recur(0)
for a in sorted(ans):
    print(*a)