import sys
input = sys.stdin.readline

candidate = []
for i in range(123, 988):
    num = str(i)
    if '0' in num:
        continue
    if num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
        continue
    candidate.append(i)
n = int(input())
questions = [list(map(int, input().split())) for _ in range(n)]
for num, strick, ball in questions:
    possible = []
    for can in candidate:
        num = str(num)
        can = str(can)
        s, b = 0, 0
        for i in range(3):
            # 스트라이크 체크
            if num[i] == can[i]:
                s += 1
            else:
                # 볼 체크
                if num[i] in can:
                    b += 1
        if s == strick and b == ball:
            possible.append(can)
    candidate = possible[::]
print(len(possible))