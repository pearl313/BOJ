import sys
input = sys.stdin.readline

k, l = map(int, input().split())
nums = dict()

for i in range(l):
    n = input().strip()
    nums[n] = i

for a, b in sorted(nums.items(), key=lambda x:x[1])[:k]:
    print(a)