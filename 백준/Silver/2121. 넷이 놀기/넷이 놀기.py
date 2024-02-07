import sys
input = sys.stdin.readline

def search(x, y):
    s, e = 0, n - 1
    while s <= e:
        mid = (s + e) // 2
        if ls[mid] == [x, y]:
            return True
        elif ls[mid] < [x, y]:
            s = mid + 1
        else:
            e = mid - 1
    return False

n = int(input())
a, b = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
ls = sorted(ls)
cnt = 0
for i, j in ls:
    if search(i + a, j) and search(i, j + b) and search(i + a, j + b):
        cnt += 1
print(cnt)