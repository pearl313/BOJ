import sys
input = sys.stdin.readline

def recur(cur, start, k):
    global ans
    if cur == k:
        health = 100
        joy = 0
        for j in selected:
            health -= lose[j]
            joy += gain[j]
            if health <= 0:
                return
        ans = max(ans, joy)
        return
    for i in range(start, N + 1):
        selected.append(i)
        recur(cur + 1, i + 1, k)
        selected.pop()

N = int(input())
lose = [0] + list(map(int, input().split()))
gain = [0] + list(map(int, input().split()))
selected = []
ans = 0
for i in range(1, N + 1):
    recur(0, 1, i)
print(ans)