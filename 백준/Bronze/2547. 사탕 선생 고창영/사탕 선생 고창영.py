import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    blank = input()
    n = int(input())
    ls = list(int(input()) for _ in range(n))
    print('YES' if sum(ls) % n == 0 else 'NO')