import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ls = list(input().split(" "))
    for i in ls:
        if '\n' in i:
            print(i[::-1][1:])
        else:
            print(i[::-1], end=' ')