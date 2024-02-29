import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())
for _ in range(t):
    ls = list(map(int, input().split()))
    n = ls[0]
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += get_gcd(ls[i], ls[j])
    print(total)