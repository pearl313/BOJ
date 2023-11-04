import sys
input = sys.stdin.readline

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    student = list(map(int, input().split()))
    cnt = 0
    for lecture in lectures:
        if set(lecture[1:]).intersection(set(student[1:])) == set(lecture[1:]):
            cnt += 1
    print(cnt)