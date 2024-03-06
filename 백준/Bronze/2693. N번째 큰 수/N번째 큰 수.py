import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = sorted(map(int, input().split()))
    print(a[-3])