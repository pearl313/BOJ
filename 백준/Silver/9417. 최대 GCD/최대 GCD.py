import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    m = len(nums)
    ans = 0
    for i in range(m):
        for j in range(i + 1, m):
            ans = max(ans, get_gcd(nums[i], nums[j]))
    print(ans)