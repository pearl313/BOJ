A, B, C, N = map(int, input().split())
for a in range(0, 51):
    for b in range(0, 51):
        for c in range(0, 51):
            if (A * a) + (B * b) + (C * c) == N:
                print(1)
                exit()
else:
    print(0)