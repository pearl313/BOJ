import sys, math
input = sys.stdin.readline

xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())


def distance(a, b):
    return math.sqrt((a - xs) ** 2 + (b - ys) ** 2)


a, b = dx, dy
# 최대공약수 구하기
while b:
    temp = a % b
    a = b
    b = temp

dx //= a
dy //= a
    
x, y = xe, ye
# 가능한 모든 점 넣어서 거리 확인해보기
while distance(x, y) > distance(x + dx, y + dy):    
    x += dx
    y += dy
print(x, y)