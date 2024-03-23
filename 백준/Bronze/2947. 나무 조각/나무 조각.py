import sys
input = sys.stdin.readline

ls = list(map(int, input().split()))

while ls != [1, 2, 3, 4, 5]:
    temp = ls[:]
    for i in range(4):
        if ls[i] > ls[i + 1]:
            temp[i] = ls[i + 1]
            temp[i + 1] = ls[i]
            print(*temp)
        ls = temp[:]