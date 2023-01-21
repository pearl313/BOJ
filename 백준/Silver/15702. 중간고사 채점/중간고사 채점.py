import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = [0] + list(map(int, input().split()))
students = {}
for i in range(M):
    temp = list(input().split())
    score = 0
    for j in range(1, N + 1):
        if temp[j] == 'O':
            score += points[j]
    students[int(temp[0])] = score

for i in sorted(students):
    if students[i] == max(students.values()):
        print(i, students[i])
        break