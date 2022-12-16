import sys
input = sys.stdin.readline

N = int(input())
candidate = []
for i in range(100, 999):
    if '0' in list(str(i)) or str(i)[0] == str(i)[1] or str(i)[1] == str(i)[2] or str(i)[0] == str(i)[2]:
        continue
    else:
        candidate.append(str(i))
ans = []
for _ in range(N):
    num, strike, ball = map(int, input().split())

    for i in candidate:         # 후보군들 순회하면서
        cnt_s = 0               # 스트라이크 개수
        cnt_b = 0               # 볼 개수
        for j in range(3):
            if i[j] in str(num):
                if i[j] == str(num)[j]:      # 입력받은 스트라이크 있으면서 후보군의 각 숫자의 위치 + 값 == 입력받은 수의 각 숫자의 위치 + 값
                    cnt_s += 1                          # 스트라이크 개수 업
                if i[j] != str(num)[j]:  # 후보군의 각 숫자의 위치 + 값 != 입력받은 수의 각 숫자의 위치 + 값 이지만, 그 숫자가 후보군 안에 존재하면
                    cnt_b += 1                          # 볼 개수 업
        if cnt_s == strike and cnt_b == ball:
            ans.append(i)

    candidate = ans
    ans = []
# print(candidate)
print(len(candidate))


