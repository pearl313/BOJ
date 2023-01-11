import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    a = 1
    for i in range(1, M + 1):
        a *= i
    b = 1
    for j in range(1, M - N + 1):
        b *= j
    c = 1
    for k in range(1, N + 1):
        c *= k
    print(a // (b * c))