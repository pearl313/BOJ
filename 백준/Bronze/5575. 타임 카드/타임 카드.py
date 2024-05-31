import sys
input = sys.stdin.readline

for _ in range(3):
    time = list(map(int, input().split()))
    s = time[0] * 3600 + time[1] * 60 + time[2]
    e = time[3] * 3600 + time[4] * 60 + time[5]
    t = e - s
    print(t // 3600 % 24, t // 60 % 60, t % 60)