import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    pw = input().strip()
    print('yes' if len(pw) >= 6 and len(pw) <= 9 else 'no')