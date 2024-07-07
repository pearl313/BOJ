import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x = set(input().strip())
    print(len(x))