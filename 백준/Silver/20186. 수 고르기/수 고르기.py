import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = sorted(map(int, input().split()))

score = 0
for i in range(1, k + 1):
    score += ls[-i] - (i - 1)
print(score)