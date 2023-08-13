import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    G = int(input())
    num = list(int(input()) for _ in range(G))
    check = set()
    ans = 0
    i = 1
    while True:
        for n in num:
            if n % i in check:
                check = set()
                break
            check.add(n % i)
        else:
            print(i)
            break
        i += 1