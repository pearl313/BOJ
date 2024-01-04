import sys
input = sys.stdin.readline

height = list(int(input()) for _ in range(9))
for i in range(9):
    for j in range(i + 1, 9):
        temp = height[i] + height[j]
        if sum(height) - temp == 100:
            height = height[:i] + height[i + 1:j] + height[j + 1:]
            for k in sorted(height):
                print(k)
            exit()