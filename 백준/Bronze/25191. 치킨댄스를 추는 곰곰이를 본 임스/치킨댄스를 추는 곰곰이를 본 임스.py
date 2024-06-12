import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
print(a // 2 + b if a // 2 + b <= n else n)