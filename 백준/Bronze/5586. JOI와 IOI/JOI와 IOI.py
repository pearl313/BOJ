import sys
input = sys.stdin.readline

s = input().strip()
cnt_joi, cnt_ioi = 0, 0
for i in range(len(s) - 2):
    if s[i:i + 3] == 'JOI':
        cnt_joi += 1
    elif s[i:i + 3] == 'IOI':
        cnt_ioi += 1
print(cnt_joi, cnt_ioi, sep='\n')