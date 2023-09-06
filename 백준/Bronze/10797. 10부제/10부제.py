import sys
input = sys.stdin.readline

n = input().strip()
car = list(input().split())
cnt = 0
for i in range(5):
    if car[i][-1] == n:
        cnt += 1
print(cnt)