import sys
input = sys.stdin.readline

n = int(input())
can = 1
for _ in range(n):
    can = can - 1 + int(input())
print(can)