import sys
input = sys.stdin.readline

def nCm(k, cnt):
    global ans
    if k == N:
        if cnt == M:
            print(*ans)
            return
    else:
        ans.append(k + 1)
        nCm(k + 1, cnt + 1)
        ans.pop()
        nCm(k + 1, cnt)


N, M = map(int, input().split())
ans = []
nCm(0, 0)