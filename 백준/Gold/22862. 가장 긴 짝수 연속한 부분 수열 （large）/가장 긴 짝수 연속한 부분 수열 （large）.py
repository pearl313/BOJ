import sys
input = sys.stdin.readline

S, K = map(int, input().split())
ls = list(map(int, input().split()))

s = 0
e = 0
# 짝수 개수
even = 0
# 홀수 개수
odd = 0
# 정답
ans = 0
# e가 끝까지 갈 때까지 반복
while e < S:
    # 홀수 개수가 K보다 크면,
    if odd > K:
        # s 당기기 -> 현재 s가 홀수인지 짝수인지 확인
        if ls[s] % 2 == 0:
            even -= 1
        else:
            odd -= 1
        s += 1
    # 홀수 개수가 K보다 안 크면, 
    else:
        # 현재 e가 짝수이면,
        if ls[e] % 2 == 0:
            even += 1
        # 현재 e가 홀수이면,
        else:
            odd += 1
        # e 늘리기
        e += 1
    ans = max(ans, even)
print(ans)