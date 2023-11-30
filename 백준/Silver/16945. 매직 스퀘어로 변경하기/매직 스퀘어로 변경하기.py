import sys
input = sys.stdin.readline

def check(ls):
    hap = sum(ls[0])
    for i in range(3):
        if sum(ls[i]) != hap:
            return False
        col = 0
        for j in range(3):
            col += ls[j][i]
        if col != hap:
            return False
    if ls[0][0] + ls[1][1] + ls[2][2] != hap:
        return False
    if ls[2][0] + ls[1][1] + ls[0][2] != hap:
        return False
    return True

def cost(ls):
    global arr
    total = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] != ls[i][j]:
                total += abs(arr[i][j] - ls[i][j])
    return total

def recur(cur):
    global ans
    if cur == 9:
        ls = [selected[:3], selected[3:6], selected[6:]]
        if check(ls):
            ans = min(ans, cost(ls))
        return
    for i in range(1, 10):
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            recur(cur + 1)
            visited[i] = False
            selected.pop()

arr = [list(map(int, input().split())) for _ in range(3)]
selected = []
visited = [False] * 10
ans = 1e10
recur(0)
print(ans)