import sys
input = sys.stdin.readline

k = int(input())
x = k
ans = []
for i in range(2, k + 1):
    if i * i > k:
        break
    while x % i == 0:
        ans.append(i)
        x //= i
if x != 1:
    ans.append(x)
print(len(ans))
print(*ans)