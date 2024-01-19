import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
total = 0
min_val = 0
if m == 1:
    m += 1
for i in range(m, n + 1):
    cnt = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        total += i
        if min_val == 0:
            min_val = i
if total:
    print(total)
    print(min_val)
else:
    print(-1)