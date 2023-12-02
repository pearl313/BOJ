import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_ls = sorted(map(int, input().split()))
b_ls = sorted(map(int, input().split()))

num = dict()
for i in range(a):
    if not a_ls[i] in num.keys():
        num[a_ls[i]] = 1
    else:
        num[a_ls[i]] += 1
for i in range(b):
    if not b_ls[i] in num.keys():
        num[b_ls[i]] = 1
    else:
        num[b_ls[i]] += 1
cnt = 0
for i in num.values():
    if i == 1:
        cnt += 1
print(cnt)