import sys
input = sys.stdin.readline

n, l = map(int, input().split())
l = str(l)
cnt = 0
i = 1
while True:
    if not l in str(i):
        cnt += 1
    if cnt == n:
        print(i)
        break
    i += 1