import sys
input = sys.stdin.readline

n = int(input())
score = list(int(input()) for _ in range(n))

cnt = 0
for i in range(n - 1, 0, -1):
    if score[i - 1] >= score[i]:
        cnt += score[i - 1] - score[i] + 1
        score[i - 1] = score[i] - 1

print(cnt)