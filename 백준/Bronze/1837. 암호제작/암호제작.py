import sys
input = sys.stdin.readline

P, K = map(int, input().split())
for i in range(2, K):
    if P % i != 0:
        continue
    print('BAD', i)
    exit()
else:
    print('GOOD')