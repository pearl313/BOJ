import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    total = 0
    for i in range(n):
        total += candy[i] // k
    print(total)