import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    num = list(map(int, input().split(',')))
    print(sum(num))