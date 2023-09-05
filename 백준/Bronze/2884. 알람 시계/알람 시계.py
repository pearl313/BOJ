import sys
input = sys.stdin.readline

h, m = map(int, input().split())
if m >= 45:
    print(h, m - 45)
else:
    m = m + 60 - 45
    h -= 1
    print(24 + h if h < 0 else h, m)