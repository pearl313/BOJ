import sys
input = sys.stdin.readline

l = int(input())
s = [0] + sorted(map(int, input().split()))
n = int(input())

if n in s:
    print(0)
else:
    for i in range(l):
        if s[i] > n or s[i + 1] < n:
            continue
        print((n - s[i]) * (s[i + 1] - n) - 1)
        break