import sys
input = sys.stdin.readline
'''
모든 체커를 옮겨 보기
1. 최소 횟수로 모일 수 있는 곳들을 순회하면서
2. 1개, 2개, ..., n개까지 해보고 그때마다 최소 횟수 출력하기
'''
n = int(input())
position = []
x_ls = set()
y_ls = set()
possible = []
for _ in range(n):
    x, y = map(int, input().split())
    x_ls.add(x)
    y_ls.add(y)
    position.append([x, y])
x_ls, y_ls = list(x_ls), list(y_ls)
for x in range(len(x_ls)):
    for y in range(len(y_ls)):
        possible.append([x_ls[x], y_ls[y]])
ans = [1e10] * n
for x, y in possible:
    dist = []
    for i, j in position:
        dist.append(abs(x - i) + abs(y - j))
    dist.sort()
    for d in range(n):
        ans[d] = min(ans[d], sum(dist[:d + 1]))
print(*ans)