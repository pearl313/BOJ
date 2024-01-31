import sys
input = sys.stdin.readline

n = int(input())
ls = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    gesture = input().strip()
    if gesture == 'H':
        ls[i] = [1, 0, 0]
    elif gesture == 'P':
        ls[i] = [0, 1, 0]
    else:
        ls[i] = [0, 0, 1]
prefix = [[0, 0, 0] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(3):
        prefix[i][j] = prefix[i - 1][j] + ls[i][j]

ans = 0
for i in range(1, n + 1):
    ans = max(max(prefix[i]) + max(prefix[n][0] - prefix[i][0], prefix[n][1] - prefix[i][1], prefix[n][2] - prefix[i][2]), ans)
print(ans)