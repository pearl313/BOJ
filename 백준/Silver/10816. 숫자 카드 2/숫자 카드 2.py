import sys
input = sys.stdin.readline

N = int(input())
sg_ls = sorted(map(int, input().split()))
M = int(input())
ls = list(map(int, input().split()))

for i in range(M):
    s = 0
    e = N - 1
    l = 0
    while s <= e:
        mid = (s + e) // 2
        if sg_ls[mid] < ls[i]:
            s = mid + 1
        elif sg_ls[mid] >= ls[i]:
            e = mid - 1
            l = mid
    s = 0
    e = N - 1
    r = -1
    while s <= e:
        mid = (s + e) // 2
        if sg_ls[mid] <= ls[i]:
            s = mid + 1
            r = mid
        elif sg_ls[mid] > ls[i]:
            e = mid - 1
    if sg_ls[l] != ls[i] or sg_ls[r] != ls[i]:
        print(0, end=' ')
        continue
    print(r - l + 1, end=' ')