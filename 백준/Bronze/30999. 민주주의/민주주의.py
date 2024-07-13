import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
for i in range(n):
    s = input().strip()
    if s.count('O') >= m / 2:
        cnt += 1
print(cnt)