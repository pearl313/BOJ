import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
s = ['a'] + list(input().strip())
prefix = [0] * (n + 1)
suffix = [0] * (n + 2)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + (1 if s[i] == 'W' else 0)
for i in range(n, 0, -1):
    suffix[i] = suffix[i + 1] + (1 if s[i] == 'E' else 0)
ans = 0
for i in range(1, n + 1):
    if s[i] == 'H':
        ans += prefix[i] * (pow(2, suffix[i], 1000000007) - suffix[i] - 1)
        ans %= 1000000007
print(ans)