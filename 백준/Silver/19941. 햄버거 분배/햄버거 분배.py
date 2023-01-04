import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = input().strip()
yumyum = 0
burger = [True] * N
for i in range(N):
    if table[i] == 'P':
        for j in range(i - K, i + K + 1):
            if 0 <= j < N and table[j] == 'H' and burger[j]:
                yumyum += 1
                burger[j] = False
                break
print(yumyum)