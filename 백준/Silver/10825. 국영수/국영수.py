import sys
input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    name, *score = input().split()
    score = list(map(int, score))
    students.append([name, score])
students.sort(key=lambda x:(-x[1][0], x[1][1], -x[1][2], x[0]))
for i in students:
    print(i[0])