import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a = str(a)
arr = [0 for _ in range(len(a))]
visited = [False for _ in range(len(a))]

def recur(cur):
    global ans
    if cur == len(a):
        temp = int(''.join(arr))
        if temp < b:
            if len(str(temp)) != len(arr):
                return
            ans = max(ans, temp)
        return
    for i in range(len(a)):
        if visited[i]:
            continue
        arr[cur] = a[i]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False
ans = -1e10
recur(0)
print(ans if ans != -1e10 else -1)