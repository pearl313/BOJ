import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
arr = [0 for _ in range(n)]
visited = [False for _ in range(n)]

def recur(cur):
    global ans
    if cur == n:
        temp = 0
        for j in range(n - 1):
            temp += abs(arr[j] - arr[j + 1])
        ans = max(ans, temp)
        return
    for i in range(n):
        if visited[i]:
            continue
        arr[cur] = ls[i]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False
ans = -1e10
recur(0)
print(ans)