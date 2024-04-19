import sys
input = sys.stdin.readline

n = int(input())

# 각 후보가 받은 점수들
result = [[] for _ in range(3)]
# 각 후보가 받은 점수들 1, 2, 3점 개수들
each = [[0] * 3 for _ in range(3)]

for _ in range(n):
    a, b, c = map(int, input().split())
    result[0].append(a)
    result[1].append(b)
    result[2].append(c)
    each[0][a - 1] += 1
    each[1][b - 1] += 1
    each[2][c - 1] += 1

result[0].sort(reverse=True)
result[1].sort(reverse=True)
result[2].sort(reverse=True)
total = [sum(result[0]), sum(result[1]), sum(result[2])]
max_val = max(total)

# 가장 큰 점수 받은 후보 한 명일 경우,
if total.count(max_val) == 1:
    print(total.index(max_val) + 1, max_val)
# 여러 명일 경우,
else:
    third = [each[0][2], each[1][2], each[2][2]]
    # 3점을 많이 받은 후보가 한 명이면,
    if third.count(max(third)) == 1:
        print(third.index(max(third)) + 1, total[third.index(max(third))])
    else:
        second = []
        for i in range(3):
            if third[i] == max(third):
                second.append(each[i][1])
            else:
                second.append(0)
        if second.count(max(second)) == 1:
            print(second.index(max(second)) + 1, total[second.index(max(second))])
        else:
            print(0, max(total))