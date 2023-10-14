import sys
input = sys.stdin.readline

def recur(cur):
    if cur == k:
        ans.add(''.join(num))
        return
    for i in range(n):
        if not visited[i]:
            num.append(str(ls[i]))
            visited[i] = True
            recur(cur + 1)
            num.pop()
            visited[i] = False

n = int(input())
k = int(input())
ls = list(int(input()) for _ in range(n))
visited = [False] * n
num = []
ans = set()
recur(0)
print(len(ans))