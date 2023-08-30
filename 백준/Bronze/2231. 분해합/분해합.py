import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    temp = 0
    for j in list(str(i)):
        temp += int(j)
    if i + temp == n:
        print(i)
        exit()
print(0)