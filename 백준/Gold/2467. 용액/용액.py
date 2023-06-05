import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))
s = 0
e = N - 1
ans = 1e10
while s < e:
    temp = ls[e] + ls[s]
    if ans > abs(temp):
        ans_1, ans_2 = ls[s], ls[e]
        ans = abs(temp)
    elif temp == 0:
        ans_1, ans_2 = ls[s], ls[e]
        break
    elif temp > 0:
        e -= 1
    else:
        s += 1
print(ans_1, ans_2)