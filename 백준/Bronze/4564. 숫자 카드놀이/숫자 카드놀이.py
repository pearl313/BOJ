import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    ls = [n]
    while len(str(n)) > 1:
        temp = 1
        for i in str(n):
            temp *= int(i)
        ls.append(temp)
        n = temp
    print(*ls)