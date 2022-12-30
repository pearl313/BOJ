import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
for idx, val in enumerate(arr):
    arr[idx] = [val, idx]
arr.sort()
for idx, ls in enumerate(arr):
    arr[idx] = [ls[1], ls[0], idx]
arr.sort()
for i in range(len(arr)):
    arr[i] = arr[i][2]
print(*arr)