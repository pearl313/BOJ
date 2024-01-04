N, M, K = map(int, input().split())
team = 0
while N >= 2 and M >= 1 and N + M >= K + 3:
    team += 1
    N -= 2
    M -= 1
print(team)
