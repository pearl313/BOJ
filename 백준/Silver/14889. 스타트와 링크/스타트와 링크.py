import sys
input = sys.stdin.readline

def team(cur, sta):
    global ans
    if len(selected) == N // 2:
        start = 0
        link = 0
        non = list(set(num) - set(selected))
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                start += S[selected[i]][selected[j]] + S[selected[j]][selected[i]]
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                link += S[non[i]][non[j]] + S[non[j]][non[i]]
        ans = min(ans, abs(start - link))
        return
    for i in range(sta, N + 1):
        selected.append(i)
        team(cur + 1, i + 1)
        selected.pop()

N = int(input())
S = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
selected = []
num = list(range(1, N + 1))
ans = 1e10
team(0, 1)
print(ans)