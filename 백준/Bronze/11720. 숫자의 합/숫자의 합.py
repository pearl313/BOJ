import sys
input = sys.stdin.readline

n = int(input())
ls = list(input().strip())
ans = 0
for i in ls:
    ans += int(i)
print(ans)