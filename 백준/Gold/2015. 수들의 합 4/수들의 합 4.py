import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i]
cnt = defaultdict(int)

ans = 0
for i in range(n + 1):
    ans += cnt[prefix[i] - k]
    cnt[prefix[i]] += 1
print(ans)