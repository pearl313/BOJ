import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
ans = [[] for _ in range(N)]
for i in range(N):
    for j in range(M):
        ans[i].append(A[i][j] + B[i][j])
for i in ans:
    print(*i)