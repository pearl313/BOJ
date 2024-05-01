import sys
input = sys.stdin.readline

m = int(input())
cup = [False] * 4
cup[1] = True
for _ in range(m):
    x, y = map(int, input().split())
    cup[x], cup[y] = cup[y], cup[x]
print(cup.index(True))