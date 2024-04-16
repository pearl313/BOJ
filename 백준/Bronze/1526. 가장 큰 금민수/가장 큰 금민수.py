import sys
input = sys.stdin.readline

n = int(input())
for i in range(n, 3, -1):
    for j in str(i):
        if j not in '47':
            break
    else:
        print(i)
        exit()