import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    a, b = input().split()
    ls.append([int(a), b])
ls.sort(key=lambda x : x[0])
for i in ls:
    print(*i)