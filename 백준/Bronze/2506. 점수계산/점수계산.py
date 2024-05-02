import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
total = 0
cur = 1
for i in range(n):
    if ls[i] == 0:
        cur = 1
    else:
        total += cur
        cur += 1
print(total)