import sys
input = sys.stdin.readline

def recur(cur, start, cnt):
    global ans
    if cur == cnt:
        r, g, b = 0, 0, 0
        for color in selected:
            r += paints[color][0]
            g += paints[color][1]
            b += paints[color][2]
        r //= cnt
        g //= cnt
        b //= cnt
        ans = min(ans, abs(moonduri[0] - r) + abs(moonduri[1] - g) + abs(moonduri[2] - b))
        return
    for i in range(start, n):
        selected.append(i)
        recur(cur + 1, i + 1, cnt)
        selected.pop()

n = int(input())
paints = [list(map(int, input().split())) for _ in range(n)]
moonduri = list(map(int, input().split()))
ans = 1e10
for i in range(2, n + 1):
    if i > 7:
        break
    selected = []
    recur(0, 0, i)
print(ans)