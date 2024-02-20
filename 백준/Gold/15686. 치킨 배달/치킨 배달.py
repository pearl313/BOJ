import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if info[i][j] == 0:
            continue
        if info[i][j] == 1:
            house.append((i, j))
        elif info[i][j] == 2:
            chicken.append((i, j))

def check(ls):
    distance = 0
    for i in range(len(house)):
        temp = 1e10
        for j in range(m):
            temp = min(temp, abs(house[i][0] - ls[j][0]) + abs(house[i][1] - ls[j][1]))
        distance += temp
    return distance

arr = [0 for _ in range(m)]
ans = 1e10
def recur(cur, start):
    global ans
    if cur == m:
        ans = min(ans, check(arr))
        return
    for i in range(start, len(chicken)):
        arr[cur] = chicken[i]
        recur(cur + 1, i + 1)
recur(0, 0)
print(ans)