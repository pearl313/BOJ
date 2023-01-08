import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
l = 0
r = n - 1
minV = float('inf')
ans_1, ans_2 = arr[l], arr[r]
while l < r:
    temp = arr[l] + arr[r]
    if abs(minV) > abs(temp):
        minV = temp
        ans_1, ans_2 = arr[l], arr[r]
    if temp < 0:
        l += 1
    elif temp > 0:
        r -= 1
    else:
        break
print(ans_1, ans_2)