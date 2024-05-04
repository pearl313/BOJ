import sys
input = sys.stdin.readline

n = int(input())
cnt = [0] * 5
name = ['Q1', 'Q2', 'Q3', 'Q4', 'AXIS']
for _ in range(n):
    x, y = map(int, input().split())
    if 0 in [x, y]:
        cnt[4] += 1
    elif x > 0 and y > 0:
        cnt[0] += 1
    elif x < 0 and y > 0:
        cnt[1] += 1
    elif x < 0 and y < 0:
        cnt[2] += 1
    else:
        cnt[3] += 1

for i in range(5):
    print(f'{name[i]}: {cnt[i]}')