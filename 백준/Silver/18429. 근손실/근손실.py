import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == n:
        total = 0
        for j in range(n):
            total += selected[j]
            total -= k
            if total < 0:
                return
        ans += 1
        return
    for i in range(n):
        if not visited[i]:
            selected.append(gain[i])
            visited[i] = True
            recur(cur + 1)
            selected.pop()
            visited[i] = False

n, k = map(int, input().split())
gain = list(map(int, input().split()))
selected = []
visited = [False] * n
ans = 0
recur(0)
print(ans)