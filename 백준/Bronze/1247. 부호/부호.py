import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    S = sum(list(int(input()) for _ in range(N)))
    if S == 0:
        print(0)
    elif S > 0:
        print('+')
    else:
        print('-')