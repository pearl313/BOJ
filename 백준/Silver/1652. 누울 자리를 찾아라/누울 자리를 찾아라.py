import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
horizontal = 0
vertical = 0
for i in range(n):
    for j in arr[i].split('X'):
        if len(j) > 1:
            horizontal += 1

new_arr = list(map(list, zip(*arr[::-1])))
for i in range(n):
    temp = ''.join(new_arr[i])
    for j in temp.split('X'):
        if len(j) > 1:
            vertical += 1
print(horizontal, vertical)