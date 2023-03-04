import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    num = sorted(map(int, input().split()))
    num_dict = {n: True for n in num}
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (num[i] + num[j]) / 2 in num_dict:
                cnt += 1
    print(cnt)