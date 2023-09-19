import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())
print(0 if k * n < m else abs(m - k * n))