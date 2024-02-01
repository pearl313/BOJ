n, x = map(int, input().split())
ls = list(map(int, input().split()))
for i in range(n):
    if ls[i] >= x:
        continue
    print(ls[i], end=' ')