import sys
input = sys.stdin.readline

def recur(cur):
    if sum(selected) > n:
        return
    elif sum(selected) == n:
        total.append(selected[:])
        return
    for i in range(1, 4):
        selected.append(i)
        recur(cur + 1)
        selected.pop()

n, k = map(int, input().split())
selected = []
total = []
recur(0)
ans = []
if len(total) >= k:
    for i in sorted(total)[k - 1]:
        ans.append(i)
        ans.append('+')
    for i in ans[:len(ans) - 1]:
        print(i, end='')
else:
    print(-1)