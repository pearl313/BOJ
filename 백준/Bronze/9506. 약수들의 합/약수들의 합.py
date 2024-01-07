import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        exit()
    ls = []
    for i in range(1, n + 1):
        if n % i == 0:
            ls.append(i)
    if sum(ls) - n == n:
        print(f'{n} = ', end='')
        for i in range(len(ls) - 2):
            print(f'{ls[i]} + ', end='')
        print(ls[-2])
    else:
        print(f'{n} is NOT perfect.')