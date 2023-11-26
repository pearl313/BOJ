import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == len(a):
        temp = int(''.join(selected))
        if temp < b and len(str(temp)) == len(a):
            ans = max(ans, temp)
        return
    for i in range(len(a)):
        if not visited[i]:
            visited[i] = True
            selected.append(a[i])
            recur(cur + 1)
            visited[i] = False
            selected.pop()

a, b = map(int, input().split())
a = list(str(a))
selected = []
visited = [False] * len(a)
ans = 0
recur(0)
print(ans if ans else -1)