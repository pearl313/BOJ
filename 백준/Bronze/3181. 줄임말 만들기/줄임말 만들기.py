import sys
input = sys.stdin.readline

s = list(input().split())
ls = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
ans = ''
for i in s:
    if i in ls:
        if ans == '':
            ans += i[0].upper()
        else:
            continue
    else:
        ans += i[0].upper()
print(ans)