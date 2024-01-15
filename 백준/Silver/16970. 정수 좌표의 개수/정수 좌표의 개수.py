import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m, k = map(int, input().split())
cnt = 0
for x1 in range(n + 1):
    for y1 in range(m + 1):
        for x2 in range(n + 1):
            for y2 in range(m + 1):
                # 두 점 골라서 선분 잇기 -> 기울기 구하고 점 k개 있는 지 확인
                if k == get_gcd(abs(x2 - x1), abs(y2 - y1)) + 1:
                    cnt += 1
print(cnt // 2)