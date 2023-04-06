import sys
input = sys.stdin.readline

N = input().strip()
if '3' in N or '4' in N or '7' in N:
    print('no')
    exit()

cnt_1 = 0
for i in range(1, int(int(N) ** 0.5) + 1):
    if int(N) % i == 0:
       cnt_1 += 1

change = ''
N = N[::-1]
for i in N:
    if i in ('0', '1', '2', '5', '8'):
        change += i
    elif i == '6':
        change += '9'
    elif i == '9':
        change += '6'

change = int(change)
if change == 1:
    print('no')
    exit()
cnt_2 = 0
for i in range(1, int(change ** 0.5) + 1):
    if change % i == 0:
        cnt_2 += 1
if cnt_2 == 1 and cnt_1 == 1:
    print('yes')
else:
    print('no')