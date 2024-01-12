import sys
input = sys.stdin.readline

A, B, D = map(int, input().split())
ans = 0
for i in range(A, B + 1):
    if i == 1:
        continue
    cnt = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        if str(D) in str(i):
            ans += 1
print(ans)
