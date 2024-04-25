import sys
input = sys.stdin.readline

n = int(input())
x_ls = []
y_ls = []
for _ in range(n):
    x, y = map(int, input().split())
    x_ls.append(x)
    y_ls.append(y)
print((max(x_ls) - min(x_ls)) * (max(y_ls) - min(y_ls)))