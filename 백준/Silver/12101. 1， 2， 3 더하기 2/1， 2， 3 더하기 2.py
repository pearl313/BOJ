import sys
input = sys.stdin.readline

n, k = map(int, input().split())
selected = []
ans = []
def recur(cur):
    if sum(selected) > n:
        return
    if sum(selected) == n:
        ans.append(selected[:])
        return
    for i in range(1, 4):
        selected.append(i)
        recur(cur + 1)
        selected.pop()
recur(0)
if k > len(ans):
    print(-1)
else:
    print('+'.join(map(str, sorted(ans)[k - 1])))