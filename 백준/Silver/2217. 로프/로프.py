import sys
input = sys.stdin.readline

n = int(input())
weight = list(int(input()) for _ in range(n))

weight.sort(reverse=True)
ans = -1e10
for i in range(n):
    ans = max(ans, weight[i] * (i + 1))
    
print(ans)