import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
cnt = 0
seat = [0] * 110
for i in range(n):
    if seat[ls[i]] == 0:
        seat[ls[i]] = 1
    else:
        cnt += 1
print(cnt)