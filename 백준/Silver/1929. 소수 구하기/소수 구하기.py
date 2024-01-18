import sys
input = sys.stdin.readline

m, n = map(int, input().split())
isPrime = [True for _ in range(n + 1)]
isPrime[1] = False
for i in range(2, n + 1):
    if not isPrime[i]:
        continue
    for j in range(i * i, n + 1, i):
        isPrime[j] = False
    if i >= m:
        print(i)