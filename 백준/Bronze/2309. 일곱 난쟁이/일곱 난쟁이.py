height = sorted([int(input()) for _ in range(9)])

for i in range(len(height)):
    for j in range(i + 1, len(height)):
        if sum(height) - height[i] - height[j] == 100:
            a = height[i]
            b = height[j]
            
for i in height:
    if i != a and i != b:
        print(i)