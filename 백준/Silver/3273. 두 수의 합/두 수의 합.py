import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))
x = int(input())

s = 0
e = n - 1
cnt = 0
while s < e:
    temp = ls[s] + ls[e]
    if temp > x:
        e -= 1
    elif temp < x:
        s += 1
    else:
        s += 1
        cnt += 1
print(cnt)