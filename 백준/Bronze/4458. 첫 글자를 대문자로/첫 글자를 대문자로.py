import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = list(input().strip())
    s[0] = s[0].upper()
    print(''.join(s))