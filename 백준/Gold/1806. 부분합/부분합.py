import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))
s, e = 0, 0
temp = sum(ls[s:e + 1])
ans = 1e10
while e < n:
    if temp == k:
        ans = min(ans, len(ls[s:e + 1]))
        e += 1
        if e == n:
            break
        temp += ls[e]
    elif temp > k:
        ans = min(ans, len(ls[s:e + 1]))
        temp -= ls[s]
        s += 1
    else:
        e += 1
        if e == n:
            break
        temp += ls[e]
print(ans if ans != 1e10 else 0)