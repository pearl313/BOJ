import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if sum(selected) > n:
        return
    if sum(selected) == n:
        ans += 1
        return
    for i in range(1, 4):
        selected.append(i)
        recur(cur + 1)
        selected.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    selected = []
    ans = 0
    recur(1)
    print(ans)