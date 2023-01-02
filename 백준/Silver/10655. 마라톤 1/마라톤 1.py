import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

max_V = 0
for i in range(1, N - 2):
    distance = (abs(points[i][0] - points[i + 1][0]) + abs(points[i][1] - points[i + 1][1]) + abs(points[i][0] - points[i - 1][0]) + abs(points[i][1] - points[i - 1][1])) - (abs(points[i + 1][0] - points[i - 1][0]) + abs(points[i + 1][1] - points[i - 1][1]))
    max_V = max(max_V, distance)

total = 0
for i in range(N - 1):
    total += abs(points[i][0] - points[i + 1][0]) + abs(points[i][1] - points[i + 1][1])

print(total - max_V)