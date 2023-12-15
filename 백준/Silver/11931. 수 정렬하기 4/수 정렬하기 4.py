import sys
input = sys.stdin.readline

n = int(input())
ls = list(int(input()) for _ in range(n))
for i in sorted(ls, reverse=True):
    print(i)