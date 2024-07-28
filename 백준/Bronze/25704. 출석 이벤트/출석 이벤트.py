import sys
input = sys.stdin.readline

n = int(input())
p = int(input())
discount = 0
if n >= 20:
    discount = max(500, p // 10, 2000, p // 4)
elif 15 <= n < 20:
    discount = max(500, p // 10, 2000)
elif 10 <= n < 15:
    discount = max(500, p // 10)
elif 5 <= n < 10:
    discount = 500
print(p - discount if p >= discount else 0)