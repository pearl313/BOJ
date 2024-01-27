import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
ls = [0]
for i in range(1, n + 1):
    ls.append(b[i] - a[i])

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + ls[i]
cnt = defaultdict(int)
ans = 0
for i in range(n + 1):
    ans += cnt[prefix[i]]
    cnt[prefix[i]] += 1
print(ans)