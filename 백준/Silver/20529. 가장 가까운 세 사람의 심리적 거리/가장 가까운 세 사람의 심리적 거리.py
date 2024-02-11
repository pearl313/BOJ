import sys
input = sys.stdin.readline

def check(a, b):
    cnt = 0
    for i in range(4):
        if a[i] == b[i]:
            continue
        cnt += 1
    return cnt

def recur(cur, start):
    global ans
    if cur == 3:
        ans = min(ans, check(selected[0], selected[1]) + check(selected[1], selected[2]) + check(selected[0], selected[2]))
        return
    for i in range(start, n):
        selected.append(mbti[i])
        recur(cur + 1, i + 1)
        selected.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = list(input().split())
    ans = 1e10
    if n == 3:
        ans = check(mbti[0], mbti[1]) + check(mbti[1], mbti[2]) + check(mbti[0], mbti[2])
    elif n > 32:
        ans = 0
    else:
        selected = []
        recur(0, 0)
    print(ans)