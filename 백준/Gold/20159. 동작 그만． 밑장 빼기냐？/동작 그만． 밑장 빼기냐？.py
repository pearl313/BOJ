import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
time = n // 2
total = 0
for i in range(n):
    if i % 2 == 0:
        total += cards[i]
ans = total
temp = total
for i in range(n - 1, 0, -2):
    temp += cards[i]
    temp -= cards[i - 1]
    ans = max(ans, temp)
temp = total
for i in range(n - 2, 1, -2):
    temp -= cards[i]
    temp += cards[i - 1]
    ans = max(ans, temp)
print(ans)