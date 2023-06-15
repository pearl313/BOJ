import sys
input = sys.stdin.readline

def choice(cur, cnt):
    global ans
    if cur == N:
        if cnt != 0:
            ans.append(sum(selected))
    else:
        selected.append(S[cur])
        choice(cur + 1, cnt + 1)
        selected.pop()
        choice(cur + 1, cnt)

N = int(input())
S = list(map(int, input().split()))
selected = []
ans = []
choice(0, 0)
ans = list(set(sorted(ans)))
for i in range(len(ans)):
    if i + 1 == ans[i]:
        continue
    print(i + 1)
    exit()
else:
    print(len(ans) + 1)