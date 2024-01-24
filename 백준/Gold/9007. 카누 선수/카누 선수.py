import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(4)]
    new_ls_1 = []
    new_ls_2 = []

    for i in range(n):
        for j in range(n):
            new_ls_1.append(ls[0][i] + ls[1][j])
            new_ls_2.append(ls[2][i] + ls[3][j])

    new_ls_1 = sorted(new_ls_1)
    new_ls_2 = sorted(new_ls_2)
    s, e = 0, len(new_ls_1) - 1
    ans = 1e10
    while s <= len(new_ls_1) - 1 and e >= 0:
        temp = new_ls_1[s] + new_ls_2[e]
        if temp == k:
            ans = temp
            break
        elif abs(k - ans) >= abs(k - temp):
            if abs(k - ans) == abs(k - temp):
                ans = min(ans, temp)
            else:
                ans = temp

        if temp > k:
            e -= 1
        else:
            s += 1
    print(ans)