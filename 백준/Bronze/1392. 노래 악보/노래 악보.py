import sys
input = sys.stdin.readline

n, q = map(int, input().split())
ls = list(int(input()) for _ in range(n))
time = list(int(input()) for _ in range(q))

cnt = []
for i in range(n):
    for j in range(ls[i]):
        cnt.append(i + 1)

for t in time:
    print(cnt[t])