from collections import defaultdict

ls = list(int(input()) for _ in range(10))
print(sum(ls) // 10)
nums = defaultdict(int)
for i in ls:
    nums[i] += 1
print(max(nums, key=nums.get))