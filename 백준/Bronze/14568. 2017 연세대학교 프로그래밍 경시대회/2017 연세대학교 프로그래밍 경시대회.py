import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for x in range(1, 101):
    for y in range(1, 101):
        z = n - x - y
        if x + y + z != n:
            continue
        if z < y + 2:
            continue
        if x % 2 == 1:
            continue
        cnt += 1
print(cnt)