import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = sorted(map(int, input().split()))
print(a[k - 1])