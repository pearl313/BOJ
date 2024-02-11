import sys
input = sys.stdin.readline

n = int(input())
players = list(map(int, input().split()))
check = set(players)
max_val = max(players)
points = [0] * (max_val + 1)
for i in range(n):
    if players[i] == max_val:
        continue
    for j in range(2 * players[i], max_val + 1, players[i]):
        if j in check:
            points[players[i]] += 1
            points[j] -= 1
for i in players:
    print(points[i], end=' ')