import sys
input = sys.stdin.readline

n = int(input())
num = dict()
for _ in range(n):
    card = int(input())
    if not card in num.keys():
        num[card] = 1
    else:
        num[card] += 1
print(max(sorted(num), key=num.get))