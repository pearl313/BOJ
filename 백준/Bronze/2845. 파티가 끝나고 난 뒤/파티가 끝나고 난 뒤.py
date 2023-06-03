L, P = map(int, input().split())
ls = list(map(int, input().split()))
total = L * P
for i in ls:
    print(i - total, end=' ')