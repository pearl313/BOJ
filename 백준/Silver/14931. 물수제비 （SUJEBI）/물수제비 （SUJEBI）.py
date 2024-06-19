l = int(input())
score = [0] + list(map(int, input().split()))

d = 0
ans = 0
for i in range(1, l + 1):
    total = 0
    for j in range(i, l + 1, i):
        total += score[j]
    if ans < total:
        d = i
        ans = total
print(d, ans)