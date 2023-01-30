import sys
input = sys.stdin.readline

U, N = map(int, input().split())
ls = list([] for _ in range(10001))
price = {}
for _ in range(N):
    S, P = input().split()
    P = int(P)
    ls[P].append(S)
    if P in price:
        price[P] += 1
    else:
        price[P] = 1

min_price = float('inf')
for key, value in price.items():
    if value == min(price.values()) and key <= min_price:
        min_price = key
print(ls[min_price][0], min_price)