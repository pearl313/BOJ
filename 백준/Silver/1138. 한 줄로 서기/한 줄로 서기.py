import sys
input = sys.stdin.readline

def recur(cur):
    if cur == n:
        for j in range(1, n + 1):
            cnt = 0
            for k in selected[:j + 1]:
                if k > selected[j]:
                    cnt += 1
            if info[selected[j]] != cnt:
                return
        print(*selected[1:])
        exit()
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            recur(cur + 1)
            visited[i] = False
            selected.pop()

n = int(input())
info = [0] + list(map(int, input().split()))
selected = [0]
visited = [False] * (n + 1)
recur(0)