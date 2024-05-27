import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = a * p
y = b if p <= c else b + (p - c) * d
print(min(x, y))