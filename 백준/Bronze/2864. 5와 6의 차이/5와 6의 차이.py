import sys
input = sys.stdin.readline

a, b = input().split()
min_ls_a = list(a)
max_ls_a = list(a)
for i in range(len(a)):
    if a[i] == '5':
        max_ls_a[i] = '6'
    elif a[i] == '6':
        min_ls_a[i] = '5'

min_ls_b = list(b)
max_ls_b = list(b)
for i in range(len(b)):
    if b[i] == '5':
        max_ls_b[i] = '6'
    elif b[i] == '6':
        min_ls_b[i] = '5'

print(int(''.join(min_ls_a)) + int(''.join(min_ls_b)), int(''.join(max_ls_a)) + int(''.join(max_ls_b)))