import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
s, e = 0, n - 1
ans = 0
temp = len(ls[s + 1:e])
while s < e:
    value = temp * min(ls[s], ls[e])
    if ls[s] < ls[e]:
        s += 1
    else:
        e -= 1
    temp -= 1
    ans = max(ans, value)
print(ans)