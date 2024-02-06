import sys
input = sys.stdin.readline

def search(num):
    global check
    s, e = 0, n - 1
    left = 0
    while s <= e:
        mid = (s + e) // 2
        if ls_1[mid] == num:
            check = True
            left = mid
            e = mid - 1
        elif ls_1[mid] < num:
            s = mid + 1
        else:
            e = mid - 1

    s, e = 0, n - 1
    right = 0
    while s <= e:
        mid = (s + e) // 2
        if ls_1[mid] == num:
            right = mid
            s = mid + 1
        elif ls_1[mid] < num:
            s = mid + 1
        else:
            e = mid - 1
    return right - left

n = int(input())
ls_1 = sorted(map(int, input().split()))
m = int(input())
ls_2 = list(map(int, input().split()))
ans = []
for i in range(m):
    check = False
    temp = search(ls_2[i])
    ans.append(temp + 1 if check else 0)
print(*ans)