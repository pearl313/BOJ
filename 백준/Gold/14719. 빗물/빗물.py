H, W = map(int, input().split())
block = list(map(int, input().split()))
total = 0

for i in range(1, W - 1):
    left = max(block[:i])
    right = max(block[i + 1:])
    if min(left, right) > block[i]:
        total += min(left, right) - block[i]
print(total)