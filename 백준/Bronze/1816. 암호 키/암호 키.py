import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = int(input())
    ls = []
    for i in range(1, 1000001):
        if num % i == 0:
            ls.append(i)
    if len(ls) == 1:
        print('YES')
    else:
        print('NO')