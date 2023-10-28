n = int(input())
ls = sorted(list(map(int, input().split())) for _ in range(n))
for i in ls:
    print(*i)