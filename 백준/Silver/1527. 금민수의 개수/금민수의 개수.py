import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def recur(cur):
    global cnt
    if cur > b:
        return
    if a <= cur and cur <= b:
        cnt += 1
    recur(cur * 10 + 4)
    recur(cur * 10 + 7)

a, b = map(int, input().split())
cnt = 0
recur(4)
recur(7)
print(cnt)