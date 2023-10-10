import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == len(ls):
        if int(''.join(selected)) <= x or selected[0] == '0':
            return
        ans = min(ans, int(''.join(selected)))
        return
    for i in range(len(ls)):
        if not visited[i]:
            selected.append(ls[i])
            visited[i] = True
            recur(cur + 1)
            selected.pop()
            visited[i] = False

x = int(input())
ls = list(str(x))
selected = []
visited = [False] * (len(ls))
ans = 1e10
recur(0)
print(ans if ans != 1e10 else 0)