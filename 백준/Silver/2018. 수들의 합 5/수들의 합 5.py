import sys
input = sys.stdin.readline

n = int(input())
nums = [i for i in range(1, n + 1)]
i, j = 0, 1
cnt = 0
while j <= n + 1:
    total = sum(nums[i:j])
    if total < n:
        j += 1
    elif total > n:
        i += 1
    elif total == n:
        cnt += 1
        i += 1
        j += 1
print(cnt)