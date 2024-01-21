import sys
input = sys.stdin.readline

n = int(input())
language = input().strip()
s, e = 0, 0
temp = language[s:e + 1]
cnt = set()
for i in temp:
    if not i in cnt:
        cnt.add(i)
ans = 0
while e < len(language):
    if len(cnt) == n:
        ans = max(ans, len(temp))
        e += 1
        if e == len(language):
            break
        temp += language[e]
        cnt.add(language[e])
    elif len(cnt) < n:
        ans = max(ans, len(temp))
        e += 1
        if e == len(language):
            break
        temp += language[e]
        cnt.add(language[e])
    else:
        s += 1
        temp = temp[1:]
        cnt = set()
        for i in temp:
            if not i in cnt:
                cnt.add(i)
print(ans)