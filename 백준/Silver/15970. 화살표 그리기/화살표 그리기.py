import sys
input = sys.stdin.readline

def plus(arr):
    total = 0
    for i in range(len(arr)):
        if i == 0:
            total += arr[1] - arr[0]
        elif i == len(arr) - 1:
            total += arr[len(arr) - 1] - arr[len(arr) - 2]
        else:
            total += min(arr[i + 1] - arr[i], arr[i] - arr[i - 1])
    return total
ans = 0
N = int(input())
dots = []
for _ in range(N):
    x, y = map(int, input().split())
    dots.append([y, x])
dots.sort(key = lambda x:(x[0], x[1]))
for i in range(1, dots[-1][0] + 1):
    arr = []
    for j in range(N):
        if dots[j][0] == i:
            arr.append(dots[j][1])
    ans += plus(arr)
print(ans)
