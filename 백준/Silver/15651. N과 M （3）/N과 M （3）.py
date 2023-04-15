def num(k):
    if k == M:
        print(*selected)
    else:
        for i in range(N):
            selected.append(i + 1)
            num(k + 1)
            selected.pop()

N, M = map(int, input().split())
selected = []
num(0)

