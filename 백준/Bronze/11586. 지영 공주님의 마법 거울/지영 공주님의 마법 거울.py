import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _  in range(n)]
k = int(input())

if k == 1:
    for i in arr:
        print(''.join(i))
elif k == 2:
    for i in arr:
        print(''.join(i[::-1]))
else:
    for i in range(n - 1, -1, -1):
        print(''.join(arr[i]))