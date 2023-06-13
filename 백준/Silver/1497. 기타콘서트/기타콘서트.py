import sys
input = sys.stdin.readline

def recur(cur, cnt):
    global ans, possible
    if cur == N:
        if cnt != 0:
            ok = set()
            for name, info in selected:
                for i in range(M):
                    if info[i] == 'Y':
                        ok.add(i + 1)
            possible = max(possible, sum(ok))
            if possible == sum(ok):
                ans = min(ans, len(selected))
            return
    else:
        selected.append(infos[cur])
        recur(cur + 1, cnt + 1)
        selected.pop()
        recur(cur + 1, cnt)

N, M = map(int, input().split())
infos = [list(input().split()) for _ in range(N)]
selected = []
ans = 1e10
possible = 0
recur(0, 0)
print(-1 if not possible else ans)