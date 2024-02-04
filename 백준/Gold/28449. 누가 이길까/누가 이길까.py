import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
win_a = 0
win_b = 0
same = 0
for i in range(n):
    s, e = 0, m - 1
    lower = m
    temp = a[i]
    while s <= e:
        mid = (s + e) // 2
        if b[mid] >= temp:
            lower = mid
            e = mid - 1
        else:
            s = mid + 1
    s, e = 0, m - 1
    upper = m
    while s <= e:
        mid = (s + e) // 2
        if b[mid] > temp:
            upper = mid
            e = mid - 1
        else:
            s = mid + 1
    win_b += m - upper
    win_a += lower
    same += upper - lower
print(win_a, win_b, same)