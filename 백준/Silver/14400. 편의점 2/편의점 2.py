import sys
input = sys.stdin.readline

n = int(input())
x_ls = []
y_ls = []
for _ in range(n):
    x, y = map(int, input().split())
    x_ls.append(x)
    y_ls.append(y)
x_ls = sorted(x_ls)
y_ls = sorted(y_ls)
x = x_ls[n // 2] if n % 2 else x_ls[n // 2 - 1]
y = y_ls[n // 2] if n % 2 else y_ls[n // 2 - 1]
ans = 0
for i in range(n):
    ans += abs(x_ls[i] - x) + abs(y_ls[i] - y)
print(ans)