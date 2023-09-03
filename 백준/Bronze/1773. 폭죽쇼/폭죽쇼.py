import sys
input = sys.stdin.readline

n, c = map(int, input().split())
num = list(int(input()) for _ in range(n))
time = [0] * (c + 1)
for i in num:
    for j in range(1, c + 1):
        if j % i == 0:
            time[j] = 1
print(sum(time))