import sys
input = sys.stdin.readline

icon = ['*x*', ' xx', '* *']

k = int(input())
ans = []
for i in range(3):
    temp = ''
    for j in range(3):
        temp += icon[i][j] * k
    for n in range(k):
        ans.append(temp)
for i in ans:
    print(i)