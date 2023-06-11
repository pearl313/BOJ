import sys, math
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
Y, M = 0, 0
for i in range(N):
    if times[i] % 30 == 0:
        Y += (math.ceil(times[i] / 30) + 1) * 10
    elif times[i] % 30 != 0:
        Y += math.ceil(times[i] / 30) * 10
    if times[i] % 60 == 0:
        M += (math.ceil(times[i] / 60) + 1) * 15
    elif times[i] % 60 != 0:
        M += math.ceil(times[i] / 60) * 15
ans = min(Y, M)
if Y == M:
    print('Y', 'M', ans)
else:
    print('Y' if ans == Y else 'M', ans)