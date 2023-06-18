import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())
if a <= 4 and b <= 4:
    print(abs(a - b))
elif a % 4 == 0:
    print(abs((a // 4) - (b // 4 + 1)) + abs(4 - (b % 4)))
elif b % 4 == 0:
    print(abs((a // 4 + 1) - (b // 4)) + abs((a % 4) - 4))
else:
    print(abs((a // 4) - (b // 4)) + abs((a % 4) - (b % 4)))