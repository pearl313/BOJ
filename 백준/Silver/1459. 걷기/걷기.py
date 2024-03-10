import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

print(min(max(x, y) * s if (x + y) % 2 == 0 else (max(x, y) - 1) * s + w, min(x, y) * s + abs(x - y) * w, (x + y) * w))