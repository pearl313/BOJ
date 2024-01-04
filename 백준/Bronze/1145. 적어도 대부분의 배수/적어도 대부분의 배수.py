ls = sorted(map(int, input().split()))
i = 1
while True:
    for n in range(1, 10000000):
        cnt = 0
        for j in range(5):
            if n % ls[j] == 0:
                cnt += 1
        if cnt >= 3:
            print(n)
            exit()
