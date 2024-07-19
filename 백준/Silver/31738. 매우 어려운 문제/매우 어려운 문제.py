import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n >= m:
    print(0)
else:
    total = 1
    for i in range(2, n + 1):
        total *= i
        total %= m
        if total == 0:
            break
    print(total % m)