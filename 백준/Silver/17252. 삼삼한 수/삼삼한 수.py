import sys
input = sys.stdin.readline

samsam = []
for i in range(21):
    samsam.append(3 ** i)
num = int(input())
cnt = 0
for i in range(20, -1, -1):
    if num >= samsam[i]:
        num -= samsam[i]
        cnt += 1
if not num and cnt:
    print('YES')
else:
    print('NO')