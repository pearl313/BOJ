import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

first = True
heart_x, heart_y = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '*' and first:
            print(i + 2, j + 1)
            heart_x, heart_y = i + 1, j
            first = False
            break
    if not first:
        break

ls = []
# 팔
left_arm, right_arm = 0, 0
for i in range(n):
    if arr[heart_x][i] == '*':
        if i < heart_y:
            left_arm += 1
        elif i == heart_y:
            continue
        else:
            right_arm += 1
ls.append(left_arm)
ls.append(right_arm)

# 허리
waist = 0
leg_start = 0
for i in range(heart_x + 1, n):
    if arr[i][heart_y] == '_':
        leg_start = i
        break
    waist += 1
ls.append(waist)

# 다리
left_leg, right_leg = 0, 0
for i in range(leg_start, n):
    if arr[i][heart_y - 1] == '*':
        left_leg += 1
    if arr[i][heart_y + 1] == '*':
        right_leg += 1
ls.append(left_leg)
ls.append(right_leg)

print(*ls)