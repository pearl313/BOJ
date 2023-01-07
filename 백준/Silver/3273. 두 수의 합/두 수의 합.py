import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())
# cnt = 0
# i = 0
# while i <= n // 2:
#     temp = arr[i] + arr[n - i - 1]
#     if temp == x:
#         cnt += 1
#     elif temp > x:
#         temp = temp - arr[n - i - 1] + arr[n - i - 2]
#     elif temp < x:
#         temp = temp - arr[i] + arr[i + 1]
#     i += 1
# print(cnt)
l = 0
r = n - 1
cnt = 0
while l < r:
    cur = arr[l] + arr[r]
    if cur == x:
        cnt += 1
        l += 1
        r -= 1
    elif cur < x:
        l += 1
    else:
        r -= 1
print(cnt)
