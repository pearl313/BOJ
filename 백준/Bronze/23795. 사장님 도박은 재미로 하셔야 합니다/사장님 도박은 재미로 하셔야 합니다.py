import sys
input = sys.stdin.readline

total = 0
while True:
    n = int(input())
    if n == -1:
        print(total)
        break
    total += n