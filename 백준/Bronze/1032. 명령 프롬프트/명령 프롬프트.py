import sys
input = sys.stdin.readline

N = int(input())
files = list(input().strip() for _ in range(N))
ans = list(files[0])
for i in range(1, N):
    for j in range(len(ans)):
        if files[i][j] == ans[j]:
            continue
        ans[j] = '?'
print(''.join(ans))