import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))

print(ls[n // 2 - 1] if n % 2 == 0 else ls[n // 2])