import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
time = [0] * 101
total = 0
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        time[i] += 1

for i in time:
    if i == 1:
        total += a
    elif i == 2:
        total += b * 2
    elif i == 3:
        total += c * 3
    else:
        continue
print(total)