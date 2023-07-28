import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break
    num = 1
    i = 1
    while True:
        if num % n == 0:
            print(i)
            break
        num = num * 10 + 1
        i += 1