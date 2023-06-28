import sys
input = sys.stdin.readline

burgers = list(int(input()) for _ in range(3))
drinks = list(int(input()) for _ in range(2))
print(min(burgers) + min(drinks) - 50)