import sys
input = sys.stdin.readline

def choose(k):
    global cnt
    if k == 10:
        for i in range(8):
            if submit[i] == submit[i + 1] == submit[i + 2]:
                return
        else:
            score = 0
            for i in range(10):
                if submit[i] == answer[i]:
                    score += 1
            if score >= 5:
                cnt += 1
        return
    
    for i in range(1, 6):
        submit.append(i)
        choose(k + 1)
        submit.pop()

answer = list(map(int, input().split()))
submit = []
cnt = 0
choose(0)
print(cnt)