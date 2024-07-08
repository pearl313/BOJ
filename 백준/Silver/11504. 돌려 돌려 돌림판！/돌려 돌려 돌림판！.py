import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = int(''.join(list(input().split())))
    y = int(''.join(list(input().split())))
    ls = list(input().split())

    possible = []
    for i in range(n):
        if i + m > n:
            possible.append(int(''.join(ls[i:] + ls[:(i + m) % n])))
        else:
            possible.append(int(''.join(ls[i:i + m])))

    cnt = 0
    for i in range(n):
        if x <= possible[i] <= y:
            cnt += 1
    print(cnt)