import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    total = 0
    for a in range(i, x + 1):
        for b in range(j, y + 1):
            total += arr[a][b]
    print(total)