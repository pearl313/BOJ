import sys
input = sys.stdin.readline

t_n = []
for i in range(1, 101):
    t_n.append(i * (i + 1) // 2)

possible = [0] * 1001
for one in t_n:
    for two in t_n:
        for three in t_n:
            if one + two + three <= 1000:
                possible[one + two + three] = 1

t = int(input())
for _ in range(t):
    k = int(input())
    print(possible[k])