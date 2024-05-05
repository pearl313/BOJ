import sys
input = sys.stdin.readline

n = int(input())
grade = [[[] for _ in range(12)] for _ in range(12)]

for i in range(1, n + 1):
    ls = list(map(int, input().split()))
    for j in range(5):
        grade[j][ls[j]].append(i)

num = [set() for _ in range(n + 1)]
for i in grade:
    for j in i:
        if not j:
            continue
        if len(j) == 1:
            continue
        for k in j:
            for v in j:
                if v == k:
                    continue
                num[k].add(v)
ans = 0
cnt = -1e10
for i in range(1, n + 1):
    if len(num[i]) > cnt:
        cnt = len(num[i])
        ans = i
print(ans)