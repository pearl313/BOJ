import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))

ans = 1e10
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        s, e = 0, n - 1
        while s < e:
            if s == i or s == j:
                s += 1
                continue
            if e == i or e == j:
                e -= 1
                continue
            ans = min(ans, abs(ls[i] + ls[j] - (ls[s] + ls[e])))
            if ls[s] + ls[e] > ls[i] + ls[j]:
                e -= 1
            else:
                s += 1
print(ans)