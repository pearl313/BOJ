import sys
input = sys.stdin.readline

cnt = []
for i in range(1, 6):
    temp = input().strip()
    if 'FBI' in temp:
        cnt.append(i)
if cnt:
    print(*cnt)
else:
    print('HE GOT AWAY!')