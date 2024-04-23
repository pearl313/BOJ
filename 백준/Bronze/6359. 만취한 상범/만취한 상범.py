import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    room = [False] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            if not room[j]:
                room[j] = True
            else:
                room[j] = False

    for i in range(1, n + 1):
        if room[i]:
            cnt += 1
    print(cnt)