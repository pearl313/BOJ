import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ls = sorted(list(map(int, input().split())) for __ in range(n))

    cnt = 1
    limit = ls[0][1]
    for i in range(1, n):
        if ls[i][1] >= limit:
            continue
        cnt += 1
        limit = ls[i][1]
    
    print(cnt)