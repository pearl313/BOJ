import sys
input = sys.stdin.readline
from collections import deque

def check(num):
    global k
    while ls[num - 1] == 0:
        k = (k + 1) % n

n, k = map(int, input().split())
ls = deque(range(1, n + 1))
ans = []

while ls:
    for _ in range(k - 1):
        ls.append(ls.popleft())
    ans.append(ls.popleft())

print(str(ans).replace('[', '<').replace(']', '>'))