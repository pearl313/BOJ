import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
ls = sorted(ls, reverse=True)
ans = 1
for i in range(n):
    ans = max(ans, ls[i] + i + 1)
print(ans + 1)