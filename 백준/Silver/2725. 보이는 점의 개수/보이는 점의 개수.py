import sys, math
input = sys.stdin.readline

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd_ls = [0] * 1001
# 1일 때 따로 처리
gcd_ls[1] = 3
# 2부터 찾아보기
for i in range(2, 1001):
    cnt = 0
    # 0은 안봐도 됨
    for j in range(1, i + 1):
        if i == j:
            continue
        if get_gcd(i, j) + 1 == 2:
            # (0, 0)이랑 (i, j)를 지나는 선분 => 두 점을 지나야 함
            # 대칭이므로 +2
            cnt += 2
    # 앞 전에 구한 거에서 더해주기
    gcd_ls[i] = gcd_ls[i - 1] + cnt

c = int(input())
for _ in range(c):
    n = int(input())
    print(gcd_ls[n])