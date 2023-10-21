import sys
input = sys.stdin.readline

def recur(cur):
    if cur == m:
        temp = selected[:]
        ans.add(tuple(temp))
        return
    for i in range(n):
        selected.append(ls[i])
        recur(cur + 1)
        selected.pop()

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))
selected = []
ans = set()
recur(0)
for i in sorted(ans):
    print(*i)