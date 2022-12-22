import sys
input = sys.stdin.readline

dial = [[1, 0], [0, 3], [1, 3], [2, 3], [0, 2], [1, 2], [2, 2], [0, 1], [1, 1], [2, 1]]

def effort(a, b):
    return abs(dial[a][0] - dial[b][0]) + abs(dial[a][1] - dial[b][1])

time = input().strip()
hour = time[:2]
minute = time[3:]

hour_ls = []
min_ls = []
same_h = same_m = ''
for i in range(100):
    if i % 24 == int(hour):
        if len(str(i)) == 1:
            same_h = '0' + str(i)
        else:
            same_h = str(i)
        hour_ls.append(same_h)
        same_h = ''
    if i % 60 == int(minute):
        if len(str(i)) == 1:
            same_m = '0' + str(i)
        else:
            same_m = str(i)
        min_ls.append(same_m)
        same_m = ''

val = []
for i in hour_ls:
    for j in min_ls:
        value = effort(int(i[0]), int(i[1])) + effort(int(i[1]), int(j[0])) + effort(int(j[0]), int(j[1]))
        val.append([value, hour_ls.index(i), min_ls.index(j)])

ans = sorted(val)[0]
print(f'{hour_ls[ans[1]]}:{min_ls[ans[2]]}')