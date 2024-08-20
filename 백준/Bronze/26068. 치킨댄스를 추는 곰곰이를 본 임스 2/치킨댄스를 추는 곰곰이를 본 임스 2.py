import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(n):
    gift = list(input().split('-'))
    if int(gift[-1]) <= 90:
        cnt += 1
print(cnt)