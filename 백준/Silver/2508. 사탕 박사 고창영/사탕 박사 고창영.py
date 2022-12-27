import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    r, c = map(int, input().split())
    box = list(input().strip() for _ in range(r))
    cnt = 0
    for i in range(r):
        for j in range(c):
            if box[i][j] == 'o':
                if j != 0 and j != c - 1 and box[i][j - 1] == '>' and box[i][j + 1] == '<':
                    cnt += 1
                elif i != 0 and i != r - 1 and box[i - 1][j] == 'v' and box[i + 1][j] == '^':
                    cnt += 1
    print(cnt)