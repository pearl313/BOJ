import sys
input = sys.stdin.readline

d, h, w = map(int, input().split())
print(int(h * (d / (h ** 2 + w ** 2) ** 0.5)), int(w * (d / (h ** 2 + w ** 2) ** 0.5)))