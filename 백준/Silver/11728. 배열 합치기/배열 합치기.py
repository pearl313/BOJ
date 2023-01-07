import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
arr = sorted(a + b)
print(*arr)