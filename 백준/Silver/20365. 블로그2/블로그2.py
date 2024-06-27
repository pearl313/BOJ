import sys
input = sys.stdin.readline

n = int(input())
ls = list(input().strip())

cnt_r = ls.count('R')
cnt_b = ls.count('B')

if cnt_r == 0 or cnt_b == 0:
    print(1)
    exit()

split_r = ''.join(ls).split('R')
split_b = ''.join(ls).split('B')

cnt_B, cnt_R = 0, 0
for i in split_r:
    if i == '':
        continue
    cnt_B += 1

for i in split_b:
    if i == '':
        continue
    cnt_R += 1

print(min(cnt_B, cnt_R) + 1)