import sys
input = sys.stdin.readline

n, b, h, w = map(int, input().split())

ans = 1e10
for _ in range(h):
    per = int(input())
    ls = list(map(int, input().split()))

    check = False
    for i in ls:
        if i >= n:
            check = True

    if check:
        if per * n <= b:
            ans = min(ans, per * n)

print(ans if ans != 1e10 else 'stay home')