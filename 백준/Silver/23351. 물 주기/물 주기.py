import sys
input = sys.stdin.readline

N, K, A, B = map(int, input().split())
pots = list(K for _ in range(N))
days = 0
while not 0 in pots:
    for i in range(0, N, A):
        for n in range(i, i + A):
            pots[n] += B
        days += 1
        for j in range(N):
            pots[j] -= 1
        if 0 in pots:
            break
print(days)
