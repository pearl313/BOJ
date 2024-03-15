import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(int(input()) for _ in range(n))

ans = 1e10
for i in ls:
    up, down = 1, 1
    for j in range(1, 5):
        if i + j in ls:
            up += 1
        if i - j in ls:
            down += 1
    ans = min(ans, 5 - up, 5 - down)

print(ans)