import sys
input = sys.stdin.readline

nums = []
cnt = 0
i = 1
while cnt < 1000001:
    check = dict()
    possible = True
    j = i
    while j:
        num = j % 10
        if num in check.keys():
            possible = False
            break
        else:
            check[num] = 1
        j //= 10
    if possible:
        nums.append(i)
        cnt += 1
    i += 1

while True:
    n = int(input())
    if not n:
        exit()
    print(nums[n - 1])