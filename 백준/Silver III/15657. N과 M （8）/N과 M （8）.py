import sys
input = sys.stdin.readline

m, n = map(int, input().split())
ls = sorted(map(int, input().split()))
arr = [0 for _ in range(n)]

def recur(cur, start):
    if cur == n:
        print(*arr)
        return
    for i in range(start, m):
        arr[cur] = ls[i]
        recur(cur + 1, i)

recur(0, 0)