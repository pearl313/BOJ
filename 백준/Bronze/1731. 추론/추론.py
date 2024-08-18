import sys
input = sys.stdin.readline

n = int(input())
ls = list(int(input()) for _ in range(n))
ans = 0
if ls[1] / ls[0] == ls[1] // ls[0]:
    ans = int(ls[-1] * (ls[1] / ls[0]))
else:
    ans = ls[-1] + (ls[1] - ls[0])
print(ans)