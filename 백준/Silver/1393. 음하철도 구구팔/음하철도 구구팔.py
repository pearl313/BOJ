import sys, math
input = sys.stdin.readline

def gcd(a, b):
    while b:
        temp = a % b
        a = b
        b = temp
    return a

def distance(a, b):
    return math.sqrt((a - xs) ** 2 + (b - ys) ** 2)

xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

get_gcd = gcd(dx, dy)
dx //= get_gcd
dy //= get_gcd

x, y = xe, ye
# 가능한 모든 점 넣어서 거리 확인해보기
while distance(x, y) > distance(x + dx, y + dy):
    x += dx
    y += dy
print(x, y)