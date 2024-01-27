import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

prefix = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(11)]
for k in range(1, 11):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] == k:
                prefix[k][i][j] = 1
for k in range(1, 11):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix[k][i][j] += prefix[k][i - 1][j] + prefix[k][i][j- 1] - prefix[k][i - 1][j - 1]

q = int(input())
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    for k in range(1, 11):
        temp = prefix[k][x2][y2] - prefix[k][x2][y1 - 1] - prefix[k][x1 - 1][y2] + prefix[k][x1 - 1][y1 - 1]
        if temp:
            cnt += 1
    print(cnt)