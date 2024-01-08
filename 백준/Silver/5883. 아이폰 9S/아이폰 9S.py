import sys
input = sys.stdin.readline
'''
1. 용량의 종류 확인하고
2. 모든 종류를 각각 없애 봤을 때 연속 구간이 가장 긴 것 찾기
'''
n = int(input())
ls = list(int(input()) for _ in range(n))
num = dict()
for i in ls:
    if not i in num.keys():
        num[i] = 1
ans = 0
for i in num.keys():
    temp = []
    for j in ls:
        if i == j:
            continue
        temp.append(j)
    check = temp[0]
    length = 1
    for j in range(1, len(temp)):
        if check != temp[j]:
            check = temp[j]
            length = 1
        else:
            length += 1
        ans = max(ans, length)
print(ans)