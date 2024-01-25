import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = [0] + list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(n + 1):
    prefix[i] = prefix[i - 1] + ls[i]
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])