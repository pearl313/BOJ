import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    basket = basket[:i - 1] + (basket[i - 1:j])[::-1] + basket[j:]
print(*basket)