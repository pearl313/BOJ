import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
ls = list(map(int, input().split()))

prefix = [0] * (n + 1)
suffix = [0] * (n + 1)
prefix[0] = ls[0]
for i in range(1, n):
    prefix[i] = get_gcd(prefix[i - 1], ls[i])
suffix[n - 1] = ls[n - 1]
for i in range(n - 2, -1, -1):
    suffix[i] = get_gcd(suffix[i + 1], ls[i])

ans = 0
minus = 0
for i in range(n):
    result = get_gcd(prefix[i - 1], suffix[i + 1])
    if ls[i] % result == 0:
        continue
    ans = result
    minus = ls[i]
if ans != 0 and minus != 0:
    print(ans, minus)
else:
    print(-1)