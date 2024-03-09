import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))

ans = -1e10
selected = []
def recur(cur):
    global ans
    if cur:
        temp = int(''.join(selected))
        if temp <= n:
            ans = max(ans, temp)
        if cur == len(str(n)):
            return
    for i in range(k):
        selected.append(str(ls[i]))
        recur(cur + 1)
        selected.pop()

recur(0)
print(ans)