n = int(input())
total = 0
for _ in range(n):
    student, apple = map(int, input().split())
    total += apple % student
print(total)