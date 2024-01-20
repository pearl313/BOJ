import sys
input = sys.stdin.readline
'''
현재 몸무게 = 시작점, 기억하고 있는 몸무게 = 끝점
두 값을 계산해서 G값이 나오는지 확인
- G값보다 작으면 현재 몸무게 +1
- G값보다 크면 기억하고 있는 몸무게 +1
'''
g = int(input())
weight = list(range(1, 100001))
s, e = 0, 0
ans = []
while s < 100000 and e < 100000:
    temp = weight[s] ** 2 - weight[e] ** 2
    if temp == g:
        ans.append(weight[s])
        s += 1
        e += 1
    elif temp < g:
        s += 1
    else:
        e += 1
if not ans:
    print(-1)
else:
    print(*ans, sep='\n')