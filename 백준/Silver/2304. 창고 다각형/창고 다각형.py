import sys
input = sys.stdin.readline

n = int(input())
ls = [0] * 1001
max_idx = 0
max_val = 0
for _ in range(n):
    l, h = map(int, input().split())
    ls[l] = h
    if max_val < h:
        max_idx = l
        max_val = h

for i in range(1, max_idx + 1):
    ls[i] = ls[i - 1] if ls[i - 1] > ls[i] else ls[i]
for i in range(999, max_idx, -1):
    ls[i] = ls[i + 1] if ls[i + 1] > ls[i] else ls[i]
print(sum(ls))