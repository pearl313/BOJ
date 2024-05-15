import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    while len(str(n)) > 1:
        n = sum(list(map(int, list(str(n)))))
    print(n)