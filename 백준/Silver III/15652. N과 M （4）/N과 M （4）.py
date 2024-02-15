import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [0 for _ in range(n)]

def recur(cur, start):
    if cur == n:
        print(*arr)
        return
    for i in range(start, m + 1):
        arr[cur] = i
        recur(cur + 1, i)

recur(0, 1)