import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
ans = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if ans < arr[i][j]:
            ans = arr[i][j]
            x, y = i, j
print(ans)
print(x + 1, y + 1)