import sys
input = sys.stdin.readline

n = int(input())
ls = [0] + list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = max(prefix[i - 1] + ls[i], ls[i])
print(max(prefix[1:]))