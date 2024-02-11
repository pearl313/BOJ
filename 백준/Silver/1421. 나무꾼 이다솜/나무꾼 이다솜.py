import sys
input = sys.stdin.readline

n, c, w = map(int, input().split())
trees = list(int(input()) for _ in range(n))
ans = 0
for i in range(1, max(trees) + 1):
    cost = 0
    for j in range(n):
        cost += max(0, trees[j] // i * i * w - (trees[j] // i * c if trees[j] % i else (trees[j] // i - 1) * c))
    ans = max(ans, cost)
print(ans)