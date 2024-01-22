import sys
input = sys.stdin.readline

n, b, w = map(int, input().split())
ls = list(input().strip())
s, e = 0, 0
cnt_w, cnt_b = 0, 0
if ls[s] == 'W':
    cnt_w += 1
else:
    cnt_b += 1
ans = 0
while e < n:
    if cnt_b <= b and cnt_w >= w:
        ans = max(ans, cnt_b + cnt_w)
        e += 1
        if e == n:
            break
        if ls[e] == 'W':
            cnt_w += 1
        else:
            cnt_b += 1
    elif cnt_w < w:
        if cnt_b > b:
            if ls[s] == 'W':
                cnt_w -= 1
            else:
                cnt_b -= 1
            s += 1
        else:
            e += 1
            if e == n:
                break
            if ls[e] == 'W':
                cnt_w += 1
            else:
                cnt_b += 1
    elif cnt_b > b:
        if cnt_w >= w:
            if ls[s] == 'W':
                cnt_w -= 1
            else:
                cnt_b -= 1
            s += 1
        else:
            e += 1
            if e == n:
                break
            if ls[e] == 'W':
                cnt_w += 1
            else:
                cnt_b += 1
print(ans)