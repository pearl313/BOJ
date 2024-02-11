import sys
input = sys.stdin.readline

n = int(input())
ls = [0] + list(map(int, input().split()))
ans = ''
j = 1
for i in range(1, n + 1):
    if ls[i] == ls[j]:
        continue
    print((str(i) + ' ') * (i - j), end='')
    j = i
print('-1 ' * (n - j + 1), end='')