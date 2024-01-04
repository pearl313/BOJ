N = int(input())
colored_paper = []
for _ in range(N):
    colored_paper.append(list(map(int, input().split())))
drawing_paper = [[0] * 100 for _ in range(100)]
for x, y in colored_paper:
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            drawing_paper[i][j] = 1
ans = 0
for a in range(100):
    for b in range(100):
        ans += drawing_paper[a][b]
print(ans)