import sys
input = sys.stdin.readline

n = int(input())
ls = list(input().strip() for _ in range(n))

diff = set()
for i in range(n):
    same = False
    for j in range(len(ls[i])):
        temp = ls[i][j:] + ls[i][:j]
        if temp in diff:
            same = True
            break
    if not same:
        diff.add(ls[i])

print(len(diff))