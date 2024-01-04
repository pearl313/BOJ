import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    temp = time[:i] + time[i + 1:]
    term = [0] * 1001
    for a, b in temp:
        for j in range(a, b):
            term[j] = 1
    ans = max(ans, sum(term))
print(ans)