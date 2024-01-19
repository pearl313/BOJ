import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
s = 0
e = 0
cnt = 0
while e < n:
    total = sum(nums[s:e + 1])
    if total == m:
        cnt += 1
        s += 1
        e += 1
        if e == n:
            break
    elif total < m:
        e += 1
        if e == n:
            break
        total += nums[e]
    else:
        total -= nums[s]
        s += 1
print(cnt)