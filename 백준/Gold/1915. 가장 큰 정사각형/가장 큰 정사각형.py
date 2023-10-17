import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        # 인덱스 때문에 i, j 모두 0보다 커야하고, 그 값이 1이면,
        if i > 0 and j > 0 and arr[i][j] == 1:
            # 해당 위치에서 최소사각형(2 x 2)를 확인해보고 거기서의 최소값을 더해주면, 그 크기만한 정사각형이 가능한 것
            arr[i][j] += min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1])
        ans = max(ans, arr[i][j])
print(ans * ans)
