import sys
input = sys.stdin.readline

ls = list(map(int, input().split()))

def recur(cur, answer, score):
    global cnt
    if len(answer) >= 3:
        for j in range(len(answer) - 2):
            if answer[j] == answer[j + 1] == answer[j + 2]:
                return
    if cur == 10:
        if score >= 5:
            cnt += 1
        return
    for i in range(1, 6):
        recur(cur + 1, answer + str(i), score + 1 if i == ls[cur] else score)

cnt = 0
recur(0, '', 0)
print(cnt)