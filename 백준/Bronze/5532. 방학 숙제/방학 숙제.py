import sys, math
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(L - int(max(math.ceil(A / C), math.ceil(B / D))))