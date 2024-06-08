import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(p)]

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

cnt = 0
for a, b in ls:
    if a >= x and a <= x + w and b >= y and b <= y + h:
        cnt += 1
    elif dist(x, y + h / 2, a, b) <= h / 2 or dist(x + w, y + h / 2, a, b) <= h / 2:
        cnt += 1
print(cnt)