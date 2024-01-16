import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

a, b = map(int, input().split())
# 가능한 두 수 찾아서 최대공약수와 최소공배수가 같은 거 찾기
x = a
ans = 1e10
ans_x, ans_y = 0, 0
while x <= int((a * b) ** 0.5):
    y = a * b // x
    if get_gcd(x, y) == a:
        if x * y == a * b:
            if ans > x + y:
                ans = x + y
                ans_x, ans_y = x, y
    x += a
print(ans_x, ans_y)