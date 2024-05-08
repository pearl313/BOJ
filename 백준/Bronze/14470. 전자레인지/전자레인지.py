import sys
input = sys.stdin.readline

temp = list(int(input()) for _ in range(5))
a, b, c, d, e = temp
ans = 0
zero = True
while a < b:
    if a < 0:
        ans += c * abs(a)
        a = 0
    else:
        if zero and a == 0:
            ans += d
            zero = False
        else:
            ans += (b - a) * e
            a = b
print(ans)