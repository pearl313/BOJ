import sys
input = sys.stdin.readline

n, h = map(int, input().split())
arr = [0] * (h + 1)
for i in range(n):
    num = int(input())
    if i % 2:
        arr[h - num + 1] += 1
    else:
        arr[1] += 1
        arr[num + 1] -= 1
prefix = [0] * (h + 1)
for i in range(1, h + 1):
    prefix[i] = prefix[i - 1] + arr[i]
print(min(prefix[1:]), prefix[1:].count(min(prefix[1:])))