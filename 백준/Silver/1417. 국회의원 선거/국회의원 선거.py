N = int(input())
nums = list(int(input()) for _ in range(N))
cnt = 0
if len(nums) > 1:
    remainder = sorted(nums[1:], reverse=True)
    while nums[0] <= max(remainder):
        remainder[0] -= 1
        nums[0] += 1
        cnt += 1
        remainder.sort(reverse=True)

print(cnt)