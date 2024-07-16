import sys
input = sys.stdin.readline

n, m = map(int, input().split())
switch = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    switch[i] = temp[1:]

for i in range(1, n + 1):
    check = [0] * (m + 1)
    for j in range(1, n + 1):
        if i == j:
            continue
        for k in switch[j]:
            check[k] = 1
    if sum(check[1:]) == m:
        print(1)
        exit()
print(0)