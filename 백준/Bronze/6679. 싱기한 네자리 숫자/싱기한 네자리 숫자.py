import sys
input = sys.stdin.readline

def jinsu(num, n):
    total = 0
    while True:
        if num // n == 0:
            total += num
            return total
        total += num % n
        num //= n

for i in range(1000, 10000):
    if sum(list(map(int, list(str(i))))) == jinsu(i, 12) == jinsu(i, 16):
        print(i)