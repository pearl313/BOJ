import sys
input = sys.stdin.readline

a, b = map(int, input().split())
val = a * ((100 - b) * 0.01)
print(0 if val >= 100 else 1)