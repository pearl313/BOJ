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

# 최소 횟수로 모일 수 있는 가능성이 있는 곳들 찾기
for x in range(len(x_ls)):
    for y in range(len(y_ls)):
        possible.append([x_ls[x], y_ls[y]])

# 각 점 개수 별 최소 횟수
ans = [1e10] * n
for x, y in possible:
    dist = []
    for i, j in position:
        dist.append(abs(x - i) + abs(y - j))
    dist.sort()
    # 가능성 있는 곳들마다 주어진 점들과의 거리 구하고 정렬
    # 앞에서부터 1개, 2개, ..., n개를 합친 거리의 최솟값 찾기
    for d in range(n):
        ans[d] = min(ans[d], sum(dist[:d + 1]))
print(*ans)