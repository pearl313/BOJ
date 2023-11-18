import sys, math
input = sys.stdin.readline

a, i = map(int, input().split())
for n in range(1, a * i + 1):
    if math.ceil(n / a) == i:
        print(n)
        break