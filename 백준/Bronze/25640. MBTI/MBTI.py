jinho = input()
n = int(input())
cnt = 0
for _ in range(n):
    mbti = input()
    if mbti == jinho:
        cnt += 1
print(cnt)