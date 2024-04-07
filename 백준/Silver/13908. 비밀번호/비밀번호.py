import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

num = [0] * 10
for i in ls:
    num[i] = 1

total = sum(num)

selected = []
def recur(cur, start):
    global ans
    if cur == n:
        temp = [0] * 10
        for j in selected:
            if num[j]:
                temp[j] = 1
        if sum(temp) < total:
            return
        ans += 1
        return
    for i in range(10):
        selected.append(i)
        recur(cur + 1, i)
        selected.pop()

ans = 0
recur(0, 0)
print(ans)