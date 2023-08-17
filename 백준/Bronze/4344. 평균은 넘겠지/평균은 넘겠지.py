import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    ls = list(map(int, input().split()))
    n = ls[0]
    students = ls[1:]
    average = sum(students) / n
    cnt = 0
    for i in students:
        if average < i:
            cnt += 1
    print(f'{round(cnt / n * 100, 3)}%')