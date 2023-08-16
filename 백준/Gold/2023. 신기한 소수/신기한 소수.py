import sys
input = sys.stdin.readline

def check(num):
    if num == 1:
        return False
    cnt = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def recur(cur):
    if len(str(cur)) == n:
        print(cur)
        return
    for j in range(1, 10):
        if check(cur * 10 + j):
            recur(cur * 10 + j)

n = int(input())
if n == 1:
    print(2, 3, 5, 7, sep='\n')
else:
    recur(0)