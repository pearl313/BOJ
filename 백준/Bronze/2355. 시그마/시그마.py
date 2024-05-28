import sys
input = sys.stdin.readline

a, b = map(int, input().split())
print((max(a, b) + 1) * max(a, b) // 2 - (min(a, b) - 1) * min(a, b) // 2)