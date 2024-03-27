import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    score = sorted(map(int, input().split()))
    score = score[1:4]
    print('KIN' if max(score) - min(score) >= 4 else sum(score))